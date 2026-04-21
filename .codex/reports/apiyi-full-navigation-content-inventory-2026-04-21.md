# APIYi 文档导航与页面内容完整盘点（2026-04-21）

> 目的：给后续改造老张 API 文档提供可追溯基准。本文只记录 APIYi 当前实站结构和页面内容，不对本项目文档做修改。
>
> 抓取来源：浏览器实看 `https://docs.apiyi.com/`，并下载 `sitemap.xml`、`llms.txt`、`llms-full.txt`、首页 HTML。
>
> 关键计数：sitemap 共 249 个 URL，其中中文 126 个、英文 123 个；`llms-full.txt` 提供 131 个中文正文页。中文 sitemap 中 `/` 和 `/live` 未作为独立 `Source:` 进入 `llms-full.txt`，标题来自浏览器/首页 docsConfig。

## 1. 实站布局结果

- 顶部公告：`Nano Banana 2 已上线 | Now Live：Pro 级画质 + Flash 级速度，按量计费低至官网 3 折！`，链接到 `/news/nano-banana-2-launch`。
- 站点 logo：APIYI docs。
- 语言选择：CN / 简体中文；sitemap 同时存在 `/en` 英文镜像。
- 搜索框：居中，placeholder 为“搜索...”，快捷键 `⌘K`。
- 右上外链：`首页` -> `https://api.apiyi.com`，`AI出图` -> `https://imagen.apiyi.com`，`控制台` -> `https://api.apiyi.com/account/profile`，另有深浅色切换。
- 顶部 tab：`首页`、`使用场景`、`常见问题`、`最新公告`、`充值活动`、`API 参考`。
- 首页内容区是三栏：左侧固定导航，中间正文，右侧“在此页面”目录。首页 H1 为“API易 - 企业级 AI 大模型 API 中转站”。

## 2. 中文导航树（按 APIYi 实站顺序）

### 首页 -> `/`

- 产品基础
  - 基本介绍 -> `/`
  - 快速开始 -> `/getting-started`
  - API 手册 -> `/api-manual`
  - 价格说明 -> `/pricing`
- 基础 API
  - 当下热门模型（保持更新） -> `/api-capabilities/model-info`
  - 图像与视频生成模型 -> `/api-capabilities/image-video-models`
  - OpenAI 官方库使用 -> `/api-capabilities/openai-sdk`
  - OpenAI Responses 支持 -> `/api-capabilities/openai-responses`
  - Claude 模型调用指南 -> `/api-capabilities/claude`
  - Gemini 原生格式调用 -> `/api-capabilities/gemini-native-format`
  - 余额查询 API -> `/api-capabilities/balance-query`
  - 废弃模型列表 -> `/api-capabilities/deprecated-models`
- 视频 API
  - Sora 2 视频生成 -> `/api-capabilities/sora-2-video`
  - Sora 2 官方直转 -> `/api-capabilities/sora-2-video-official`
  - Sora 2 角色接口 -> `/api-capabilities/sora-2-character-api`
  - Sora 2 视频生成（异步） -> `/api-capabilities/sora-2-video-async`
  - VEO 3.1 视频生成
    - 综述（官逆Flow） -> `/api-capabilities/veo/overview`
    - 异步调用 API -> `/api-capabilities/veo/async-api`
    - 同步调用 API -> `/api-capabilities/veo/quick-start`
- 图片 API
  - Nano Banana 2 生图
    - Nano Banana 2 生图/编辑 -> `/api-capabilities/nano-banana-2-image/overview`
    - 文生图 API 参考 -> `/api-capabilities/nano-banana-2-image/text-to-image`
    - 图片编辑 API 参考 -> `/api-capabilities/nano-banana-2-image/image-edit`
  - Nano Banana Pro 生图
    - Nano Banana Pro 图片生成 -> `/api-capabilities/nano-banana-image/overview`
    - 文生图 API 参考 -> `/api-capabilities/nano-banana-image/text-to-image`
    - 图片编辑 API 参考 -> `/api-capabilities/nano-banana-image/image-edit`
  - Nano Banana 系列价格总览 -> `/api-capabilities/nano-banana-pricing`
  - Sora Image 生图 API -> `/api-capabilities/sora-image-generation`
  - Sora Image 图片编辑 API -> `/api-capabilities/sora-image-edit`
  - Flux 图像生成 API -> `/api-capabilities/flux-image-generation`
  - Flux 图像编辑 API -> `/api-capabilities/flux-image-edit`
  - GPT-Image 系列
    - GPT-Image 系列图像生成 -> `/api-capabilities/gpt-image-series`
    - GPT-Image-1.5 图像生成 API -> `/api-capabilities/gpt-image-1-5`
    - GPT-Image-1 图像生成 API - OpenAI 当下最新图片 API -> `/api-capabilities/gpt-image-1`
  - 图像编辑 API -> `/api-capabilities/image-edit`
  - SeeDream 4.5 生图/编辑 -> `/api-capabilities/seedream-image`
- 多模态理解 API
  - 图像理解（识图）API -> `/api-capabilities/vision-understanding`
  - 视频理解 API -> `/api-capabilities/video-understanding`
- 文本 API
  - 文本生成（对话补全） -> `/api-capabilities/text-generation`
  - Kimi K2.5 文本生成 -> `/api-capabilities/kimi-k2-5`
  - 文本向量化（Embedding） -> `/api-capabilities/text-embedding`
  - 文本审核（Moderation） -> `/api-capabilities/text-moderation`

### 使用场景 -> `/scenarios`

- 概览
  - 使用场景总览 -> `/scenarios`
- AI Agent
  - OpenClaw
    - OpenClaw -> `/scenarios/agent/openclaw/overview`
    - 安装指南 -> `/scenarios/agent/openclaw/installation`
    - 配置文件方式 -> `/scenarios/agent/openclaw/config-json`
    - CLI 交互式配置 -> `/scenarios/agent/openclaw/config-cli`
    - Anthropic 原生配置 -> `/scenarios/agent/openclaw/config-anthropic`
    - 使用指南 -> `/scenarios/agent/openclaw/usage`
    - 进阶功能与故障排除 -> `/scenarios/agent/openclaw/advanced`
- 对话型 AI
  - Cherry Studio -> `/scenarios/chat/cherry-studio`
  - Chatbox AI -> `/scenarios/chat/chatbox`
  - Open WebUI -> `/scenarios/chat/open-webui`
  - ChatGPT Next Web -> `/scenarios/chat/chatgpt-next-web`
- 编程开发
  - Cline (VS Code) -> `/scenarios/programming/cline`
  - Roo Code (VS Code) -> `/scenarios/programming/roo-code`
  - Gemini CLI -> `/scenarios/programming/gemini-cli`
  - Claude Code -> `/scenarios/programming/claude-code`
  - OpenAI Codex CLI -> `/scenarios/programming/codex-cli`
  - OpenCode -> `/scenarios/programming/opencode`
  - Cursor -> `/scenarios/programming/cursor`
  - CC Switch -> `/scenarios/programming/cc-switch`
- 技术工程
  - LangChain -> `/scenarios/engineering/langchain`
  - Dify -> `/scenarios/engineering/dify`
- 翻译场景
  - Bob 翻译 -> `/scenarios/translation/bob`
  - 沉浸式翻译 -> `/scenarios/translation/immersive`
- 社区贡献
  - Paper2Any 论文多模态工作流 -> `/scenarios/ecosystem/paper2any`
  - ComfyUI 节点合集
    - Nano Banana ComfyUI 节点 -> `/scenarios/ecosystem/nano-banana-comfyui`
    - Luck Nano Banana Pro - ComfyUI 节点 -> `/scenarios/ecosystem/lucknanobananapro-comfyui`
    - Image Annotator - ComfyUI 节点 -> `/scenarios/ecosystem/image-annotator-comfyui`
    - APIYI Nano Banana ComfyUI 节点（轻量示例版） -> `/scenarios/ecosystem/apiyi-nano-banana-node`
  - Nano Banana Pro 生图 Skill -> `/scenarios/ecosystem/nano-banana-skill`
  - Make.com 接入 Gemini 图像理解 -> `/scenarios/ecosystem/make-com-gemini-vision`

### 常见问题 -> `/faq/model-selection-guide`

- 模型与调用
  - 如何选择合适的 AI 模型？ -> `/faq/model-selection-guide`
  - 为什么有些模型我用不了？ -> `/faq/model-availability`
  - 为什么大模型不知道自己的版本号？ -> `/faq/model-version-identity`
  - 模型名称后缀 -c 是什么意思？ -> `/faq/model-name-suffix-c`
  - Base URL 怎么填？/v1、根域名、/v1beta 有什么区别？ -> `/faq/base-url-config`
  - API 可以开多少并发？ -> `/faq/api-concurrency`
  - max_tokens 是什么？不设置会怎样？ -> `/faq/max-tokens`
  - Nano Banana 系列出图失败，常见原因有哪些？ -> `/faq/nano-banana-image-failure`
- 令牌与日志
  - 如何创建 KEY？ -> `/faq/token-management`
  - 令牌需要设置可用模型吗？ -> `/faq/token-model-whitelist`
  - 令牌的按量优先/按次计费有什么区别？ -> `/faq/token-billing-modes`
  - 如何查看我的调用记录？ -> `/faq/call-logs`
  - 为方便排查问题，可以在后台看到详细日志吗？ -> `/faq/user-logs-control`
- 充值与安全
  - 系统里模型的【倍率】是什么？ -> `/faq/model-multiplier`
  - 为什么还有余额跑不通？ -> `/faq/balance-insufficient`
  - 如何设置余额告警提醒？ -> `/faq/balance-alerts`
  - 支持对公或 USDT 付款吗？ -> `/faq/payment-methods`
  - 网站有什么充值活动吗？ -> `/faq/recharge-promotions`
  - API易 的退款政策是怎样的？ -> `/faq/refund-policy`
  - 内容安全如何合规性？ -> `/faq/content-safety`
  - API易如何保障数据安全？ -> `/faq/data-security`
- 网络与连接
  - 使用 API 接口需要代理网络吗？ -> `/faq/network-proxy`
  - API易的服务器在哪里？应该选择什么服务器？ -> `/faq/server-location`
  - 下载 CDN 图片/视频很慢怎么办？ -> `/faq/cdn-download-slow`
- 账号与登录
  - GitHub 登录提示「该账户已绑定」怎么办？ -> `/faq/github-bindng-bindng-error`
  - 忘记密码了怎么办？ -> `/faq/forgot-password`
  - 为什么提示 API Key 无效？ -> `/faq/invalid-api-key`

### 最新公告 -> `/changelog`

- 更新日志
  - 网站公告 -> `/changelog`
  - 实时动态 -> `/live`
