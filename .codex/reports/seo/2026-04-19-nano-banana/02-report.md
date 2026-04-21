# SEO / GEO 关键词研究报告：nano banana

> 数据局限性说明：本报告基于 Computer Use 实时浏览器 SERP 采集、补充搜索、Google Suggest API、自有资产扫描与社区/论坛证据。无 Ahrefs/SEMrush 等专业工具支持，搜索量和关键词难度为基于 SERP、广告、Autocomplete、Trends 的间接推断。SERP 数据为搜索时快照，排名会动态变化。

- 关键词：`nano banana`
- 采集日期：2026-04-19
- 目标语言/地区：英文 US/全球 + 中文 API/价格/教程意图
- 主要采集方式：Computer Use Google SERP/Trends、Google Suggest API、官方 Google 文档、站群资产扫描
- Computer Use SERP 证据：已完成 7 个 SERP + 2 个 Google Trends 截图，见 `01-evidence.md` 的 `Capture Status`
- Google/Trends 阻塞或降级：权限完成后未遇到 CAPTCHA；无 paid keyword volume

## 一、结论先行

- **这个词值不值得做**：值得做，但不能把 `nano banana` 当作单一泛词硬打。它已经是 Google Gemini 图像能力、第三方在线工具、免费入口、API 价格、教程、Prompt、Pro/2 对比的混合入口。证据：`SERP-main`、`SERP-variant-api`、`Suggest-en-root`。
- **Google Trends 趋势**：全球 12 个月峰值在 2025-09-07，当前 2026-04-19 为 22；美国峰值在 2025-11-23，当前为 26。不是爆发初期，但仍有稳定长尾和商业查询。证据：`Trends-worldwide`、`Trends-us`。
- **搜索量级别**：中高。裸词有官方页面、广告、视频和第三方工具竞争；API/pricing/free/vs/tutorial 的长尾非常密集。证据：`SERP-main`、`Suggest-api`、`Suggest-pricing`。
- **不建议直接打的原因**：裸词首页同时有 Google Gemini 官方、第三方工具、广告、视频、PAA 和相关搜索。没有明确页面角色会变成泛百科，难以承接转化。证据：`SERP-main`。
- **最值得切入的次级角度**：`nano banana api`、`nano banana api pricing`、`nano banana 2 api`、`nano banana pro pricing`、`nano banana free api`、`nano banana 2 vs nano banana pro`、`nano banana cost per image`。证据：`SERP-variant-api`、`SERP-variant-pricing`、`Suggest-api`。
- **自有资产现状**：站群覆盖很强，尤其 docs、blog、yingtu、aifreeapi 都已有页面。但 docs 存在高优先级 drift：sitemap 仍推 `gemini-flash-image` 旧 URL；英文旧页把 Banana2 映射成 Pro 模型。证据：`Owned-docs-local`。
- **推荐主力发布站点**：docs.laozhang.ai 先做 API 路由真相源；blog.laozhang.ai 做技术教程/错误/对比；aifreeapi.com 做 free/cheap 合同纠偏；yingtu.ai 做图片工具、Prompt、教程和创作者对比。
- **对业务网络的核心价值**：把用户的昵称/入口/价格混乱转成老张 API 的模型选择、价格优势、试用和调用转化。证据：`Official-Google-Image-Docs`、`Official-Google-Pricing`、`Owned-docs-local`。
- **最终判断**：P0 不是新建泛泛的 "What is Nano Banana"；P0 是修 docs canonical/模型映射，并做一个 `Nano Banana API route map`，首屏直接回答 Standard、Banana2、Pro 该怎么选。

## 二、关键词机会分层

### 1. 优先做

