# SEO/GEO Evidence Pack: openai

- Seed keyword: `openai`
- Run date: 2026-04-23
- Timezone: Asia/Shanghai
- Target locale: United States / English SERP first, with Chinese commercial variants for LaoZhang network routing
- Output directory: `.codex/reports/seo/2026-04-23-openai/`
- Method: Computer Use browser capture first, then Google Suggest API, official OpenAI docs, web breadth search, and local owned-asset scans.

## Evidence Index

| Group | Method | Status |
| --- | --- | --- |
| `SERP-main-openai` | Computer Use in Chrome + screenshot | Clean capture |
| `SERP-variant-openai-api` | Computer Use in Chrome + screenshot | Clean capture |
| `Trends-openai-comparison` | Computer Use in Google Trends + screenshot | Clean capture |
| `Suggest-en-root` | Google Suggest API | Clean fetch |
| `Suggest-en-commercial` | Google Suggest API | Clean fetch |
| `Suggest-zh-commercial` | Google Suggest API | Clean fetch |
| `OpenAI-official-docs` | OpenAI developer docs MCP | Clean fetch |
| `Owned-docs` | Local repo scan + indexed search | Clean scan |
| `Owned-blog-laozhang` | Local repo scan + indexed search | Clean scan |
| `Owned-aifreeapi` | Indexed site search | Partial; no local repo found |
| `Owned-yingtu` | Local repo scan + indexed search | Clean scan |
| `Community-and-video` | Computer Use SERP blocks | Partial but visible |
| `Limitations` | Research boundary | No Ahrefs/SEMrush volume data |

## `SERP-main-openai`

- Query: `openai`
- URL: `https://www.google.com/search?q=openai&hl=en&gl=us&pws=0&num=10`
- Capture method: Computer Use controlling Google Chrome.
- Capture time: 2026-04-23 around 19:19 Asia/Shanghai.
- Screenshot: `screenshots/google-openai-main.png`
- Status: clean Google SERP capture. Google was readable; no CAPTCHA or `sorry` page.

Visible SERP structure:

- Top ad: ChatGPT / `chatgpt.com` appeared as a sponsored result. Ad copy was localized unexpectedly, likely due browser/account/extension context.
- Organic #1: OpenAI official site / `openai.com`, with sitelinks for Careers, ChatGPT, OpenAI Platform, API Platform, About.
- Fresh official block: "Latest from openai.com" contained recent OpenAI news and launch pages, including clinician improvement, workspace agents, Responses API WebSockets, Privacy Filter, Codex enterprise, ChatGPT Images 2.0, and GPT-Rosalind items.
- Organic brand/knowledge results: Wikipedia page for OpenAI and ChatGPT result on `chatgpt.com`.
- News block: major publisher coverage around OpenAI, workspace agents, and business/news events.
- Social/community block: X, Reddit, and YouTube surfaces around recent OpenAI launches and ChatGPT Images 2.0.
- Video block: YouTube videos around ChatGPT Images 2.0, OpenAI Image 2, and OpenAI founder/podcast coverage.
- Related searches visible from the capture: `OpenAI API`, `OpenAI careers`, `OpenAI stock`, `Openai image2`, `Openai image`, `OpenAI app`, `OpenAI download`, `OpenAI - wikipedia`.

Interpretation:

- The bare keyword `openai` is overwhelmingly navigational, brand, latest-news, and entity-disambiguation intent.
- A non-official site has very low realistic chance of ranking top 3 for the exact seed keyword.
- The useful business opportunity starts from modifiers: API, key, pricing, domestic access, docs, SDK, Responses, Codex, image generation, and comparison/alternative intent.

## `SERP-variant-openai-api`

- Query: `openai api`
- URL: `https://www.google.com/search?q=openai+api&hl=en&gl=us&pws=0&num=10`
- Capture method: Computer Use controlling Google Chrome in a new tab.
- Capture time: 2026-04-23 around 19:25 Asia/Shanghai.
- Screenshot: `screenshots/google-openai-api.png`
- Status: clean Google SERP capture. Result structure was readable.

Visible top results and features:

