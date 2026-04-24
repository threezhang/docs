# SEO / GEO 关键词研究报告：openai

> 数据局限性说明：本报告基于 Computer Use 实时浏览器 SERP 采集、Google Trends、Google Suggest API、官方 OpenAI 文档、自有资产扫描与社区/视频证据。无 Ahrefs/SEMrush 等专业工具支持，搜索量和关键词难度为基于 SERP、广告、Autocomplete、Trends 的间接推断。SERP 数据为搜索时快照，排名会动态变化。

- 关键词：`openai`
- 采集日期：2026-04-23
- 目标语言/地区：英文 / 美国优先，补充中文商业意图
- 主要采集方式：Computer Use + Google Suggest API + OpenAI 官方文档 + 本地仓库扫描 + indexed site search
- Computer Use SERP 证据：`SERP-main-openai`、`SERP-variant-openai-api`、`Trends-openai-comparison`
- Google/Trends 阻塞或降级：无 CAPTCHA；Trends 成功读取。浏览器为用户现有 Chrome profile，有扩展/账号上下文，已在证据中标注。

## 一、结论先行

- **这个词值不值得做**：`openai` 这个泛词本身不值得硬打。它是官方品牌/新闻/百科/登录/投资/招聘混合意图，非官方站点很难拿 Top 3。值得做的是它下面的 API、Key、价格、国内使用、中转、SDK、Responses、Codex、GPT Image 2、对比和替代方案集群。证据：`SERP-main-openai`、`Suggest-en-root`。
- **Google Trends 趋势**：美国过去 5 年平均热度中，`openai` 平均 2，明显低于 `chatgpt` 30、`gemini` 8、`claude` 3。`openai` 更适合作为开发者/官方来源修饰词，而不是主入口。证据：`Trends-openai-comparison`。
- **搜索量级别**：泛词大但不可抢；`openai api`、`openai api key`、`openai api pricing`、`openai api docs`、`openai api 国内使用` 属于中高意图商业词。证据：`SERP-variant-openai-api`、`Suggest-en-commercial`、`Suggest-zh-commercial`。
- **不建议直接打的原因**：首页被 `openai.com`、`platform.openai.com`、`developers.openai.com`、Wikipedia、ChatGPT、新闻和视频主导；Google 对泛词偏官方/实体/新闻。证据：`SERP-main-openai`。
- **最值得切入的次级角度**：`OpenAI API 国内使用：Key、价格、充值、中转与 SDK 接入路线`。这是中文 Suggest 里最贴近 LaoZhang API 业务的组合意图。证据：`Suggest-zh-commercial`、`Owned-docs`。
- **自有资产现状**：docs 已有 OpenAI SDK、OpenAI Responses、OpenAI 模型、GPT Image 2、Codex CLI 等页面；blog 网络已有大量 OpenAI/Codex/GPT Image/价格/免费/替代文章。问题是部分页面偏旧，尤其 `api-reference/openai.mdx` 仍以 GPT-4o/O1 为主，`openai-responses.mdx` 的模型合同也落后于官方 GPT-5.4/Responses 现状。证据：`Owned-docs`、`OpenAI-official-docs`。
- **推荐主力发布站点**：P0 应落在 `laozhang.ai` / `docs.laozhang.ai` 的产品与文档层；`blog.laozhang.ai` 做教程、对比、时效更新；`aifreeapi.com` 做免费/便宜/低成本；`yingtu.ai` 做图像测试和图像模型路线。证据：`Owned-docs`、`Owned-blog-laozhang`、`Owned-aifreeapi`、`Owned-yingtu`。
- **对业务网络的核心价值**：把高热品牌词转化成「国内开发者如何实际接入、付费、调用、选模型、控成本」的决策页，并为 API 网关、文档、低成本站和图像站建立清晰内链。
- **最终判断**：不做 `openai` 泛词页；做 OpenAI API 业务路由集群，P0 先刷新/新增一个国内接入路线页，并同步修正现有 OpenAI 模型与 Responses 文档。

