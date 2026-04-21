# SEO / GEO 关键词研究报告：codex

> 数据局限性说明：本报告基于 Computer Use 实时浏览器 SERP 采集、补充搜索、Google Suggest API、自有资产扫描与社区/论坛证据。无 Ahrefs/SEMrush 等专业工具支持，搜索量和关键词难度为基于 SERP、广告、Autocomplete、Trends 的间接推断。SERP 数据为搜索时快照，排名会动态变化。

- 关键词：`codex`
- 采集日期：2026-04-21
- 目标语言/地区：英文 Google US + 中文查询变体
- 主要采集方式：Computer Use Google SERP、Google Trends、Google Suggest API、官方来源复核、站内资产扫描
- Computer Use SERP 证据：已完成，截图见 `screenshots/`
- Google/Trends 阻塞或降级：无主要阻塞；Google Trends Worldwide / US 均完成截图

## 一、结论先行

- **这个词值不值得做**：值得做，但不建议打裸词 `codex`。裸词被 OpenAI 官方页、GitHub、ChatGPT、百科/食品法典等混合意图占据，LaoZhang 更应该打 `Codex API / pricing / usage limits / API key / CLI config / domestic setup / vs Claude Code`。
- **Google Trends 趋势**：强上升。Worldwide 从 2025-04 的低位约 13，升到 2026-03-29 的 100，2026-04-19 仍在 74；US 在 2026-02-08 达 100，2026-04-19 仍在 70。[Trends-worldwide-12m][Trends-us-12m]
- **搜索量级别**：中高。主词有官方强控，但 Suggest 产生 483 个唯一联想词、261 个高意图词，且 SERP 出现广告、视频、Reddit、PAA、社区讨论和多语言教程页。[Suggest-codex][SERP-variant-pricing]
- **不建议直接打的原因**：裸词混合了 OpenAI 产品、历史书籍概念、食品法典、宗教手稿和第三方产品；Google 对裸词首屏优先给 OpenAI 官方生态与定义类结果。[SERP-main-codex]
- **最值得切入的次级角度**：`Codex pricing and limits`、`Codex API key vs ChatGPT subscription`、`Codex CLI config.toml / AGENTS.md`、`Codex 国内使用/价格/额度`、`Codex vs Claude Code`。[SERP-variant-api][SERP-zh-pricing][Suggest-codex]
- **自有资产现状**：`docs.laozhang.ai` 已有中英文 `OpenAI Codex CLI 配置教程`；`blog.laozhang.ai` 已有 Codex March 2026、usage limits、computer use、Claude Code vs Codex 等文章。现状是有基础页，但 docs 页过窄且偏旧。[Owned-docs][Owned-blog-laozhang]
- **推荐主力发布站点**：P0 放在 `docs.laozhang.ai`，先刷新/扩展现有 Codex CLI 页面为路线图型页面；`blog.laozhang.ai` 承接比较、变化解读、Computer Use 和迁移选择；`aifreeapi.com` 承接 free/cheap/API-key 低价意图；`yingtu.ai` 暂不优先。[Owned-docs][Owned-blog-laozhang][Owned-yingtu]
- **对业务网络的核心价值**：这是开发者入口词，能承接 API key、模型选择、CLI 配置、计费/额度、替代路线和 Claude Code 迁移流量，对 LaoZhang API 的开发者获客价值高。
- **最终判断**：做，但要以“路线/合同纠偏”为主，不做泛百科。P0 应该是 docs 的 Codex 路线图/配置刷新页，P1 扩展价格限制、国内使用和 Claude Code 对比。

## 二、关键词机会分层

### 1. 优先做