| Position / block | Visible result | URL / type | Signal |
| --- | --- | --- | --- |
| Organic #1 with sitelinks | API Platform | `openai.com/api/` | Official API platform result dominates |
| Sitelink | OpenAI API | `openai.com/index/openai-api/` | Historical/overview official API page |
| Sitelink | API Platform | `developers.openai.com/api/docs` | Official docs intent |
| Sitelink | API Key? | OpenAI Help | Key/account intent |
| Sitelink | API Overview | `developers.openai.com/api/reference/overview/` | Reference intent |
| Sitelink | API Pricing | `openai.com/api/pricing/` | Commercial pricing intent |
| Organic | OpenAI Platform | `platform.openai.com` | Login/signup intent |
| Organic | OpenAI root | `openai.com` | Platform and docs sitelinks |
| Video block | YouTube tutorials | YouTube | Beginner/tutorial intent |
| Forum/community | Reddit: what people use OpenAI APIs for | Reddit | Use-case/community validation |
| People also search for | API key, pricing, documentation, key free, console, login, Python, playground | Google feature | Strong modifier map |

Notes:

- The visible Google page included a "Search performance for this query" overlay for `blog.laozhang.ai`; this appears to be account/extension/Search Console context and is not treated as organic ranking evidence.
- Footer stated "Results are not personalized"; however, browser extensions and logged-in Chrome context were visible, so screenshots are recorded as browser evidence, not neutral rank-tracking data.

Interpretation:

- `openai api` is still official-source dominated, but the SERP exposes commercial and problem-solving modifiers that LaoZhang can target.
- Top 3 for head `openai api` is difficult; long-tail pages can win by answering local access, payment, SDK base URL, pricing interpretation, and route choice.

## `Trends-openai-comparison`

- Google Trends URL: `https://trends.google.com/trends/explore?date=today%205-y&geo=US&q=openai,chatgpt,claude,gemini,grok&hl=en`
- Capture method: Computer Use in Chrome.
- Capture time: 2026-04-23 around 19:26 Asia/Shanghai.
- Screenshot: `screenshots/google-trends-openai-comparison.png`
- Status: clean Google Trends capture; graph and tabular data were readable.

Visible average interest over the past 5 years, United States, Web Search:

| Term | Average |
| --- | ---: |
| `openai` | 2 |
| `chatgpt` | 30 |
| `claude` | 3 |
| `gemini` | 8 |
| `grok` | 1 |

Recent visible rows near 2026-04:

- 2026-04-05: openai 9, chatgpt 77, claude 29, gemini 31, grok 6.
- 2026-04-12: openai 4, chatgpt 76, claude 27, gemini 33, grok 5.
- 2026-04-19: openai 4, chatgpt 81, claude 27, gemini 34, grok 5.

Visible related rising queries for `openai`:

- `chatgpt`
- `openai codex`
- `sora`
- `anthropic`
- `openai vs chatgpt`

Interpretation:

- In broad user interest, `ChatGPT` is much stronger than `OpenAI` as a consumer/search term.
- `OpenAI` is useful as an authority/entity modifier, but better commercial pages should attach it to API, Codex, Sora, pricing, model, or comparison intent.

## `Suggest-en-root`

Source: `https://suggestqueries.google.com/complete/search?client=chrome&hl=en&gl=us&q=openai`

Suggestions:

- `openai api`
- `https://openai.com/`
- `openai stock`
- `openai chatgpt`
- `openai careers`
- `openai api key`
- `openai codex`
- `openai news`
- `openai login`
- `openai jobs`
- `openai ipo`
- `openai image 2.0`
- `openai spud`
- `openai valuation`
- `openai workspace agents`

Interpretation:

- Root autocomplete splits into navigational, investor/employment, login, API, Codex, and fresh product/news queries.
- LaoZhang should not target stock/careers/jobs/IPO/valuation/news as primary business pages.

## `Suggest-en-commercial`

Source: Google Suggest API for `openai api`, `openai pricing`, `openai vs`, and `openai alternative`.

`openai api` suggestions:

- `openai api key`
- `openai api pricing`
- `openai api login`
- `openai api platform`
- `openai api models`
- `openai api key free`
- `openai api usage`
- `openai api documentation`
- `openai api docs`
- `openai api costs`
- `openai api dashboard`
- `openai api billing`
- `openai api console`
- `openai api key pricing`
- `openai api status`

`openai pricing` suggestions:

- `openai pricing api`
- `openai pricing plans`
- `openai pricing models`
- `openai pricing tiers`
- `openai pricing calculator`
- `openai pricing codex`
- `openai pricing page`
- `openai pricing changes`
- `openai pricing lead`
- `openai pricing tokens`
- `openai pricing table`
- `openai pricing api models`
- `openai pricing vs claude`
- `openai pricing per token`
- `openai pricing azure`

