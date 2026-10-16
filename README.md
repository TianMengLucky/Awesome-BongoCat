# Awesome-BongoCat

从 [BongoCat 免费模型中心](https://bongocat.pet/models/) 下载的免费版本，保留原始 ZIP 和作者预览图。

2026-10-16 整理：保留原下载清单中 ZIP 最小的 5 个免费模型，ZIP 总计 9,134,645 字节（约 8.7 MiB）。已检查全部 ZIP 的 CRC、实际 SHA-256 和预览图。

目录格式：

```text
model.json
model/
  <模型名>/
    model.zip
    preview.webp
sources/
  models.json
```

`model.json` 使用 BongoCat 的 `bongo-store` / `store_catalog.rs` 所需格式：`name`、`author`、`author_url`、`repository_path`、`folder_path`、`preview_path`、`sha256`。路径均相对于仓库根目录，SHA-256 根据实际下载的 ZIP 计算；网站清单的 `size` 是模型资源大小，`checksum` 不作为 ZIP 文件哈希使用。`sources/models.json` 保存下载时的网站原始清单，用于追溯来源及完整版本链接。

重新下载或更新（Python 3，依赖 `requests` 和 `Pillow`）：

```powershell
python scripts/download_models.py
```

脚本按现有 `model.json` 保留选定的模型，只下载社区页面提供“下载免费版”的模型，检查 ZIP CRC 和预览图，并生成商店索引。已存在的文件会复用。模型权利及使用条件以各作者声明和压缩包内说明为准，免费提供下载不代表统一授权转载或商用。