| 关键词 | 理由和证据 | 推荐站点 | 业务匹配 |
| --- | --- | --- | --- |
| codex pricing | SERP 顶部是 OpenAI Pricing，PAA/Reddit/Related 都在问价格、Plus/Pro、limits、计划变化。[SERP-variant-pricing] | docs.laozhang.ai | 高：价格/额度直接影响 API/订阅选择 |
| codex usage limits | Suggest 出现 usage dashboard、rate limit、quota、Plus limits；官方页也要求用户看 dashboard 和 `/status`。[Suggest-codex][Official-openai] | docs.laozhang.ai + blog.laozhang.ai | 高：合同纠偏和排障价值强 |
| codex api | SERP 顶部是 OpenAI Developers；Related 出现 API key、API pricing、API key free。[SERP-variant-api] | docs.laozhang.ai | 高：能承接 LaoZhang API route |
| codex api key | Suggest 密集出现 API key、free、login、pricing、vs subscription。[Suggest-codex] | docs.laozhang.ai | 高：配置和付费路线核心词 |
| codex api key vs subscription | 真实用户想知道 ChatGPT 登录、API key、Business credits 的区别。[Suggest-codex][Official-openai] | docs.laozhang.ai | 高：决策型关键词 |
| codex cli install | Tutorial SERP 和 Suggest 都出现 CLI install/npm/GitHub；现有 docs 页已有基础但可刷新。[SERP-variant-tutorial][Owned-docs] | docs.laozhang.ai | 高：已有资产可快速提升 |
| codex config.toml | Trends related query 和 Suggest 都出现；社区也围绕配置、MCP、approval、skills 发问。[Trends-worldwide-12m][Suggest-codex] | docs.laozhang.ai | 高：技术深度和 GEO 引用价值强 |
| codex agents.md | US Trends rising query 出现 `agents.md codex`；Suggest 有 example/template/location/skills。[Trends-us-12m][Suggest-codex] | docs.laozhang.ai + blog.laozhang.ai | 中高：适合高质量开发者指南 |
| codex 国内使用 | 中文 SERP 明显偏安装、支付、国内配置、API route。[SERP-zh-tutorial][SERP-zh-pricing] | docs.laozhang.ai | 高：中文商业承接强 |
| codex 价格 | 中文 SERP/PAA/Related 都在拆订阅、额度、免费、Pro/Plus。[SERP-zh-pricing] | docs.laozhang.ai | 高：中文转化强 |
| codex 免费额度 | 中文 Related 出现免费额度；英文 Suggest 有 free credits/free limits/free tier。[SERP-zh-pricing][Suggest-codex] | aifreeapi.com + docs.laozhang.ai | 高：低价/试用流量 |
| codex vs claude code | VS SERP 有 AI Overview、Reddit、Builder.io、DataCamp；自有博客已有资产可更新。[SERP-variant-vs][Owned-blog-laozhang] | blog.laozhang.ai | 高：迁移/替代决策流量 |
| codex app vs cli | 官方和 SERP 都显示 App/CLI/IDE/Cloud 多入口；搜索者需要路线选择。[Official-openai][SERP-variant-tutorial] | blog.laozhang.ai + docs.laozhang.ai | 中高：避免泛教程同质化 |
| codex app download | Quickstart 明确 App 支持 macOS/Windows，SERP/Suggest 出现 download/app/windows/mac/linux。[Official-openai][Suggest-codex] | docs.laozhang.ai | 中高：安装入口词 |
| codex rate limit check | Suggest 出现 rate limit check/reset/remaining/dashboard；官方页面提 `/status` 和 usage dashboard。[Suggest-codex][Official-openai] | docs.laozhang.ai | 高：排障和留存价值 |

### 2. 可做但不优先

