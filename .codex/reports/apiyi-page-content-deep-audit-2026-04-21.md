# API易逐页内容深度审计（基础 / 图片 / 视频 API）

审计时间：2026-04-21  
竞品站点：[https://docs.apiyi.com/](https://docs.apiyi.com/)  
本项目：`/Users/laozhang/Projects/docs`

## 核对方式

- 使用 Computer Use 打开真实站点，确认顶部公告、主导航、左侧栏、右侧筛选、页面首屏结构。
- 抓取 `https://docs.apiyi.com/sitemap.xml`，提取 `api-capabilities` 下中英文页面。
- 抓取页面 HTML，抽取每页 H1、首屏说明、H2/H3、表格数、代码块数、模型 ID 和主要端点。
- 对照本项目 `docs.json` 和 `api-capabilities/**.mdx`，只判断与“基础 API、视频 API、图片 API”相关的页面差距。

## 结论

上一轮改造只做到“导航接近”，还没有做到 API易那种“每页一件事”的调用文档密度。API易更强的点不是视觉，而是信息架构：

- 基础 API 页面首屏都先说明调用边界，再给 endpoint / authorization / response / error / code。
- 图片 API 把一个模型族拆成“总览、文生图、图改图、价格、系列对比、单模型详情”，用户不用在长页里找参数。
- 视频 API 把同步、异步、官转、角色接口拆开，每页都有独立端点、流程和代码。
- 页面里表格和代码比例高，尤其 `balance-query`、`openai-sdk`、`openai-responses`、`flux-*`、`sora-*`、`veo/*`。

本轮执行前确认的主要短板：

- `Nano Banana 2` 仍是单页，缺少 API易式 `overview / text-to-image / image-edit` 三页。
- `GPT-Image 系列` 缺少 `GPT-Image-1.5` 独立页，虽然 `model-info` 已提到该模型。
- 图片导航是平铺列表，不如 API易的模型族分组清晰。
- 部分页面有说明性内容，但缺少首屏 API 速查表和“参数说明速查”。

## API易页面清单与内容结构

### 基础 API

| 页面 | 内容结构 | 可借鉴点 |
| --- | --- | --- |
| `/api-capabilities/model-info` | 当前推荐模型、模型分类、定价说明、使用建议、相关资源；14 个表格 | 首屏直接回答“现在该用哪个模型”，不是只列目录 |
| `/api-capabilities/image-video-models` | 图像生成模型、视频生成模型、定价说明；2 个表格 | 把图片/视频模型作为入口页，链接到细页 |
| `/api-capabilities/openai-sdk` | Python / Node.js / .NET / Go / Java SDK，高级功能；31 个代码块 | 每种 SDK 都给可复制配置 |
| `/api-capabilities/openai-responses` | Responses API 端点、模型、参数、实际响应、工具调用；18 个代码块 | 新 API 先给端点和支持模型，再展开能力 |
| `/api-capabilities/claude` | Claude 双格式、Claude Code、OpenAI 兼容、Anthropic 原生；11 个代码块 | 同一模型族按“兼容格式 / 原生格式 / 工具场景”拆 |
| `/api-capabilities/gemini-native-format` | Gemini 原生格式、推理预算、多模态、工具、缓存；16 个代码块 | 适合迁移官方 Gemini SDK 的用户 |
| `/api-capabilities/balance-query` | Authorization 获取、接口信息、请求/响应、换算规则、错误、示例；9 个代码块 | 管理类 API 需要完整 response schema 和错误码 |
| `/api-capabilities/deprecated-models` | 废弃预告、已下线模型；2 个表格 | 生命周期页非常短，但能降低线上迁移风险 |

### 图片 API

| 页面 | 内容结构 | 可借鉴点 |
| --- | --- | --- |
| `/api-capabilities/nano-banana-2-image/overview` | 总览、文生图、图片编辑、核心特性、价格、分辨率、宽高比 | 模型族总览不塞完整代码，只负责选型和入口 |
| `/api-capabilities/nano-banana-2-image/text-to-image` | OpenAPI 参考式页面、POST endpoint、代码示例、参数速查 | 文生图独立成短页，用户能直接复制 |
| `/api-capabilities/nano-banana-2-image/image-edit` | OpenAPI 参考式页面、输入图片 + 指令、代码示例、参数速查 | 图改图独立成短页，避免和文生图混在一起 |
| `/api-capabilities/nano-banana-image/overview` | Nano Banana Pro 总览、最新版本提醒、文生图/编辑入口、价格、错误处理 | 旧路由保留，但首屏指向新版本和稳定版本 |
| `/api-capabilities/nano-banana-image/text-to-image` | Pro 文生图 API 参考 | 与 2 代页面保持同样模板 |
| `/api-capabilities/nano-banana-image/image-edit` | Pro 图片编辑 API 参考 | 与 2 代页面保持同样模板 |
| `/api-capabilities/nano-banana-pricing` | Pro / 2 / 第一代价格、按次/按量、充值、令牌建议；9 个表格 | 价格页独立，不把价格散落在每个调用页 |
| `/api-capabilities/gpt-image-series` | GPT-Image-1.5 / 1 / Mini 对比、快速开始、参数、FAQ | 系列页负责横向选择 |
| `/api-capabilities/gpt-image-1-5` | 1.5 核心特性、与 1 对比、定价、调用、场景、FAQ | 新模型必须独立页，不只在总览里提一句 |
| `/api-capabilities/gpt-image-1` | 参数详解、模型定价、示例、提示词优化；11 个代码块 | 单模型页放完整 SDK 示例 |
| `/api-capabilities/flux-image-generation` | 核心特性、模型对比、宽高比、参数、场景、成本；13 个代码块 | 商业图像模型需要场景示例和成本计算 |
| `/api-capabilities/flux-image-edit` | 核心特性、技术规格、参数、蒙版、编辑场景；22 个代码块 | 编辑类页面重点是输入图片、mask、批量处理 |
| `/api-capabilities/sora-image-generation` | 模型信息、快速开始、尺寸、最佳实践、成本、限制；10 个代码块 | 低价路线需要明确限制 |
| `/api-capabilities/sora-image-edit` | 功能对比、快速开始、场景、高级技巧、FAQ；9 个代码块 | 编辑页需要展示多图融合、风格转换、限制 |
| `/api-capabilities/image-edit` | OpenAI Image Edit 工作原理、mask、完整示例、场景；16 个代码块 | 通用编辑页作为 OpenAI 格式入口 |
| `/api-capabilities/seedream-image` | SeeDream 版本、端点、步骤、cURL；4 个代码块 | 版本与官方来源单独说明 |

### 视频 API

| 页面 | 内容结构 | 可借鉴点 |
| --- | --- | --- |
| `/api-capabilities/sora-2-video` | Sora 2 概述、官方 API、同步调用、模型定价、使用场景；5 个代码块 | 同步页先讲适用场景，再讲端点 |
| `/api-capabilities/sora-2-video-async` | 提交、轮询、下载三步流程、模型定价、批量处理；15 个代码块 | 异步页必须把任务生命周期拆出来 |
| `/api-capabilities/sora-2-video-official` | 官转 vs 官逆、稳定性、定价、异步三步；7 个代码块 | 供应路线差异必须单独成页 |
| `/api-capabilities/sora-2-character-api` | 角色一致性、创建角色、引用 `@id`、电商/动漫场景；11 个代码块 | 特殊能力独立页，不混入视频总览 |
| `/api-capabilities/veo/overview` | 官逆 Flow、基础 URL、版本、服务状态、核心特性；1 个表格 | 总览短，快速说明路线和状态 |
| `/api-capabilities/veo/quick-start` | 同步调用、认证、文生视频、帧转视频、流式响应；4 个代码块 | 快速开始页只保留最短成功路径 |
| `/api-capabilities/veo/async-api` | 模型定价、端点、创建/查询/下载、帧转视频、错误；11 个代码块 | 异步和同步分别维护，避免混乱 |

## 本轮改造任务清单

1. 新增 `GPT-Image-1.5` 中英文页面，并把 GPT-Image 系列导航改为分组。
2. 新增 `Nano Banana 2` 中英文三页：总览、文生图 API、图改图 API。
3. 更新 `image-video-models` 和 `gpt-image-series`，把 GPT-Image-1.5 纳入模型选择和价格表。
4. 更新 `docs.json` 图片 API 导航：模型族用嵌套分组，而不是单纯平铺。
5. 保留现有长页作为历史入口，但导航默认指向更短、更可执行的新细页。

## 2026-04-21 执行记录

已按 API易的信息架构继续收敛，重点不是照搬价格和品牌，而是保持“左侧结构、页面颗粒度、调用文档密度”一致，并替换为老张API的 Base URL、模型 ID、价格和控制台链接。

### 已完成

- `docs.json` 中 `基础 API / 视频 API / 图片 API` 已改为中英文一致结构：
  - 基础 API：8 个页面。
  - 视频 API：Sora 2 四页 + VEO 3.1 三页。
  - 图片 API：Nano Banana 2 三页、Nano Banana Pro 分组、Sora 图片、Flux 图片、GPT-Image 系列、通用编辑、SeeDream。
- 新增 API易式 Nano Banana 2 三页：
  - `api-capabilities/nano-banana-2-image/overview`
  - `api-capabilities/nano-banana-2-image/text-to-image`
  - `api-capabilities/nano-banana-2-image/image-edit`
  - 英文镜像同路径加 `en/` 前缀。
- 新增 `GPT-Image-1.5` 中英文独立页，并把 `gpt-image-series` 更新为 GPT-Image-1.5 / GPT-Image-1 / Mini 的系列入口。
- 新增 `api-capabilities/veo/async-api` 与英文镜像，匹配 API易左侧 VEO 三页结构；旧 `veo-31-async-api` 保留兼容。
- 可见命名统一为 `Nano Banana 2`，主导航和正文链接统一指向 `nano-banana-2-image`；旧 `nano-banana2-image` 文件保留为兼容入口，不再作为主导航目标。

### 校验结果

- `docs.json` 解析通过，导航引用 `142` 个页面，缺失 `0` 个。
- 中英文导航一致：
  - 基础 API / Basic APIs：`8 / 8`
  - 视频 API / Video APIs：`7 / 7`
  - 图片 API / Image APIs：`16 / 16`
- 检查 `docs.json` 引用的 `api-capabilities` 页面：正文 H1 违规 `0` 个，符合 Mintlify frontmatter 自动 H1 规则。
-  scoped 检查基础/视频/图片三类 API 的 `62` 个页面，`242` 个本地链接，断链 `0` 个。
- 本地预览验证通过；当前可访问 `http://localhost:3000`。批量请求基础/视频/图片三类 API 的 `62` 个主导航页面，HTTP 成功 `62` 个，失败 `0` 个。
- 使用 Chrome 打开 `http://localhost:3000/api-capabilities/nano-banana-2-image/overview`，确认左侧栏实际显示 `基础 API / 视频 API / 图片 API`，并且 `Nano Banana 2 生图` 展开为 `总览 / 文生图 API / 图改图 API`。
- `git diff --check` 通过。

### 已知边界

`mintlify broken-links` 全站仍报告 `37` 个历史断链，集中在 `api-reference/`、`scenarios/`、`backup/`、`essentials/` 等旧页面；本次基础 API、视频 API、图片 API 范围内没有新增断链。

## 后续仍可继续优化

- 把 `Nano Banana Standard` 也拆成 `overview / text-to-image / image-edit`，与 2 代和 Pro 保持一致。
- 把 `Veo 3.1` 当前多页与 API易的三页模型再收敛一次，减少重复。
- 为 `balance-query`、`openai-sdk`、`openai-responses` 增加统一的“接口速查”首屏表。
- 增加类似 API易 `live` 的模型状态页；如果没有实时数据源，至少先做“模型公告 / 状态说明”静态入口。