## 二、关键词机会分层

### 1. 优先做

| 关键词 | 理由和证据 | 推荐站点 | 业务匹配 |
| --- | --- | --- | --- |
| `OpenAI API 国内使用` | 中文 Suggest 出现国内使用/访问/调用，强支付与接入意图。证据：`Suggest-zh-commercial` | `laozhang.ai` / `docs.laozhang.ai` | 直接转化 |
| `OpenAI API 国内 中转` | 与 LaoZhang API 网关定位高度一致。证据：`Suggest-zh-commercial`、`Owned-docs` | `laozhang.ai` / `docs.laozhang.ai` | 直接转化 |
| `OpenAI API key 国内` | Key 获取、购买、充值是明确交易前问题。证据：`Suggest-zh-commercial` | `laozhang.ai` / `docs.laozhang.ai` | 直接转化 |
| `openai api pricing` / `openai api价格表` | API SERP sitelink和 Suggest 都出现 pricing/costs/billing。证据：`SERP-variant-openai-api`、`Suggest-en-commercial`、`Suggest-zh-commercial` | `blog.laozhang.ai` + docs 内链 | 高商业 |
| `openai api key pricing` | key 与价格合并，适合解释余额、账单、调用费、官方价与网关价边界。证据：`Suggest-en-commercial` | `blog.laozhang.ai` | 高商业 |
| `openai api docs` / `openai api documentation` | Google 直接把官方 docs 放到 sitelink；LaoZhang 可做兼容接入版。证据：`SERP-variant-openai-api` | `docs.laozhang.ai` | 文档入口 |
| `OpenAI SDK base_url` | 现有 `openai-sdk.mdx` 已匹配“一行改 base_url”。证据：`Owned-docs` | `docs.laozhang.ai` | 直接接入 |
| `OpenAI Responses API` | 官方明确推荐新项目使用 Responses；现有页面需刷新。证据：`OpenAI-official-docs`、`Owned-docs` | `docs.laozhang.ai` | 开发者 |
| `gpt-5.4 api` | 官方当前模型合同；现有 OpenAI 模型页偏旧。证据：`OpenAI-official-docs`、`Owned-docs` | `docs.laozhang.ai` + `blog.laozhang.ai` | 模型入口 |
| `gpt-image-2 api` | 官方已列 `gpt-image-2` 和成本估算；自有 GPT Image 2 页面已有承接。证据：`OpenAI-official-docs`、`Owned-docs` | `docs.laozhang.ai` + `yingtu.ai` | 图像/API |
| `openai api status` / `openai api rate limit` | API Suggest 出现 status；错误/限速是高价值排障词。证据：`Suggest-en-commercial` | `blog.laozhang.ai` | 支持/留存 |
| `openai api alternative` / `openai alternative api` | Suggest 明确出现 alternative/free alternative；适合网关与低成本路由。证据：`Suggest-en-commercial` | `blog.laozhang.ai` / `aifreeapi.com` | 比较转化 |

### 2. 可做但不优先

