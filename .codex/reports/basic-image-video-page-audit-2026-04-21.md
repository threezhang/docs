# 基础 / 图片 / 视频 API 页面逐页审计与修正记录

日期：2026-04-21

## 审计边界

- 范围：`docs.json` 中中文 `基础 API`、`视频 API`、`图片 API` 以及英文 `Basic APIs`、`Video APIs`、`Image APIs`。
- 页面数量：中文 46 页，英文 46 页；中英文逻辑页面一一对应。
- 目标：保障导航一致、内容方向正确、价格和调用方式不互相冲突，并记录哪些页面需要修改、哪些页面确认保留。

## 价格和调用方式边界

- 价格源头：本地 `docs.json` banner、现有产品页、模型页和控制台价格入口 `https://api.laozhang.ai/account/pricing`。
- 控制台价格页是 JS 应用，未登录情况下只能确认入口可访问，不能从 HTML 直接抽取实时价格；因此文档中的固定价格只保留已有页面内一致的公开值，并继续提示以控制台实时价格为准。
- 通用 OpenAI 兼容调用统一使用 `https://api.laozhang.ai/v1` 和 `Authorization: Bearer ...`。
- Gemini 原生格式统一记录为 `/v1beta/models/{model}:generateContent`，优先使用 `Authorization: Bearer ...`，旧页面中额外列出的 Google 风格认证只作为兼容说明。

## 导航一致性结果

| 检查项 | 结果 |
| --- | --- |
| 中文三组页面数量 | 46 |
| 英文三组页面数量 | 46 |
| 中英文 slug 顺序 | 一致 |
| 基础 / 图片 / 视频三组名称 | 已同步到中英文对应结构 |
| 新增入口页是否纳入中英文导航 | 已纳入 |

## 本轮已修正的问题

| 问题 | 文件 | 修正 |
| --- | --- | --- |
| 图片选择指南仍使用旧 `Gemini Flash` 入口和旧链接 | `api-capabilities/image-generation-guide.mdx`、`en/api-capabilities/image-generation-guide.mdx` | 改为 `Nano Banana Standard` / `Nano Banana2` 路线，修正价格、场景、FAQ 和入口卡片 |
| Flux 编辑价格与 Flux 编辑页不一致 | `api-capabilities/image-video-models.mdx`、`en/api-capabilities/image-video-models.mdx`、图片选择指南 | 生成与编辑拆开：Pro 生成 `$0.035`，Max 生成/编辑 `$0.07` |
| 英文页内部链接跳回中文路径 | 英文 Sora、Flux、Sora2 troubleshooting 页面 | 全部改为 `/en/...` 对应页面 |
| Sora 中文页链接到不存在的 `/gpt-image-1` | `api-capabilities/sora-image-generation.mdx` | 改为 `/api-capabilities/gpt-image-1` |
| Veo 示例正文误用 `#`，会被识别成 H1 | `api-capabilities/veo/veo-31-examples.mdx`、`en/...` | 改为 Mintlify `Warning` 组件 |
| Nano Banana Pro 图改图 OpenAI 兼容示例使用 Google 风格 header | `api-capabilities/nano-banana-pro-image-edit.mdx`、`en/...` | 改为 `Authorization: Bearer sk-YOUR_API_KEY` |
| 热门模型页使用旧价格域名和过期“January”首屏措辞 | `api-capabilities/model-info.mdx`、`en/...` | 改为 `api.laozhang.ai/account/pricing`，移除首屏过期月份表述 |

## 逐页审计矩阵