| 关键词 | 理由和证据 | 推荐站点 | 业务匹配 |
| --- | --- | --- | --- |
| nano banana api | API SERP 第一屏官方 docs 领先，PAA 明确问是否可通过 API 使用；适合模型 ID/端点转换。证据：`SERP-variant-api` | docs.laozhang.ai | 直接转化 |
| nano banana api pricing | pricing SERP 混杂官方价、wrapper 价、Reddit；需要权威合同页。证据：`SERP-variant-pricing`、`Official-Google-Pricing` | docs.laozhang.ai | 直接转化 |
| nano banana api key | Suggest 明确，用户需要入口和调用路线。证据：`Suggest-api` | docs.laozhang.ai | 直接转化 |
| nano banana api documentation | 官方 docs 排名强，但 LaoZhang 需要 OpenAI-compatible + native route。证据：`SERP-variant-api`、`Owned-docs-local` | docs.laozhang.ai | 直接转化 |
| nano banana 2 api | 官方定义 Banana2 = `gemini-3.1-flash-image-preview`；当前 docs 中文页已具备基础。证据：`Official-Google-Image-Docs`、`Owned-docs-local` | docs.laozhang.ai | 直接转化 |
| nano banana 2 pricing | Suggest 和 pricing related search 明确；官方价按 0.5K/1K/2K/4K 拆分。证据：`Suggest-pricing`、`Official-Google-Pricing` | docs.laozhang.ai | 直接转化 |
| nano banana pro api | Pro 是高画质/复杂指令/4K/API 需求；Google Cloud 也强调 Vertex AI/Gemini API。证据：`Official-Google-Launches` | docs.laozhang.ai | 直接转化 |
| nano banana pro pricing | 官方 Pro 为 1K/2K $0.134、4K $0.24；老张 docs $0.09，有明确价格差。证据：`Official-Google-Pricing`、`Owned-docs-local` | docs.laozhang.ai | 直接转化 |
| nano banana cost per image | Suggest 明确；用户不只问套餐，而是每张成本。证据：`Suggest-problem-and-developer` | blog.laozhang.ai | 间接转化 |
| nano banana free api | 搜索强，但必须纠偏：官方 image model API pricing rows 没有 free tier。证据：`Suggest-free`、`Official-Google-Pricing` | aifreeapi.com | 间接转化 |
| nano banana api key free | 高流量但风险高，适合 free/paid boundary 页。证据：`Suggest-api` | aifreeapi.com | 间接转化 |
| nano banana 2 vs nano banana pro | 用户需要当前默认路线：Banana2 高性价比，Pro 高质量/复杂任务。证据：`SERP-variant-vs`、`Official-Google-Image-Docs` | blog.laozhang.ai | GEO/转化 |
| nano banana vs nano banana pro | Suggest 和 SERP 都强，但必须先澄清 Standard/2/Pro。证据：`Suggest-models-and-comparison` | yingtu.ai | 品牌支持 |
| nano banana api 中转站 | 中文 Suggest 明确，和 LaoZhang API 中转业务强匹配。证据：`Suggest-zh` | docs.laozhang.ai | 直接转化 |
| nano banana 价格 / nano banana api 价格 | 中文 SERP 已出现 docs.laozhang.ai Pro 页，值得巩固。证据：`SERP-zh-pricing` | docs.laozhang.ai | 直接转化 |

### 2. 可做但不优先

| 关键词 | 理由和证据 | 推荐站点 |
| --- | --- | --- |
| nano banana prompt guide | 教程 SERP 视频/Prompt 导向强，适合工具站而非 docs。证据：`SERP-variant-tutorial` | yingtu.ai |
| nano banana prompt generator | Creator 工具意图强，可做交互/模板。证据：`Suggest-en-root` | yingtu.ai |
| nano banana tutorial | 视频竞争强，转化较弱。证据：`SERP-variant-tutorial` | yingtu.ai |
| nano banana tutorial for beginners | 可做入门，但不要和 API docs 混写。证据：`Suggest-tutorial` | yingtu.ai |
| nano banana tutorial photoshop | Creator/Photoshop 场景，不适合 docs。证据：`Suggest-tutorial` | yingtu.ai |
| nano banana guide prompt | 可做 Prompt 库和案例。证据：`Suggest-tutorial` | yingtu.ai |
| nano banana not working | 问题强，但应归入排障 hub。证据：`Suggest-problem-and-developer` | blog.laozhang.ai |
| nano banana error 429 | 明确 API/配额问题，适合技术博客。证据：`Suggest-problem-and-developer` | blog.laozhang.ai |
| nano banana error 503 | 明确 overloaded/服务可用性问题。证据：`Suggest-problem-and-developer` | blog.laozhang.ai |
| nano banana rate limit api | 可做配额/限流解释。证据：`Suggest-problem-and-developer` | blog.laozhang.ai |
| nano banana python api | 技术长尾，可放在 API guide 支撑文章。证据：`Suggest-problem-and-developer` | blog.laozhang.ai |
| nano banana api endpoint | 直接贴合 OpenAI-compatible/native endpoint。证据：`Suggest-api` | docs.laozhang.ai |
| nano banana gemini app | 消费端 app 意图，适合图片工具站。证据：`SERP-main`、`Official-Google-Launches` | yingtu.ai |
| nano banana 国内使用 | 只有配合 API/中转/价格才值得做。证据：`Suggest-zh`、`SERP-zh-pricing` | docs.laozhang.ai |
| nano banana 国内 怎么用 | 中文教程/入口意图，适合工具站。证据：`Suggest-zh` | yingtu.ai |
| nano banana pro 4k price | Pro 4K 价格明确，但需避免重复 pricing 主文。证据：`Official-Google-Pricing` | blog.laozhang.ai |
| nano banana vs midjourney | 大流量但偏评测/创作者，不是 API 转化主线。证据：`SERP-variant-vs` | yingtu.ai |
| nano banana vs chatgpt image generation | 需要规范比较对象，适合创作者/模型选择。证据：`Suggest-models-and-comparison` | yingtu.ai |

