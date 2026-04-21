# SEO/GEO evidence ledger: codex

> Capture date: 2026-04-21  
> Workspace: `/Users/laozhang/Projects/docs`  
> Keyword seed: `codex`  
> Target market: Google US / English, plus Chinese-language variants  
> Method: Computer Use browser SERP capture, Google Trends browser capture, Google Suggest API, official-source verification, web breadth search, owned-asset scan.

## Data Boundaries

- This is a live snapshot, not a professional search-volume export. No Ahrefs, SEMrush, Similarweb, or GSC bulk export was used.
- Browser SERP capture succeeded. The main Google page stated that results were not personalized and that Google could not determine a precise location.
- Google Trends capture succeeded for Worldwide and US, 12-month web search.
- Suggest data came from `suggestqueries.google.com` with `client=firefox`, `gl=us`, and `hl=en` / `hl=zh-CN`.
- Pricing, plan, model, and usage-limit facts are freshness-sensitive. Publication should recheck OpenAI official pages on the day of editing.

## Source Groups

### SERP-main-codex

- Query: `https://www.google.com/search?q=codex&hl=en&gl=us&pws=0&num=10`
- Screenshot: `screenshots/serp-main-codex.png`
- Capture status: clean browser SERP.
- Visible top results and features:
  - `Codex | AI Coding Partner from OpenAI` from `openai.com/codex/`.
  - Sitelinks for `Codex CLI` and `Codex app` on `developers.openai.com`.
  - Fresh OpenAI links in the result cluster: `Codex for (almost) everything`, `Remote connections - Codex`, `Chronicle - Codex`, `Native development - Codex`, `Computer Use - Codex app`, and `Hooks - Codex`.
  - People Also Ask included: "What does the term codex mean?", "Is codex part of ChatGPT?", "Is codex free or paid?", and "What is the codex of the Devil's Bible?"
  - Other visible results included `github.com/openai/codex`, `chatgpt.com/codex`, FAO Codex Alimentarius, and Wikipedia `Codex`.
  - Community/media modules included Reddit, X, LinkedIn, YouTube, and Medium.
- Inference: the naked head term is controlled by OpenAI plus legacy/non-OpenAI meanings. It is not a good standalone target for LaoZhang unless framed as a product route map.

### SERP-variant-api

- Query: `https://www.google.com/search?q=codex%20API&hl=en&gl=us&pws=0&num=10`
- Screenshot: `screenshots/serp-variant-api.png`
- Capture status: clean browser SERP.
- Visible signals:
  - Top result: `Codex` on OpenAI Developers with sitelinks for `Codex Pricing`, `Codex CLI`, `Codex web`, `Quickstart - Codex`, and `Codex app`.
  - Official OpenAI product page and OpenAI API code-generation guide were both visible.
  - GitHub `openai/codex` was visible and framed CLI/API-key setup as a separate route from the cloud agent.
  - Reddit result asked whether Codex can be used via API and paid by usage instead of Plus.
  - Sponsored result from Anthropic Claude Code appeared.
  - Related searches included `Codex API pricing`, `Codex API key`, `Codex download`, `Codex OpenAI`, `Codex CLI`, `Codex IDE`, `Codex API key free`, and `Codex app`.
- Inference: `codex API` is not a pure API endpoint query. It splits into ChatGPT account, API key, CLI/IDE setup, cloud features, and pricing/limits.

### SERP-variant-pricing

- Query: `https://www.google.com/search?q=codex%20pricing&hl=en&gl=us&pws=0&num=10`
- Screenshot: `screenshots/serp-variant-pricing.png`
- Capture status: clean browser SERP.
- Visible signals:
  - Top result: OpenAI Developers `Codex Pricing`.
  - SERP snippet referenced a limited-time Pro usage promo through May 31, 2026.
  - OpenAI blog result: `Codex now offers pay-as-you-go pricing for teams`, dated April 2, 2026.
  - Reddit pricing threads were prominent.
  - People Also Ask included cost/month, ChatGPT subscription inclusion, Plus free/included access, and model-cost questions.
  - Related searches included `Codex pricing student`, `ChatGPT Codex pricing`, `Codex pricing Free`, `Codex pricing vs Claude Code`, `Codex pricing change`, `Codex pricing limits`, `Codex pricing Reddit`, and `Codex plans`.