| 分组 | 中文页面 | 英文页面 | 处理结果 |
| --- | --- | --- | --- |
| 基础 API | `api-capabilities/model-info` | `en/api-capabilities/model-info` | 已修正价格域名和过期月份表述 |
| 基础 API | `api-capabilities/image-video-models` | `en/api-capabilities/image-video-models` | 已修正 Flux 生成/编辑价格边界 |
| 基础 API | `api-capabilities/openai-sdk` | `en/api-capabilities/openai-sdk` | 已审计；OpenAI 兼容 base URL 和 SDK 路线保留 |
| 基础 API | `api-capabilities/openai-responses` | `en/api-capabilities/openai-responses` | 已审计；`/v1/responses` 入口保留 |
| 基础 API | `api-capabilities/claude` | `en/api-capabilities/claude` | 已审计；OpenAI 兼容调用与控制台价格边界保留 |
| 基础 API | `api-capabilities/gemini-native-format` | `en/api-capabilities/gemini-native-format` | 已审计；Gemini 原生端点和认证方式保留 |
| 基础 API | `api-capabilities/balance-query` | `en/api-capabilities/balance-query` | 已审计；与 FAQ 的 AccessToken、字段和额度换算一致 |
| 基础 API | `api-capabilities/deprecated-models` | `en/api-capabilities/deprecated-models` | 已审计；迁移导向和实时模型状态边界保留 |
| 视频 API | `api-capabilities/seedance2-video-generation` | `en/api-capabilities/seedance2-video-generation` | 已审计；权限门槛、`/v1/videos` 创建/查询流程保留 |
| 视频 API | `api-capabilities/sora2/overview` | `en/api-capabilities/sora2/overview` | 已审计；Sora 2 总览和路线入口保留 |
| 视频 API | `api-capabilities/sora2/models-pricing` | `en/api-capabilities/sora2/models-pricing` | 已审计；模型/价格说明保留，后续以控制台价格为准 |
| 视频 API | `api-capabilities/sora2/character` | `en/api-capabilities/sora2/character` | 已审计；角色创建和复用流程保留 |
| 视频 API | `api-capabilities/sora2/quick-start` | `en/api-capabilities/sora2/quick-start` | 英文页已修不存在的 Best Practices 卡片链接；同步 API 快速开始保留 |
| 视频 API | `api-capabilities/sora2/api-reference` | `en/api-capabilities/sora2/api-reference` | 已审计；技术参数页保留 |
| 视频 API | `api-capabilities/sora2/examples` | `en/api-capabilities/sora2/examples` | 已审计；示例页保留 |
| 视频 API | `api-capabilities/sora2/async-api` | `en/api-capabilities/sora2/async-api` | 已审计；异步任务路线保留 |
| 视频 API | `api-capabilities/sora2/official-forward` | `en/api-capabilities/sora2/official-forward` | 已审计；官转路线和官方稳定性边界保留 |
| 视频 API | `api-capabilities/sora2/troubleshooting` | `en/api-capabilities/sora2/troubleshooting` | 英文页已修跨语言链接；中文页保留 |
| 视频 API | `api-capabilities/veo/veo-31-overview` | `en/api-capabilities/veo/veo-31-overview` | 已审计；Veo 3.1 总览保留 |
| 视频 API | `api-capabilities/veo/veo-31-quick-start` | `en/api-capabilities/veo/veo-31-quick-start` | 已审计；同步 API 快速开始保留 |
| 视频 API | `api-capabilities/veo/veo-31-examples` | `en/api-capabilities/veo/veo-31-examples` | 已修正文 H1；Base64 限制改为 Warning |
| 视频 API | `api-capabilities/veo/veo-31-async-api` | `en/api-capabilities/veo/veo-31-async-api` | 已审计；异步任务路线保留 |
| 视频 API | `api-capabilities/veo/veo-31-best-practices` | `en/api-capabilities/veo/veo-31-best-practices` | 已审计；最佳实践内容保留 |
| 视频 API | `api-capabilities/veo/veo-31-troubleshooting` | `en/api-capabilities/veo/veo-31-troubleshooting` | 已审计；排障结构保留 |
| 视频 API | `api-capabilities/veo/overview` | `en/api-capabilities/veo/overview` | 已审计；旧自定义 API 已标注过时，保留迁移价值 |
| 视频 API | `api-capabilities/veo/quick-start` | `en/api-capabilities/veo/quick-start` | 已审计；旧自定义 API 快速开始保留，并指向新版 |
| 视频 API | `api-capabilities/veo/models-pricing` | `en/api-capabilities/veo/models-pricing` | 已审计；旧自定义 API 价格页保留迁移用途 |
| 视频 API | `api-capabilities/veo/api-reference` | `en/api-capabilities/veo/api-reference` | 已审计；旧接口参考保留迁移用途 |
| 视频 API | `api-capabilities/veo/examples` | `en/api-capabilities/veo/examples` | 已审计；旧示例页保留迁移用途 |
| 视频 API | `api-capabilities/veo/best-practices` | `en/api-capabilities/veo/best-practices` | 已审计；旧最佳实践保留迁移用途 |
| 视频 API | `api-capabilities/veo/troubleshooting` | `en/api-capabilities/veo/troubleshooting` | 已审计；旧错误处理保留迁移用途 |
| 图片 API | `api-capabilities/image-generation-guide` | `en/api-capabilities/image-generation-guide` | 已重写旧 Gemini Flash 路线、价格和入口 |
| 图片 API | `api-capabilities/nano-banana2-image` | `en/api-capabilities/nano-banana2-image` | 已审计；`$0.055`、`gemini-3.1-flash-image-preview` 和双格式调用保留 |
| 图片 API | `api-capabilities/nano-banana-pro-image` | `en/api-capabilities/nano-banana-pro-image` | 已审计；`$0.09`、Pro 定位和双格式调用保留 |
| 图片 API | `api-capabilities/nano-banana-pro-image-edit` | `en/api-capabilities/nano-banana-pro-image-edit` | 已修 OpenAI 兼容示例认证头 |
| 图片 API | `api-capabilities/nano-banana-pricing` | `en/api-capabilities/nano-banana-pricing` | 已审计；新增价格总览保留 |
| 图片 API | `api-capabilities/sora-image-generation` | `en/api-capabilities/sora-image-generation` | 中文缺失链接已修；英文跨语言链接已修 |
| 图片 API | `api-capabilities/sora-image-edit` | `en/api-capabilities/sora-image-edit` | 英文跨语言链接已修；中文页保留 |
| 图片 API | `api-capabilities/nano-banana-image` | `en/api-capabilities/nano-banana-image` | 已审计；Standard `$0.025` 路线保留 |
| 图片 API | `api-capabilities/nano-banana-image-edit` | `en/api-capabilities/nano-banana-image-edit` | 已审计；Standard 编辑 `$0.025` 路线保留 |
| 图片 API | `api-capabilities/flux-image-generation` | `en/api-capabilities/flux-image-generation` | 英文跨语言链接已修；生成价格保留 |
| 图片 API | `api-capabilities/flux-image-edit` | `en/api-capabilities/flux-image-edit` | 英文跨语言链接已修；编辑价格以 `$0.07` 保留 |
| 图片 API | `api-capabilities/gpt-image-series` | `en/api-capabilities/gpt-image-series` | 已审计；新增 GPT-Image 总览保留 |
| 图片 API | `api-capabilities/gpt-image-1` | `en/api-capabilities/gpt-image-1` | 已审计；Token 计费和 Image API 路线保留 |
| 图片 API | `api-capabilities/image-edit` | `en/api-capabilities/image-edit` | 已审计；OpenAI Image Edit API 路线保留 |
| 图片 API | `api-capabilities/seedream-image` | `en/api-capabilities/seedream-image` | 已审计；SeeDream 4.0/4.5 价格边界保留 |