| 关键词 | 理由和证据 | 推荐站点 |
| --- | --- | --- |
| openai codex | 官方强控，适合作为页内实体词，不适合单独硬打。[SERP-main-codex] | docs.laozhang.ai |
| chatgpt codex | 与订阅/登录/价格相关，但官方和 ChatGPT 自身强势。[SERP-main-codex][Suggest-codex] | docs.laozhang.ai |
| codex login | Suggest 有 login CLI/device auth/API key/ChatGPT，适合 FAQ 或排障页。[Suggest-codex] | docs.laozhang.ai |
| codex vscode | SERP Related 和 Suggest 都出现，但 VS Code/IDE extension 竞争会比较分散。[SERP-main-codex][Suggest-codex] | docs.laozhang.ai |
| codex ide | Related 出现；适合作为 route-map 子章节。[SERP-variant-api] | docs.laozhang.ai |
| codex examples | Tutorial Related 出现，但泛例子页竞争力不如配置/价格页。[SERP-variant-tutorial] | blog.laozhang.ai |
| codex best practices | 官方 best practices 强势，适合作为支持页。[Official-openai] | blog.laozhang.ai |
| codex subagents | Suggest 出现 how to use subagents；技术深但搜索量较窄。[Suggest-codex] | blog.laozhang.ai |
| codex skills | Suggest/官方 App 页面都提到 Skills；适合和 AGENTS.md/config 合并。[Official-openai][Suggest-codex] | blog.laozhang.ai |
| codex mcp | Suggest 出现 CLI MCP、config.toml MCP；适合技术支持页。[Suggest-codex] | docs.laozhang.ai |
| codex vs cursor | Related/社区比较方向，但业务承接弱于 Claude Code 对比。[SERP-variant-vs] | blog.laozhang.ai |
| codex vs copilot | 可做比较页，但 SERP 当前没有 `Claude Code` 那么强的显性需求。[SERP-variant-vs] | blog.laozhang.ai |
| gpt-5.4 codex | 自有博客已有 March 2026/product-shift 覆盖；适合作为更新页而非新 docs P0。[Owned-blog-laozhang] | blog.laozhang.ai |
| gpt-5.3 codex pricing | 模型层词，容易过时，适合作为价格页小节。[Official-openai] | docs.laozhang.ai |
| codex desktop app | 与 app download / app vs CLI 合并处理更好。[SERP-variant-tutorial][Suggest-codex] | blog.laozhang.ai |

### 3. 不建议做

| 关键词 | 不建议原因 | 证据 |
| --- | --- | --- |
| codex meaning | PAA 首个问题就是术语含义，会引向书籍/手稿/定义，不是 LaoZhang 业务。[SERP-main-codex] |
| Codex Alimentarius | FAO 食品法典结果在裸词 SERP 出现，完全错业务。[SERP-main-codex] |
| Codex Gigas | PAA 出现 Devil's Bible，宗教/历史意图，不承接 API。[SERP-main-codex] |
| Codex Sinaiticus | 古籍/宗教文本意图，非 AI 开发者流量。[SERP-main-codex] |
| codex book | 泛书籍/手稿意图，转化弱。[SERP-main-codex] |
| codex.io | SERP API 变体中出现第三方 blockchain/token/prediction market 结果，容易错配。[SERP-variant-api] |
| codex python | 语义太宽，可能指代码/库/教程；不如打 `Codex CLI Python project setup`。[SERP-variant-vs] |
| codex vs gpt | 比较对象不清，容易混淆产品层和模型层。[SERP-variant-vs] |

### 附录：关键词原始来源

- Autocomplete：`raw/google-suggest-codex.json`，60 个根查询、483 个唯一联想词、261 个高意图词。[Suggest-codex]
- 标题反向提词：OpenAI Pricing、Quickstart、Codex app、GitHub repo、Reddit pricing/limits、Builder/DataCamp comparison。[SERP-variant-pricing][SERP-variant-tutorial][SERP-variant-vs]
- 竞品覆盖词：Claude Code、Cursor、VS Code/IDE、Copilot、OpenRouter、OpenClaw。[SERP-variant-vs][SERP-zh-pricing]
- 社区问题：API key vs subscription、pricing changes、usage dashboard、config.toml、AGENTS.md、subagents、limits。[Community-competitor]
- 自有资产：docs Codex CLI setup；blog Codex March 2026、usage limits、computer use、Claude Code vs Codex。[Owned-docs][Owned-blog-laozhang]
- Google Trends：Worldwide/US 12-month interest both spiked in Feb-Mar 2026 and remain elevated in Apr 2026.[Trends-worldwide-12m][Trends-us-12m]