| 关键词 | 理由和证据 | 推荐站点 |
| --- | --- | --- |
| `openai vs anthropic` | Suggest 强，但偏公司/竞争格局，需转成 API 路线比较。证据：`Suggest-en-commercial` | `blog.laozhang.ai` |
| `openai vs claude` | 可做模型/API选择页，避免公司八卦。证据：`Suggest-en-commercial` | `blog.laozhang.ai` |
| `openai vs gemini` | 适合成本、模型、国内接入、图像/多模态比较。证据：`Suggest-en-commercial` | `blog.laozhang.ai` |
| `openai pricing calculator` | 有商业意图，但需要维护成本计算器或表格，更新负担高。证据：`Suggest-en-commercial` | `blog.laozhang.ai` |
| `openai pricing tokens` | 适合解释 token billing，但需官方同日复核。证据：`Suggest-en-commercial` | `blog.laozhang.ai` |
| `openai api usage` | 开发者教程词，转化低于国内接入词。证据：`Suggest-en-commercial` | `docs.laozhang.ai` |
| `openai api dashboard` | 官方平台登录意图强，第三方可解释 LaoZhang 控制台映射。证据：`Suggest-en-commercial` | `docs.laozhang.ai` |
| `openai api console` | 与 dashboard 类似，适合 FAQ，不适合单独长文。证据：`Suggest-en-commercial` | `docs.laozhang.ai` |
| `openai api billing` | 商业意图强，但官方账单说明和网关账单需分开。证据：`Suggest-en-commercial` | `docs.laozhang.ai` |
| `openai codex` | Trends related rising；现有 Codex CLI 页面可扩展。证据：`Trends-openai-comparison`、`Owned-docs` | `docs.laozhang.ai` / `blog.laozhang.ai` |
| `openai workspace agents` | 新鲜度高，适合新闻解释，不一定直连 API 转化。证据：`SERP-main-openai`、`Suggest-en-root` | `blog.laozhang.ai` |
| `openai image 2.0` | SERP 和 Suggest 有热度，最好路由到图像站/图像 API，不做泛新闻。证据：`SERP-main-openai`、`Suggest-en-root` | `yingtu.ai` / `blog.laozhang.ai` |

### 3. 不建议做

| 关键词 | 不建议原因 | 证据 |
| --- | --- | --- |
| `openai` | 官方品牌/百科/新闻/登录意图；非官方站难进 Top 3。 | `SERP-main-openai` |
| `https://openai.com/` | 纯导航。 | `Suggest-en-root` |
| `openai stock` | 投资/股票意图，与 API 网关业务弱相关。 | `Suggest-en-root` |
| `openai careers` / `openai jobs` | 招聘意图，业务不匹配。 | `Suggest-en-root` |
| `openai ipo` / `openai valuation` | 投资新闻意图，需财经权威，不适合本站网络。 | `Suggest-en-root` |
| `openai login` | 官方登录意图，第三方页很难满足。 | `Suggest-en-root` |
| `openai news` | 新闻时效消耗高，转化低。 | `Suggest-en-root`、`SERP-main-openai` |
| `openai vs musk` / `openai vs anthropic revenue` | 公司/人物/收入八卦，偏新闻和商业数据库，不适合 API 承接。 | `Suggest-en-commercial` |

### 附录：关键词原始来源

- Autocomplete：`Suggest-en-root`、`Suggest-en-commercial`、`Suggest-zh-commercial`
- 标题反向提词：`SERP-main-openai`、`SERP-variant-openai-api`
- 竞品覆盖词：官方 OpenAI API Platform、OpenAI docs、platform login、YouTube 教程、Reddit 社区。证据：`SERP-variant-openai-api`
- 社区问题：OpenAI API 用途、OpenAI API 教程、ChatGPT Images/OpenAI Image 2 讨论。证据：`Community-and-video`
- 自有资产：`Owned-docs`、`Owned-blog-laozhang`、`Owned-blog-secondary`、`Owned-aifreeapi`、`Owned-yingtu`
- Google Trends：`Trends-openai-comparison`

## 三、SERP 结构判断

1. **搜索意图**：`openai` 是品牌导航 + 官方新闻 + 实体百科；`openai api` 是官方平台/文档/价格/key + 教程 + 社区用途。证据：`SERP-main-openai`、`SERP-variant-openai-api`。

2. **首页前 10 逐条分析**：