### 3. 不建议做

| 关键词 | 不建议原因 | 证据 |
| --- | --- | --- |
| nano banana 3 | Suggest 有，但无官方模型证据；容易做成谣言页。 | `Suggest-en-root`、`Official-Google-Image-Docs` |
| nano banana free unlimited | 官方 API pricing rows 不支持这种承诺；只能做纠偏，不可做承诺页。 | `Suggest-free`、`Official-Google-Pricing` |
| nano banana free video generator | Nano Banana 是 image generation/editing；视频应路由 Veo/Flow。 | `Suggest-free`、`Official-Google-Image-Docs` |
| nano banana download | 下载意图不清，容易变成第三方 app/wrapper 噪声。 | `Suggest-free` |
| nano banana no sign up | 和业务转化冲突，且多数是 wrapper 承诺。 | `Suggest-free` |
| nano banana watermark removal / 去水印 | 合规风险高；最多解释 SynthID/水印政策。 | `Official-Google-Image-Docs` |
| nano banana 破解版 / 越狱 | 中文 SERP 相关词有风险，不应承接。 | `SERP-zh-tutorial` |
| nano banana tutorial architecture | 语义不清，可能是建筑也可能是技术架构；需要二次拆词。 | `Suggest-tutorial` |

### 附录：关键词原始来源

- Autocomplete：`Suggest-en-root`、`Suggest-api`、`Suggest-pricing`、`Suggest-free`、`Suggest-models-and-comparison`、`Suggest-problem-and-developer`、`Suggest-zh`
- 标题反向提词：`SERP-main`、`SERP-variant-api`、`SERP-variant-pricing`、`SERP-variant-tutorial`、`SERP-variant-vs`
- 竞品覆盖词：Google Gemini, nanobanana.io, nanobananaapi.ai, Adobe Firefly, Artlist, wrapper pricing pages, Fal.ai, forum/Reddit pages
- 社区问题：`Community Evidence`
- 自有资产：`Owned-docs-local`、`Owned-blog-laozhang-local`、`Owned-blog-local`、`Owned-yingtu-local`、`Owned-aifreeapi-web`
- Google Trends：`Trends-us`、`Trends-worldwide`

## 三、SERP 结构判断

1. **搜索意图**：裸词 = 官方产品/第三方工具/免费/教程混合；API = 开发者购买和接入；pricing/free = 合同纠偏；tutorial/prompt/vs = creator 和模型选择。证据：`SERP-main`、`SERP-variant-api`、`SERP-variant-tutorial`。
2. **首页前 10 逐条分析**：

| 排名 | 标题 | URL | 域名类型 | 摘要关键信号 |
| --- | --- | --- | --- | --- |
| 1 | Nano Banana 2 - Gemini AI image generator & photo editor | `gemini.google/overview/image-generation/` | Google 官方/消费端 | 官方产品入口，覆盖 image generator/photo editor |
| 2 | Nano Banana: Free Online AI Image Editor | `nanobanana.io` | 第三方工具 | 免费在线编辑器，强吃 free/tool intent |
| 3 | Image editing in Gemini just got a major upgrade | `blog.google/.../updated-image-editing-model/` | Google 官方博客 | 解释 Gemini app Nano Banana |
| 4 | Gemini 3.1 Flash Image model page | `aistudio.google.com/models/gemini-3-1-flash-image` | Google AI Studio | 明确 `aka Nano Banana 2` 和 API key |
| 5 | Gemini Image / Nano Banana family | `deepmind.google/models/gemini-image/` | Google DeepMind | 模型家族权威页面 |
| 6 | Nano Banana online tool | `nano-banana.com` | 第三方工具 | 工具入口，通常声明非官方 |
| 7 | Artlist Nano Banana Pro | `artlist.io` | 商业工具/广告生态 | Pro 商业创作入口 |
| 8 | Video block: 48 ways / update / review | YouTube | 视频 | 教程和玩法强需求 |
| 9 | PAA block | Google SERP feature | 问答 | what/free/famous/cost |
| 10 | Related searches | Google SERP feature | 查询扩展 | 2 Pro/free/AI/Gemini/English/Google |