## 三、SERP 结构判断

1. **搜索意图**：裸词是 mixed intent；商业可做的是 OpenAI Codex 产品路线、使用/配置、价格/额度、API key、对比迁移、中文国内使用。
2. **首页前 10 逐条分析**：

| 排名 | 标题 | URL | 域名类型 | 摘要关键信号 |
| --- | --- | --- | --- | --- |
| 1 | Codex \| AI Coding Partner from OpenAI | `openai.com/codex/` | 官方产品页 | 官方实体强控，sitelinks 指向 CLI/App |
| 2 | Codex CLI | `developers.openai.com/codex/cli` | 官方文档 | CLI 是首屏官方子意图 |
| 3 | Codex app | `developers.openai.com/codex/app` | 官方文档 | App 是新主入口 |
| 4 | Latest from openai.com | OpenAI docs/blog cluster | 官方新鲜内容 | 多个 4 天/小时级新文，说明主题变化快 |
| 5 | openai/codex | `github.com/openai/codex` | 官方开源仓库 | CLI install/config/source truth |
| 6 | ChatGPT Codex | `chatgpt.com/codex` | 官方应用入口 | ChatGPT account route |
| 7 | Codex Alimentarius | FAO | 非 AI 官方 | 裸词歧义 |
| 8 | Codex | Wikipedia | 百科 | 定义型意图 |
| 9 | What people are saying | Reddit/X/LinkedIn/YouTube | 社区/UGC | 新鲜体验、争议和比较 |
| 10 | Videos | YouTube/OpenAI/creator | 视频 | Tutorial/how-to demand |

3. **域名类型分布**：官方 OpenAI/ChatGPT/GitHub 占主导；社区和视频补充；裸词夹杂百科/非 AI 官方机构。[SERP-main-codex]
4. **SERP 主导意图**：官方产品导航 + 快速理解 + app/CLI/docs 路线。
5. **标题模式总结**：`Codex Pricing`、`Quickstart - Codex`、`Codex vs Claude Code`、`OpenAI Codex Tutorial`、`Codex 国内使用教程`、`Codex 价格详解`。
6. **Google 偏好的内容形态**：官方 docs、价格页、quickstart、视频教程、Reddit 讨论、对比页、中文实操安装/支付页。
7. **前 3 名赢在哪里**：官方权威、产品实体、结构化 sitelinks、更新时间新、覆盖多入口。
8. **4-10 位是否存在切入窗口**：存在。窗口不在裸词，而在 pricing/API key/config/domestic setup/limits/comparison 这些非官方解释需求。
9. **SERP 特殊元素**：PAA、视频、What people are saying、Related searches、AI Overview、广告。[SERP-main-codex][SERP-variant-vs]
10. **广告信号**：`codex API` SERP 出现 Anthropic Claude Code Sponsored，说明 coding-agent 商业竞争已经进入投放层。[SERP-variant-api]
11. **Google Trends 趋势**：强上升且 2026 年仍高位，支持尽快更新现有资产。[Trends-worldwide-12m][Trends-us-12m]
12. **Google Trends 相关查询**：`codex config.toml`、`openai codex app`、`agents.md codex`、`codex cli github`、`npm`，说明配置/CLI/app 是真实增量意图。[Trends-worldwide-12m][Trends-us-12m]
13. **风险判断**：价格、额度、模型名、计划可用性更新快；OpenAI 页面和 AI Overview 可能几天内变化，发布当天必须复核。[Official-openai]

## 四、内容缺口与切入机会

