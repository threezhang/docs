# SEO/GEO Evidence Log: gpt-image-2

> 采集日期：2026-04-21  
> 工作目录：`/Users/laozhang/Projects/docs`  
> 关键词：`gpt-image-2`  
> 目标市场：英语/美国为主，中文补充  
> 采集方式：Computer Use 浏览器 SERP、Google Suggest API、Google Trends、OpenAI 官方开发者文档、站内资产扫描、补充网页搜索  
> 注意：本目录下误生成的本地截图 `screenshots/serp-gpt-image-2.png` 不作为证据使用，等待用户确认后删除。

## Evidence Map

| 证据组 | 内容 | 用途 |
| --- | --- | --- |
| `SERP-main` | Google US `gpt-image-2` 首页 | 判断主词 SERP 形态、时效性、社区/新闻占比 |
| `SERP-variant-api` | Google US `gpt-image-2 API` | 判断开发者/API 意图与官方文档承接 |
| `SERP-variant-pricing` | Google US `gpt-image-2 pricing` | 判断定价意图、官方/第三方混杂风险 |
| `SERP-variant-vs` | Google US `gpt-image-2 vs` | 判断对比意图和竞争内容形态 |
| `SERP-variant-howto` | Google US `how to use gpt-image-2` | 判断用户启用/访问意图 |
| `SERP-zh-release` | Google 中文 `gpt-image-2 api 什么时候发布` | 判断中文发布状态需求 |
| `SERP-zh-pricing` | Google 中文 `gpt-image-2 价格` | 判断中文价格需求 |
| `Suggest-en-root` | Google Suggest API 英文根词 | 关键词扩展 |
| `Suggest-en-intent` | Google Suggest API 英文意图词 | API、free、how-to 扩展 |
| `Suggest-zh` | Google Suggest API 中文/日文混合建议 | 中文需求和噪声识别 |
| `Trends-us-7d` | Google Trends US Past 7 days | 趋势强度与爆发窗口判断 |
| `Official-openai-docs` | OpenAI Developers Image API 与 model docs | 官方事实边界 |
| `Owned-docs` | `/Users/laozhang/Projects/docs` 扫描 | docs.laozhang.ai 现有覆盖 |
| `Owned-blog-laozhang` | `/Users/laozhang/Projects/blog-laozhang` 扫描 | blog.laozhang.ai 现有覆盖 |
| `Owned-blog` | `/Users/laozhang/Projects/blog` 扫描 | blog 旧站/副站覆盖 |
| `Owned-yingtuai` | `/Users/laozhang/Projects/yingtuai` 扫描 | yingtu.ai 现有覆盖 |

## Collection Boundary

- `gpt-image-2` 是搜索市场已经使用的词，但 OpenAI 官方开发者文档在采集时仍以 `gpt-image-1.5`、`gpt-image-1`、`gpt-image-1-mini` 为公开 Image API 模型族核心。
- 因此本研究把两件事分开：
  - **事实边界**：是否存在公开、官方、可调用的 `gpt-image-2` API/model/pricing。
  - **搜索意图边界**：用户是否已经用 `gpt-image-2` 搜索发布、API、价格、免费、怎么用、对比。
- 本报告不能把社区、X、Reddit、第三方 provider、AI Overview 或新闻稿的说法当作 OpenAI 官方发布证明。

## SERP-main: Google US `gpt-image-2`

采集方式：Computer Use 打开 Google 搜索，参数近似 `hl=en&gl=us&pws=0`。浏览器可访问，未使用误截的本地截图。

主要结果与信号：