- Inference: pricing demand is high and volatile. The page shape should be a contract-correction page, not a single-number answer.

### SERP-variant-tutorial

- Query: `https://www.google.com/search?q=codex%20tutorial&hl=en&gl=us&pws=0&num=10`
- Screenshot: `screenshots/serp-variant-tutorial.png`
- Capture status: clean browser SERP.
- Visible signals:
  - Top result: OpenAI Developers `Quickstart - Codex`.
  - Video block included OpenAI, John Kim, and tutorial creators.
  - Reddit result: `New to Codex, how to properly work with it?`
  - Other visible results included OpenAI `Get started with Codex`, YouTube playlists, Medium, and DataCamp.
  - Related searches included `Codex tutorial for beginners`, `Codex tutorial vscode`, `Codex CLI tutorial`, `Openai codex tutorial`, `Codex CLI install`, `Codex examples`, and `How to use Codex desktop app`.
- Inference: tutorial intent is accepted, but the first page rewards route-specific setup, video, and beginner workflow clarity.

### SERP-variant-vs

- Query: `https://www.google.com/search?q=codex%20vs&hl=en&gl=us&pws=0&num=10`
- Screenshot: `screenshots/serp-variant-vs.png`
- Capture status: clean browser SERP.
- Visible signals:
  - AI Overview compared OpenAI Codex and Claude Code.
  - Visible organic results included Reddit `Codex vs claude code`, Builder.io, Medium, Build.ms, Visual Studio Marketplace, and DataCamp.
  - Related searches included `Codex vs gpt`, `Codex vs chatgpt`, `Codex vs python`, `Codex vs Claude Code 2026`, `Codex VS Code`, `Codex vs Claude Code Reddit`, `Codex vs free`, and `Codex vs claude`.
- Inference: `vs` demand is strong, but the winning page should compare workflow route, trust boundary, cost contract, and plan availability instead of only benchmark claims.

### SERP-zh-tutorial

- Query: `https://www.google.com/search?q=codex%20%E6%95%99%E7%A8%8B&hl=zh-CN&gl=us&pws=0&num=10`
- Screenshot: `screenshots/serp-zh-tutorial.png`
- Capture status: clean browser SERP.
- Visible signals:
  - Top result: OpenAI Chinese `开始使用 Codex`.
  - Visible Chinese results included Zhihu, Runoob, GitHub Chinese guides, XiaoLin Coding, Tencent Cloud, and YouTube tutorials.
  - Related searches included `Codex vscode 教程`, `Codex 使用 文档`, `Codex 文档`, `Codex 使用 技巧`, `Codex cli 使用 教程`, `Codex 桌面 版 使用 教程`, `Codex 教程 bilibili`, and `Codex windows 安装 包`.
- Inference: Chinese demand is not just "what is Codex"; it is install, payment, domestic route, CLI/app setup, and local workflow.

### SERP-zh-pricing

- Query: `https://www.google.com/search?q=codex%20%E4%BB%B7%E6%A0%BC&hl=zh-CN&gl=us&pws=0&num=10`
- Screenshot: `screenshots/serp-zh-pricing.png`
- Capture status: clean browser SERP.
- Visible signals:
  - AI Overview summarized plan/API pricing, but should be treated as volatile and not used as a source of truth.
  - Top web result: OpenAI Developers `Codex Pricing`.
  - OpenAI Chinese blog result for team pay-as-you-go pricing appeared.
  - Unofficial Chinese pricing explainers, OpenAI API pricing pages, OpenRouter model pricing, and Reddit were visible.
  - Related searches included `Codex 订阅 价格`, `Codex 额度 查询`, `Codex pro 价格`, `Codex 收费 标准`, `Codex plus 价格`, `Codex 免费 额度`, `Codex 官网`, and `Codex plus 额度`.
- Inference: Chinese pricing intent needs plan/subscription/API-key/credit separation. It should not repeat AI Overview numbers without official recheck.

### Trends-worldwide-12m