`openai vs` suggestions:

- `openai vs anthropic`
- `openai vs chatgpt`
- `openai vs claude`
- `openai vs gemini`
- `openai vs anthropic revenue`
- `openai vs claude vs gemini`
- `openai vs anthropic vs gemini`
- `openai vs google`
- `openai vs copilot`
- `openai vs xai`
- `openai vs anthropic reddit`
- `openai vs chatgpt vs copilot`
- `openai vs grok`
- `openai vs deepseek`
- `openai vs musk`

`openai alternative` suggestions:

- `openai alternatives`
- `openai alternative to github`
- `openai alternative to claude code`
- `openai alternative free`
- `openai alternative to notebooklm`
- `openai alternatives reddit`
- `openai alternative api`
- `openai alternative free api`
- `openai alternatives to chatgpt`
- `openai alternative for coding`
- `openai alternative to mcp`

Interpretation:

- High-value commercial clusters: API key, pricing, models, docs, costs, billing, status, alternatives, comparisons, and coding/Codex.
- `free` and `cheap` should route to `aifreeapi.com` or carefully framed low-cost pages, not to official-price claims.

## `Suggest-zh-commercial`

Source: Google Suggest API for `OpenAI API 国内` and `OpenAI API 价格`.

`OpenAI API 国内` suggestions:

- `openai api 国内 购买`
- `openai api 国内 代理`
- `openai api 国内 充值`
- `openai api 国内 信用卡`
- `openai api 国内 使用`
- `openai api 国内 中转`
- `openai api 国内 访问`
- `openai api 国内 调用`
- `openai api 充值 国内 信用卡`
- `openai api key 国内`
- `openai api key 国内 购买`
- `国内 如何 使用 openai api`
- `国内 如何 调用 openai api`
- `国内 如何购买 openai api`
- `国内 使用 openai api key`

`OpenAI API 价格` suggestions:

- `openai api价格表`
- `openai api key 价格`
- `openai whisper api 价格`
- `openai realtime api 价格`
- `openai api token价格`
- `openai api 调用 价格`
- `openai api模型价格`
- `openai o1 api 价格`
- `openai api使用`
- `openai api充值`
- `openai api开发`
- `openai api 教程`
- `azure openai api 价格`

Interpretation:

- Chinese intent is much more business-aligned than the English head term.
- The strongest LaoZhang route is `OpenAI API 国内使用 / 中转 / 价格 / Key / 充值 / SDK 接入`, not a generic "what is OpenAI" page.

## `OpenAI-official-docs`

Official OpenAI docs fetched through the OpenAI developer docs MCP.

Sources:

- GPT-5.4 model page: `https://developers.openai.com/api/docs/models/gpt-5.4`
- Latest model guide: `https://developers.openai.com/api/docs/guides/latest-model`
- Pricing page: `https://developers.openai.com/api/docs/pricing`
- Migrate to Responses API: `https://developers.openai.com/api/docs/guides/migrate-to-responses`
- Image generation guide: `https://developers.openai.com/api/docs/guides/image-generation`
- GPT Image 2 model page: `https://developers.openai.com/api/docs/models/gpt-image-2`
- Image cost calculator section: `https://developers.openai.com/api/docs/guides/image-generation#calculating-costs`

Current official facts relevant to content planning:

- `gpt-5.4` model page lists Model ID `gpt-5.4`, current snapshot `gpt-5.4-2026-03-05`, supported tools including function calling, web search, file search, tool search, image generation, code interpreter, hosted shell, skills, computer use, and MCP.
- The latest model guide states `gpt-5.4` is the default model for broad general-purpose work and most coding tasks, with `gpt-5.4-pro`, `gpt-5.4-mini`, and `gpt-5.4-nano` as variants.
- The migration guide says Chat Completions remains supported, but Responses is recommended for all new projects.
- The migration guide describes Responses as a unified interface with built-in tools including web search, file search, computer use, code interpreter, remote MCPs, and native multimodal support.
- The pricing page lists current GPT-5.4 family token pricing, including `gpt-5.4`, `gpt-5.4-mini`, `gpt-5.4-nano`, and `gpt-5.4-pro`; pricing is volatile and must be rechecked before publication.
- The image generation guide says single prompt image generation/editing should use Image API, while conversational/editable image experiences should use Responses API.
- The image generation guide says GPT Image models may require API Organization Verification.
- The GPT Image 2 model page lists Model ID `gpt-image-2`, snapshot `gpt-image-2-2026-04-21`.
- The image generation cost section lists GPT Image 2 sample per-image estimates such as 1024 x 1024 low `$0.006`, medium `$0.053`, high `$0.211`, while reminding users to account for text and image input tokens.