| 位置/元素 | 标题或来源 | URL/域名 | 关键信号 |
| --- | --- | --- | --- |
| Sponsored | ChatGPT / AI image generation | `chatgpt.com` / OpenAI | 广告位说明该词与 ChatGPT 图像生成需求强相关，但广告不等于自然排名证据。 |
| Organic / Social | “OpenAI Rolls Out GPT-Image-2 Upgrade in ChatGPT” | `x.com` | X 帖子称 ChatGPT 中出现升级/灰度，时效强但非官方文档。 |
| Forums | `r/OpenAI` / `GPT Image 2 preview` | `reddit.com` | Reddit 讨论量高，约 360+ comments，说明社区验证/体验需求强。 |
| Top stories | “GPT-Image-2 reviews and corrects its own output before you ever see it” | `startupfortune.com` | 新闻型结果，标题强调自我审查/修正能力。 |
| Top stories | “OpenAI Nears Launch Of New Image Model To Replace DALL-E” | `dataconomy.com` | 新闻型结果，强调“即将发布/替代 DALL-E”。 |
| Top stories | “OpenAI Takes Aim at Google with New Image Model” | `theinformation.com` | 新闻型结果，竞争叙事明显。 |
| People are saying | X、Reddit、LinkedIn | 多域名 | 讨论集中在 “rolling out”、“ChatGPT access”、“Thinking” 等体验词。 |

判断：

- 首页不是稳定 evergreen SERP，而是新闻、社交、论坛、灰度体验驱动。
- 主词更适合做“状态/可用性/路线判断”页，不适合直接写成官方模型百科。
- Google 对新鲜度和社区证据敏感，但这也意味着页面需要频繁更新。

## SERP-variant-api: Google US `gpt-image-2 API`

采集方式：Computer Use Google US。

主要结果与信号：

| 位置/元素 | 标题或来源 | URL/域名 | 关键信号 |
| --- | --- | --- | --- |
| AI Overview | GPT Image 2 API overview | Google AI Overview | 直接称 GPT Image 2 API 是下一代接口；该说法需官方复核，不能直接采用。 |
| Organic | Image generation guide | `https://developers.openai.com/api/docs/guides/image-generation` | OpenAI 官方开发者文档排名靠前，但文档公开模型是 GPT Image family，不是 `gpt-image-2`。 |
| Organic | What Is GPT Image 2? | `mindstudio.ai` | 第三方解释型页面，抢占新词解释意图。 |
| Organic | GPT Image 2 coming soon | `fal.ai` | provider 预告/coming-soon 型页面，说明 API 路由需求已经被 provider 捕获。 |
| Forums | `r/ChatGPT` / GPT Image 2 | `reddit.com` | 用户在问能否用、如何体验、和 API 是否相关。 |
| Provider pages | APIYI、Atlas Cloud、Kie.ai | 多域名 | 第三方 API/网关类页面混入首页，容易造成官方/第三方合同混淆。 |
| Video | OpenAI image model API / gpt-image-1.5 | YouTube 等 | 部分内容实际讲 `gpt-image-1.5` 或旧 Image API。 |

判断：

- API 意图强，且首页存在官方文档入口。
- 机会点不是“宣布官方 gpt-image-2 API”，而是解释：用户搜 `gpt-image-2 API` 时，当前可验证的 OpenAI 官方路径是什么，第三方 provider 路径是什么，哪些说法不能当成官方发布。

## SERP-variant-pricing: Google US `gpt-image-2 pricing`

采集方式：Computer Use Google US。

主要结果与信号：

| 位置/元素 | 标题或来源 | URL/域名 | 关键信号 |
| --- | --- | --- | --- |
| Organic | Pricing | `https://openai.com/api/pricing` | 官方价格页排名靠前，但公开价格需要映射到官方公开模型，不应虚构 `gpt-image-2` 官方价格。 |
| Organic | gptimages-2.com pricing | 第三方站点 | 第三方套餐页，用 `gpt-image-2` 词承接价格意图。 |
| AI Overview | Topview/Seedance 等混杂内容 | Google AI Overview | 明显混入非 OpenAI 价格/视频模型，可靠性低。 |
| Social | FutureStacked/X | `x.com` | 社交预测/爆料类内容，不是官方价格证据。 |
| Provider pages | Atlas Cloud、Kie.ai、CostGoat、IntuitionLabs、MindStudio | 多域名 | 第三方 provider 价格、测算或估算混杂。 |
| Cloud pricing | Azure OpenAI pricing | `azure.microsoft.com` | 出现 GPT-Image-1.5 Global 等相关官方/云厂商定价线索，但不是 `gpt-image-2` 官方直接证据。 |