- Page: Google Trends, query `codex`, Worldwide, Past 12 months, Web Search.
- Screenshot: `screenshots/google-trends-worldwide-12m.png`
- Capture status: clean browser capture.
- Visible chart values from browser accessibility state:
  - Apr 20 2025: 13
  - Aug 10 2025: 35
  - Jan 25 2026: 47
  - Feb 1 2026: 84
  - Feb 8 2026: 99
  - Mar 29 2026: 100
  - Apr 19 2026: 74
- Visible interest by region top 5:
  - China 100
  - South Korea 27
  - Singapore 23
  - Belgium 11
  - Taiwan 11
- Visible related queries rising:
  - `openclaw`
  - `codex config.toml`
  - `chatgpt pro`
  - `ai news today`
  - `openai news today`
- Inference: interest rose sharply in Q1 2026 and remains high. China/Taiwan/Singapore signal supports Chinese route/pricing/tutorial coverage.

### Trends-us-12m

- Page: Google Trends, query `codex`, United States, Past 12 months, Web Search.
- Screenshot: `screenshots/google-trends-us-12m.png`
- Capture status: clean browser capture.
- Visible chart values from browser accessibility state:
  - Apr 20 2025: 14
  - Jan 25 2026: 47
  - Feb 1 2026: 85
  - Feb 8 2026: 100
  - Mar 1 2026: 99
  - Mar 29 2026: 94
  - Apr 5 2026: 73
  - Apr 19 2026: 70
- Visible interest by subregion top 5:
  - Wyoming 100
  - Washington 68
  - California 66
  - District of Columbia 51
  - Massachusetts 51
- Visible related queries rising:
  - `openai codex app`
  - `openclaw`
  - `agents.md codex`
  - `codex cli github`
  - `npm`
- Inference: US demand also spiked around app/model/pricing changes, with configuration terms (`AGENTS.md`, CLI GitHub, npm) appearing as related queries.

### Suggest-codex

- Raw file: `raw/google-suggest-codex.json`
- Endpoint: `https://suggestqueries.google.com/complete/search?client=firefox`
- Locale: `gl=us`; `hl=en` and `hl=zh-CN`
- Query roots: 60
- Unique suggestions: 483
- High-intent suggestions filtered by API/pricing/tutorial/CLI/app/config/limits/free/Chinese patterns: 261
- Representative high-intent suggestions:
  - `chatgpt codex pricing`
  - `chatgpt codex usage`
  - `chatgpt codex vs claude code`
  - `codex agents.md`
  - `codex agents.md best practices`
  - `codex api`
  - `codex api key`
  - `codex api key free`
  - `codex api key vs subscription`
  - `codex api pricing`
  - `codex app download`
  - `codex cli install`
  - `codex cli mcp`
  - `codex config.toml`
  - `codex config.toml api key`
  - `codex cost per million tokens`
  - `codex desktop app`
  - `codex free credits`
  - `codex free limits`
  - `codex how to use api key`
  - `codex how to use subagents`
  - `codex login with api key`
  - `codex pricing and limits`
  - `codex rate limit check`
  - `codex usage dashboard`
  - `codex usage limits openai`
  - `codex cli 使用 教程`
  - `codex 国内使用`
  - `codex 价格`
  - `codex 额度`
  - `codex 订阅`
- Inference: Suggest confirms that practical route/config/pricing/limits terms are more ownable than a generic Codex explainer.

### Official-openai

Primary official URLs checked:

- [OpenAI Codex product page](https://openai.com/codex/)
- [OpenAI Developers Codex docs](https://developers.openai.com/codex)
- [OpenAI Developers Codex Quickstart](https://developers.openai.com/codex/quickstart)
- [OpenAI Developers Codex Pricing](https://developers.openai.com/codex/pricing)
- [OpenAI GitHub repo: openai/codex](https://github.com/openai/codex)
- [OpenAI blog: Introducing the Codex app](https://openai.com/index/introducing-the-codex-app/)
- [OpenAI blog: Codex now offers pay-as-you-go pricing for teams](https://openai.com/index/codex-flexible-pricing-for-teams/)

Key official facts observed:

- OpenAI product page positions Codex as a coding agent powered by ChatGPT and emphasizes App, editor, terminal, multi-agent workflows, Skills, Automations, and code review.
- Quickstart states every ChatGPT plan includes Codex and that Codex can also be used with API credits by signing in with an OpenAI API key.
- Quickstart lists setup paths for app, IDE extension, CLI, and cloud. CLI install examples include `npm install -g @openai/codex` and `brew install codex`.
- Pricing page states Codex is included in ChatGPT Free, Go, Plus, Pro, Business, Edu, and Enterprise, while API Key usage is billed by standard API rates and does not include some cloud-based features.
- Pricing page states Plus/Pro users can purchase additional credits after limits, can see current limits in the Codex usage dashboard, and can use `/status` in an active CLI session.
- OpenAI April 2, 2026 blog says ChatGPT Business and Enterprise can add Codex-only seats with pay-as-you-go pricing; usage is billed on token consumption, and the annual ChatGPT Business price was lowered from $25 to $20 per seat.

### Community-competitor

Representative community and competitor URLs observed in SERP/web breadth:

- [Reddit r/codex](https://www.reddit.com/r/codex/)
- Reddit pricing and limits discussions surfaced for `codex pricing`, `codex usage limits`, API-key usage, plan changes, and AGENTS/config issues.
- [Builder.io: Codex vs Claude Code](https://www.builder.io/blog/codex-vs-claude-code)
- [DataCamp: Codex vs Claude Code](https://www.datacamp.com/blog/codex-vs-claude-code)
- Hacker News discussion surfaced for Codex pricing/rate-card changes.
- GitHub and community config examples surfaced around `config.toml`, MCP, subagents, Skills, and `AGENTS.md`.

Inference:

- Community demand is especially strong around practical frustration: pricing changes, API key vs ChatGPT login, remaining limits, `/status`, `config.toml`, `AGENTS.md`, app vs CLI, and Claude Code migration.
- Comparison content must be current. Older `Codex = cloud only` framing is now wrong because current official docs and product pages show app, IDE, CLI, web/cloud, and API-key paths.

### Owned-docs

Commands run:

- `rg -n -i "codex|gpt-5.*codex|openai codex|agents\\.md|config\\.toml" docs.json llms.txt . --glob '!node_modules' ...`
- `sed -n '1,320p' scenarios/programming/codex-cli.mdx`
- `sed -n '1,300p' en/scenarios/programming/codex-cli.mdx`

Findings:

- Existing Chinese page: `scenarios/programming/codex-cli.mdx`
  - Title: `OpenAI Codex CLI 配置教程`
  - Description: `使用老张API配置 OpenAI Codex CLI 命令行编程助手，接入 GPT-5 编程能力`
  - Navigated in `docs.json`.
- Existing English page: `en/scenarios/programming/codex-cli.mdx`
  - Title: `OpenAI Codex CLI Setup Guide`
  - Description: `Configure OpenAI Codex CLI with LaoZhang API for stable access to GPT-5 coding capabilities`
  - Navigated in `docs.json`.
- Existing model-info pages mention `GPT-5.1-Codex` family.
- Current Codex CLI pages are useful but too narrow and partly stale against current SERP:
  - They are CLI-only, while official SERP now splits app, IDE, CLI, cloud, API key, and pricing.
  - They do not visibly cover `Codex pricing`, `Codex API key vs subscription`, `/status`, usage dashboard, `config.toml`, `AGENTS.md`, app download, or app-vs-CLI route choice.
  - They still center older model choices such as GPT-4.1 and o4-mini, while current official Codex docs and SERP emphasize GPT-5.4, GPT-5.4-mini, GPT-5.3-Codex, credits, and plan usage windows.

Inference:

- `docs.laozhang.ai` already has a ranking asset and should be refreshed/expanded before creating a new duplicate docs page.
- The highest-value docs move is a route-map refresh: CLI setup plus app/IDE/cloud/API-key/pricing/limits/config.

### Owned-blog-laozhang

Local and live search found existing blog assets:

- [OpenAI Codex in March 2026](https://blog.laozhang.ai/en/posts/openai-codex-march-2026)
- [Codex Computer Use](https://blog.laozhang.ai/en/posts/codex-computer-use/)
- Existing multilingual local files also include:
  - `openai-codex-usage-limits`
  - `claude-code-vs-codex`
  - `claude-opus-4-6-vs-gpt-5-3-codex`
  - `codex-computer-use`

Inference:

- `blog.laozhang.ai` already owns current/product-shift and comparison/supporting angles.
- New blog work should not duplicate docs CLI setup. It should support docs with decision pages: `Codex vs Claude Code`, `Codex app vs CLI`, `Codex Computer Use`, `Codex usage limits`, and model migration.

### Owned-blog-secondary

Local `blog` repo has many model/comparison pages:

- `gpt-5-4-vs-gpt-5-3-codex`
- `gpt-5-4-mini-vs-gpt-5-3-codex`
- `gpt-5-3-codex-vs-claude-opus-4-6`
- `gemini-3-1-pro-vs-opus-4-6-vs-codex-5-3`
- `claude-code-vs-codex`

Inference:

- The secondary blog is already saturated with model-vs-model Codex comparisons.
- Avoid creating another broad benchmark unless the query is explicitly model-layer. For product-layer queries, route to `blog-laozhang` or docs.

### Owned-yingtu

Local scan of `yingtuai` found no directly relevant content path for Codex as a coding agent. The repo has internal Codex workflow docs but not user-facing Codex search pages.

Inference:

- `yingtu.ai` is not a recommended first destination for Codex coding-agent keywords.
- Only reconsider if the query becomes image/video generation or a tool embedded in Yingtu workflows.

### Site-search-owned

Google site search found:

- [docs.laozhang.ai Codex CLI setup guide](https://docs.laozhang.ai/en/scenarios/programming/codex-cli)
- [docs.laozhang.ai Chinese Codex CLI setup guide](https://docs.laozhang.ai/scenarios/programming/codex-cli)
- [blog.laozhang.ai Codex Computer Use](https://blog.laozhang.ai/en/posts/codex-computer-use/)
- [blog.laozhang.ai OpenAI Codex in March 2026](https://blog.laozhang.ai/en/posts/openai-codex-march-2026)

Inference:

- Search engines can already see LaoZhang Codex assets.
- The opportunity is cluster expansion and refresh, not first-index discovery.

## Evidence-Based Intent Clusters

1. **Official/product route**: `codex`, `openai codex`, `chatgpt codex`, `codex app`, `codex cli`, `codex download`.
2. **Pricing/limits route**: `codex pricing`, `codex free`, `codex usage limits`, `codex rate limit`, `codex quota`, `codex credits`.
3. **API/auth route**: `codex api`, `codex api key`, `codex api key vs subscription`, `codex login with api key`.
4. **Configuration route**: `codex config.toml`, `codex agents.md`, `codex mcp`, `codex subagents`, `codex skills`.
5. **Tutorial route**: `codex tutorial`, `how to use codex`, `codex cli install`, `codex app download`, `codex desktop app`.
6. **Comparison route**: `codex vs claude code`, `codex vs cursor`, `codex vs chatgpt`, `codex vs copilot`.
7. **Chinese route**: `codex 教程`, `codex 价格`, `codex 国内使用`, `codex 免费额度`, `codex 订阅`.
8. **No-go ambiguity route**: book/manuscript meaning, Codex Alimentarius, Codex Gigas, Codex Sinaiticus, codex.io blockchain product.

## Evidence Gaps / Publication Recheck

- Recheck OpenAI pricing and limits on publish day. The page itself indicates ongoing migration to token/credit pricing and limited-time promos.
- Recheck model names and availability before editing docs pages. Current official pages mention GPT-5.4, GPT-5.4-mini, GPT-5.3-Codex, and GPT-5.3-Codex-Spark with different plan/API availability.
- If targeting Chinese domestic-use terms, confirm the exact LaoZhang API route and supported Codex-compatible model IDs before publishing setup commands.
- If targeting `AGENTS.md` or `config.toml`, use official developer docs and the current `openai/codex` repository as implementation truth, not older community snippets.