1. **当前内容同质化点**：大量页面停留在安装命令、什么是 Codex、简单 Claude Code 对比、视频教程；价格/额度经常给单一数字，忽略 ChatGPT plan、API key、Business credits、cloud features 的差异。
2. **确认的内容缺口**：
   - API key vs ChatGPT subscription 的路线表。
   - Codex pricing / usage limits / credits / `/status` / dashboard 的合同纠偏。
   - `config.toml`、MCP、AGENTS.md、Skills、subagents 的现代配置指南。
   - App / IDE / CLI / Cloud 入口选择。
   - 中文国内使用、支付、额度、API route 的安全边界。
3. **社区真实痛点**：价格变动、Pro/Plus 限制、API key 是否能替代订阅、CLI 登录问题、config 文件在哪里、AGENTS.md 是否生效、Claude Code 迁移是否值得。[Community-competitor]
4. **最容易赢的切角**：`Codex API Key vs Subscription: Pricing, Limits, CLI Config, and LaoZhang Route` 这类决策型页面。
5. **不建议正面硬打的方向**：裸词 `codex`、百科定义、历史/食品法典、单纯 benchmark winner、过时的 “Codex only cloud” 对比。
6. **更适合打的次级意图**：`codex pricing and limits`、`codex api key`、`codex config.toml`、`codex agents.md`、`codex 国内使用`、`codex vs claude code`。
7. **自有资产利用建议**：以 `scenarios/programming/codex-cli.mdx` 为 docs P0，扩大为 Codex route map；blog 文章互链到 docs P0，避免重复写安装命令。[Owned-docs][Owned-blog-laozhang]

## 五、业务承接判断

1. **这个词更适合拿什么**：开发者 API key、CLI 配置、模型/计费咨询、替代方案、国内稳定访问、Claude Code 迁移用户。
2. **最适合承接到什么页面类型**：docs 决策页 + 配置指南，不是纯 blog 新闻页。
3. **用户真实需求偏向**：不是只想知道 Codex 是什么，而是“我该用 App、CLI、IDE、Cloud 还是 API key？费用/额度怎么计算？国内怎么稳定跑？”
4. **对业务的真实价值**：高。它连接 API 消费、订阅替代、模型路由、CLI 开发者流量和价格敏感用户。
5. **在站内集群中的角色**：docs P0 作为 pillar route map；blog 做对比/变化/风险解释；aifreeapi 做低价/免费/替代路线；yingtu 暂不参与。

## 六、切入角度优先级

1. **第一推荐切入角度**：刷新 docs Codex CLI 页面为 `Codex API/CLI/App/Pricing Route Map`，先回答 App/IDE/CLI/Cloud/API key 怎么选，再给 LaoZhang API 配置。
2. **第二推荐切入角度**：`Codex Pricing and Usage Limits`，拆 Free/Go/Plus/Pro/Business/API Key、credits、dashboard、`/status` 和模型可用性。
3. **第三推荐切入角度**：`Codex config.toml and AGENTS.md`，做现代配置、MCP、skills、subagents、approval/security 的技术页。
4. **不建议优先做的角度**：`What is Codex`、`Codex meaning`、泛视频教程、旧式 Claude Code benchmark 胜负表。

## 七、内容规划

### 7.1 文章优先级列表