判断：

- 价格 SERP 的核心问题是“合同边界混乱”：官方 OpenAI pricing、Azure/云厂商模型、第三方 reseller、估算页混排。
- 这类词很适合做 contract-correction 页面：先告诉用户官方是否有独立 `gpt-image-2` 价格，再拆第三方路由。

## SERP-variant-vs: Google US `gpt-image-2 vs`

采集方式：Computer Use Google US。

主要结果与信号：

| 位置/元素 | 标题或来源 | URL/域名 | 关键信号 |
| --- | --- | --- | --- |
| Forums | Reddit r/OpenAI | `reddit.com` | 对比、体验、预览讨论明显。 |
| Top stories | Startup Fortune、Dataconomy、The Information、Geek Vibes Nation | 多新闻域名 | 对比叙事集中在 OpenAI 新图像模型与 Google/其他图像模型竞争。 |
| Provider | GPT Image 2 | `fal.ai` | provider 预告/路由页面。 |
| Comparison | Imagen 2 vs GPT Image 1.5 vs Midjourney | `mindstudio.ai` | 对比页面存在，但不一定准确覆盖 `gpt-image-2`。 |
| Social | Nano Banana Pro comparison posts | X/社区 | “vs Nano Banana Pro” 有市场可见度。 |

相关搜索：

- `Gpt image 2 vs reddit`
- `Gpt image 2 vs openai`
- `OpenAI image-2`
- `GPT Hazel`

判断：

- 对比词不是稳定型号对型号参数页，而是“灰度体验 + 竞品路线”。
- 最值得做的对比不是泛泛 `gpt-image-2 vs all models`，而是 `gpt-image-2 vs Nano Banana Pro`、`gpt-image-2 vs gpt-image-1.5`、`gpt-image-2 vs ChatGPT image generation` 这类有明确决策边界的页面。

## SERP-variant-howto: Google US `how to use gpt-image-2`

采集方式：Computer Use Google US。

主要结果与信号：

| 位置/元素 | 标题或来源 | URL/域名 | 关键信号 |
| --- | --- | --- | --- |
| AI Overview | How to use GPT Image 2 | Google AI Overview | 建议 prompts、reference images、masking、iterations 等，但来源偏教程/视频，需复核。 |
| Sponsored | ChatGPT | `chatgpt.com` | 用户可能把 “use” 理解为 ChatGPT 入口，而不是 API。 |
| Organic | What Is GPT Image 2? | `mindstudio.ai` | 第三方解释。 |
| Organic | how-to-use pages | `gpt-image2.net` 等 | 薄教程页抢占流量。 |
| Forums | Reddit r/OpenAI preview | `reddit.com` | 用户询问是否已经能用、如何看到入口。 |
| Forums | OpenAI Community: “How to use new image generation update?” | `community.openai.com` | 官方社区类问题，说明入口/账号灰度是实际痛点。 |

判断：

- How-to 词应拆成两层：ChatGPT 消费者入口和 API 开发者入口。
- 在官方 API 未公开 `gpt-image-2` model row 前，API 文章必须引导到官方 Image API / Responses API 的可用模型族，而不是承诺 `gpt-image-2` 可调用。

## SERP-zh-release: Google 中文 `gpt-image-2 api 什么时候发布`

采集方式：Computer Use Google 中文。

主要结果与信号：