| 排名 | 标题 | URL | 域名类型 | 摘要关键信号 |
| --- | --- | --- | --- | --- |
| Ad | ChatGPT | `chatgpt.com` | 官方产品广告 | 消费者入口，广告信号强 |
| 1 | OpenAI / OpenAI | `openai.com` | 官方品牌 | sitelinks 覆盖 Careers、ChatGPT、Platform、API、About |
| Feature | Latest from openai.com | `openai.com` | 官方新闻 | Google 展示 13h-6d 内新鲜内容 |
| 2 | Wikipedia: OpenAI | `wikipedia.org` | 百科 | 实体解释 |
| 3 | ChatGPT | `chatgpt.com` | 官方产品 | 消费者产品入口 |
| Feature | Top stories / news | Washington Post, Sifted, Bloomberg 等 | 新闻 | 公司与产品新闻 |
| Feature | What people are saying | X / Reddit | 社区 | 最新发布讨论 |
| Feature | Videos | YouTube | 视频教程/解读 | 图像 2.0、OpenAI Image 2、访谈 |
| Related | People also search for | Google feature | 搜索扩展 | API、careers、stock、image、app、download |
| API variant #1 | API Platform | `openai.com/api/` | 官方产品 | API 入口 + docs/pricing/key sitelinks |
| API variant #2 | OpenAI Platform | `platform.openai.com` | 官方平台 | signup/login |
| API variant #3 | Reddit API use cases | `reddit.com` | 社区 | 用途和真实问题 |

3. **域名类型分布**：泛词首页官方/品牌/百科/新闻/社区/视频为主；API 变体首页官方文档和平台绝对主导，辅以视频教程和 Reddit 社区。证据：`SERP-main-openai`、`SERP-variant-openai-api`。
4. **SERP 主导意图**：泛词是官方导航；API 词是官方文档 + key/pricing/login + tutorial。
5. **标题模式总结**：官方结果短标题；非官方可见窗口多为 "how to", "pricing", "API key", "tutorial", "vs", "alternative"。
6. **Google 偏好的内容形态**：官方文档、平台页、帮助页、教程视频、社区问答、更新新闻。
7. **前 3 名赢在哪里**：OpenAI 拥有实体权威和官方入口；Wikipedia 满足实体百科；ChatGPT 满足消费者产品入口。
8. **4-10 位是否存在切入窗口**：泛词几乎没有；API 长尾存在，尤其中文国内接入、网关替代、价格解释、SDK 迁移、错误排障。
9. **SERP 特殊元素**：广告、Latest from official site、Top stories、social/community、videos、People also search for。
10. **广告信号**：ChatGPT 广告证明官方产品入口商业化强，但也说明泛词点击会被官方吸走。证据：`SERP-main-openai`。
11. **Google Trends 趋势**：`openai` 平均热度低于 `chatgpt`、`gemini`、`claude`；近期 `chatgpt` 仍强，`gemini` 和 `claude` 在 2026 年明显抬升。证据：`Trends-openai-comparison`。
12. **Google Trends 相关查询**：`openai codex`、`sora`、`anthropic`、`openai vs chatgpt`。证据：`Trends-openai-comparison`。
13. **风险判断**：所有模型、价格、免费层、速率、验证状态都必须发布当天复核官方文档。证据：`OpenAI-official-docs`。

## 四、内容缺口与切入机会

1. **当前内容同质化点**：大多数页面要么是官方 API 文档，要么是泛教程；很少把官方 API、国内支付/充值/访问、SDK 迁移、网关边界、成本核验和模型选择放在同一张决策表里。证据：`SERP-variant-openai-api`、`Suggest-zh-commercial`。
2. **确认的内容缺口**：中文 `OpenAI API 国内使用` 与 `OpenAI API 国内 中转` 有明确 Suggest，但 docs 当前没有一个首屏直答的 P0 路由页。证据：`Suggest-zh-commercial`、`Owned-docs`。
3. **社区真实痛点**：用户关心 API 能做什么、怎么第一次调用、token/rate limit、key、定价、免费/替代路线。证据：`Community-and-video`、`Suggest-en-commercial`。
4. **最容易赢的切角**：把 `openai api` 官方源头翻译成国内开发者可执行路线：官方 API、LaoZhang API 兼容网关、Azure/OpenRouter 等替代路线、价格/模型/SDK/限制边界。
5. **不建议正面硬打的方向**：`OpenAI 公司介绍`、`OpenAI 最新新闻`、`OpenAI 股票/IPO/招聘`。
6. **更适合打的次级意图**：API key、pricing、docs、SDK base_url、Responses migration、GPT-5.4 models、GPT Image 2 API、status/rate-limit、alternative/free/cheap。
7. **自有资产利用建议**：优先更新 `api-reference/openai.mdx`、`api-capabilities/openai-responses.mdx`、`api-capabilities/openai-sdk.mdx`，并让 `api-capabilities/gpt-image-2.mdx` 与 `yingtu.ai` 图像测试入口互链。证据：`Owned-docs`、`Owned-yingtu`。