- AI风向标
  - Claude Opus 4.7 重磅上线：编程再进化，视觉能力三倍升级 -> `/news/claude-opus-4-7-launch`
  - GLM-5.1 上线：智谱开源最强编程 Agent 模型 -> `/news/glm-5-1-launch`
  - Qwen3.6-Plus 上线：阿里千问最强编程 Agent 模型 -> `/news/qwen-3-6-plus-launch`
  - Gemini Embedding 2 Preview 上线：首个原生多模态嵌入模型 -> `/news/gemini-embedding-2-preview-launch`
  - Seed 2.0 Pro 旗舰版上线：字节跳动最强推理模型 -> `/news/seed-2-0-pro-launch`
  - MiniMax-M2.7 上线：10B 参数的自进化智能体模型，性价比惊人 -> `/news/minimax-m2-7-launch`
  - MiMo-V2 系列上线：小米万亿参数智能体模型，性能逼近 Opus 4.6 -> `/news/mimo-v2-launch`
  - Grok 4.20 Beta 系列上线：四智能体协作架构，200 万上下文 -> `/news/grok-4-20-beta-launch`
  - GPT-5.4 Mini & Nano 上线：轻量高性价比，为规模化场景而生 -> `/news/gpt-5-4-mini-nano-launch`
  - Seed 2.0 Lite 上线：字节跳动高性价比企业级多模态模型 -> `/news/seed-2-0-lite-launch`
  - GPT-5.4 重磅发布：OpenAI 最强专业模型，原生计算机使用能力 -> `/news/gpt-5-4-launch`
  - Gemini 3.1 Flash Lite Preview：谷歌最新轻量级模型，代理任务与低延迟场景首选 -> `/news/gemini-3-1-flash-lite-preview-launch`
  - GPT-5.3 Chat 上线：更少幻觉、更自然的 ChatGPT 聊天模型 -> `/news/gpt-5-3-chat-launch`
  - Nano Banana 2 上线：Pro画质 Flash价格 -> `/news/nano-banana-2-launch`
  - Gemini 3 Flash Preview 震撼发布：Pro 级性能，Flash 级速度 -> `/news/gemini-3-flash-preview-launch`
  - OpenAI GPT Image 1.5 正式上线：4倍速度提升，精准编辑新体验 -> `/news/gpt-image-1-5-launch`
  - GPT-5.2 重磅发布：OpenAI 反击 Gemini 3，推出三大版本应对竞争 -> `/news/gpt-5-2-launch`
  - SeeDream 4.5 震撼上线：BytePlus 火山方舟最强 4K 图像生成模型 -> `/news/seedream-4-5-launch`
  - Claude Opus 4.5 震撼发布：编程能力登顶，价格降至原版 1/3 -> `/news/claude-opus-4-5-launch`
  - Gemini 2.5 Flash Lite：谷歌最快最省的轻量级模型，海量文本处理首选 -> `/news/gemini-2-5-flash-lite-preview-launch`
  - Google AI Studio 使用指南：轻松体验 Gemini 模型的三种方案 -> `/news/google-ai-studio-usage-guide`
  - Gemini 3 Pro Preview 正式发布：LMArena 全球第一 -> `/news/gemini-3-pro-preview-launch`
  - Nano Banana Pro 震撼上线：4K高清图像生成 -> `/news/nano-banana-pro-launch`

### 充值活动 -> `/faq/recharge-promotions`

- 优惠活动
  - 网站有什么充值活动吗？ -> `/faq/recharge-promotions`

### API 参考 -> `/api-reference/chat/chat-completions`

- API 参考
  - Chat Completions -> `/api-reference/chat/chat-completions`
  - List Models -> `/api-reference/models/list-models`
  - Create Embeddings -> `/api-reference/embeddings/create-embeddings`

## 3. 核心页面内容索引（首页 / 基础 API / 视频 API / 图片 API / 多模态 / 文本）

| Path | Title | Lastmod | Code blocks | Table lines | H2/H3 outline |
| --- | --- | --- | ---: | ---: | --- |
| `/api-capabilities/balance-query` | 余额查询 API | 2026-01-28 | 9 | 22 | H2 接口概述 / H2 如何获取 Authorization / H2 接口信息 / H2 请求说明 / H3 请求 Headers / H3 请求参数 / H2 响应说明 / H3 成功响应示例 / H3 核心响应字段说明 / H3 额度换算说明 / H2 错误响应 / H3 HTTP 401 - 认证失败 |
| `/api-capabilities/claude` | Claude 模型调用指南 | 2026-03-19 | 11 | 19 | H2 核心优势 / H2 可用模型 / H2 OpenAI 兼容格式调用 / H3 Python 示例 / H3 Node.js 示例 / H3 cURL 示例 / H2 Anthropic 原生格式调用 / H3 Python 原生 SDK / H3 流式响应 / H3 视觉理解（多模态） / H2 推理深度控制（effort 参数） / H3 Anthropic 原生格式设置 effort |
| `/api-capabilities/deprecated-models` | 废弃模型列表 | 2026-03-12 | 0 | 13 | H2 说明 / H2 ⚠️ 废弃模型预告 / H2 🚫 已下线模型 |
| `/api-capabilities/flux-image-edit` | Flux 图像编辑 API | 2026-01-28 | 23 | 21 | H2 🌟 核心特性 / H2 📋 技术规格 / H2 🚀 快速开始 / H3 基础示例 - 本地图片编辑 / H2 📝 参数详解 / H3 核心参数 / H3 通过 extra_body 传递的参数 / H3 高级示例 - 在线图片编辑 / H3 批量编辑示例 / H2 🎯 专业编辑技巧 / H3 1. 文字编辑和添加 / H3 2. 智能上下文保持 |
| `/api-capabilities/flux-image-generation` | Flux 图像生成 API | 2026-01-28 | 14 | 22 | H2 🌟 核心特性 / H2 📋 模型对比 / H2 📐 支持的宽高比 / H2 🚀 快速开始 / H3 基础示例 / H2 📝 参数详解 / H3 通过 extra_body 传递的参数 / H3 高级示例 - 批量生成不同比例 / H3 Node.js 示例 / H2 🎯 使用场景 / H3 1. Web 设计素材 / H3 2. 社交媒体内容 |
| `/api-capabilities/gemini-native-format` | Gemini 原生格式调用 | 2026-01-28 | 16 | 16 | H2 优势 / H2 配置与使用 / H3 环境准备 / H3 基础配置 / H2 基础文本生成 / H3 非流式响应 / H3 流式响应 / H2 Gemini 2.5 系列推理功能 / H3 推理模型类型 / H3 控制推理预算 / H3 显示思考过程 / H2 多模态处理 |
| `/api-capabilities/gpt-image-1` | GPT-Image-1 图像生成 API - OpenAI 当下最新图片 API | 2026-03-21 | 11 | 51 | H2 概述 / H3 主要特性 / H2 快速开始 / H3 基础配置 / H3 生成图像 / H2 API 参数详解 / H3 请求参数 / H3 参数详细说明 / H3 响应格式 / H2 模型与定价 / H3 可用模型 / H3 定价方式 |
| `/api-capabilities/gpt-image-1-5` | GPT-Image-1.5 图像生成 API | 2026-03-21 | 7 | 39 | H2 核心特性 / H2 与 GPT-Image-1 对比 / H2 模型定价 / H3 Token 计费 / H3 按图片计费 / H2 API 调用方式 / H3 端点地址 / H3 请求示例 / H2 请求参数 / H2 响应格式 / H2 最佳应用场景 / H3 信息图和文字排版 |
| `/api-capabilities/gpt-image-series` | GPT-Image 系列图像生成 | 2026-04-13 | 1 | 19 | H2 模型对比 / H2 快速开始 / H2 通用参数 / H2 详细文档 / H2 常见问题 / H2 相关资源 |
| `/api-capabilities/image-edit` | 图像编辑 API | 2026-01-28 | 16 | 9 | H2 概述 / H2 API 工作原理 / H2 快速开始 / H3 基础配置 / H3 基本编辑示例 / H2 API 参数详解 / H3 请求参数 / H3 响应格式 / H2 创建遮罩图像 / H3 使用 Python PIL 创建遮罩 / H3 使用圆形遮罩 / H2 完整使用示例 |
| `/api-capabilities/image-video-models` | 图像与视频生成模型 | 2026-04-14 | 0 | 19 | H2 🎨 图像生成模型 / H2 🎬 视频生成模型 / H2 💰 定价说明 |
| `/api-capabilities/kimi-k2-5` | Kimi K2.5 文本生成 | 2026-04-20 | 9 | 30 | H2 核心优势 / H2 模型信息 / H2 定价 / H2 如何开启 Thinking 模式 / H3 cURL 示例（开启 Thinking） / H2 调用方式 / H3 端点地址 / H3 基础调用（Instant 模式） / H3 进阶调用（Thinking 模式） / H3 流式输出 / H2 请求参数 / H2 响应格式 |
| `/api-capabilities/model-info` | 当下热门模型（保持更新） | 2026-03-15 | 0 | 86 | H2 🔥 当前推荐模型 / H2 模型分类 / H3 🤖 OpenAI 系列 / H3 🎭 Claude 系列 (Anthropic) / H3 🌟 Google Gemini 系列 / H3 🚀 xAI Grok 系列 / H3 🔍 DeepSeek 系列 / H3 🐘 国产模型系列 / H3 🌐 MiniMax 系列 / H2 💰 定价说明 / H3 计费方式 / H3 价格优势 |
| `/api-capabilities/nano-banana-2-image/image-edit` | 图片编辑 API 参考 | 2026-04-16 | 4 | 10 | H2 代码示例 / H3 Python / H3 Node.js / H3 cURL / H2 参数说明速查 |
| `/api-capabilities/nano-banana-2-image/overview` | Nano Banana 2 生图/编辑 | 2026-04-13 | 0 | 31 | H2 概述 / H2 核心特性 / H2 版本对比 / H2 模型定价 / H3 按次计费 / H3 按量计费（Nano Banana 2 专属） / H3 按量计费价格预估 / H2 支持的分辨率与宽高比 / H3 输出分辨率 / H3 支持的宽高比（14 种） / H2 常见问题 / H2 相关文档 |
| `/api-capabilities/nano-banana-2-image/text-to-image` | 文生图 API 参考 | 2026-04-16 | 3 | 8 | H2 代码示例 / H3 Python / H3 cURL / H3 Node.js / H2 参数说明速查 |
| `/api-capabilities/nano-banana-image/image-edit` | 图片编辑 API 参考 | 2026-04-16 | 4 | 8 | H2 代码示例 / H3 Python / H3 Node.js / H3 cURL / H2 参数说明速查 |
| `/api-capabilities/nano-banana-image/overview` | Nano Banana Pro 图片生成 | 2026-04-16 | 1 | 7 | H3 最新版本 / H3 前代版本 / H2 在线调试 API / H2 调用方式 / H3 不支持的功能 / H2 价格对比 / H2 兼容性说明 / H3 升级到最新版本 / H3 使用稳定版本 / H2 API 错误处理指南 / H2 FAQ / H2 相关文档 |
| `/api-capabilities/nano-banana-image/text-to-image` | 文生图 API 参考 | 2026-04-16 | 3 | 6 | H2 代码示例 / H3 Python / H3 cURL / H3 Node.js / H2 参数说明速查 |
| `/api-capabilities/nano-banana-pricing` | Nano Banana 系列价格总览 | 2026-04-16 | 0 | 46 | H2 概述 / H2 三款模型速览 / H2 Nano Banana Pro 定价 / H3 按次计费 / H3 按量计费（未开放，可内测） / H2 Nano Banana 2 定价 / H3 按次计费 / H3 按量计费 / H2 Nano Banana 第一代定价 / H2 充值活动：更能降本 / H2 令牌类型选择建议 / H2 相关文档 |
| `/api-capabilities/openai-responses` | OpenAI Responses 支持 | 2026-01-28 | 21 | 40 | H2 🚀 核心特性 / H2 📋 支持的模型 / H3 推理模型（推荐） / H3 对话模型 / H2 🔧 基础用法 / H3 简单对话 / H3 实际响应示例 / H2 📊 请求参数详解 / H3 必需参数 / H3 可选参数 / H2 🛠️ 内置工具支持 / H3 1. 函数调用 |
| `/api-capabilities/openai-sdk` | OpenAI 官方库使用 | 2026-01-28 | 31 | 0 | H2 支持的官方 SDK / H2 Python SDK / H3 安装 / H3 基础配置 / H3 环境变量配置 / H3 异步使用 / H3 流式输出 / H2 Node.js SDK / H3 安装 / H3 基础配置 / H3 环境变量配置 / H3 流式输出 |
| `/api-capabilities/seedream-image` | SeeDream 4.5 生图/编辑 | 2026-04-13 | 4 | 7 | H2 概述 / H3 可用版本 / H2 调用方式 / H3 正确端点 ✅ / H2 Python 示例代码 / H2 使用步骤 / H2 cURL 示例 / H2 价格对比 / H2 特性对比 / H3 质量特点 / H3 API 特性 / H2 支持的尺寸 |
| `/api-capabilities/sora-2-character-api` | Sora 2 角色接口 | 2026-01-28 | 13 | 22 | H2 概述 / H2 核心要义 / H2 为什么需要角色？ / H3 电商场景 / H3 动漫场景 / H3 其他场景 / H2 端点地址 / H2 请求参数 / H3 参数说明 / H2 代码示例 / H3 cURL 示例 / H3 Python 示例 |
| `/api-capabilities/sora-2-video` | Sora 2 视频生成 | 2026-01-28 | 7 | 7 | H2 概述 / H2 详细文档【飞书版】 / H2 核心特性 / H2 模型定价 / H2 调用方式 / H3 端点地址 / H3 文生视频 / H3 图生视频 / H2 响应格式 / H3 流式输出 / H3 生成时间 / H2 使用场景 |
| `/api-capabilities/sora-2-video-async` | Sora 2 视频生成（异步） | 2026-01-28 | 23 | 36 | H2 概述 / H2 核心特性 / H2 完整流程 / H2 模型定价 / H2 端点地址 / H2 第一步：提交视频生成请求 / H3 请求参数 / H3 文生视频示例 / H3 图生视频示例 / H3 响应格式 / H2 第二步：轮询查询视频状态 / H3 请求方式 |
| `/api-capabilities/sora-image-edit` | Sora Image 图片编辑 API | 2026-04-13 | 9 | 12 | H2 🌟 核心特性 / H2 📋 功能对比 / H2 🚀 快速开始 / H3 基础示例 - 单张图片编辑 / H3 高级示例 - 多图融合 / H2 🎯 编辑场景示例 / H3 1. 风格转换 / H3 2. 智能抠图换背景 / H3 3. 物体编辑 / H3 4. 颜色和光线调整 / H2 💡 高级技巧 / H3 1. 批量处理优化 |
| `/api-capabilities/sora-image-generation` | Sora Image 生图 API | 2026-01-28 | 10 | 14 | H2 🌟 核心特性 / H2 📋 模型信息 / H2 🚀 快速开始 / H3 基础示例 / H3 批量生成示例 / H2 📐 尺寸比例说明 / H3 尺寸使用示例 / H2 🎯 最佳实践 / H3 1. 提示词优化 / H3 2. 错误处理 / H3 3. 结果保存 / H2 💡 高级技巧 |
| `/api-capabilities/text-embedding` | 文本向量化（Embedding） | 2026-01-28 | 17 | 12 | H2 🌟 核心特性 / H2 📋 支持的 Embedding 模型 / H2 🚀 快速开始 / H3 1. 最简单示例 - 使用 curl 命令 / H3 2. 基础示例 - 使用 OpenAI SDK / H3 3. 批量文本向量化 / H3 4. 使用 requests 库 / H2 🎯 典型应用场景 / H3 1. 语义搜索引擎 / H3 2. 构建向量数据库 / H3 3. 文本去重和聚类 / H3 4. RAG（检索增强生成）系统 |
| `/api-capabilities/text-generation` | 文本生成（对话补全） | 2026-01-28 | 19 | 7 | H2 功能概述 / H2 快速开始 / H3 基础对话示例 / H3 多轮对话示例 / H2 核心参数详解 / H3 model（必填） / H3 messages（必填） / H3 temperature（可选） / H3 max_tokens（可选） / H3 top_p（可选） / H3 stream（可选） / H2 高级用法 |
| `/api-capabilities/text-moderation` | 文本审核（Moderation） | 2026-01-28 | 13 | 13 | H2 功能概述 / H3 主要能力 / H2 快速开始 / H3 基础调用示例 / H3 批量检测示例 / H2 审核类别 / H3 OpenAI Moderation 支持的类别 / H2 返回结果详解 / H3 响应结构 / H3 字段说明 / H2 集成示例 / H3 聊天内容审核 |
| `/api-capabilities/veo/async-api` | 异步调用 API | 2026-01-29 | 21 | 37 | H2 模型与定价 / H2 API 端点 / H3 1. 创建视频任务 / H3 2. 查询任务状态 / H3 3. 获取视频内容 / H2 完整调用流程 / H2 Python 完整示例 / H2 帧转视频模式 / H3 请求参数 / H3 首帧模式示例（单图） / H3 首尾帧模式示例（双图） / H3 响应与后续处理 |
| `/api-capabilities/veo/overview` | 综述（官逆Flow） | 2026-01-29 | 0 | 10 | H2 综述 / H2 核心特性 / H2 调用方式 / H2 支持的模型 / H2 开始使用 / H2 相关链接 |
| `/api-capabilities/veo/quick-start` | 同步调用 API | 2026-01-29 | 4 | 6 | H2 同步调用说明 / H2 快速开始 / H2 认证方式 / H2 示例 1：文生视频 / H3 参数说明 / H2 示例 2：帧转视频（Frame-to-Video） / H3 图片参数说明 / H2 流式响应说明 / H3 响应示例 / H3 响应说明 / H2 生成速度 / H2 下一步 |
| `/api-capabilities/video-understanding` | 视频理解 API | 2026-01-28 | 13 | 8 | H2 🌟 核心特性 / H2 📋 支持的视频理解模型 / H2 🚀 快速开始 / H3 1. 基础示例 - 本地视频 Base64 编码 / H3 2. 完整示例 - 包含结果保存 / H3 3. 使用 requests 库的示例 / H2 🎯 常见应用场景 / H3 1. 视频内容摘要 / H3 2. 教学视频分析 / H3 3. 监控视频分析 / H3 4. 营销视频评估 / H3 5. 体育动作分析 |
| `/api-capabilities/vision-understanding` | 图像理解（识图）API | 2026-01-28 | 12 | 13 | H2 🌟 核心特性 / H2 📋 支持的视觉模型 / H2 🚀 快速开始 / H3 1. 基础示例 - 图片 URL / H3 2. 本地图片示例 - Base64 编码 / H3 3. 高级示例 - 多图对比分析 / H2 🎯 常见应用场景 / H3 1. 商品识别与分析 / H3 2. 文档 OCR 识别 / H3 3. 医学影像辅助分析 / H3 4. 安全监控场景分析 / H2 💡 最佳实践 |
| `/api-manual` | API 手册 | 2026-03-19 | 34 | 56 | H2 平台特色 / H3 OpenAI 兼容模式 / H3 功能支持范围 / H3 简单切换模型 / H2 快速开始 / H3 获取API Key / H3 查看请求示例 / H2 基础信息 / H3 API 端点 / H3 认证方式 / H3 请求格式 / H2 核心接口 |
| `/getting-started` | 快速开始 | 2026-04-01 | 5 | 0 | H2 第一步：账户准备 / H3 1.1 注册账号 / H3 1.2 账户充值 / H2 第二步：创建 API 密钥 / H3 2.1 生成密钥 / H2 第三步：开始调用 / H3 3.1 获取接入信息 / H3 3.2 测试调用 / H3 3.3 代码示例 / H2 下一步 / H2 常见问题 / H3 如何切换模型？ |
| `/` | 基本介绍 | 2026-04-14 | - | - | sitemap-only / no llms-full Source |
| `/pricing` | 价格说明 | 2026-03-31 | 1 | 0 | H2 API易 定价原则 / H3 1. 模型价格对齐 / H2 充值优势 / H3 2. 汇率优惠 / H3 3. 充值赠送 / H2 API易 比官网的更多优势 / H2 科普：计费基础知识 / H3 什么是『按量计费』？ / H3 计费模式优先级 / H3 『按次计费』场景 / H3 什么是 Tokens？ / H3 提示词与补全 |