| 优先级 | 文章主题 | 目标关键词 | 页面类型 | 推荐 Title | 推荐 URL slug | 发布站点 | 页面角色 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| P0 | Codex 路线图与 LaoZhang API 配置 | codex api, codex cli, codex api key | docs pillar refresh | OpenAI Codex API、CLI、App 怎么选：LaoZhang API 配置与价格路线图 | `/scenarios/programming/codex-cli` | docs.laozhang.ai | 刷新现有中英页面 |
| P0 | English Codex route map refresh | codex api key, codex cli install, codex pricing | docs pillar refresh | OpenAI Codex API, CLI, App, and Pricing Route Map for Developers | `/en/scenarios/programming/codex-cli` | docs.laozhang.ai | 英文同步 |
| P1 | Codex 价格和额度纠偏 | codex pricing, codex usage limits | docs guide | Codex Pricing and Usage Limits: Plus, Pro, Business, API Key, Credits, and `/status` | `/en/scenarios/programming/codex-pricing-limits` | docs.laozhang.ai | 商业承接页 |
| P1 | Codex 国内使用 | codex 国内使用, codex 价格, codex 免费额度 | docs guide | Codex 国内使用指南：CLI、API Key、订阅、价格和额度怎么选 | `/scenarios/programming/codex-china-guide` | docs.laozhang.ai | 中文转化页 |
| P1 | Codex vs Claude Code | codex vs claude code | blog decision page | Codex vs Claude Code: Which Coding Agent Should Developers Use in 2026? | `/en/posts/codex-vs-claude-code` refresh | blog.laozhang.ai | 对比/迁移 |
| P2 | Codex app vs CLI vs IDE vs Cloud | codex app vs cli, codex app download | blog/docs support | Codex App vs CLI vs IDE vs Cloud: Choose the Right Route First | `/en/posts/codex-app-vs-cli` | blog.laozhang.ai | 入口决策 |
| P2 | config.toml 与 AGENTS.md | codex config.toml, codex agents.md | docs technical guide | Codex config.toml 和 AGENTS.md 配置指南：MCP、Skills、Subagents 与审批策略 | `/scenarios/programming/codex-config-agents-md` | docs.laozhang.ai | 技术权威 |
| P2 | 免费/低价路线 | codex free, codex api key free, codex cheap alternative | free/route guide | Is Codex Free? Free Limits, API Key Costs, Credits, and Cheaper Routes | `/codex-free-api-key` | aifreeapi.com | 低价流量 |

### 7.2 P0 首篇执行方案

1. **页面唯一目标**：让读者在首屏决定自己该走 `Codex App / IDE extension / CLI / Cloud / API key / LaoZhang API` 哪条路线，并知道价格/额度在哪里查。
2. **推荐 H2 结构**：
   - `## 先选路线：App、IDE、CLI、Cloud、API Key 有什么区别`
   - `## Codex CLI 使用 LaoZhang API 的配置步骤`
   - `## API Key 与 ChatGPT 登录：功能、价格和限制差异`
   - `## Codex Pricing 和 Usage Limits 怎么看`
   - `## config.toml、AGENTS.md、MCP 和 Skills 基础配置`
   - `## 常见错误：登录、模型不可用、额度不足、API Key 无效`
   - `## Codex vs Claude Code / Cursor：什么时候换工具`
   - `## FAQ`
3. **FAQ 建议**：
   - Codex 是 ChatGPT 订阅内置的吗？
   - Codex 可以只用 API Key 吗？
   - Codex API Key 和 ChatGPT 登录有什么区别？
   - Codex 免费版能用吗？
   - Codex CLI 怎么查看剩余额度？
   - Codex 的 `config.toml` 在哪里？
   - Codex 会读取 `AGENTS.md` 吗？
   - 国内使用 Codex 应该选什么路线？
4. **是否需要对比表**：需要。至少两张：路线选择表、价格/额度合同表。
5. **是否需要代码示例**：需要。保留 npm/brew 安装、环境变量/API base URL、`config.toml` 示例，但发布前必须按当前 Codex CLI 官方配置复核。
6. **CTA 策略**：docs 内 CTA 应该是“获取 LaoZhang API Key / 查看模型和价格 / 检查余额”，不要用泛促销口吻。
7. **页面偏向**：技术决策页 + 配置页，不是营销页。

### 7.3 文章间内链关系

- pillar page：`/scenarios/programming/codex-cli` 与 `/en/scenarios/programming/codex-cli`
- support pages：
  - `Codex pricing and usage limits`
  - `Codex 国内使用指南`
  - `Codex config.toml and AGENTS.md`
  - `Codex App vs CLI`
  - `Codex vs Claude Code`
  - `Codex Computer Use`