## 五、业务承接判断

1. **这个词更适合拿什么**：不是拿品牌泛流量，而是拿 OpenAI API 接入、国内可用路线、成本解释和迁移教程的高意图流量。
2. **最适合承接到什么页面类型**：P0 为 docs/product route page；P1 为技术博客比较/价格/排障；P2 为低成本和图像模型专题。
3. **用户真实需求偏向**：英文用户偏官方 docs/key/pricing/tutorial；中文用户偏国内访问、充值、信用卡、中转、调用。证据：`Suggest-en-commercial`、`Suggest-zh-commercial`。
4. **对业务的真实价值**：能把搜索用户从“想找 OpenAI 官方入口”转成“我现在要在本地项目里接 API，怎么更稳、更容易付费、更少改代码”。
5. **在站内集群中的角色**：OpenAI API 是主干入口；GPT-5.4、Responses、GPT Image 2、Codex、pricing、free/cheap、comparison 是支持节点。

## 六、切入角度优先级

1. **第一推荐切入角度**：`OpenAI API 国内使用：Key、价格、充值、中转与 SDK 接入路线`。落在 `docs.laozhang.ai` 或 `laozhang.ai`，首屏直接回答“走官方、走老张 API、走 Azure/其他平台分别适合谁”。
2. **第二推荐切入角度**：`OpenAI API Pricing / 价格表：官方价格、LaoZhang 路由价格、token 账单和图像成本怎么分开看`。落在 `blog.laozhang.ai`，强制当天复核官方价格。
3. **第三推荐切入角度**：`OpenAI Responses API 迁移与 SDK 接入：从 Chat Completions 到 Responses，再到 LaoZhang base_url`。落在 `docs.laozhang.ai`。
4. **不建议优先做的角度**：`OpenAI 是什么`、`OpenAI 新闻汇总`、`OpenAI 股票/招聘/估值`。

## 七、内容规划

### 7.1 文章优先级列表