Volatility warning:

- Any pricing, model availability, free-tier, verification, rate-limit, or supported-tool claim must be rechecked against official docs immediately before publication.
- Some existing owned and third-party indexed pages predate the current GPT Image 2 official surface and should be refreshed if they still say no public `gpt-image-2` model row exists.

## `Owned-docs`

Local repo: `/Users/laozhang/Projects/docs`.

Representative local assets:

- `docs.json`: navigation includes OpenAI-compatible API surfaces and pages such as `api-capabilities/openai-sdk`, `api-capabilities/openai-responses`, and `api-reference/openai`.
- `public/sitemap.xml`: includes `/api-capabilities/openai-sdk` and `/api-capabilities/openai-responses`.
- `llms.txt`: describes LaoZhang API as OpenAI API compatible and links to OpenAI SDK usage and OpenAI-compatible Responses.
- `index.mdx`: links to OpenAI SDK and OpenAI Responses; includes API base URL replacement pattern.
- `getting-started.mdx`: mentions OpenAI SDK compatibility and API setup.
- `api-reference/openai.mdx`: current page title "OpenAI 模型"; describes GPT-4o, GPT-4, O1, GPT-3.5. This is useful but dated against current official GPT-5.4/GPT Image 2 docs.
- `api-capabilities/openai-sdk.mdx`: strong SDK/base URL page; currently fits `openai sdk`, `openai api compatible`, and `base_url` intent.
- `api-capabilities/openai-responses.mdx`: current page title "OpenAI Responses API 支持"; useful but model list appears behind current official GPT-5.4 + Responses guidance.
- `api-capabilities/gpt-image-2.mdx`: route-specific LaoZhang GPT Image 2 API page with `yingtu.ai` testing CTA and provider price. This is a valuable owned page, but must keep official OpenAI pricing separate from LaoZhang provider pricing.
- `scenarios/programming/codex-cli.mdx`: OpenAI Codex CLI configuration page.

Indexed owned results visible through web search:

- `https://docs.laozhang.ai/api-reference/openai`
- `https://docs.laozhang.ai/en/api-reference/openai`
- `https://docs.laozhang.ai/api-capabilities/openai-sdk`
- `https://docs.laozhang.ai/api-manual`
- `https://docs.laozhang.ai/`

Interpretation:

- Existing docs already own the technical foundation. Best first move is optimization/refresh, not creating a duplicate generic page.
- Strongest gap: a consolidated route page for `OpenAI API 国内使用：Key、价格、充值、中转与 SDK 接入`, then refresh model and Responses pages to current official GPT-5.4/GPT Image 2 contracts.

## `Owned-blog-laozhang`

Local repo: `/Users/laozhang/Projects/blog-laozhang`.

Representative pages found across locales:

- `openai-api-key-free-trial`
- `openai-sora-api`
- `openai-codex-march-2026`
- `openai-file-type-not-supported-pdf`
- `openai-codex-usage-limits`
- `openai-api-key-organization-id`
- `gpt-5-4-cyber`
- `gpt-5-4-vs-gemini-3-1`
- `gpt-image-2-api`
- `gpt-image-2-api-pricing`
- `is-gpt-image-2-free`
- `gpt-image-2-vs-nano-banana-pro`
- `chatgpt-images-2-0`
- `how-to-use-gpt-image-2`
- `claude-code-vs-codex`
- `gemini-api-vs-openai-vs-claude`

Indexed site-search examples:

- `https://blog.laozhang.ai/en/posts/gpt-image-2-api-pricing/`

Interpretation:

- `blog.laozhang.ai` has rich topical mass around OpenAI, Codex, GPT-5.4, GPT Image 2, free/pricing/access, and comparisons.
- Some image-pricing posts may now be stale because official OpenAI docs currently list GPT Image 2. These should be refreshed before using them as internal links for a current report.
- Blog is the right place for comparison/tutorial/news-derived angles; docs should own durable integration and route pages.

