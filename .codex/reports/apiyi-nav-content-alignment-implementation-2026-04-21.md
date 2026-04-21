## APIYi 导航与正文对齐实施记录

时间：2026-04-21  
项目：`/Users/laozhang/Projects/docs`  
目标：按 `docs.apiyi.com` 的结构改造老张 API 文档，重点对齐「基础 API / 视频 API / 图片 API」导航和正文内容，同时保留老张 API 的域名、调用方式和价格边界。

## 参考来源

本次使用并归档的 APIYi 来源：

- `https://docs.apiyi.com/`
- `https://docs.apiyi.com/sitemap.xml`
- `https://docs.apiyi.com/llms.txt`
- `https://docs.apiyi.com/llms-full.txt`

完整采集结果已写入：

- `.codex/reports/apiyi-full-navigation-content-inventory-2026-04-21.md`
- `.codex/reports/apiyi-full-navigation-content-inventory-2026-04-21.json`

## 导航落地

`docs.json` 的中英文首页 API 导航已按 APIYi 结构收束：

- 产品基础 / Basics
- 基础 API / Basic API
- 视频 API / Video API
- 图片 API / Image API
- 多模态理解 API / Multimodal Understanding API
- 文本 API / Text API

中文重点路径：

- 基础 API：`model-info`、`image-video-models`、`openai-sdk`、`openai-responses`、`claude`、`gemini-native-format`、`balance-query`、`deprecated-models`
- 视频 API：`sora-2-video`、`sora-2-video-official`、`sora-2-character-api`、`sora-2-video-async`、`veo/overview`、`veo/async-api`、`veo/quick-start`
- 图片 API：`nano-banana-2-image/*`、`nano-banana-image/*`、`nano-banana-pricing`、`sora-image-*`、`flux-image-*`、`gpt-image-*`、`image-edit`、`seedream-image`

英文导航保持同构，统一使用 `en/` 前缀。

## 正文改造原则

- APIYi 品牌、域名和示例密钥已替换为老张 API 表达。
- `api.apiyi.com`、`vip.apiyi.com`、`www.apiyi.com`、`docs.apiyi.com`、`imagen.apiyi.com` 不进入正文。
- 调用域名统一保留 `https://api.laozhang.ai`。
- 图像测试入口保留 `https://yingtu.ai`，国内入口保留 `https://image.laozhang.ai`。
- Nano Banana Pro 参考价保留 `$0.09/张`。
- Nano Banana 2 参考价保留 `$0.055/张`，不再把 `$0.025/张` 作为 Nano Banana 2 主价格。
- 旧 `sora2/*`、`nano-banana-pro-image*`、`nano-banana2-image*`、`veo/veo-31-*` 链接已收束到 APIYi 风格的新路径。

## 兼容重定向

`docs.json` 增加旧路径到新路径的 redirects，避免历史链接直接断开：

- `sora2/*` -> `sora-2-video*`
- `nano-banana-pro-image*` -> `nano-banana-image/*`
- `nano-banana2-image*` -> `nano-banana-2-image/*`
- `veo/veo-31-*` -> `veo/overview`、`veo/async-api`、`veo/quick-start`
- `/models`、`/api-reference/introduction`、旧 integrations 等项目内旧入口也增加了兼容跳转

## 额外清理

- `api-capabilities/balance-query.mdx` 中 APIYi 导出的空 `<img alt="获取系统令牌" />` 已替换为明确的控制台路径说明。
- `backup/docs-how-to-add-images.md` 中示例图片引用改为代码块，避免 Mintlify 把示例占位符当作真实图片链接。

## 验证结果

静态结构校验：

- 导航页面数：134
- 导航引用缺失：0
- 导航页面正文 H1：0
- HTML 注释：0
- APIYi 品牌/域名残留：0
- 主导航页面旧路径残留：0
- 空 `img` 标签：0

Mintlify 官方断链检查：

```bash
mintlify broken-links
```

结果：

```text
success no broken links found
```

本地预览：

- 端口 3000 已被现有 Node 服务占用
- Mintlify 自动使用 `http://localhost:3001`
- 已抽查首页、Sora 2、Nano Banana Pro、Nano Banana 2、Veo 3.1 页面，HTTP 均返回 `200 OK`

## 收尾修正

用户确认后，将正文处理原则调整为：**导航按 APIYi 风格改名和调位置，已有文章内容不覆盖、不丢失**。

因此进行了以下收尾：

- 已恢复被覆盖的原有文章正文，导航改为引用原有文章路径。
- 保留新增补充页：`image-video-models`、`claude`、`gemini-native-format`、`balance-query`、`deprecated-models`、`video-understanding`、`kimi-k2-5`、`text-moderation`、`nano-banana-pricing`、`gpt-image-series`、`gpt-image-1-5`。
- 删除不再用于导航的临时 APIYi 路径页面，避免导航或 redirects 指向临时内容。
- 调整 redirects：不再从原有文章路径跳转到新临时路径；新别名统一跳回原文章路径。
- 从主导航移除一个过短的旧 VEO 自定义示例占位页，文件保留但不作为主导航入口。
- 修正原文章内 2 个旧断链。
- 修正原文章里导致 Lucide CDN 403 的无效 icon 名。

收尾后验证：

```text
导航页面数：174
导航引用缺失：0
短内容/空内容导航页：0
正文 H1：0
redirect 与导航路径冲突：0
mintlify broken-links：success no broken links found
Playwright 抽查 Sora 2 页面：Console 0 errors
```

## 再次深入复查

用户再次要求复查后，按以下标准重新检查：

- 当前 APIYi sitemap / llms 与本项目导航分组是否仍匹配。
- 原有 tracked 文章内容是否被覆盖或大段删除。
- `docs.json` 是否存在导航路径缺失、短内容页、正文 H1、HTML 注释、redirect 与导航路径冲突。
- 真实 Mintlify 页面是否能打开，并检查浏览器 console。
- 当前页面中的 Lucide icon 是否仍有 CDN 403。

复查结论：

- 当前 APIYi sitemap 共 250 条 URL，基础 / 图片 / 视频 / 多模态 / 文本相关路径仍是本次对齐的那组。
- `docs.json` 首页 API 分组保持为：产品基础、基础 API、视频 API、图片 API、多模态理解 API、文本 API。
- 图片 API 顺序已进一步收紧为：Nano Banana 2、Nano Banana Pro、Nano Banana 标准版、价格页、Sora Image、Flux、GPT-Image 系列、通用图像编辑、Seedream、原图像选择指南。
- 文本 API 顺序已进一步收紧为：文本生成、Kimi K2.5、Embedding、Text Moderation、原 Moderation。
- 原有 tracked 文章只有少量非正文语义改动：无效 icon 名替换、Veo 示例中误写成 H1 的两行改为列表、英文首页一个旧 Embeddings 链接改到现有 Models 页。
- `mintlify broken-links` 再次通过：`success no broken links found`。
- 自定义校验结果：导航页面 174；缺失 0；短内容页 0；正文 H1 0；HTML 注释 0；redirect 冲突 0。
- 并发检查 127 个唯一 Lucide icon，最终确认无 403 残留；单次网络 SSL 抖动的 `x.svg` 复测 3 次均为 200。
- Playwright 抽查 `sora2/overview`、`nano-banana-pro-image`、`image-generation-guide`、`veo/veo-31-examples` 均正常打开；关键页面 Console 0 errors，仅保留 Mintlify dev 的 socket warning。