3. **域名类型分布**：官方 Google + 第三方工具 + 视频 + 广告 + PAA 混排。API 变体则官方 docs 第一，pricing 变体第三方价格页和 Reddit 更强。证据：`SERP-main`、`SERP-variant-api`、`SERP-variant-pricing`。
4. **SERP 主导意图**：裸词不是纯 API；API/pricing/free 才是 LaoZhang 最该抓的商业意图。证据：`SERP-variant-api`。
5. **标题模式总结**：`Nano Banana API`、`Nano Banana 2`、`Nano Banana Pro`、`Pricing`、`Free`、`Tutorial`、`Vs` 是主模式。证据：`Suggest-*`。
6. **Google 偏好的内容形态**：官方模型页、工具页、价格表、视频教程、社区讨论、比较页。证据：`SERP-main` 到 `SERP-variant-vs`。
7. **前 3 名赢在哪里**：官方页面赢权威和品牌；第三方工具页赢直接可用；价格页赢简单表格和 exact-match intent。证据：`SERP-main`、`SERP-variant-pricing`。
8. **4-10 位是否存在切入窗口**：存在，尤其是 API route map、价格合同、free API reality、模型对比。证据：`SERP-variant-api`、`SERP-variant-pricing`。
9. **SERP 特殊元素**：广告、PAA、视频块、AI Overview、相关搜索、"people also search for" 均出现。证据：`SERP-main`、`SERP-variant-pricing`、`SERP-variant-tutorial`。
10. **广告信号**：主词和 API 词都有广告，说明商业价值明确。证据：`SERP-main`、`SERP-variant-api`。
11. **Google Trends 趋势**：全球当前 22，美国当前 26，已从峰值回落但仍有长尾。证据：`Trends-worldwide`、`Trends-us`。
12. **Google Trends 相关查询**：US rising 包含 pro/AI/Google 组合；worldwide rising 包含 Gemini/API/Google AI Studio。证据：`Trends-us`、`Trends-worldwide`。
13. **风险判断**：价格、免费层、consumer quota、模型生命周期高度易变；发布前必须复核官方 pricing/deprecations。证据：`Volatile Facts To Recheck Before Publishing`。

## 四、内容缺口与切入机会

1. **当前内容同质化点**：很多页面承诺 free/cheap 或只列一个价格，不解释官方模型 ID、分辨率、Batch/Flex、consumer app 与 API 的差异。证据：`SERP-variant-pricing`、`Owned-aifreeapi-web`。
2. **确认的内容缺口**：可信的三模型 API 路由表：Standard = `gemini-2.5-flash-image`，Banana2 = `gemini-3.1-flash-image-preview`，Pro = `gemini-3-pro-image-preview`，同时给老张价、官方价、端点、分辨率、适用场景。证据：`Official-Google-Image-Docs`、`Owned-docs-local`。
3. **社区真实痛点**：API key/free、rate limit、429/503、价格、Pro vs 2、no image、request denied、质量/分辨率。证据：`Community Evidence`、`Suggest-problem-and-developer`。
4. **最容易赢的切角**：docs 先修 sitemap/旧英文页，然后用一个 route-map hub 汇聚现有 Standard/Banana2/Pro 页面。证据：`Owned-docs-local`。
5. **不建议正面硬打的方向**：`free unlimited`、下载、去水印、破解版、Nano Banana 3、视频生成。证据：`不建议做`。
6. **更适合打的次级意图**：API pricing、API key、cost per image、free API reality、Banana2 vs Pro、Python/endpoint、中文 API 中转。证据：`Suggest-api`、`Suggest-zh`。
7. **自有资产利用建议**：docs 做 canonical router；blog 做技术长尾；aifreeapi 做 free/cheap 纠偏；yingtu 做 Prompt/教程/工具体验。证据：`Owned-*`。

## 五、业务承接判断