| 优先级 | 文章主题 | 目标关键词 | 页面类型 | 推荐 Title | 推荐 URL slug | 发布站点 | 页面角色 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| P0 | OpenAI API 国内接入路线 | `OpenAI API 国内使用`, `OpenAI API 国内 中转`, `OpenAI API key 国内` | 产品/文档路由页 | OpenAI API 国内使用：Key、价格、充值、中转与 SDK 接入路线 | `openai-api-china-access` | `docs.laozhang.ai` / `laozhang.ai` | 主承接页 |
| P0 | OpenAI 模型页刷新 | `gpt-5.4 api`, `openai api models` | 文档刷新 | OpenAI API 模型选择：GPT-5.4、GPT Image 2、Responses 与兼容调用 | `openai-models` | `docs.laozhang.ai` | 权威更新 |
| P1 | OpenAI API 价格解释 | `openai api pricing`, `openai api价格表`, `openai pricing tokens` | 技术博客 | OpenAI API Pricing 2026：模型价格、token 账单、图像成本和网关路线 | `openai-api-pricing-2026` | `blog.laozhang.ai` | 商业解释 |
| P1 | Responses API 迁移 | `OpenAI Responses API`, `Chat Completions to Responses` | 文档/教程 | OpenAI Responses API 接入：从 Chat Completions 迁移到 Responses | `openai-responses-api-migration` | `docs.laozhang.ai` | 开发者教程 |
| P1 | API Key 与充值 | `openai api key 国内`, `openai api 充值`, `openai api key pricing` | FAQ/教程 | OpenAI API Key 国内获取与充值：信用卡、余额、账单和替代路线 | `openai-api-key-china` | `blog.laozhang.ai` | 转化前问题 |
| P1 | API 替代路线 | `openai api alternative`, `openai alternative api`, `openai alternative free api` | 对比页 | OpenAI API Alternatives：官方、LaoZhang、Azure、OpenRouter 应该怎么选 | `openai-api-alternatives` | `blog.laozhang.ai` / `aifreeapi.com` | 选择页 |
| P2 | 免费/低成本入口 | `openai api key free`, `openai api free tier`, `openai alternative free` | 低成本指南 | OpenAI API Free Tier Reality：免费层、低成本替代和误导性免费 API | `openai-api-free-tier` | `aifreeapi.com` | 免费流量承接 |
| P2 | 图像 API 路线 | `gpt-image-2 api`, `openai image 2.0`, `openai image api` | 图像专题 | GPT Image 2 API：OpenAI Image API、Responses 工具与 YingTu 测试路线 | `gpt-image-2-api-route` | `yingtu.ai` / `docs.laozhang.ai` | 图像转化 |
| P2 | Codex 路线 | `openai codex`, `openai codex cli`, `codex api key` | 开发者教程 | OpenAI Codex CLI 配置：官方 API Key、订阅和 LaoZhang API 路线 | `openai-codex-cli-api-route` | `docs.laozhang.ai` / `blog.laozhang.ai` | 编程入口 |
| P2 | 状态/限速排障 | `openai api status`, `openai api rate limit`, `quota exceeded` | 排障页 | OpenAI API Status 与 Rate Limit 排查：官方状态、账户限制和网关重试 | `openai-api-status-rate-limit` | `blog.laozhang.ai` | 支持留存 |

### 7.2 P0 首篇执行方案

1. **页面唯一目标**：让国内开发者在 3 分钟内判断自己应该走官方 OpenAI、LaoZhang 兼容网关、Azure，还是低成本/图像/备用路线。
2. **推荐 H2 结构**：
   - `## 快速结论：你应该走哪条 OpenAI API 路线`
   - `## 三条路线对比：官方 API、LaoZhang API、Azure/其他平台`
   - `## 国内使用 OpenAI API 的关键问题：Key、充值、信用卡、访问`
   - `## SDK 接入：只改 base_url 的 Python / Node.js 示例`
   - `## 价格和账单边界：官方价格、网关价格、图像成本要分开看`
   - `## Responses API 与 Chat Completions 应该怎么选`
   - `## GPT-5.4、GPT Image 2、Codex 的当前合同边界`
   - `## 常见错误：401、429、quota exceeded、模型不可用`
   - `## 下一步：注册、测试、查看模型与价格`
3. **FAQ 建议**：`国内能直接用 OpenAI API 吗？`、`OpenAI API key 国内怎么买？`、`LaoZhang API 是不是 OpenAI 官方？`、`改 base_url 会不会影响 SDK？`、`GPT Image 2 官方价格和 LaoZhang 价格怎么区分？`
4. **是否需要对比表**：需要。第一屏必须有路线表。
5. **是否需要代码示例**：需要。Python、Node.js、curl 各一组，强调 base_url 和 key 的替换。
6. **CTA 策略**：首屏轻 CTA 到注册/测试；代码后 CTA 到控制台；图像段 CTA 到 `yingtu.ai`；免费/低成本 FAQ CTA 到 `aifreeapi.com`。
7. **页面偏向**：产品文档，而不是博客观点文。

### 7.3 文章间内链关系