## 验证命令

```bash
node -e "JSON.parse(require('fs').readFileSync('docs.json','utf8')); console.log('docs.json ok')"
node scripts/in-repo-navigation-parity-check.js # 本次实际以内联 Node 脚本执行，结果：46 vs 46, diff 0
node scripts/in-repo-link-check.js # 本次实际以内联 Node 脚本执行，覆盖 Markdown 链接和 href，结果：三组范围内 missing/cross-lang 0
mintlify broken-links
```

说明：`scripts/in-repo-*.js` 是本报告中的命令说明名，实际没有新增脚本文件；本轮用等价的内联 Node 脚本执行，以避免给仓库增加临时校验脚本。

## 验证结果

| 校验 | 结果 |
| --- | --- |
| `docs.json` JSON 解析 | 通过 |
| `docs.json` 页面引用存在性 | 通过 |
| 基础 / 图片 / 视频三组中英文 slug 顺序 | 通过，`zh=46`、`en=46`、`diffs=0` |
| 三组范围内正文 H1 | 通过，`0` 个 |
| 三组范围内 Markdown 链接和 JSX `href` | 通过，缺失链接和跨语言链接均为 `0` |
| 本地预览 | `http://localhost:3001` 下关键页面均返回 `200 OK` |
| `mintlify broken-links` | 仍失败：剩余 37 个 broken links，分布在 19 个历史/非本轮三组页面中 |

剩余 broken links 不在本轮修正范围内，主要集中在 `api-reference/*`、`getting-started.mdx`、`scenarios/*`、`backup/docs-how-to-add-images.md` 和 `essentials/*`。
