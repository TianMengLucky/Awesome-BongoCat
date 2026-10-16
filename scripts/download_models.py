"""Download the website's free models and build the bongo-store catalog."""
import concurrent.futures
import hashlib
import json
from pathlib import Path
import re
import time
from urllib.parse import urlparse
import zipfile

import requests

ROOT = Path(__file__).resolve().parents[1]
SOURCE = 'https://admin.bongocat.pet/models.json'


def fetch(url, target):
    if target.exists():
        return
    target.parent.mkdir(parents=True, exist_ok=True)
    partial = target.with_suffix(target.suffix + '.part')
    for attempt in range(4):
        try:
            offset = partial.stat().st_size if partial.exists() else 0
            headers = {'Range': f'bytes={offset}-'} if offset else {}
            with requests.get(url, stream=True, timeout=(20, 30), headers=headers) as response:
                response.raise_for_status()
                append = response.status_code == 206 and offset > 0
                if append:
                    assert response.headers['Content-Range'].startswith(f'bytes {offset}-')
                count = offset if append else 0
                expected = int(response.headers.get('Content-Length', 0)) + count
                with partial.open('ab' if append else 'wb') as output:
                    for chunk in response.iter_content(256 * 1024):
                        output.write(chunk)
                        count += len(chunk)
            if response.headers.get('Content-Length') and count != expected:
                raise ValueError(f'Incomplete HTTP body: {target}: {count} != {expected}')
            partial.replace(target)
            return
        except Exception as error:
            if attempt == 3:
                raise
            print(f'Retrying {target.name}: {error}', flush=True)
            time.sleep(2 ** attempt)


def download(model, repositories):
    author = repositories[model['repositoryKey']]
    identifier = model['id']
    assert re.fullmatch(r'[A-Za-z0-9_-]+', identifier), identifier
    name = model['name']
    assert not any(c in name for c in '<>:"/\\|?*%#') and name not in {'.', '..'}
    assert name == name.rstrip('. ')
    folder = Path('model') / name
    archive = folder / 'model.zip'
    extension = Path(urlparse(model['preview']).path).suffix.lower()
    assert extension in {'.png', '.jpg', '.jpeg', '.webp', '.gif'}
    preview = folder / ('preview' + extension)
    partial = (ROOT / archive).with_suffix('.zip.part')
    if partial.exists() and zipfile.is_zipfile(partial):
        with zipfile.ZipFile(partial) as package:
            complete = package.testzip() is None
        if complete:
            partial.replace(ROOT / archive)
    fetch(model['downloadUrl'], ROOT / archive)
    with zipfile.ZipFile(ROOT / archive) as package:
        assert package.namelist(), f'Empty ZIP: {identifier}'
        bad = package.testzip()
        assert bad is None, f'Bad ZIP member: {bad}'
    fetch(model['preview'], ROOT / preview)
    from PIL import Image
    with Image.open(ROOT / preview) as image:
        image.verify()
    links = author.get('authorLinks', [])
    author_url = next((link['url'] for link in links if not link['label'].upper().startswith('QQ')), author['repository'])
    return dict(name=model['name'], author=author.get('displayName') or model['repositoryKey'],
                author_url=author_url, repository_path=archive.as_posix(),
                folder_path=folder.as_posix(), preview_path=preview.as_posix(),
                sha256=hashlib.sha256((ROOT / archive).read_bytes()).hexdigest())


def main():
    response = requests.get(SOURCE, timeout=30)
    response.raise_for_status()
    manifest = response.json()
    assert manifest['version'] == 1
    models = [m for m in manifest['models'] if m.get('downloadUrl') and
              manifest['repositories'][m['repositoryKey']].get('category') != 'custom']
    catalog_path = ROOT / 'model.json'
    if catalog_path.exists():
        selected = {entry['name'] for entry in json.loads(catalog_path.read_text(encoding='utf-8'))}
        models = [model for model in models if model['name'] in selected]
        assert {model['name'] for model in models} == selected, 'Selected models missing from source'
    assert 0 < len(models) <= 512
    assert len({m['id'] for m in models}) == len(models)
    assert len({m['name'].casefold() for m in models}) == len(models), 'Duplicate model folder names'
    provenance = ROOT / 'sources'
    provenance.mkdir(exist_ok=True)
    (provenance / 'models.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    entries = {}
    failures = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
        jobs = {pool.submit(download, m, manifest['repositories']): m for m in models}
        for future in concurrent.futures.as_completed(jobs):
            model = jobs[future]
            try:
                entries[model['id']] = future.result()
                print(f"OK {len(entries)}/{len(models)} {model['name']}", flush=True)
            except Exception as error:
                failures.append((model['id'], str(error)))
                print(f"FAILED {model['id']}: {error}", flush=True)
    if failures:
        raise RuntimeError(failures)
    catalog = [entries[m['id']] for m in models]
    content = json.dumps(catalog, ensure_ascii=False, indent=2) + '\n'
    assert len(content.encode()) <= 2 * 1024 * 1024
    (ROOT / 'model.json').write_text(content, encoding='utf-8')
    total = sum((ROOT / entry['repository_path']).stat().st_size for entry in catalog)
    print(f"DONE {len(catalog)} models; {total:,} ZIP bytes", flush=True)


if __name__ == '__main__':
    main()