## 4. FAQ 页面内容索引

| Path | Title | Lastmod | Code blocks | Table lines | H2/H3 outline |
| --- | --- | --- | ---: | ---: | --- |
| `/faq/api-concurrency` | API 可以开多少并发？ | 2026-04-01 | 0 | 5 | H2 简短回答 / H2 不同模型类型的并发限制 / H2 为什么图片模型有并发控制？ / H2 并发计算方式 / H3 按单一模型计算 / H2 如何申请更高并发？ / H3 个人用户 / H3 企业客户 / H2 常见问题 / H2 并发优化建议 / H2 联系我们 |
| `/faq/balance-alerts` | 如何设置余额告警提醒？ | 2026-04-11 | 0 | 0 | H2 简短回答 / H2 告警方式详解 / H2 配置步骤 / H2 告警渠道推荐 / H2 常见问题 / H2 相关文档 |
| `/faq/balance-insufficient` | 为什么还有余额跑不通？ | 2026-04-01 | 0 | 0 | H2 请求预扣机制 / H2 常见原因分析 / H3 1. 输入内容Token超长 / H3 2. 超过模型上下文限制 / H2 解决方案 / H3 1. 检查输入内容 / H3 2. 检查账户余额 / H3 3. 选择合适的模型 / H3 4. 分析Token使用 / H2 技术支持 / H2 预防措施 / H3 1. 内容预处理 |
| `/faq/base-url-config` | Base URL 怎么填？/v1、根域名、/v1beta 有什么区别？ | 2026-03-26 | 3 | 36 | H2 快速答案 / H2 为什么不同模型的 Base URL 不一样？ / H2 代码示例 / H3 OpenAI 兼容模型（GPT / DeepSeek / Llama 等） / H3 Claude 模型（Anthropic SDK） / H3 Gemini 模型（Google GenAI SDK） / H2 域名节点选择 / H2 常见报错排查 / H2 完整配置速查 / H3 OpenAI 兼容模型 / H3 Claude 模型（Anthropic SDK） / H3 Gemini 模型 |
| `/faq/call-logs` | 如何查看我的调用记录？ | 2026-01-28 | 0 | 0 | H2 访问调用日志 / H2 日志记录内容 / H3 成功调用记录 / H3 报错日志 / H2 隐私和数据政策 / H2 日志查看技巧 / H3 筛选功能 / H3 计费分析 / H2 常见问题 / H3 为什么看不到具体的对话内容？ / H3 日志保存多长时间？ / H3 如何导出调用记录？ |
| `/faq/cdn-download-slow` | 下载 CDN 图片/视频很慢怎么办？ | 2026-04-11 | 7 | 0 | H2 简短回答 / H2 常见原因分析 / H2 排查步骤 / H2 解决方案 / H3 方案一：更换公共 DNS（最简单） / H3 方案二：优化下载方式 / H3 方案三：更换服务器所在区域 / H3 方案四：中转落盘（终极方案） / H2 常见问题 / H2 相关文档 |
| `/faq/content-safety` | 内容安全如何合规性？ | 2026-04-01 | 0 | 0 | H2 内容安全保障体系 / H2 内容审核机制 / H3 专业审核系统 / H3 审核覆盖范围 / H2 合规要求 / H3 用户责任 / H3 禁止内容类型 / H2 违规处理措施 / H3 违规后果 / H3 申诉机制 / H2 政策文档 / H3 服务条款 |
| `/faq/data-security` | API易如何保障数据安全？ | 2026-04-01 | 0 | 0 | H2 数据安全承诺 / H2 核心安全措施 / H3 端到端加密 / H3 最小化数据存储 / H3 有限日志记录 / H3 短期日志保留 / H2 访问控制机制 / H3 严格的权限管理 / H3 技术团队管理 / H2 安全保障体系 / H3 定期安全审计 / H3 合规性保障 |
| `/faq/forgot-password` | 忘记密码了怎么办？ | 2026-03-12 | 0 | 0 | H2 简短回答 / H2 方案一：邮箱重置密码 / H2 方案二：联系客服找回 / H2 方案三：找回后绑定邮箱 / H2 常见问题 / H2 联系我们 |
| `/faq/github-bindng-bindng-error` | GitHub 登录提示「该账户已绑定」怎么办？ | 2026-03-12 | 0 | 0 | H2 简短回答 / H2 问题现象 / H2 解决步骤 / H2 常见问题 / H2 联系我们 |
| `/faq/invalid-api-key` | 为什么提示 API Key 无效？ | 2026-01-28 | 16 | 6 | H2 常见错误现象 / H2 什么是 Base URL？ / H3 Base URL 和 API Key 必须一一对应 / H2 正确的配置方法 / H3 方法一：修改 Base URL（推荐） / H3 方法二：使用环境变量 / H2 API易支持的请求地址格式 / H2 常见问题排查 / H2 错误示例 vs 正确示例 / H2 快速测试方法 / H2 相关文档 |
| `/faq/max-tokens` | max_tokens 是什么？不设置会怎样？ | 2026-03-26 | 0 | 22 | H2 简短回答 / H2 max_tokens 的作用 / H2 OpenAI 参数名称演变 / H3 为什么要改名？ / H2 不设置 max_tokens 会怎样？ / H2 各模型最大输出 tokens 参考 / H2 使用建议 / H2 常见问题 / H2 相关文档 |
| `/faq/model-availability` | 为什么有些模型我用不了？ | 2026-04-01 | 0 | 0 | H2 用户分组和模型权限 / H3 充值用户自动升级 / H3 手动调整分组 / H2 模型不可用的具体原因 / H3 1. 高价格模型限制 / H3 2. 平台方下线模型 / H2 用户分组说明 / H3 Default 分组 / H3 VIP/SVIP 分组 / H2 检查模型可用性 / H3 确认当前分组 / H3 测试模型调用 |
| `/faq/model-multiplier` | 系统里模型的【倍率】是什么？ | 2026-03-24 | 0 | 12 | H2 快速答案 / H2 定价策略 / H2 文本模型计费方式 / H2 基本概念 / H2 倍率计算规则 / H2 计算示例 / H2 图片/视频模型计费 / H2 总结 |
| `/faq/model-name-suffix-c` | 模型名称后缀 -c 是什么意思？ | 2026-03-02 | 0 | 4 | H2 简短回答 / H2 官方解释 / H2 为什么会有 -c 后缀？ / H2 如何选择？ / H2 未来计划 / H2 常见问题 / H2 相关文档 |
| `/faq/model-selection-guide` | 如何选择合适的 AI 模型？ | 2026-04-01 | 0 | 0 | H2 快速查看模型信息 / H2 核心选型原则 / H2 常见场景推荐 / H3 文本生成与对话 / H3 图像生成 / H3 代码与技术应用 / H2 具体场景咨询 / H2 实际案例 / H2 模型更新说明 |
| `/faq/model-version-identity` | 为什么大模型不知道自己的版本号？ | 2026-04-01 | 3 | 0 | H2 简短回答 / H2 实际案例 / H2 通俗理解 / H2 技术原理 / H2 如何验证你调用的模型是否正确？ / H2 API易 服务保障 / H2 如何让模型正确回答自己的版本？ / H2 相关问题 / H2 联系我们 |
| `/faq/nano-banana-image-failure` | Nano Banana 系列出图失败，常见原因有哪些？ | 2026-04-01 | 0 | 4 | H2 简要说明 / H2 常见触发原因 / H3 Nano Banana 2 新增限制 / H2 政策更新时间线 / H2 出图失败的典型表现 / H3 常见的报错文案示例 / H2 C 端产品开发者建议 / H2 联系支持 |
| `/faq/network-proxy` | 使用 API 接口需要代理网络吗？ | 2026-04-01 | 1 | 0 | H2 简短回答 / H2 网络访问说明 / H3 国内用户 / H3 海外用户 / H2 网络问题解决方案 / H3 备选方案：HTTP 地址 / H2 常见问题 / H3 为什么国内可以直连？ / H3 HTTPS 和 HTTP 有什么区别？ / H3 如何判断网络连接是否正常？ / H2 网络优化建议 / H2 技术支持 |
| `/faq/payment-methods` | 支持对公或 USDT 付款吗？ | 2026-04-01 | 0 | 0 | H2 支付方式概览 / H2 对公打款 / H3 支持对公转账 / H3 获取打款信息 / H2 USDT 加密货币支付 / H3 支持的区块链网络 / H3 获取 USDT 收款地址 / H2 联系方式 / H3 企业微信客服 / H3 官方邮箱 / H2 支付流程 / H3 对公打款流程 |
| `/faq/recharge-promotions` | 网站有什么充值活动吗？ | 2026-04-01 | 0 | 6 | H2 充值优惠概览 / H2 首充加赠活动 / H3 普通用户首充 / H3 如何领取首充加赠？ / H2 充值阶梯加赠 / H3 加赠比例表 / H3 加赠发放说明 / H3 计算示例 / H2 额度使用说明 / H3 额度特点 / H3 适用模型 / H2 企业客户服务 |
| `/faq/refund-policy` | API易 的退款政策是怎样的？ | 2026-04-01 | 0 | 9 | H2 简短回答 / H2 退款条件 / H2 退款手续费 / H2 退款金额计算 / H2 退款流程 / H2 常见问题 / H2 相关文档 |
| `/faq/server-location` | API易的服务器在哪里？应该选择什么服务器？ | 2026-04-01 | 3 | 0 | H2 服务器位置 / H2 不同地区的网络表现 / H2 服务器选购建议 / H3 海外服务器推荐 / H3 中国大陆服务器 / H2 如何测试网络延迟？ / H3 方法 1：Ping 测试 / H3 方法 2：cURL 延迟测试 / H3 方法 3：实际 API 调用测试 / H2 网络优化建议 / H3 针对高延迟场景 / H3 针对大图片传输 |
| `/faq/token-billing-modes` | 令牌的按量优先/按次计费有什么区别？ | 2026-04-14 | 4 | 17 | H2 快速答案 / H2 5 种计费模式详解 / H3 1. 按量计费 / H3 2. 按次计费 / H3 3. 混合计费 / H3 4. 按量优先（推荐） / H3 5. 按次优先 / H2 如何选择计费模式？ / H3 推荐方案（适合 95% 用户） / H3 特殊场景 / H2 常见问题 / H2 总结建议 |
| `/faq/token-management` | 如何创建 KEY？ | 2026-01-28 | 0 | 0 | H2 获取现有的默认令牌 / H2 新增KEY / H3 新增KEY的优势 / H2 KEY格式说明 / H2 使用建议 |
| `/faq/token-model-whitelist` | 令牌需要设置可用模型吗？ | 2026-01-28 | 1 | 4 | H2 一般情况：不需要设置 / H2 为什么不建议设置？ / H3 1. 限制调用范围 / H3 2. 模型别名问题 / H3 3. 业务场景变化 / H2 什么情况下需要设置？ / H3 场景 1：共享令牌给他人 / H3 场景 2：预算控制 / H3 场景 3：安全合规 / H2 如何设置可用模型？ / H2 总结 / H2 相关文档 |
| `/faq/user-logs-control` | 为方便排查问题，可以在后台看到详细日志吗？ | 2026-04-01 | 0 | 0 | H2 默认隐私保护策略 / H2 批量调用场景的问题 / H2 管理员协助排查功能 / H3 如何请求开启 / H3 管理员后台界面 / H2 详细日志包含的内容 / H2 适用场景 / H3 推荐请求开启的场景 / H3 何时无需开启 / H2 数据安全说明 / H2 常见问题 / H3 我可以自己在后台开启这个功能吗？ |