| 标题或来源 | URL/域名 | 关键信号 |
| --- | --- | --- |
| `GPT Image 2 上线了吗? 2026-04-17 最新汇总: 灰度测试中...` | `help.apiyi.com` | 中文市场已有“上线了吗/灰度测试/发布时间”需求。 |
| `GPT-Image-2 API 什么时候发布：还没有公开日期，现在先用 ...` | `blog.laozhang.ai` | 自有资产已覆盖发布状态核心词。 |
| EvoLink 相关页面 | 第三方 | 可能存在“已公开/可用”类冲突表述，需事实复核。 |
| 掘金、知乎、CSDN、W2Solo、Mew.Design | 中文内容站/社区 | 中文社区正在追踪灰度、可用性和替代路线。 |
| OpenAI Help release notes | `help.openai.com` | SERP 混入官方 release notes，但结果不一定直接证明 `gpt-image-2` API 发布。 |

判断：

- 中文发布状态词已有自有排名资产，应优先更新，不应新建重复页面。
- 中文 SERP 对“灰度测试中/还没有公开日期/现在先用什么”接受度高。

## SERP-zh-pricing: Google 中文 `gpt-image-2 价格`

采集方式：Computer Use Google 中文。

主要结果与信号：

| 标题或来源 | URL/域名 | 关键信号 |
| --- | --- | --- |
| gptimg2.io pricing | 第三方 | 第三方价格页顶部可见。 |
| `官方 OpenAI 其实看 GPT-Image-1.5，低价页另算` | `blog.laozhang.ai` | 自有资产已用 contract-correction 方式覆盖价格词。 |
| APIYI vs Nano Banana Pro | `help.apiyi.com` | 明确提示 gpt-image-2 价格是行业估算，最终以官方为准。 |
| OpenAI 中文 API pricing | OpenAI / 中文路径 | 官方价格页进入 SERP。 |
| APIMart、PoloAPI 等 | 第三方 provider | 出现 `$0.04`、`$0.05` 等 provider 价格主张，需区分官方/第三方。 |
| PAA | ChatGPT API free、SORA 2 price、GPT 4.1 price、OpenAI API credits | 价格词会外溢到免费、API credits、相邻模型价格。 |

判断：

- 中文价格意图很适合自有 contract-correction 页面继续维护。
- 必须把官方 OpenAI、Azure/云厂商、第三方 provider、应用套餐拆开。

## Suggest-en-root

采集方式：Google Suggest API `client=chrome`。

`gpt-image-2` 返回：

- `gpt-image-2 release date`
- `gpt image 2.0`
- `gpt image 2.5`
- `gpt image 2 reddit`
- `gpt image 2 model`
- `gpt image 2 api`
- `gpt image 2 openai`
- `gpt image 2 release`
- `gpt oss 20b image`
- `gpt image gen 2`
- `gpt 2 image generation`
- `gpt 2.5 flash image`
- `chatgpt image prompts 2025`
- `gpt image 2 free`

`gpt image 2` 返回：

- `gpt image 2 release date`
- `gpt image 2.0`
- `gpt image 2 lmarena`
- `gpt image 2 reddit`
- `gpt image 2 api`
- `gpt image 2 model`
- `gpt image 2 arena`
- `gpt image 2.5`
- `gpt image 2 openai`
- `gpt image 2 release`
- `gpt 2 image generation`
- `gpt image v2`
- `gpt image gen 2`
- `chatgpt image 2`
- `chat gpt image 2.0`

判断：

- Autocomplete 明确支持 release/date/API/reddit/model/openai/LM Arena/ChatGPT/free 等方向。
- `gpt 2 image generation`、`gpt oss 20b image`、`gpt 2.5 flash image` 属于噪声或跨产品混淆，不建议主打。

## Suggest-en-intent

采集方式：Google Suggest API `client=chrome`。

`gpt-image-2 api` 返回：

- `gpt image 2 api`
- `gpt-4 api image`
- `gpt-4 api image input`
- `gpt openai api`
- `gpt-4 api 画像`