1. **这个词更适合拿什么**：API 模型选择、价格认知、注册试用、调用迁移和故障排查流量。
2. **最适合承接到什么页面类型**：docs hub + 模型专页 + pricing guide；不要优先做泛百科。
3. **用户真实需求偏向**：英文用户问 API、pricing、free、vs、tutorial；中文用户问价格、入口、国内使用、API 中转。
4. **对业务的真实价值**：将 Google 官方复杂命名转换为老张 API 简化调用路线，并把价格优势可视化。
5. **在站内集群中的角色**：docs 是 truth source；blog/aifreeapi/yingtu 是意图分发和转化辅助。

## 六、切入角度优先级

1. **第一推荐切入角度**：`Nano Banana API Route Map`，首屏给模型选择表和端点。证据：`Official-Google-Image-Docs`、`Owned-docs-local`。
2. **第二推荐切入角度**：`Nano Banana API Pricing`，拆官方价、老张价、resolution、Batch/Flex、consumer/app 边界。证据：`Official-Google-Pricing`、`SERP-variant-pricing`。
3. **第三推荐切入角度**：`Nano Banana Free API Reality`，把 free app/AI Studio/production API/wrapper credits 分开。证据：`Suggest-free`、`Official-Google-Pricing`。
4. **不建议优先做的角度**：naked `nano banana` 泛解释、download、free unlimited、去水印、Nano Banana 3。

## 七、内容规划

### 7.1 文章优先级列表

| 优先级 | 文章主题 | 目标关键词 | 页面类型 | 推荐 Title | 推荐 URL slug | 发布站点 | 页面角色 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| P0 | docs 旧 alias / sitemap 修复 | nano banana 2 api, gemini flash image | maintenance | 修正 gemini-flash-image 与 Nano Banana2 / Pro 的模型映射 | existing docs | docs.laozhang.ai | trust repair |
| P0 | Nano Banana API 路由总表 | nano banana api, nano banana api docs | docs hub | Nano Banana API：Standard、Nano Banana2、Pro 应该怎么选 | `/api-capabilities/nano-banana-api` | docs.laozhang.ai | canonical router |
| P1 | Nano Banana API Pricing | nano banana api pricing, nano banana cost per image | docs/pricing | Nano Banana API Pricing：官方价、老张价、4K 和 Batch/Flex 对照 | `/api-capabilities/nano-banana-pricing` | docs.laozhang.ai | conversion page |
| P1 | Nano Banana Free API Reality | nano banana free api, nano banana api key free | contract correction | Is Nano Banana API Free? App Quota, AI Studio, and Paid API Reality | `/en/posts/nano-banana-api-free` | aifreeapi.com | free-intent capture |
| P1 | Nano Banana2 vs Pro | nano banana 2 vs nano banana pro | comparison | Nano Banana2 vs Nano Banana Pro：默认用哪个，什么时候升级 | `/en/posts/nano-banana-2-vs-pro` | blog.laozhang.ai | GEO comparison |
| P2 | Nano Banana API errors | nano banana error 429, 503, no image | troubleshooting | Nano Banana API Not Working：429、503、No Image 和 Request Denied | `/en/posts/nano-banana-api-errors` | blog.laozhang.ai | support capture |
| P2 | Nano Banana Prompt Guide | nano banana prompt guide, tutorial | creator guide | Nano Banana Prompt Guide：图片生成、图改图和文字图模板 | `/blog/nano-banana-prompt-guide` | yingtu.ai | creator capture |
| P2 | Nano Banana vs ChatGPT/Midjourney | nano banana vs chatgpt, vs midjourney | comparison | Nano Banana vs ChatGPT Image vs Midjourney：按任务选模型 | `/blog/nano-banana-vs-chatgpt-midjourney` | yingtu.ai | upper-funnel |

### 7.2 P0 首篇执行方案

1. **页面唯一目标**：开发者 30 秒内选对 Nano Banana 模型、价格和端点，并进入 LaoZhang API 调用。
2. **推荐 H2 结构**：
   - `Which Nano Banana API should you use first?`
   - `Nano Banana model IDs: Standard, Banana2, Pro`
   - `Price table: LaoZhang vs Google official`
   - `Endpoint choices: OpenAI-compatible vs Google native`
   - `When Nano Banana2 is enough`
   - `When Nano Banana Pro is worth it`
   - `Code examples`
   - `FAQ`
3. **FAQ 建议**：
   - Is Nano Banana 2 the same as Gemini 3.1 Flash Image Preview?
   - Is Nano Banana Pro the same as Gemini 3 Pro Image Preview?
   - Is Nano Banana API free?
   - Which Nano Banana model supports 4K?
   - Should I use OpenAI-compatible mode or Google native format?
   - Why is `gemini-flash-image` not the best canonical slug now?