## 5. 使用场景页面内容索引

| Path | Title | Lastmod | Code blocks | Table lines | H2/H3 outline |
| --- | --- | --- | ---: | ---: | --- |
| `/scenarios` | 使用场景总览 | 2026-04-16 | 0 | 0 | H2 🎯 四大核心应用领域 / H2 💬 对话型 AI / H3 典型应用场景 / H3 推荐工具和平台 / H2 💻 编程开发 / H3 典型应用场景 / H3 推荐工具和平台 / H3 支持的编程语言 / H2 🔧 技术工程 / H3 典型应用场景 / H3 推荐工具和平台 / H3 技术栈支持 |
| `/scenarios/agent/openclaw/advanced` | 进阶功能与故障排除 | 2026-03-09 | 6 | 0 | H2 故障排除 / H2 自定义技能 / H2 记忆功能 / H2 多设备同步 / H2 安全提示 / H2 相关资源 |
| `/scenarios/agent/openclaw/config-anthropic` | Anthropic 原生配置 | 2026-03-09 | 6 | 20 | H2 为什么选择 Anthropic 原生模式 / H2 推荐配置 / H3 关键配置说明 / H3 关于 `reasoning: false` / H2 模型白名单配置 / H2 与 OpenAI 兼容模式的对比 / H2 Claude 模型 ID 列表 / H2 混合配置（推荐） / H2 验证配置 / H2 常见问题 |
| `/scenarios/agent/openclaw/config-cli` | CLI 交互式配置 | 2026-03-25 | 11 | 6 | H2 安装向导（推荐新用户） / H3 步骤一：选择模型提供商 / H3 步骤二：填写 API 地址 / H3 步骤三：选择密钥输入方式 / H3 步骤四：粘贴 API 密钥 / H3 步骤五：选择端点兼容模式 / H3 步骤六：设置模型 ID / H3 步骤七：验证并完成 / H3 配置完成后的参数 / H2 修改配置 / H2 单项配置命令 / H2 Web UI 配置面板 |
| `/scenarios/agent/openclaw/config-json` | 配置文件方式 | 2026-03-09 | 4 | 7 | H2 配置文件位置 / H2 基础配置 / H2 配置字段说明 / H2 多模型配置 / H2 完整配置示例 |
| `/scenarios/agent/openclaw/installation` | 安装指南 | 2026-03-09 | 10 | 0 | H2 系统要求 / H2 安装 Node.js / H2 安装 OpenClaw / H2 验证安装 / H2 下一步 |
| `/scenarios/agent/openclaw/overview` | OpenClaw | 2026-03-09 | 0 | 0 | H2 概述 / H2 快速导航 |
| `/scenarios/agent/openclaw/usage` | 使用指南 | 2026-03-09 | 7 | 48 | H2 使用方式 / H3 方式一：Web UI（推荐） / H3 方式二：Telegram Bot / H3 方式三：其他平台 / H2 核心技能 / H3 文件操作 / H3 系统操作 / H3 智能功能 / H2 常用命令 / H3 终端命令 / H3 聊天命令 / H2 使用示例 |
| `/scenarios/chat/chatbox` | Chatbox AI | 2026-01-28 | 5 | 7 | H2 快速开始 / H3 下载安装 / H3 配置 API易 / H2 支持的模型 / H2 核心功能 / H3 多平台同步 / H3 对话管理 / H3 文档处理 / H3 图像生成 / H3 高级设置 / H2 使用技巧 / H3 提示词优化 |
| `/scenarios/chat/chatgpt-next-web` | ChatGPT Next Web | 2026-01-28 | 4 | 0 | H2 快速部署 / H3 Vercel 一键部署 / H3 Docker 部署 / H2 配置说明 / H3 基础配置 / H3 非 OpenAI 模型 / H2 核心功能 / H3 预设提示词 / H3 面具功能 / H3 对话导出 / H3 访问控制 / H2 环境变量 |
| `/scenarios/chat/cherry-studio` | Cherry Studio | 2026-03-19 | 0 | 8 | H2 快速集成（OpenAI 兼容格式） / H3 1. 获取 API 密钥 / H3 2. 配置步骤 / H2 三种渠道类型对比 / H2 Anthropic 渠道类型 / H3 配置步骤 / H3 适用场景 / H2 Gemini 渠道类型 / H3 配置步骤 / H3 特色功能 / H2 添加模型 / H2 高级功能 |
| `/scenarios/chat/open-webui` | Open WebUI | 2026-01-28 | 13 | 0 | H2 快速部署 / H3 Docker 快速启动 / H3 Docker Compose 部署 / H2 配置 API易 / H3 方法一：环境变量配置 / H3 方法二：界面配置 / H2 支持的模型 / H2 核心功能 / H3 RAG (检索增强生成) / H3 OpenAI 兼容 API / H3 工具集成 / H2 高级配置 |
| `/scenarios/ecosystem/apiyi-nano-banana-node` | APIYI Nano Banana ComfyUI 节点（轻量示例版） | 2026-04-14 | 4 | 12 | H2 概述 / H2 核心功能 / H2 支持的 API易 模型 / H2 节点说明 / H3 APIYI Text to Image（文生图） / H3 APIYI Multi Image Edit（多图编辑） / H3 节点参数 / H2 安装配置 / H2 使用示例 / H3 示例 1：文生图 / H3 示例 2：多图融合 / H2 拓展建议 |
| `/scenarios/ecosystem/image-annotator-comfyui` | Image Annotator - ComfyUI 节点 | 2026-04-14 | 4 | 11 | H2 概述 / H2 核心功能 / H2 支持的 API易 模型 / H2 节点说明 / H3 输入 / H3 输出 / H2 安装配置 / H2 使用示例 / H3 示例 1：局部换物（小白友好） / H3 示例 2：多区域精准标注 / H3 示例 3：视觉问答 / 理解 / H2 常见问题 |
| `/scenarios/ecosystem/lucknanobananapro-comfyui` | Luck Nano Banana Pro - ComfyUI 节点 | 2026-04-14 | 4 | 15 | H2 概述 / H2 核心功能 / H2 支持的 API易 模型 / H2 节点参数 / H2 安装配置 / H2 使用示例 / H3 示例 1：高稳定性文生图 / H3 示例 2：多图融合 / H3 示例 3：Seed 批量探索 / H2 常见问题 / H2 相关资源 |
| `/scenarios/ecosystem/make-com-gemini-vision` | Make.com 接入 Gemini 图像理解 | 2026-03-15 | 5 | 20 | H2 概述 / H2 为什么选择 Make.com + API易 / H2 支持的 API易 模型 / H2 配置步骤 / H2 完整请求示例 / H3 请求参数说明 / H2 实用场景 / H3 场景一：自动分析邮件附件中的图片 / H3 场景二：电商产品图自动标签 / H3 场景三：社交媒体内容审核 / H2 进阶技巧 / H3 动态替换图片 URL |
| `/scenarios/ecosystem/nano-banana-comfyui` | Nano Banana ComfyUI 节点 | 2026-04-14 | 6 | 24 | H2 概述 / H2 为什么选择这个节点 / H2 支持的 API易 模型 / H2 四大核心节点 / H2 从零开始：安装与配置 / H2 实战教程：从文字到图片 / H3 场景一：文字生成图片（最基础） / H3 场景二：图片编辑与融合 / H3 场景三：多轮对话式编辑 / H2 节点参数详解 / H3 Nano Banana AIO / Nano Banana 2 AIO / H3 支持的宽高比 |
| `/scenarios/ecosystem/nano-banana-skill` | Nano Banana Pro 生图 Skill | 2026-03-14 | 8 | 16 | H2 概述 / H2 为什么用这个 Skill / H2 支持的 API易 模型 / H2 快速上手：3 步开始生图 / H2 实战教程 / H3 用法一：命令行文字生图 / H3 用法二：编辑已有图片 / H3 用法三：在 AI 编程助手中使用 / H2 命令参数详解 / H3 支持的宽高比 / H3 分辨率与耗时参考 / H2 常见问题 |
| `/scenarios/ecosystem/paper2any` | Paper2Any 论文多模态工作流 | 2026-03-24 | 5 | 15 | H2 概述 / H2 为什么选择 Paper2Any / H2 核心功能模块 / H2 通过 API易 接入大模型 / H3 Docker 部署配置 / H3 CLI 命令行使用 / H2 部署方式 / H2 常见问题 / H2 相关资源 |
| `/scenarios/engineering/dify` | Dify | 2026-01-28 | 13 | 0 | H2 快速集成 / H3 1. 获取 API 密钥 / H3 2. 配置模型供应商 / H2 核心功能 / H3 对话助手 / H3 工作流应用 / H3 知识库问答 / H2 应用类型 / H3 1. 聊天助手 / H3 2. 文档分析 / H3 3. 代码助手 / H2 高级功能 |
| `/scenarios/engineering/langchain` | LangChain | 2026-01-28 | 18 | 0 | H2 快速开始 / H3 安装 / H3 基础配置 / H2 核心功能 / H3 基础对话 / H3 对话链 / H3 文档问答系统 / H2 模型切换 / H3 使用不同模型 / H2 高级应用 / H3 Agent 系统 / H3 批量处理 |
| `/scenarios/programming/cc-switch` | CC Switch | 2026-03-20 | 2 | 10 | H2 概述 / H2 核心功能 / H3 Provider 管理 / H3 MCP 服务器管理 / H3 更多特性 / H2 快速开始 / H3 第一步：安装 CC Switch / H3 第二步：获取 API易 密钥 / H3 第三步：在 CC Switch 中配置 API易 / H3 第四步：添加模型 / H3 第五步：一键切换 / H2 使用指南 |
| `/scenarios/programming/claude-code` | Claude Code | 2026-03-31 | 12 | 5 | H2 概述 / H2 快速开始 / H3 1. 安装 Claude Code / H3 2. 配置 API 密钥 / H3 3. 使配置生效 / H3 4. 启动 Claude Code / H2 高级配置 / H3 配置文件（推荐） / H3 全局授权（不推荐） / H2 使用指南 / H3 基本命令 / H3 工作流程 |
| `/scenarios/programming/cline` | Cline (VS Code) | 2026-01-28 | 17 | 11 | H2 快速安装 / H3 1. 安装插件 / H3 2. 配置 API易 / H3 推荐模型 / H2 核心功能 / H3 智能代码补全 / H3 代码解释 / H3 代码重构 / H3 生成测试 / H2 常用命令 / H2 高级功能 / H3 多文件操作 |
| `/scenarios/programming/codex-cli` | OpenAI Codex CLI | 2026-01-28 | 21 | 5 | H2 概述 / H2 环境准备 / H3 必要软件 / H2 快速开始 / H3 1. 安装 Codex CLI / H3 2. 获取 API 密钥 / H3 3. 配置 Codex / H3 4. 设置环境变量 / H3 5. 开始使用 / H2 使用技巧 / H3 项目初始化 / H3 中文支持 |
| `/scenarios/programming/cursor` | Cursor | 2026-01-28 | 5 | 12 | H2 快速配置 / H3 1. 打开设置 / H3 2. 配置 API / H3 3. 模型配置 / H2 使用模式说明 / H3 Chat 模式工作流程 / H3 替代方案对比 / H2 核心功能 / H3 智能代码补全 / H3 AI 对话 / H3 代码编辑 / H2 快捷键 |
| `/scenarios/programming/gemini-cli` | Gemini CLI | 2026-04-01 | 29 | 17 | H2 概述 / H2 快速开始 / H3 前置要求 / H3 第一步：安装 Gemini CLI / H3 第二步：获取 API易 密钥 / H3 第三步：配置环境变量 / H3 第四步：初始化和测试 / H2 核心功能 / H3 代码生成 / H3 代码审查 / H3 技术问答 / H3 文档生成 |
| `/scenarios/programming/opencode` | OpenCode | 2026-02-03 | 22 | 29 | H2 概述 / H2 环境准备 / H3 安装 OpenCode / H2 快速配置 / H3 方法一：自定义 Provider（推荐） / H3 方法二：/connect 命令认证 / H3 方法三：覆盖现有 Provider / H3 方法四：项目级配置 / H2 Agent 系统 / H3 Agent 模型配置 / H2 推荐模型 / H3 场景化模型推荐 |
| `/scenarios/programming/roo-code` | Roo Code (VS Code) | 2026-04-01 | 15 | 17 | H2 概述 / H2 快速安装 / H3 方式一：VS Code 扩展商店（推荐） / H3 方式二：Open VSX Registry / H2 配置 API易 / H3 基础配置 / H3 获取 API易 密钥 / H2 多模式配置（核心特性） / H3 五大开发模式 / H3 配置多模式 / H2 推荐模型 / H2 核心功能 |
| `/scenarios/translation/bob` | Bob 翻译 | 2026-01-28 | 5 | 0 | H2 快速配置 / H3 1. 安装 Bob / H3 2. 配置 API易 / H3 3. 测试配置 / H2 使用方法 / H3 划词翻译 / H3 截图翻译 / H3 输入翻译 / H2 模型选择 / H3 不同场景的推荐 / H3 多模型配置 / H2 高级设置 |
| `/scenarios/translation/immersive` | 沉浸式翻译 | 2026-01-28 | 5 | 6 | H2 快速安装 / H3 支持的浏览器 / H3 安装步骤 / H2 配置 API易 / H3 1. 打开设置 / H3 2. 配置翻译服务 / H3 3. 填写配置 / H2 核心功能 / H3 网页翻译 / H3 翻译模式 / H3 划词翻译 / H2 高级设置 |