`gpt-image-2 pricing` 返回：无明显建议。

`gpt-image-2 vs` 返回：无明显建议。

`how to use gpt-image-2` 返回：

- `how to use image gpt`
- `how to use gpt 4 with images`
- `how can i use gpt-4 with images`

`gpt-image-2 free` 返回：

- `gpt image 2 free`
- `is gpt 2 free`
- `gpt-2 image generation`
- `image gpt2`
- `gpt image`
- `gpt 4 無料`
- `gpt-4 画像 使い方`

判断：

- API/free/how-to 会被 Google 自动联想到更老的 GPT-4 image、GPT-2、日文“画像/無料”查询。
- 需要在标题和首屏中主动消歧：`GPT Image 2` 不是旧 `GPT-2 image generation`，也不是所有第三方免费站。

## Suggest-zh

采集方式：Google Suggest API `client=chrome`。

`gpt-image-2 价格` 返回：

- `gpt-2 料金`
- `gpt-4 image`
- `gpt-4 images`
- `gpt-4 image demo`
- `image gpt2`

`gpt-image-2 怎么用` 返回：

- `gpt-4怎么用`
- `gpt-4 image`
- `gpt-4 图像输入`
- `image gpt2`

`gpt-image-2 api 什么时候发布` 返回：

- `gpt-4 api image`
- `gpt-4 api 画像`
- `gpt-4 图像处理`
- `gpt-4 apiとは`
- `api gpt-4`

判断：

- 中文 Suggest 对 exact `gpt-image-2` 还不稳定，常回退到 GPT-4 image / GPT-2 / 日文词。
- 中文侧更适合用 SERP 和已有自有资产判断机会，不宜只看 Suggest。

## Trends-us-7d

采集方式：Google Trends，US，Past 7 days，Web Search，查询 `gpt-image-2`。

观察信号：

- Interest over time 大多数时段为 0。
- 2026-04-17 16:00 左右出现峰值 100。
- 2026-04-17 15:00 约 67，17:00 约 71。
- 2026-04-16 22:00、2026-04-17 09:00 约 16。
- 2026-04-20 11:00 左右有小峰值约 21。
- Interest by subregion：California 100、Washington 43、Arizona 25、New York 12、Texas 6。
- Related topics Rising：Generative pre-trained transformer、Duct tape、2023、Claude、PDF 等，部分可能来自代号/社区噪声。
- Related queries Rising：
  - `gpt image 2 怎么 用`：Breakout
  - `gpt`：+300%
  - `gpt image 2`：+120%

判断：

- 这是明显的 spike-driven topic，不是长期稳定高量词。
- 适合快速更新/抢新鲜度，也适合 GEO/AI answer 引用，但需要版本日期和复核机制。

## Official-openai-docs

采集方式：OpenAI Developer Docs 官方文档搜索与抓取。

使用来源：

- `https://developers.openai.com/api/docs/guides/image-generation`
- `https://developers.openai.com/api/docs/guides/image-generation#image-api`
- `https://developers.openai.com/api/docs/models/gpt-image-1.5`
- `https://openai.com/api/pricing`

关键事实：

- OpenAI Image API 文档公开支持的 GPT Image family 包括：
  - `gpt-image-1.5`
  - `gpt-image-1`
  - `gpt-image-1-mini`
  - 以及旧的 `dall-e-2`、`dall-e-3`
- `gpt-image-1.5` model page 将其描述为 latest / state-of-the-art image generation model，模型 ID 为 `gpt-image-1.5`，snapshot 为 `gpt-image-1.5-2025-12-16`。
- 文档说明可以通过 Image API 或 Responses API 做图像生成/编辑；Image API 承接 generations/edits/variations，Responses API 承接对话和多步工作流。
- GPT Image models 可能需要 organization verification。
- DALL-E 2/3 被标为 deprecated，支持停止日期为 2026-05-12。
- 在本次采集中，没有从 OpenAI 官方开发者文档确认到公开可调用的 `gpt-image-2` model row、官方 API 发布日期或独立官方定价行。