4. **是否需要对比表**：必须需要，这是 GEO 引用的核心资产。
5. **是否需要代码示例**：需要，给 OpenAI-compatible 和 Google native 两套最小调用。
6. **CTA 策略**：首屏模型表后放 Console/Try；价格表后放注册试用；正文不要过度广告化。
7. **页面偏向**：API reference + buyer route map。

### 7.3 文章间内链关系

- pillar page：`/api-capabilities/nano-banana-api`
- support pages：Standard 文生图/图改图、Banana2、Pro 文生图/图改图、Nano Banana pricing、free API reality、troubleshooting。
- 内链方向和锚文本：
  - docs hub -> `Nano Banana2 API`, `Nano Banana Pro API`, `Nano Banana Standard`
  - aifreeapi free article -> docs hub with anchor `Nano Banana API route map`
  - yingtu prompt/tutorial -> docs hub with anchor `Nano Banana API for developers`
  - blog comparison/troubleshooting -> docs model pages with anchors `gemini-3.1-flash-image-preview` and `gemini-3-pro-image-preview`

## 八、评分

| 维度 | 评分（1-5） | 原因 |
| --- | --- | --- |
| 可抢性 | 3 | 裸词难，API/pricing/free/model-route 长尾可抢。 |
| 点击可得性 | 4 | 用户会点击能直接回答模型 ID、价格、端点和免费边界的页面。 |
| 搜索量/趋势 | 4 | Trends 已回落但仍有 22/26 当前值，Suggest 密集。 |
| 商业承接性 | 5 | API key、pricing、cost、endpoint、国内中转强转化。 |
| GEO / AI 引用潜力 | 5 | 三模型映射和价格表非常适合 AI 摘要引用。 |
| 程序化扩展潜力 | 4 | 可扩展到 errors、rate limit、Python、vs、prompt、free。 |
| **总优先级** | **4.2** | 先修 docs，再补 route/pricing/free 长尾。 |

## 九、最终结论

- **结论**：做，但先做 docs 可信度修复和 API 路由 hub，不要先写泛词科普。
- **建议文章总数**：8 个以内，先 2 个 P0，再做 3 个 P1，剩下 P2 视资源更新。
- **P0 首发页**：`Nano Banana API：Standard、Nano Banana2、Pro 应该怎么选`
- **P1 第二批**：`Nano Banana API Pricing`、`Nano Banana Free API Reality`、`Nano Banana2 vs Pro`
- **P2 第三批**：API errors、Prompt guide、vs ChatGPT/Midjourney
- **当前最不值得投入的方向**：free unlimited、download、watermark removal、破解版、Nano Banana 3、video generator
- **时效性提醒**：发布前复核 Google pricing/deprecations、AI Studio paid key 状态、老张价格、docs sitemap/canonical。

## 十、站点协同策略

1. **各站点分工总览**：
   - `docs.laozhang.ai`：API route map、model ID、endpoint、pricing table、quickstart。
   - `laozhang.ai`：控制台、账户、充值、模型入口。
   - `blog.laozhang.ai`：API 教程、错误排查、模型对比、Batch/Flex 深度解释。
   - `aifreeapi.com`：free/cheap/quota/low-cost contract correction。
   - `yingtu.ai`：image generator、Prompt、教程、案例、创作者对比。
2. **跨站自相残杀风险提示**：
   - docs 和 blog 不要同时用同一个 first-screen 争 `nano banana api pricing`。
   - `free` 词由 aifreeapi 主承接，docs 只说明官方 API 免费层边界。
   - `tutorial/prompt` 由 yingtu 主承接，docs 不写创作长文。
   - `gemini-flash-image` 旧 URL/旧英文页必须重新审查，避免把 Banana2 和 Pro 混在一起。
3. **跨站内链机会**：
   - aifreeapi free/cheap 页链接到 docs route map。
   - yingtu prompt/tutorial 页链接到 docs API hub。
   - blog troubleshooting 链接到对应 model docs。
   - docs model pages 链接到 yingtu 在线试用，但保持 docs 的参考页语气。
4. **站点优先级建议**：
   - 第 1 优先级：docs 修复和 hub。
   - 第 2 优先级：docs pricing guide + aifreeapi free reality。
   - 第 3 优先级：blog 对比/错误长尾。
   - 第 4 优先级：yingtu Prompt/教程 refresh。