## 6. 最新公告 / 实时动态页面内容索引

| Path | Title | Lastmod | Code blocks | Table lines | H2/H3 outline |
| --- | --- | --- | ---: | ---: | --- |
| `/changelog` | 网站公告 | 2026-04-16 | 0 | 0 | H2 🔥 最新动态 / H2 📅 2026年4月 / H3 💰 Nano Banana 2 按量计费微调 / H3 🌟 Claude Opus 4.7 上线：不加价的编程与 Agent 升级 / H3 💰 Nano Banana Pro 价格调整 & 新增企业高可用分组 / H3 🌟 GLM-5.1 上线：智谱开源最强编程 Agent 模型 / H3 🌟 Qwen3.6-Plus 上线：阿里千问最强编程 Agent 模型 / H2 📅 2026年3月 / H3 🌟 Gemini Embedding 2 Preview 上线 / H3 🌟 Seed 2.0 Pro 旗舰版上线 / H3 🌟 MiniMax-M2.7 / M2.7-highspeed 上线 / H3 🌟 MiMo-V2-Pro / MiMo-V2-Omni 上线 |
| `/live` | 实时动态 | 2026-04-21 | - | - | sitemap-only / no llms-full Source |
| `/news/claude-opus-4-5-launch` | Claude Opus 4.5 震撼发布：编程能力登顶，价格降至原版 1/3 | 2026-01-28 | 3 | 23 | H2 核心要点 / H2 背景介绍 / H2 详细解析 / H3 核心特性 / H3 性能亮点 / H3 技术规格 / H2 实际应用 / H3 推荐场景 / H3 代码示例 / H3 最佳实践 / H2 价格与可用性 / H3 定价信息 |
| `/news/claude-opus-4-7-launch` | Claude Opus 4.7 重磅上线：编程再进化，视觉能力三倍升级 | 2026-04-16 | 3 | 26 | H2 核心要点 / H2 背景介绍 / H2 详细解析 / H3 核心特性 / H3 性能亮点 / H3 技术规格 / H3 新增功能 / H2 实际应用 / H3 推荐场景 / H3 代码示例 / H3 最佳实践 / H2 价格与可用性 |
| `/news/gemini-2-5-flash-lite-preview-launch` | Gemini 2.5 Flash Lite：谷歌最快最省的轻量级模型，海量文本处理首选 | 2026-01-28 | 1 | 8 | H2 核心要点 / H2 背景介绍 / H2 详细解析 / H3 核心特性 / H3 性能亮点 / H3 技术规格 / H2 实际应用 / H3 推荐场景 / H3 代码示例 / H3 最佳实践 / H2 价格与可用性 / H3 API易 独家定价 |
| `/news/gemini-3-1-flash-lite-preview-launch` | Gemini 3.1 Flash Lite Preview：谷歌最新轻量级模型，代理任务与低延迟场景首选 | 2026-03-04 | 2 | 26 | H2 核心要点 / H2 背景介绍 / H2 详细解析 / H3 核心特性 / H3 技术规格 / H3 与前代对比 / H2 实际应用 / H3 推荐场景 / H3 代码示例 / H3 最佳实践 / H2 价格与可用性 / H3 API易定价 |
| `/news/gemini-3-flash-preview-launch` | Gemini 3 Flash Preview 震撼发布：Pro 级性能，Flash 级速度 | 2026-01-28 | 4 | 38 | H2 核心要点 / H2 背景介绍 / H2 详细解析 / H3 核心特性 / H3 性能亮点 / H3 技术规格 / H2 模型变体说明 / H3 1. gemini-3-flash-preview（自动推理） / H3 2. gemini-3-flash-preview-thinking（强制推理） / H3 3. gemini-3-flash-preview-nothinking（默认不推理） / H3 模型选择建议 / H2 实际应用 |
| `/news/gemini-3-pro-preview-launch` | Gemini 3 Pro Preview 正式发布：LMArena 全球第一 | 2026-01-28 | 3 | 11 | H2 核心要点 / H2 背景介绍 / H2 详细解析 / H3 新增模型 / H3 性能亮点 / H3 核心特性 / H2 实际应用 / H3 推荐场景 / H3 代码示例 / H3 最佳实践 / H2 价格与可用性 / H3 定价信息 |
| `/news/gemini-embedding-2-preview-launch` | Gemini Embedding 2 Preview 上线：首个原生多模态嵌入模型 | 2026-03-31 | 3 | 62 | H2 核心要点 / H2 背景介绍 / H2 详细解析 / H3 核心特性 / H3 性能亮点 / H3 与前代模型对比 / H3 多模态输入规格 / H3 支持的任务类型 / H3 技术规格 / H2 实际应用 / H3 推荐场景 / H3 代码示例 |
| `/news/glm-5-1-launch` | GLM-5.1 上线：智谱开源最强编程 Agent 模型 | 2026-04-09 | 2 | 23 | H2 核心要点 / H2 背景介绍 / H2 详细解析 / H3 核心特性 / H3 性能亮点 / H3 技术规格 / H2 实际应用 / H3 推荐场景 / H3 代码示例 / H3 最佳实践 / H2 价格与可用性 / H3 定价信息 |
| `/news/google-ai-studio-usage-guide` | Google AI Studio 使用指南：轻松体验 Gemini 模型的三种方案 | 2026-01-28 | 1 | 16 | H2 核心要点 / H2 Google AI Studio 是什么？ / H3 产品定位 / H3 核心功能 / H3 使用场景 / H2 为什么 Nano Banana Pro 需要绑定 API Key？ / H3 Nano Banana Pro 是什么？ / H3 为何需要 API Key？ / H3 门槛在哪里？ / H2 三种解决方案对比 / H3 方案一：使用 API 中转站（API易） / H3 方案二：会员代充（林兄 AI） |
| `/news/gpt-5-2-launch` | GPT-5.2 重磅发布：OpenAI 反击 Gemini 3，推出三大版本应对竞争 | 2026-01-28 | 3 | 40 | H2 核心要点 / H2 背景介绍 / H2 详细解析 / H3 核心特性 / H3 性能亮点 / H3 技术规格 / H3 三大版本对比 / H2 实际应用 / H3 推荐场景 / H3 代码示例 / H3 最佳实践 / H2 价格与可用性 |
| `/news/gpt-5-3-chat-launch` | GPT-5.3 Chat 上线：更少幻觉、更自然的 ChatGPT 聊天模型 | 2026-03-06 | 3 | 26 | H2 核心要点 / H2 背景介绍 / H2 详细解析 / H3 核心改进 / H3 性能提升 / H3 技术规格 / H3 GPT-5.3 系列全家福 / H2 实际应用 / H3 推荐场景 / H3 快速开始 / H3 流式输出 / H3 从 GPT-5.2 迁移 |
| `/news/gpt-5-4-launch` | GPT-5.4 重磅发布：OpenAI 最强专业模型，原生计算机使用能力 | 2026-03-06 | 2 | 34 | H2 核心要点 / H2 背景介绍 / H2 详细解析 / H3 核心特性 / H3 性能亮点 / H3 技术规格 / H3 三大版本对比 / H2 实际应用 / H3 推荐场景 / H3 代码示例 / H3 最佳实践 / H2 价格与可用性 |
| `/news/gpt-5-4-mini-nano-launch` | GPT-5.4 Mini & Nano 上线：轻量高性价比，为规模化场景而生 | 2026-03-18 | 2 | 29 | H2 核心要点 / H2 背景介绍 / H2 详细解析 / H3 核心特性 / H3 GPT-5.4 Mini 性能亮点 / H3 GPT-5.4 Nano 性能定位 / H3 推理能力可调 / H2 实际应用 / H3 推荐场景 / H3 代码示例 / H2 价格与可用性 / H3 定价信息 |
| `/news/gpt-image-1-5-launch` | OpenAI GPT Image 1.5 正式上线：4倍速度提升，精准编辑新体验 | 2026-01-28 | 1 | 16 | H2 核心要点 / H2 背景介绍 / H2 详细解析 / H3 核心特性 / H3 性能亮点 / H3 技术规格 / H2 实际应用 / H3 推荐场景 / H3 代码示例 / H3 最佳实践 / H2 价格与可用性 / H3 定价信息 |
| `/news/grok-4-20-beta-launch` | Grok 4.20 Beta 系列上线：四智能体协作架构，200 万上下文 | 2026-03-19 | 2 | 19 | H2 核心要点 / H2 背景介绍 / H2 详细解析 / H3 4 款模型对比 / H3 核心特性 / H3 性能数据 / H3 多智能体版特别说明 / H2 实际应用 / H3 代码示例 / H3 推荐使用场景 / H2 价格与可用性 / H3 定价信息 |
| `/news/mimo-v2-launch` | MiMo-V2 系列上线：小米万亿参数智能体模型，性能逼近 Opus 4.6 | 2026-03-21 | 2 | 25 | H2 核心要点 / H2 背景介绍 / H2 详细解析 / H3 核心特性 / H3 MiMo-V2-Pro 性能数据 / H3 MiMo-V2-Omni 性能数据 / H3 技术规格 / H2 实际应用 / H3 代码示例 / H3 推荐使用场景 / H2 价格与可用性 / H3 定价信息 |
| `/news/minimax-m2-7-launch` | MiniMax-M2.7 上线：10B 参数的自进化智能体模型，性价比惊人 | 2026-03-24 | 0 | 19 | H2 核心要点 / H2 背景介绍 / H2 详细解析 / H3 核心特性 / H3 性能评测 / H3 M2.7 vs M2.7-highspeed / H3 技术规格 / H2 价格与可用性 / H2 总结与建议 |
| `/news/nano-banana-2-launch` | Nano Banana 2 上线：Pro画质 Flash价格 | 2026-04-14 | 5 | 38 | H2 核心要点 / H2 背景介绍 / H2 详细解析 / H3 新增模型 / H3 与前代版本对比 / H3 独家新特性 / H3 其他亮点 / H2 实际应用 / H3 快速开始 / H3 从 Nano Banana Pro 迁移 / H2 价格与可用性 / H3 定价对比 |
| `/news/nano-banana-pro-launch` | Nano Banana Pro 震撼上线：4K高清图像生成 | 2026-04-14 | 7 | 20 | H2 核心要点 / H2 背景介绍 / H2 详细解析 / H3 新增模型 / H3 核心特性对比 / H3 核心特性详解 / H2 实际应用 / H3 推荐场景 / H3 代码示例 / H3 最佳实践 / H2 价格与可用性 / H3 定价信息 |
| `/news/qwen-3-6-plus-launch` | Qwen3.6-Plus 上线：阿里千问最强编程 Agent 模型 | 2026-04-07 | 2 | 23 | H2 核心要点 / H2 背景介绍 / H2 详细解析 / H3 核心特性 / H3 性能亮点 / H3 技术规格 / H2 实际应用 / H3 推荐场景 / H3 代码示例 / H3 最佳实践 / H2 价格与可用性 / H3 定价信息 |
| `/news/seed-2-0-lite-launch` | Seed 2.0 Lite 上线：字节跳动高性价比企业级多模态模型 | 2026-03-08 | 3 | 32 | H2 核心要点 / H2 背景介绍 / H2 详细解析 / H3 核心特性 / H3 性能亮点 / H3 多模态能力详解 / H3 技术规格 / H2 实际应用 / H3 推荐场景 / H3 代码示例 / H3 最佳实践 / H2 价格与可用性 |
| `/news/seed-2-0-pro-launch` | Seed 2.0 Pro 旗舰版上线：字节跳动最强推理模型 | 2026-03-30 | 3 | 34 | H2 核心要点 / H2 背景介绍 / H2 详细解析 / H3 核心特性 / H3 性能亮点 / H3 技术规格 / H2 实际应用 / H3 推荐场景 / H3 代码示例 / H3 最佳实践 / H2 价格与可用性 / H3 Seed 2.0 系列对比 |
| `/news/seedream-4-5-launch` | SeeDream 4.5 震撼上线：BytePlus 火山方舟最强 4K 图像生成模型 | 2026-03-01 | 3 | 15 | H2 核心要点 / H2 背景介绍 / H2 详细解析 / H3 核心特性 / H3 性能亮点 / H3 技术规格 / H2 实际应用 / H3 推荐场景 / H3 代码示例 / H3 最佳实践 / H2 价格与可用性 / H3 定价信息 |