判断：

- 官方事实页的主线仍应是 `gpt-image-1.5` / GPT Image family。
- 面向搜索的页面可以保留 `gpt-image-2` 作为用户查询词，但正文必须把官方可验证路线写清楚。

## Owned-docs

扫描路径：`/Users/laozhang/Projects/docs`。

主要发现：

- 未发现公开 MDX 文档中已有 exact `gpt-image-2` 主题页。
- 已有相关覆盖：
  - `api-manual.mdx` 提及/推荐 `gpt-image-1`。
  - `docs.json` 包含 `api-capabilities/gpt-image-1` 与 `en/api-capabilities/gpt-image-1` 导航。
  - `public/sitemap.xml` 包含 `https://docs.laozhang.ai/gpt-image-1`。
  - `llms.txt` 包含 GPT-Image-1 生成相关说明。
  - `api-capabilities/model-info.mdx` 包含 GPT-Image-1.5、GPT-Image-1、GPT-Image-1 Mini、Sora Image、GPT-4o Image 等 image models。
  - `api-capabilities/gpt-image-1.mdx` 是 GPT-Image-1 能力页。

判断：

- docs.laozhang.ai 当前不适合直接创建 SEO 型 `gpt-image-2` rumor/status 页面。
- 可以在模型能力页增加“当前官方公开模型边界”说明，但应以产品文档准确性为目标，不承担主 SEO 入口。

## Owned-blog-laozhang

扫描路径：`/Users/laozhang/Projects/blog-laozhang`。

已存在 exact cluster：

- `data/posts/en/gpt-image-2-api-release-date/gpt-image-2-api-release-date.mdx`
- `data/posts/zh/gpt-image-2-api-release-date/gpt-image-2-api-release-date.mdx`
- `data/posts/ru/gpt-image-2-api-release-date/gpt-image-2-api-release-date.mdx`
- `data/posts/ja/gpt-image-2-api-release-date/gpt-image-2-api-release-date.mdx`
- `data/posts/ko/gpt-image-2-api-release-date/gpt-image-2-api-release-date.mdx`
- `data/posts/es/gpt-image-2-api-release-date/gpt-image-2-api-release-date.mdx`
- `data/posts/en/gpt-image-2-api-pricing/gpt-image-2-api-pricing.mdx`
- `data/posts/zh/gpt-image-2-api-pricing/gpt-image-2-api-pricing.mdx`
- `data/posts/ru/gpt-image-2-api-pricing/gpt-image-2-api-pricing.mdx`
- `data/posts/ja/gpt-image-2-api-pricing/gpt-image-2-api-pricing.mdx`
- `data/posts/ko/gpt-image-2-api-pricing/gpt-image-2-api-pricing.mdx`
- `data/posts/es/gpt-image-2-api-pricing/gpt-image-2-api-pricing.mdx`
- `data/posts/en/gpt-image-2-reverse-api-call/gpt-image-2-reverse-api-call.mdx`
- `data/posts/zh/gpt-image-2-reverse-api-call/gpt-image-2-reverse-api-call.mdx`
- `data/posts/ru/gpt-image-2-reverse-api-call/gpt-image-2-reverse-api-call.mdx`
- `data/posts/ja/gpt-image-2-reverse-api-call/gpt-image-2-reverse-api-call.mdx`
- `data/posts/ko/gpt-image-2-reverse-api-call/gpt-image-2-reverse-api-call.mdx`
- `data/posts/es/gpt-image-2-reverse-api-call/gpt-image-2-reverse-api-call.mdx`

读取到的核心定位：