## `Owned-blog-secondary`

Local repo: `/Users/laozhang/Projects/blog`.

Representative pages found across locales:

- `openai-api-key-vs-azure-openai`
- `openai-api-key-free-trial`
- `openai-api-key-how-to-get`
- `openai-api-key-pricing`
- `openai-api-key-requirements`
- `openai-api-key-usage`
- `openai-api-key-quota-exceeded`
- `openai-api-key-purchase`
- `openai-api-key-free`
- `openai-api-key-cost`
- `openai-api-pricing-gpt-4o-2025`
- `openai-gpt-4o-api-pricing-guide`
- `openai-image-generation-api-pricing`
- `openai-image-generation-api-free`
- `openai-image-generation-api-cheaper-alternative`
- `openai-image-generation-api-endpoint`
- `openai-image-generation-api-curl`
- `openai-image-api-tutorial`
- `gemini-api-vs-openai-vs-claude-2026-cost-guide`

Interpretation:

- The secondary blog repo has many historical OpenAI API/key/pricing pages. It is useful as historical coverage evidence, but duplicate creation risk is high.
- For the current docs SEO report, recommend cross-site canonical role separation before creating any new OpenAI API page.

## `Owned-aifreeapi`

Local repo search:

- No local `aifreeapi` project directory found under `/Users/laozhang/Projects` with shallow directory search.

Indexed site-search examples:

- `https://www.aifreeapi.com/en/posts/openai-api-key-free`
- `https://www.aifreeapi.com/en/posts/openai-api-key-free-trial`
- `https://www.aifreeapi.com/en/posts/openai-image-generation-api-free`

Interpretation:

- `aifreeapi.com` already maps naturally to free/cheap/low-cost OpenAI API searches.
- The indexed examples contain volatile free-tier and model claims. Treat them as coverage inventory, not as current truth unless reverified.
- Best route: reserve `aifreeapi.com` for "free tier", "cheap alternative", "key free", and "minimum cost" queries; do not let it compete with docs for SDK/API integration pages.

## `Owned-yingtu`

Local repo: `/Users/laozhang/Projects/yingtuai`.

Representative assets found:

- `content/blog/zh/openai-refund-appeal-guide`
- `content/blog/zh/openai-enterprise-account-verification`
- `content/blog/zh/openai-api-verification-required-models-china`
- `content/blog/en/gpt-image-1-5-vs-nano-banana-pro`
- `content/blog/en/nano-banana-pro-vs-gpt-image-text-rendering`
- `content/blog/en/gemini-3-pro-vs-gpt-image-1-5-pricing-quality-comparison`
- Multiple ChatGPT Plus, payment, image-limit, and image-generation route pages.
- Product-level image testing/creation entry point: `yingtu.ai`.

Interpretation:

- `yingtu.ai` should own image testing and image-model selection angles, especially `openai image`, `chatgpt image`, `gpt-image-2`, and image prompt/use cases.
- It should not own generic `openai api` pages unless the query is image-specific.

## `Community-and-video`

Visible from Computer Use SERP captures:

- `openai api` SERP included YouTube tutorials such as "3 Tips for Working With the OpenAI API", "OpenAI API: How to Make Your First API Call", and "Getting Started with the OpenAI API".
- `openai api` SERP included Reddit result "What are people using the OpenAI APIs for?".
- `openai` main SERP included social/community and video blocks around ChatGPT Images 2.0, OpenAI Image 2, and product launches.
- Google Trends related queries for `openai` included `openai codex`, `sora`, `anthropic`, and `openai vs chatgpt`.

Interpretation:

- Real user demand is not only "what is OpenAI"; it is "how do I use the API", "what can I build", "what changed", "how does it compare", and "which route should I take".
- Tutorial, comparison, troubleshooting, and route-choice content are more useful than generic company/entity explainers.

## `Limitations`

- No Ahrefs, Semrush, Similarweb, or Google Ads Keyword Planner volumes were available.
- Search volume and difficulty labels in the report are inferred from SERP structure, autocomplete density, Trends, ads/features, and owned-index coverage.
- Browser captures occurred in the user's existing Chrome profile with visible extensions and account context. Clean result structures were captured, but this should not be treated as neutral rank-tracking.
- Official OpenAI pricing, model availability, rate limits, free-tier, and verification requirements are volatile and require same-day recheck before publishing any content that quotes them.