## 7. API 参考页面内容索引

| Path | Title | Lastmod | Code blocks | Table lines | H2/H3 outline |
| --- | --- | --- | ---: | ---: | --- |
| `/api-reference/chat/chat-completions` | Chat Completions | 2026-03-15 | 0 | 0 |  |
| `/api-reference/embeddings/create-embeddings` | Create Embeddings | 2026-03-15 | 0 | 0 |  |
| `/api-reference/models/list-models` | List Models | 2026-03-15 | 0 | 0 |  |

## 8. 基础 / 图片 / 视频页面的关键事实

### 当下热门模型（保持更新） -> `/api-capabilities/model-info`

- H2：`🔥 当前推荐模型`、`模型分类`、`💰 定价说明`、`🛠️ 使用建议`、`🔗 相关资源`
- H3 前 12 个：`🤖 OpenAI 系列`、`🎭 Claude 系列 (Anthropic)`、`🌟 Google Gemini 系列`、`🚀 xAI Grok 系列`、`🔍 DeepSeek 系列`、`🐘 国产模型系列`、`🌐 MiniMax 系列`、`计费方式`、`价格优势`、`查看实时价格`、`模型选择指南`、`成本优化建议`
- 模型名：`GPT-5.4`、`gpt-5.4`、`gpt-5.4-pro`、`GPT-5.2`、`gpt-5.2`、`GPT-5.3`、`gpt-5.3-chat-latest`、`GPT-5.1`、`gpt-5.1`、`gpt-5.3-codex`、`gpt-5.3-codex-spark`、`GPT-5`、`gpt-5`、`gpt-5-mini`、`gpt-5-nano`、`o3`、`o4-mini`、`GPT-4.1`、`gpt-4.1`、`gpt-4.1-mini`、`GPT-4o`、`gpt-4o`、`gpt-4o-mini`、`claude-opus-4-6`
- 价格字样：`$0.20/1M tokens`、`$0.50/1M tokens`、`$1`、`$0.01 `、`$0.035/张`、`$0.025/张`、`$0.15/次`

### 图像与视频生成模型 -> `/api-capabilities/image-video-models`

- H2：`🎨 图像生成模型`、`🎬 视频生成模型`、`💰 定价说明`
- 模型名：`sora-image-generation`、`seedream-image`、`gpt-image-1-5-launch`、`gpt-image-1`、`flux-image-generation`、`sora-2-video-official`、`sora-2-video`、`sora-2-pro`
- 价格字样：`$0.09/张`、`$0.055/张`、`$0.025`、`$0.02/张`、`$0.01/张`、`$0.035/张`、`$0.045/张`、`$0.24/张`、`$0.15`、`$0.25`、`$0.6`、`$0.12/次`

### OpenAI 官方库使用 -> `/api-capabilities/openai-sdk`

- H2：`支持的官方 SDK`、`Python SDK`、`Node.js SDK`、`.NET SDK`、`Go SDK`、`Java SDK`、`模型切换`、`高级功能`、`错误处理`、`最佳实践`、`迁移指南`
- H3 前 12 个：`安装`、`基础配置`、`环境变量配置`、`异步使用`、`流式输出`、`安装`、`基础配置`、`环境变量配置`、`流式输出`、`TypeScript 支持`、`安装`、`基础配置`
- 模型名：`gpt-3.5-turbo`、`gpt-4`、`claude-3-opus-20240229`、`gemini-pro`、`gpt-4o`、`text-embedding-3-small`