- pillar page：`OpenAI API 国内使用：Key、价格、充值、中转与 SDK 接入路线`
- support pages：OpenAI SDK、OpenAI Responses、OpenAI 模型、GPT Image 2 API、Codex CLI、Pricing、Free tier、Alternatives、Status/Rate limit。
- 内链方向和锚文本：
  - P0 -> `OpenAI 官方库使用`：锚文本 `OpenAI SDK base_url 配置`
  - P0 -> `OpenAI Responses API 支持`：锚文本 `Responses API 接入`
  - P0 -> `GPT Image 2 API`：锚文本 `GPT Image 2 图像 API`
  - P0 -> `yingtu.ai`：锚文本 `先在线测试图像生成效果`
  - P0 -> `aifreeapi.com`：锚文本 `免费层和低成本替代路线`
  - Blog pricing -> P0：锚文本 `国内 OpenAI API 接入路线`

## 八、评分

| 维度 | 评分（1-5） | 原因 |
| --- | ---: | --- |
| 可抢性 | 3 | 泛词不可抢，但 API/国内/价格/SDK 长尾可抢。 |
| 点击可得性 | 4 | 价格、Key、国内使用、教程词点击意图强。 |
| 搜索量/趋势 | 4 | `openai` 本身趋势不如 ChatGPT，但 API/Key/Pricing Suggest 密集。 |
| 商业承接性 | 5 | 与 LaoZhang API 网关、充值、SDK、模型调用直接相关。 |
| GEO / AI 引用潜力 | 5 | 路线表、价格边界、官方/网关区分、FAQ 都适合被 AI 摘引用。 |
| 程序化扩展潜力 | 4 | 可扩展到模型、错误码、价格、语言、地区、SDK。 |
| **总优先级** | **P0 集群 / 非泛词 P0** | 不做 `openai` 泛词；做 OpenAI API 路由集群。 |

## 九、最终结论

- **结论**：`openai` 不应作为独立泛词目标；OpenAI API 商业长尾应作为 P0 集群。
- **建议文章总数**：先做 1 个 P0 路由页 + 2 个文档刷新 + 4-6 篇支持页。
- **P0 首发页**：`OpenAI API 国内使用：Key、价格、充值、中转与 SDK 接入路线`
- **P1 第二批**：OpenAI API Pricing 2026、Responses API 迁移、OpenAI API Key 国内获取与充值、OpenAI API Alternatives。
- **P2 第三批**：Free tier、GPT Image 2 route、Codex CLI route、Status/Rate limit。
- **当前最不值得投入的方向**：OpenAI 公司介绍、OpenAI 股票/IPO/估值、OpenAI 招聘、泛新闻汇总。
- **时效性提醒**：发布前必须重新核验 OpenAI 官方模型页、pricing、Responses guide、GPT Image 2 model page、image cost calculator。证据：`OpenAI-official-docs`。

## 十、站点协同策略

1. **各站点分工总览**：

| 站点 | 应负责的 OpenAI 机会 | 不应负责 |
| --- | --- | --- |
| `laozhang.ai` / `docs.laozhang.ai` | 国内 API 接入、SDK、Responses、模型列表、Key/充值/控制台、GPT Image 2 API 文档 | 泛新闻、公司八卦 |
| `blog.laozhang.ai` | 定价解释、模型比较、OpenAI vs Anthropic/Gemini/Claude、Codex、错误排障、最新变更解读 | 与 docs 重复的纯接口参数页 |
| `aifreeapi.com` | free tier、cheap API、low-cost alternative、最低成本路线 | 官方权威文档、企业 API 主入口 |
| `yingtu.ai` | GPT Image 2、OpenAI Image、ChatGPT Images、图像测试、prompt 和图像模型对比 | 泛 OpenAI API 接入 |

2. **跨站自相残杀风险提示**：不要让 `blog.laozhang.ai`、`docs.laozhang.ai`、`aifreeapi.com` 同时争 `openai api pricing`。建议 docs 做接入与合同，blog 做解释与比较，aifreeapi 做免费/低成本。
3. **跨站内链机会**：docs P0 页面向 blog pricing/alternatives、aifreeapi free tier、yingtu image testing 输出；blog 和 aifreeapi 回链 docs P0 页面作为权威接入路线。
4. **站点优先级建议**：先 docs/product，后 blog，最后 aifreeapi/yingtu 专题扩展。
