# API易文档结构审计与老张API改造映射

日期：2026-04-21

## 竞品页面来源

- 首页与左侧导航：https://docs.apiyi.com/
- 基础 API 样例页：https://docs.apiyi.com/api-capabilities/model-info
- 图像与视频模型总览：https://docs.apiyi.com/api-capabilities/image-video-models
- 余额查询 API：https://docs.apiyi.com/api-capabilities/balance-query
- Gemini 原生格式调用：https://docs.apiyi.com/api-capabilities/gemini-native-format
- Claude 模型调用指南：https://docs.apiyi.com/api-capabilities/claude
- Sora 2 / Veo / Nano Banana / GPT-Image 系列页面通过线上 sitemap 与浏览器左侧菜单核对。

## 左侧菜单结构

API易把所有主要开发者入口集中在一个主标签页下，左侧菜单按任务分组：

| 分组 | 代表页面 | 结构作用 |
| --- | --- | --- |
| 产品基础 | 基本介绍、快速开始、API 手册、价格说明 | 让新用户先完成账号、价格、调用入口理解 |
| 基础 API | 热门模型、图像与视频模型、OpenAI SDK、Responses、Claude、Gemini 原生、余额查询、废弃模型 | 放通用接入、账户查询、模型迁移与基础能力 |
| 视频 API | Sora 2、Sora 2 官转、角色接口、异步接口、Veo 3.1 | 按视频供应路线和调用形态拆分 |
| 图片 API | Nano Banana 2/Pro、价格总览、Sora Image、Flux、GPT-Image、SeeDream | 按模型族拆总览和接口页，价格入口前置 |
| 多模态理解 API | 图像理解、视频理解 | 把“生成”和“理解”分开 |
| 文本 API | 对话补全、Kimi、Embedding、Moderation | 文本能力独立，避免淹没在模型列表中 |

## 页面内容形态

### 基础 API

- `model-info` 是模型推荐和模型表，适合回答“现在能用什么模型”。
- `image-video-models` 是图像与视频模型价格/状态总览，适合回答“我要生成图/视频，先选哪个模型”。
- `openai-sdk` 与 `openai-responses` 是兼容调用路径。
- `claude` 页面同时给 OpenAI 兼容格式与 Anthropic 原生格式，并强调 Claude Code 兼容。
- `gemini-native-format` 页面给 `/v1beta/models/{model}:generateContent` 原生格式、SDK 配置、多模态、工具调用、token 统计。
- `balance-query` 从账户令牌、接口、字段、额度换算、代码示例讲清楚自动余额监控。
- `deprecated-models` 用预告和已下线列表引导迁移。

### 视频 API

- Sora 2 按路线拆成同步/官逆、官转、角色接口、异步任务接口。
- Veo 3.1 先有 overview，再拆同步、异步。
- 页面共同点：首屏先说端点、调用方式、价格/稳定性边界，然后再给参数和代码。

### 图片 API

- Nano Banana 2 与 Pro 都拆成总览、文生图 API、图片编辑 API。
- 价格总览单独成页，不让用户在多个模型页里找价格。
- GPT-Image 有系列总览，再拆 GPT-Image-1.5 与 GPT-Image-1。
- 页面共同点：先比较模型族差异，再给可复制调用方式和迁移建议。

## 老张API当前状态

- 已有中英文双语 Mintlify 文档，`docs.json` 导航完整，但核心能力分散在“核心 API / 文本 API / 视频生成 API / 图像生成 API / AI 理解能力”。
- 已有大量具体能力页：Sora 2、Veo 3.1、Seedance 2.0、Nano Banana、Flux、Sora Image、GPT-Image-1、图像/视频理解、Moderation。
- 缺口主要不是“没有内容”，而是缺少几个高价值入口页：
  - 图像与视频模型总览
  - Nano Banana 系列价格总览
  - Gemini 原生格式调用
  - 余额查询 API 的能力入口
  - 废弃模型列表
  - 视频理解独立入口
  - GPT-Image 系列总览
  - Claude 模型调用指南入口

## 本轮改造决策

1. 导航按“产品基础 / 基础 API / 视频 API / 图片 API / 多模态理解 API / 文本 API”重排。
2. 不照搬 API易内容；只复用信息架构，文案、端点、价格、调用方式全部使用老张 API 当前文档中的约定。
3. 新增入口/总览页，减少超长页面和多 Tab 跳转。
4. 中英文导航一起更新，避免默认英文站点落后。
5. 所有新增 MDX 遵守 Mintlify 规范：frontmatter `title` 生成 H1，正文从 `##` 开始。

## 二次逐页校正记录

用户要求继续确认“内容正确”和“基础 / 图片 / 视频导航一致”后，本轮补充了逐页审计矩阵与修正记录：

- 记录文件：`.codex/reports/basic-image-video-page-audit-2026-04-21.md`
- 范围：中文 46 页 + 英文 46 页，覆盖 `基础 API / 图片 API / 视频 API` 三组。
- 结果：中英文导航 slug 顺序一致；三组范围内正文 H1、缺失链接、英文页跨语言链接已清零。