- `gpt-image-2-api-release-date`：标题为 “No Public API Date Yet, Use GPT Image 1.5 Now”，日期 2026-04-19。首屏结论是截至 2026-04-19 没有公开 OpenAI API 日期或 model row，当前应使用官方 Image API / Responses API 与 `gpt-image-1.5`。
- `gpt-image-2-api-pricing`：标题为 “Official OpenAI Pricing Maps to GPT Image 1.5, Cheap Pages Are a Different Route”，日期 2026-04-17，更新 2026-04-18。首屏结论是没有独立官方 `gpt-image-2` pricing row，官方价格应映射到 `gpt-image-1.5` / GPT Image Latest，低价页属于第三方路由。
- `gpt-image-2-reverse-api-call`：路线优先，拆分 official OpenAI、provider route、reverse account pool、consumer surface。

判断：

- blog.laozhang.ai 已经覆盖 P0 发布日期、P0 价格、P1/P2 反向调用边界。
- 2026-04-21 SERP 已出现更强新闻/社交/Trends 信号，现有页面应更新而不是新建重复页。
- 缺口更可能是 `gpt-image-2 vs Nano Banana Pro`、`gpt-image-2 ChatGPT access vs API`、`gpt-image-2 how to use` 的决策页。

## Owned-blog

扫描路径：`/Users/laozhang/Projects/blog`。

主要发现：

- 未发现 exact `gpt-image-2` 主题页。
- 有大量 `gpt-image-1.5`、OpenAI image API、pricing/tutorial 相关页面。

判断：

- 如果该站仍承担内容生产，可以作为旧 image API cluster 的补充，但不应和 blog.laozhang.ai 抢 exact `gpt-image-2` 首发。
- 如要做，应做站内上下文自然的 `gpt-image-1.5` 到 `gpt-image-2` 状态更新，而不是重复发布 exact cluster。

## Owned-yingtuai

扫描路径：`/Users/laozhang/Projects/yingtuai`。

主要发现：

- 未发现公开内容中的 exact `gpt-image-2` SEO 页面。
- 存在 tmp/smoke-test 相关痕迹，例如 provider 模型名 `gpt-image-2-all`、`gpt-image-2` 的测试失败/无可用 channel 信息；这些不应作为公开 SEO 证据。
- 公开内容中已有 GPT Image 1.5 与图像模型对比/工具使用类内容。

判断：

- yingtu.ai 更适合承接图像生成工作流、提示词、质量对比、工具入口类页面。
- 在官方 API 未清晰之前，不建议让 yingtu.ai 做 `gpt-image-2 API release/pricing` 主入口。

## External Source Notes

可用于后续文章复核的源：

- OpenAI Image generation guide: `https://developers.openai.com/api/docs/guides/image-generation`
- OpenAI GPT Image 1.5 model page: `https://developers.openai.com/api/docs/models/gpt-image-1.5`
- OpenAI API pricing: `https://openai.com/api/pricing`
- Google SERP US: `https://www.google.com/search?q=gpt-image-2&hl=en&gl=us&pws=0`
- Google SERP API variant: `https://www.google.com/search?q=gpt-image-2+API&hl=en&gl=us&pws=0`
- Google SERP pricing variant: `https://www.google.com/search?q=gpt-image-2+pricing&hl=en&gl=us&pws=0`
- Google Trends: `https://trends.google.com/trends/explore?date=now%207-d&geo=US&q=gpt-image-2&hl=en-US`

## Evidence Risks

- Google SERP、Top stories、X、Reddit 变化很快，24-48 小时内可能明显漂移。
- AI Overview 在 API/pricing/how-to 变体里存在不可靠混杂，不能作为事实来源。
- 第三方 provider 的 “GPT Image 2” 命名、价格和可用性可能是预告、包装名、内部路由名或非官方别名。
- 中文 Suggest 对 exact 词不稳定，不能单独证明中文搜索量。
- 本研究没有 Ahrefs/SEMrush 等专业量级数据，搜索量判断为间接推断。