### OpenAI Responses 支持 -> `/api-capabilities/openai-responses`

- H2：`🚀 核心特性`、`📋 支持的模型`、`🔧 基础用法`、`📊 请求参数详解`、`🛠️ 内置工具支持`、`🔄 状态管理`、`📈 推理模型特性`、`🆚 与 Chat Completions 对比`、`🔧 高级功能`、`📊 响应字段详解`、`🚨 错误处理`、`💡 最佳实践`、`🔮 未来发展`
- H3 前 12 个：`推理模型（推荐）`、`对话模型`、`简单对话`、`实际响应示例`、`必需参数`、`可选参数`、`1. 函数调用`、`2. 代码解释器`、`3. 文件搜索`、`维护对话上下文`、`多轮工具调用`、`O3/O4-mini 推理保持`
- 端点/URL：`/v1/responses`
- 模型名：`O3`、`O4-mini`、`GPT-4.1`、`o3`、`o3-pro`、`o4-mini`、`gpt-4.1`、`gpt-4.1-mini`、`GPT-3.5`、`gpt-4.1-2025-04-14`、`O4`、`gpt-3.5-turbo`

### Claude 模型调用指南 -> `/api-capabilities/claude`

- H2：`核心优势`、`可用模型`、`OpenAI 兼容格式调用`、`Anthropic 原生格式调用`、`推理深度控制（effort 参数）`、`最佳实践`、`技术规格对比`、`常见问题`、`相关资源`
- H3 前 12 个：`Python 示例`、`Node.js 示例`、`cURL 示例`、`Python 原生 SDK`、`流式响应`、`视觉理解（多模态）`、`Anthropic 原生格式设置 effort`、`OpenAI 格式设置 effort`、`cURL 示例`、`1. 模型选择建议`、`2. 成本优化技巧`、`3. 提示词优化`
- 端点/URL：`/v1/chat/completions`、`/v1/messages`
- 模型名：`claude-opus-4-5-20251101`、`claude-sonnet-4-5-20250929`、`claude-haiku-4-5-20251001`、`claude-opus-4-1-250806`、`claude-opus-4-5-launch`
- 价格字样：`$5 `、`$25  `、`$3 `、`$15  `、`$1 `、`$5   `、`$15 `、`$75 `

### Gemini 原生格式调用 -> `/api-capabilities/gemini-native-format`

- H2：`优势`、`配置与使用`、`基础文本生成`、`Gemini 2.5 系列推理功能`、`多模态处理`、`代码执行功能`、`Function Calling（工具调用）`、`上下文缓存`、`Tokens 用量追踪`、`注意事项`、`与 OpenAI 兼容格式的对比`、`完整示例`、`获取帮助`
- H3 前 12 个：`环境准备`、`基础配置`、`非流式响应`、`流式响应`、`推理模型类型`、`控制推理预算`、`显示思考过程`、`图片处理`、`视频处理`、`音频处理`、`媒体分辨率优化`、`定义工具`
- 端点/URL：`https://api.apiyi.com/v1/chat/completions`
- 模型名：`gemini-3-pro-preview`、`gemini-2.0-flash`、`gemini-2.5-flash`、`gemini-2.5-pro`

### 余额查询 API -> `/api-capabilities/balance-query`

- H2：`接口概述`、`如何获取 Authorization`、`接口信息`、`请求说明`、`响应说明`、`错误响应`、`代码示例`、`常见问题`、`注意事项`
- H3 前 12 个：`请求 Headers`、`请求参数`、`成功响应示例`、`核心响应字段说明`、`额度换算说明`、`HTTP 401 - 认证失败`、`HTTP 403 - 权限不足`、`cURL 示例`、`Python 示例（基础版）`、`Python 示例（完整优化版）`
- 端点/URL：`https://api.apiyi.com/api/user/self`
- 价格字样：`$1.00 `、`$49.99 `、`$20.05 `

### 废弃模型列表 -> `/api-capabilities/deprecated-models`

- H2：`说明`、`⚠️ 废弃模型预告`、`🚫 已下线模型`
- 模型名：`gemini-2.0-flash-lite`、`gemini-2.5-flash`、`gemini-2.0-flash-lite-001`、`gemini-2.0-flash`、`gemini-2.0-flash-001`、`gemini-2.0-flash-lite-preview-02-05`、`gemini-api`、`GPT-4`、`gpt-4`、`gpt-5.2`、`gpt-4-32k`

### Sora 2 视频生成 -> `/api-capabilities/sora-2-video`

- H2：`概述`、`详细文档【飞书版】`、`核心特性`、`模型定价`、`调用方式`、`响应格式`、`使用场景`、`常见问题`、`进阶功能`、`技术支持`
- H3 前 12 个：`端点地址`、`文生视频`、`图生视频`、`流式输出`、`生成时间`、`1. AI 对话客户端`、`2. 代码集成`、`高清视频生成`
- 端点/URL：`/v1/chat/completions`
- 模型名：`sora-2-pro`
- 价格字样：`$0.15/次`、`$0.12/次`、`$0.8/次`、`$0.20/次`

### Sora 2 官方直转 -> `/api-capabilities/sora-2-video-official`

- H2：`概述`、`官转 vs 官逆对比`、`核心特性`、`模型定价`、`使用要求`、`API 调用方式`、`请求参数`、`响应格式`、`常见问题`、`相关资源`
- H3 前 12 个：`sora-2（标准版）`、`sora-2-pro（专业版）`、`端点地址`、`调用流程（异步三步）`、`第一步：提交生成请求`、`第二步：轮询任务状态`、`第三步：下载视频`、`提交请求响应`、`查询状态响应`、`状态说明`
- 模型名：`sora-2`、`sora-2-pro`、`sora-2-video`、`sora-2-video-async`
- 价格字样：`$0.1`、`$0.4 `、`$0.8 `、`$1.2 `、`$0.3`、`$2.4 `、`$3.6 `、`$0.5`、`$2.0 `、`$4.0 `、`$6.0 `

### Sora 2 角色接口 -> `/api-capabilities/sora-2-character-api`

- H2：`概述`、`核心要义`、`为什么需要角色？`、`端点地址`、`请求参数`、`代码示例`、`响应格式`、`定价`、`在视频生成中使用角色`、`注意事项与限制`、`最佳实践`、`常见问题`、`相关资源`
- H3 前 12 个：`电商场景`、`动漫场景`、`其他场景`、`参数说明`、`cURL 示例`、`Python 示例`、`成功响应`、`响应字段说明`、`使用方式`、`完整示例`、`成功率说明`、`视频要求`
- 模型名：`sora-character`、`sora-2`、`sora-2-video`、`sora-2-video-async`
- 价格字样：`$0.01 / 次`、`$0.01/次`

### Sora 2 视频生成（异步） -> `/api-capabilities/sora-2-video-async`

- H2：`概述`、`核心特性`、`完整流程`、`模型定价`、`端点地址`、`第一步：提交视频生成请求`、`第二步：轮询查询视频状态`、`第三步：下载生成的视频`、`完整流程示例`、`最佳实践`、`配额和限制`、`错误处理`、`常见问题`、`相关资源`
- H3 前 12 个：`请求参数`、`文生视频示例`、`图生视频示例`、`响应格式`、`请求方式`、`查询示例`、`状态说明`、`生成中的响应示例`、`完成后的响应示例`、`请求方式`、`下载示例`、`Prompt 编写建议`
- 端点/URL：`/v1/videos`、`/v1/videos/{video_id}`、`/v1/videos/{video_id}/content`
- 模型名：`sora-2-video`、`sora-2-pro`、`sora-2`、`Sora-2`
- 价格字样：`$0.12/次`、`$0.8/次`、`$5`

### 综述（官逆Flow） -> `/api-capabilities/veo/overview`

- H2：`综述`、`核心特性`、`调用方式`、`支持的模型`、`开始使用`、`相关链接`
- 模型名：`veo-3.1`、`veo-3.1-fl`、`veo-3.1-fast`、`veo-3.1-fast-fl`、`veo-3.1-landscape`、`veo-3.1-landscape-fl`、`veo-3.1-landscape-fast`、`veo-3.1-landscape-fast-fl`
- 价格字样：`$0.15/次`、`$0.25 `、`$0.15 `

### 异步调用 API -> `/api-capabilities/veo/async-api`

- H2：`模型与定价`、`API 端点`、`完整调用流程`、`Python 完整示例`、`帧转视频模式`、`错误处理`、`常见问题`、`技术规格速查表`
- H3 前 12 个：`1. 创建视频任务`、`2. 查询任务状态`、`3. 获取视频内容`、`请求参数`、`首帧模式示例（单图）`、`首尾帧模式示例（双图）`、`响应与后续处理`、`使用建议`
- 端点/URL：`/v1/videos`、`/v1/videos/{video_id}`、`/v1/videos/{video_id}/content`、`https://api.apiyi.com/v1/videos/${videoId}`、`https://api.apiyi.com/v1/videos/${videoId}/content`
- 模型名：`veo-3.1`、`veo-3.1-fl`、`veo-3.1-fast`、`veo-3.1-fast-fl`、`veo-3.1-landscape`、`veo-3.1-landscape-fl`、`veo-3.1-landscape-fast`、`veo-3.1-landscape-fast-fl`、`veo-video.gptkey.asia`
- 价格字样：`$0.25 `、`$0.15 `、`$0.15`、`$0.25`

### 同步调用 API -> `/api-capabilities/veo/quick-start`

- H2：`同步调用说明`、`快速开始`、`认证方式`、`示例 1：文生视频`、`示例 2：帧转视频（Frame-to-Video）`、`流式响应说明`、`生成速度`、`下一步`
- H3 前 12 个：`参数说明`、`图片参数说明`、`响应示例`、`响应说明`
- 端点/URL：`/v1/chat/completions`
- 模型名：`veo-3.1`、`veo-3.1-landscape`、`veo-3.1-landscape-fast-fl`、`veo-3.1-fast`、`veo-video.gptkey.asia`

### Nano Banana 2 生图/编辑 -> `/api-capabilities/nano-banana-2-image/overview`

- H2：`概述`、`核心特性`、`版本对比`、`模型定价`、`支持的分辨率与宽高比`、`常见问题`、`相关文档`
- H3 前 12 个：`按次计费`、`按量计费（Nano Banana 2 专属）`、`按量计费价格预估`、`输出分辨率`、`支持的宽高比（14 种）`
- 模型名：`gemini-3.1-flash-image-preview`、`gemini-3-pro-image-preview`、`gemini-2.5-flash-image`
- 价格字样：`$0.055/次`、`$0.025/张`、`$0.03 `、`$0.14`、`$16.8`、`$0.05/次`、`$0.02/次`、`$0.151/次`、`$0.09/次`、`$0.020/次`、`$0.039/次`、`$0.126/次`、`$0.50`、`$60`、`$1.5`、`$0.045   `

### 文生图 API 参考 -> `/api-capabilities/nano-banana-2-image/text-to-image`

- H2：`代码示例`、`参数说明速查`
- H3 前 12 个：`Python`、`cURL`、`Node.js`
- 端点/URL：`/v1beta/models/gemini-3.1-flash-image-preview:generateContent`
- 模型名：`gemini-3.1-flash-image-preview`

### 图片编辑 API 参考 -> `/api-capabilities/nano-banana-2-image/image-edit`

- H2：`代码示例`、`参数说明速查`
- H3 前 12 个：`Python`、`Node.js`、`cURL`
- 端点/URL：`/v1beta/models/gemini-3.1-flash-image-preview:generateContent`
- 模型名：`gemini-3.1-flash-image-preview`

### Nano Banana Pro 图片生成 -> `/api-capabilities/nano-banana-image/overview`

