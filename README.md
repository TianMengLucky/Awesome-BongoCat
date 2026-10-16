# Awesome-BongoCat

从 [BongoCat 免费模型中心](https://bongocat.pet/models/) 下载的免费版本，保留原始 ZIP 和作者预览图。

2026-10-16 整理：当前收录 20 个免费模型，上限 35 个，优先收录宇痕冫的模型。ZIP 总计 352,962,837 字节（约 336.6 MiB）。全部 ZIP 已通过 CRC、SHA-256 及预览图检查。

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

## 模型列表

| 模型 | 作者 | ZIP 大小 | 预览 | 下载 |
| --- | --- | ---: | --- | --- |
| xiaohei-cat | [树苗](https://admin.bongocat.pet/authors/15b2d975-220f-47de-97c5-37d0efb06169) | 1.47 MiB | [预览](model/xiaohei-cat/preview.webp) | [ZIP](model/xiaohei-cat/model.zip) |
| lucky-plush-2 | [树苗](https://admin.bongocat.pet/authors/15b2d975-220f-47de-97c5-37d0efb06169) | 1.47 MiB | [预览](model/lucky-plush-2/preview.webp) | [ZIP](model/lucky-plush-2/model.zip) |
| lucky2 | [树苗](https://admin.bongocat.pet/authors/15b2d975-220f-47de-97c5-37d0efb06169) | 1.47 MiB | [预览](model/lucky2/preview.webp) | [ZIP](model/lucky2/model.zip) |
| sage免费版 | [Sisya](https://admin.bongocat.pet/authors/3886c5f7-9ea4-411c-81dd-a720cb7103f0) | 2.44 MiB | [预览](model/sage%E5%85%8D%E8%B4%B9%E7%89%88/preview.webp) | [ZIP](model/sage%E5%85%8D%E8%B4%B9%E7%89%88/model.zip) |
| 月岛水希 | [めお_314](https://admin.bongocat.pet/authors/4f953388-fddd-45a9-82d0-dcf0974f00f9) | 1.85 MiB | [预览](model/%E6%9C%88%E5%B2%9B%E6%B0%B4%E5%B8%8C/preview.webp) | [ZIP](model/%E6%9C%88%E5%B2%9B%E6%B0%B4%E5%B8%8C/model.zip) |
| 弗洛洛-无表情版 | [宇痕冫](https://space.bilibili.com/348616056) | 11.60 MiB | [预览](model/%E5%BC%97%E6%B4%9B%E6%B4%9B-%E6%97%A0%E8%A1%A8%E6%83%85%E7%89%88/preview.webp) | [ZIP](model/%E5%BC%97%E6%B4%9B%E6%B4%9B-%E6%97%A0%E8%A1%A8%E6%83%85%E7%89%88/model.zip) |
| 莫宁-无表情版 | [宇痕冫](https://space.bilibili.com/348616056) | 15.53 MiB | [预览](model/%E8%8E%AB%E5%AE%81-%E6%97%A0%E8%A1%A8%E6%83%85%E7%89%88/preview.webp) | [ZIP](model/%E8%8E%AB%E5%AE%81-%E6%97%A0%E8%A1%A8%E6%83%85%E7%89%88/model.zip) |
| 千咲-无表情版 | [宇痕冫](https://space.bilibili.com/348616056) | 15.64 MiB | [预览](model/%E5%8D%83%E5%92%B2-%E6%97%A0%E8%A1%A8%E6%83%85%E7%89%88/preview.webp) | [ZIP](model/%E5%8D%83%E5%92%B2-%E6%97%A0%E8%A1%A8%E6%83%85%E7%89%88/model.zip) |
| 恐龙流萤-无表情版 | [宇痕冫](https://space.bilibili.com/348616056) | 16.18 MiB | [预览](model/%E6%81%90%E9%BE%99%E6%B5%81%E8%90%A4-%E6%97%A0%E8%A1%A8%E6%83%85%E7%89%88/preview.webp) | [ZIP](model/%E6%81%90%E9%BE%99%E6%B5%81%E8%90%A4-%E6%97%A0%E8%A1%A8%E6%83%85%E7%89%88/model.zip) |
| 星见雅-无表情版 | [宇痕冫](https://space.bilibili.com/348616056) | 16.23 MiB | [预览](model/%E6%98%9F%E8%A7%81%E9%9B%85-%E6%97%A0%E8%A1%A8%E6%83%85%E7%89%88/preview.webp) | [ZIP](model/%E6%98%9F%E8%A7%81%E9%9B%85-%E6%97%A0%E8%A1%A8%E6%83%85%E7%89%88/model.zip) |
| 仇远-无表情版 | [宇痕冫](https://space.bilibili.com/348616056) | 18.69 MiB | [预览](model/%E4%BB%87%E8%BF%9C-%E6%97%A0%E8%A1%A8%E6%83%85%E7%89%88/preview.webp) | [ZIP](model/%E4%BB%87%E8%BF%9C-%E6%97%A0%E8%A1%A8%E6%83%85%E7%89%88/model.zip) |
| 尤诺-无表情版 | [宇痕冫](https://space.bilibili.com/348616056) | 20.24 MiB | [预览](model/%E5%B0%A4%E8%AF%BA-%E6%97%A0%E8%A1%A8%E6%83%85%E7%89%88/preview.webp) | [ZIP](model/%E5%B0%A4%E8%AF%BA-%E6%97%A0%E8%A1%A8%E6%83%85%E7%89%88/model.zip) |
| 爱弥斯-无表情版 | [宇痕冫](https://space.bilibili.com/348616056) | 20.79 MiB | [预览](model/%E7%88%B1%E5%BC%A5%E6%96%AF-%E6%97%A0%E8%A1%A8%E6%83%85%E7%89%88/preview.webp) | [ZIP](model/%E7%88%B1%E5%BC%A5%E6%96%AF-%E6%97%A0%E8%A1%A8%E6%83%85%E7%89%88/model.zip) |
| 赛琳娜-无表情版 | [宇痕冫](https://space.bilibili.com/348616056) | 22.91 MiB | [预览](model/%E8%B5%9B%E7%90%B3%E5%A8%9C-%E6%97%A0%E8%A1%A8%E6%83%85%E7%89%88/preview.webp) | [ZIP](model/%E8%B5%9B%E7%90%B3%E5%A8%9C-%E6%97%A0%E8%A1%A8%E6%83%85%E7%89%88/model.zip) |
| 卡提-无表情版 | [宇痕冫](https://space.bilibili.com/348616056) | 23.35 MiB | [预览](model/%E5%8D%A1%E6%8F%90-%E6%97%A0%E8%A1%A8%E6%83%85%E7%89%88/preview.webp) | [ZIP](model/%E5%8D%A1%E6%8F%90-%E6%97%A0%E8%A1%A8%E6%83%85%E7%89%88/model.zip) |
| 达妮娅-无表情版 | [宇痕冫](https://space.bilibili.com/348616056) | 24.45 MiB | [预览](model/%E8%BE%BE%E5%A6%AE%E5%A8%85-%E6%97%A0%E8%A1%A8%E6%83%85%E7%89%88/preview.webp) | [ZIP](model/%E8%BE%BE%E5%A6%AE%E5%A8%85-%E6%97%A0%E8%A1%A8%E6%83%85%E7%89%88/model.zip) |
| 大月下-无表情版 | [宇痕冫](https://space.bilibili.com/348616056) | 24.87 MiB | [预览](model/%E5%A4%A7%E6%9C%88%E4%B8%8B-%E6%97%A0%E8%A1%A8%E6%83%85%E7%89%88/preview.webp) | [ZIP](model/%E5%A4%A7%E6%9C%88%E4%B8%8B-%E6%97%A0%E8%A1%A8%E6%83%85%E7%89%88/model.zip) |
| 守岸人-无表情版 | [宇痕冫](https://space.bilibili.com/348616056) | 27.17 MiB | [预览](model/%E5%AE%88%E5%B2%B8%E4%BA%BA-%E6%97%A0%E8%A1%A8%E6%83%85%E7%89%88/preview.webp) | [ZIP](model/%E5%AE%88%E5%B2%B8%E4%BA%BA-%E6%97%A0%E8%A1%A8%E6%83%85%E7%89%88/model.zip) |
| 菲比-无表情版 | [宇痕冫](https://space.bilibili.com/348616056) | 34.73 MiB | [预览](model/%E8%8F%B2%E6%AF%94-%E6%97%A0%E8%A1%A8%E6%83%85%E7%89%88/preview.webp) | [ZIP](model/%E8%8F%B2%E6%AF%94-%E6%97%A0%E8%A1%A8%E6%83%85%E7%89%88/model.zip) |
| 爱莉-无表情版 | [宇痕冫](https://space.bilibili.com/348616056) | 35.52 MiB | [预览](model/%E7%88%B1%E8%8E%89-%E6%97%A0%E8%A1%A8%E6%83%85%E7%89%88/preview.webp) | [ZIP](model/%E7%88%B1%E8%8E%89-%E6%97%A0%E8%A1%A8%E6%83%85%E7%89%88/model.zip) |