- 内链方向和锚文本：
  - blog `Codex Computer Use` -> docs `Codex route map`
  - blog `Codex vs Claude Code` -> docs `Codex API key vs subscription`
  - docs pricing page -> docs CLI setup + API console
  - aifreeapi free/cheap page -> docs pricing/limits page

## 八、评分

| 维度 | 评分（1-5） | 原因 |
| --- | --- | --- |
| 可抢性 | 3 | 裸词不可抢，长尾配置/价格/国内路线可抢 |
| 点击可得性 | 4 | PAA、Reddit、视频、Related 和教程词说明用户会点非官方解释页 |
| 搜索量/趋势 | 4 | Trends 在 2026 Q1 明显上涨，Suggest 高意图词密集 |
| 商业承接性 | 5 | API key、价格、额度、国内使用、替代路线都能承接 |
| GEO / AI 引用潜力 | 4 | route-map、合同纠偏、配置表容易被 AI 摘要引用 |
| 程序化扩展潜力 | 4 | 可扩展到 App/CLI/IDE/Cloud/API-key、config、limits、models、地区 |
| **总优先级** | **4** | 不做裸词，但长尾集群值得立即刷新 |

## 九、最终结论

- **结论**：`codex` 不是一个适合直接新建泛词页的关键词，但它是值得立刻运营的开发者意图集群。主攻方向应是 docs route map 和 pricing/limits/config contract correction。
- **建议文章总数**：先做 6-8 个页面/刷新项，不要一次性铺太多泛教程。
- **P0 首发页**：刷新 `docs.laozhang.ai/scenarios/programming/codex-cli` 和英文对应页，把 CLI 页升级成 Codex App/CLI/IDE/Cloud/API Key/Pricing route map。
- **P1 第二批**：Codex pricing/usage limits、Codex 国内使用、Codex vs Claude Code refresh。
- **P2 第三批**：Codex config.toml + AGENTS.md、Codex app vs CLI、Codex free/cheap/API-key routes。
- **当前最不值得投入的方向**：`codex meaning`、Codex Alimentarius、历史手稿、泛百科定义、过时模型 benchmark。
- **时效性提醒**：价格、额度、模型和 plan 可用性变化极快。任何页面上线前必须当天复核 OpenAI Pricing、Quickstart、Codex docs、GitHub repo 和 LaoZhang 可用模型。

## 十、站点协同策略

1. **各站点分工总览**：
   - `docs.laozhang.ai`：权威配置、API key、pricing/limits、国内使用、`config.toml`、`AGENTS.md`。
   - `blog.laozhang.ai`：产品变化、Codex vs Claude Code、Codex Computer Use、App vs CLI、迁移决策。
   - `aifreeapi.com`：Codex free、free API key、cheap route、limits reality、替代方案。
   - `yingtu.ai`：暂不参与，除非后续出现与图像/视频生产工作流直接相关的 Codex 搜索意图。
2. **跨站自相残杀风险提示**：
   - docs 和 blog 不要同时写 `Codex CLI setup`。docs 做步骤和配置，blog 做为什么选这条路线。
   - pricing 页面要避免 docs/aifreeapi 互相抢；docs 讲合同和配置，aifreeapi 讲免费/低价路线。
   - Claude Code 对比不要和模型层 `GPT-5.4 vs GPT-5.3-Codex` 混写。
3. **跨站内链机会**：
   - blog 比较页导向 docs 配置页。
   - docs pricing 页导向 aifreeapi free/cheap route。
   - Codex Computer Use 文章导向 docs App/CLI route map。
   - Chinese domestic-use docs 页导向 API console 和中文 FAQ。
4. **站点优先级建议**：
   - 第一优先：`docs.laozhang.ai` 刷新现有 Codex CLI 页。
   - 第二优先：`blog.laozhang.ai` 更新/补齐 comparison 和 app/CLI 决策页。
   - 第三优先：`aifreeapi.com` 做 free/cheap/API-key 角度。
   - 暂缓：`yingtu.ai`。