- H2：`在线调试 API`、`调用方式`、`价格对比`、`兼容性说明`、`API 错误处理指南`、`FAQ`、`相关文档`
- H3 前 12 个：`最新版本`、`前代版本`、`不支持的功能`、`升级到最新版本`、`使用稳定版本`
- 端点/URL：`/v1beta/models/gemini-3-pro-image-preview:generateContent`
- 模型名：`gemini-3-pro-image-preview`、`gemini-3.1-flash-image-preview`、`gemini-2.5-flash-image`、`gemini-2.5-flash-image-preview`、`gemini-api`、`gpt-image-1`、`flux-kontext-pro`、`gpt-4o-image`
- 价格字样：`$0.025/张`、`$0.09/张`、`$0.035/张`、`$0.126/张`、`$0.05/次`

### 文生图 API 参考 -> `/api-capabilities/nano-banana-image/text-to-image`

- H2：`代码示例`、`参数说明速查`
- H3 前 12 个：`Python`、`cURL`、`Node.js`
- 端点/URL：`/v1beta/models/gemini-3-pro-image-preview:generateContent`
- 模型名：`gemini-3-pro-image-preview`

### 图片编辑 API 参考 -> `/api-capabilities/nano-banana-image/image-edit`

- H2：`代码示例`、`参数说明速查`
- H3 前 12 个：`Python`、`Node.js`、`cURL`
- 端点/URL：`/v1beta/models/gemini-3-pro-image-preview:generateContent`
- 模型名：`gemini-3-pro-image-preview`

### Nano Banana 系列价格总览 -> `/api-capabilities/nano-banana-pricing`

- H2：`概述`、`三款模型速览`、`Nano Banana Pro 定价`、`Nano Banana 2 定价`、`Nano Banana 第一代定价`、`充值活动：更能降本`、`令牌类型选择建议`、`相关文档`
- H3 前 12 个：`按次计费`、`按量计费（未开放，可内测）`、`按次计费`、`按量计费`
- 模型名：`gemini-3-pro-image-preview`、`gemini-3.1-flash-image-preview`、`gemini-2.5-flash-image`
- 价格字样：`$0.09/次`、`$0.055/次`、`$0.02/次`、`$0.09 `、`$0.0818  `、`$0.075    `、`$0.24 `、`$0.88`、`$2`、`$52.8`、`$120`、`$0.075 `、`$0.134 `、`$0.11  `、`$0.24  `、`$0.055 `

### Sora Image 生图 API -> `/api-capabilities/sora-image-generation`

- H2：`🌟 核心特性`、`📋 模型信息`、`🚀 快速开始`、`📐 尺寸比例说明`、`🎯 最佳实践`、`💡 高级技巧`、`📊 成本计算器`、`⚠️ 使用限制`、`🔍 常见问题`、`🎨 效果展示`、`🔗 相关资源`
- H3 前 12 个：`基础示例`、`批量生成示例`、`尺寸使用示例`、`1. 提示词优化`、`2. 错误处理`、`3. 结果保存`、`1. 风格化生成`、`2. 场景模板`、`3. 批量主题变体`、`Q: 为什么价格这么便宜？`、`Q: 图片质量如何？`、`Q: 支持哪些语言？`
- 模型名：`GPT-Image-1`、`GPT-4o`、`gpt-4o-image`、`sora-image-edit`、`gpt-image-1`
- 价格字样：`$0.01/张`、`$0.01`、`$10`、`$40`、`$0.01 `

### Sora Image 图片编辑 API -> `/api-capabilities/sora-image-edit`

- H2：`🌟 核心特性`、`📋 功能对比`、`🚀 快速开始`、`🎯 编辑场景示例`、`💡 高级技巧`、`📊 效果对比`、`⚠️ 使用建议`、`🔍 常见问题`、`🎨 创意应用`、`🔗 相关资源`
- H3 前 12 个：`基础示例 - 单张图片编辑`、`高级示例 - 多图融合`、`1. 风格转换`、`2. 智能抠图换背景`、`3. 物体编辑`、`4. 颜色和光线调整`、`1. 批量处理优化`、`2. 编辑历史管理`、`3. 智能编辑建议`、`Q: 支持哪些图片格式？`、`Q: 可以处理多大的图片？`、`Q: 编辑后的图片分辨率？`
- 模型名：`gpt-4o-image`、`sora-image-generation`
- 价格字样：`$0.01/张`、`$0.02`、`$0.018/张`

### Flux 图像生成 API -> `/api-capabilities/flux-image-generation`

- H2：`🌟 核心特性`、`📋 模型对比`、`📐 支持的宽高比`、`🚀 快速开始`、`📝 参数详解`、`🎯 使用场景`、`💡 最佳实践`、`📊 成本对比分析`、`⚠️ 重要注意事项`、`🔍 常见问题`、`🎯 多图处理解决方案`、`🔗 相关资源`
- H3 前 12 个：`基础示例`、`通过 extra_body 传递的参数`、`高级示例 - 批量生成不同比例`、`Node.js 示例`、`1. Web 设计素材`、`2. 社交媒体内容`、`3. 专业设计`、`1. URL 管理和下载策略`、`2. 模型选择建议`、`3. 提示词优化`、`4. 宽高比选择策略`、`5. 批量处理优化`
- 模型名：`flux-kontext-pro`、`flux-kontext-max`、`flux-Image-API`、`flux-simple-batch.sh`、`flux-image-edit`
- 价格字样：`$0.035/次`、`$0.040/张`、`$0.07/次`、`$0.08/张`、`$0.035/张`、`$0.07/张`

### Flux 图像编辑 API -> `/api-capabilities/flux-image-edit`

- H2：`🌟 核心特性`、`📋 技术规格`、`🚀 快速开始`、`📝 参数详解`、`🎯 专业编辑技巧`、`🎯 编辑场景示例`、`🎨 蒙版制作指南`、`💡 最佳实践`、`📊 使用统计和优化`、`⚠️ 重要注意事项`、`🔍 常见问题`、`🎯 多图编辑解决方案`、`🔗 相关资源`
- H3 前 12 个：`基础示例 - 本地图片编辑`、`核心参数`、`通过 extra_body 传递的参数`、`高级示例 - 在线图片编辑`、`批量编辑示例`、`1. 文字编辑和添加`、`2. 智能上下文保持`、`3. 角色一致性维护`、`1. 背景替换`、`2. 物体编辑`、`3. 风格转换`、`4. 精确蒙版编辑`
- 模型名：`flux-kontext-max`、`flux-Image-API`、`flux-simple-batch.sh`、`flux-image-generation`
- 价格字样：`$0.07/次`、`$0.08/张`、`$0`

### GPT-Image 系列图像生成 -> `/api-capabilities/gpt-image-series`

- H2：`模型对比`、`快速开始`、`通用参数`、`详细文档`、`常见问题`、`相关资源`
- 模型名：`GPT-Image`、`GPT-Image-1.5`、`GPT-Image-1`、`GPT-Image-1-Mini`、`gpt-image-1.5`、`gpt-image-1`、`gpt-image-1-mini`、`gpt-image-1-5`、`sora-image-generation`
- 价格字样：`$5.00 `、`$2.50 `、`$10.00 `、`$8.00 `、`$0.01/张`、`$0.09/张`

### GPT-Image-1.5 图像生成 API -> `/api-capabilities/gpt-image-1-5`

- H2：`核心特性`、`与 GPT-Image-1 对比`、`模型定价`、`API 调用方式`、`请求参数`、`响应格式`、`最佳应用场景`、`常见问题`、`相关资源`
- H3 前 12 个：`Token 计费`、`按图片计费`、`端点地址`、`请求示例`、`信息图和文字排版`、`产品展示和电商素材`、`迭代编辑`
- 模型名：`GPT-Image-1.5`、`GPT-Image-1`、`gpt-image-1.5`、`GPT-5`、`gpt-image-1`、`GPT-Image`、`gpt-image-series`
- 价格字样：`$5.00 `、`$10.00 `、`$0.009 / 张`、`$0.013 / 张`、`$0.034 / 张`、`$0.051 / 张`、`$0.050 / 张`、`$0.133 / 张`、`$0.200 / 张`、`$5.00`、`$10.00`

### GPT-Image-1 图像生成 API - OpenAI 当下最新图片 API -> `/api-capabilities/gpt-image-1`

- H2：`概述`、`快速开始`、`API 参数详解`、`模型与定价`、`使用示例`、`提示词优化建议`、`批量生成`、`错误处理`、`最佳实践`、`与 Sora Image 的区别`、`常见问题`、`相关资源`
- H3 前 12 个：`主要特性`、`基础配置`、`生成图像`、`请求参数`、`参数详细说明`、`响应格式`、`可用模型`、`定价方式`、`模型对比`、`Python 示例`、`Node.js 示例`、`cURL 示例`
- 模型名：`GPT-Image-1`、`GPT-Image-1.5`、`gpt-image-1-5`、`gpt-image-1`、`gpt-image-1-mini`、`GPT-Image`
- 价格字样：`$2.50`、`$8.00`、`$0.005`、`$0.052/张`、`$2.50 `、`$8.00 `、`$0.005 / 张`、`$0.006 / 张`、`$0.011 / 张`、`$0.015 / 张`、`$0.036 / 张`、`$0.052 / 张`、`$0.01/张`

### 图像编辑 API -> `/api-capabilities/image-edit`

- H2：`概述`、`API 工作原理`、`快速开始`、`API 参数详解`、`创建遮罩图像`、`完整使用示例`、`实际应用场景`、`高级技巧`、`最佳实践`、`常见问题`、`相关资源`
- H3 前 12 个：`基础配置`、`基本编辑示例`、`请求参数`、`响应格式`、`使用 Python PIL 创建遮罩`、`使用圆形遮罩`、`Python 完整示例`、`Node.js 示例`、`1. 背景替换`、`2. 对象移除`、`3. 服装更换`、`4. 图像修复`
- 模型名：`gpt-image-1`

### SeeDream 4.5 生图/编辑 -> `/api-capabilities/seedream-image`

- H2：`概述`、`调用方式`、`Python 示例代码`、`使用步骤`、`cURL 示例`、`价格对比`、`特性对比`、`支持的尺寸`、`常见问题`、`最佳实践`、`相关资源`
- H3 前 12 个：`可用版本`、`正确端点 ✅`、`质量特点`、`API 特性`、`方法1：分辨率规格`、`方法2：精确像素尺寸`、`提示词优化`、`示例提示词`
- 端点/URL：`/v1/images/generations`
- 模型名：`seedream-4-5-251128`、`seedream-4-0-250828`、`GPT-Image-1`
- 价格字样：`$0.035/张`、`$0.03/张`、`$0.24/张`、`$0.09/张`、`$0.04/张`、`$0.02/张`

## 9. 重要实现结论

- APIYi 的“基础 API / 视频 API / 图片 API / 多模态理解 API / 文本 API”同属于顶部 `首页` tab 的左侧导航，不是三个孤立导航。
- `Nano Banana Pro 生图` 的真实路径是 `/api-capabilities/nano-banana-image/*`，不是 `/api-capabilities/nano-banana-pro-image/*`。
- `Nano Banana 2 生图` 与 `Nano Banana Pro 生图` 都是 3 页结构：概览、文生图 API 参考、图片编辑 API 参考。
- `VEO 3.1 视频生成` 是视频 API 里的折叠分组，包含综述、异步调用 API、同步调用 API 3 页。
- `GPT-Image 系列` 是图片 API 里的折叠分组，包含系列总览、GPT-Image-1.5、GPT-Image-1 3 页；`GPT-Image-1 图像编辑` 是同级单页。
- `API 参考` tab 当前只有 3 个页面：Chat Completions、Models List、Embeddings Create。
- `llms-full.txt` 只给中文正文页；英文页面在 sitemap 中存在，但没有进入本次正文抽取。

## 10. 机器可读 inventory

同目录 JSON：`.codex/reports/apiyi-full-navigation-content-inventory-2026-04-21.json`，包含 sitemap、导航树、每页 headings/code/table/endpoints/models/prices 抽取结果。
