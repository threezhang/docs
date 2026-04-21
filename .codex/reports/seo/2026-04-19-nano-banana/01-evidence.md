# SEO Evidence: nano banana

- Seed keyword: `nano banana`
- Run date: 2026-04-19
- Timezone: Asia/Shanghai
- Target locale: English global/US + Chinese API, pricing, tutorial, domestic-access intent
- Artifact path: `/Users/laozhang/Projects/docs/.codex/reports/seo/2026-04-19-nano-banana/`
- Primary workflow: `$docs-seo-research`

## Capture Status

### Computer Use Browser Capture

Computer Use was initially blocked by macOS/Chrome permission approval, then the user completed permissions. After that, Google SERP and Trends were captured in a live Chrome browser.

Status: clean browser capture after permission completion.

Captured screenshots:

| Evidence ID | Query / Page | Locale | Final URL pattern | Capture time | Screenshot |
| --- | --- | --- | --- | --- | --- |
| `SERP-main` | `nano banana` | `hl=en&gl=us&pws=0` | `google.com/search?q=nano+banana...` | 2026-04-19 22:12:03 CST | `screenshots/serp-main-nano-banana.png` |
| `SERP-variant-api` | `nano banana API` | `hl=en&gl=us&pws=0` | `google.com/search?q=nano+banana+API...` | 2026-04-19 22:12:36 CST | `screenshots/serp-variant-api.png` |
| `SERP-variant-pricing` | `nano banana pricing` | `hl=en&gl=us&pws=0` | `google.com/search?q=nano+banana+pricing...` | 2026-04-19 22:12:50 CST | `screenshots/serp-variant-pricing.png` |
| `SERP-variant-tutorial` | `nano banana tutorial` | `hl=en&gl=us&pws=0` | `google.com/search?q=nano+banana+tutorial...` | 2026-04-19 22:13:18 CST | `screenshots/serp-variant-tutorial.png` |
| `SERP-variant-vs` | `nano banana vs` | `hl=en&gl=us&pws=0` | `google.com/search?q=nano+banana+vs...` | 2026-04-19 22:13:34 CST | `screenshots/serp-variant-vs.png` |
| `SERP-zh-tutorial` | `nano banana 教程` | `hl=zh-CN&gl=CN&pws=0` | `google.com/search?q=nano+banana+教程...` | 2026-04-19 22:13:49 CST | `screenshots/serp-zh-tutorial.png` |
| `SERP-zh-pricing` | `nano banana 价格` | `hl=zh-CN&gl=CN&pws=0` | `google.com/search?q=nano+banana+价格...` | 2026-04-19 22:14:08 CST | `screenshots/serp-zh-pricing.png` |
| `Trends-us` | Google Trends: `nano banana`, US, past 12 months | US | `trends.google.com/trends/explore?...geo=US...` | 2026-04-19 22:14:32 CST | `screenshots/google-trends-us-12m.png` |
| `Trends-worldwide` | Google Trends: `nano banana`, worldwide, past 12 months | Worldwide | `trends.google.com/trends/explore?q=nano%20banana...` | 2026-04-19 22:14:53 CST | `screenshots/google-trends-worldwide-12m.png` |

No Google CAPTCHA, `sorry` page, or bot challenge appeared after permissions were completed. Some Google Search Console extension/private metrics were visible in the browser environment and are intentionally ignored.

### Supplemental Methods

- Official Google AI / Google Blog / Google Cloud sources via web open/search.
- Google Suggest API via `https://suggestqueries.google.com/complete/search?client=chrome`.
- Local owned-asset scans in:
  - `/Users/laozhang/Projects/docs`
  - `/Users/laozhang/Projects/blog-laozhang`
  - `/Users/laozhang/Projects/blog`
  - `/Users/laozhang/Projects/yingtuai`
- Site search for `aifreeapi.com`, because no local repo was found under `/Users/laozhang/Projects`.

## Exact Search Queries Used

### Browser SERP Queries

- `nano banana`
- `nano banana API`
- `nano banana pricing`
- `nano banana tutorial`
- `nano banana vs`
- `nano banana 教程`
- `nano banana 价格`

### Google Trends Pages

- `https://trends.google.com/trends/explore?date=today%2012-m&geo=US&q=nano%20banana&hl=en-US`
- `https://trends.google.com/trends/explore?date=today%2012-m&q=nano%20banana&hl=en-US`

### Official / Timeliness Queries

- `site:ai.google.dev/gemini-api/docs image generation Nano Banana Gemini 3.1 Flash Image Nano Banana 2`
- `site:ai.google.dev/gemini-api/docs pricing gemini-3.1-flash-image-preview gemini-3-pro-image-preview`
- `site:blog.google build with Nano Banana 2 Gemini API Google AI Studio`
- `site:cloud.google.com Nano Banana Pro available enterprise Gemini API Vertex AI`

### Owned-Site Queries

- `site:docs.laozhang.ai nano banana`
- `site:blog.laozhang.ai nano banana`
- `site:aifreeapi.com nano banana`
- `site:yingtu.ai nano banana`

## Official Evidence

### Official-Google-Image-Docs

Source: https://ai.google.dev/gemini-api/docs/image-generation

Current official API naming captured on 2026-04-19:

- `Nano Banana 2` = `gemini-3.1-flash-image-preview`
- `Nano Banana Pro` = `gemini-3-pro-image-preview`
- `Nano Banana` = `gemini-2.5-flash-image`

The official docs define Nano Banana as Gemini native image generation capability and state that the API family currently has the three models above. The same page shows text-to-image and image-editing examples using `gemini-3.1-flash-image-preview`.

Relevant web lines captured:

- `ai.google.dev/gemini-api/docs/image-generation` lines 234-240: alias map and SynthID note.
- Lines 241-370: text-to-image code examples for `gemini-3.1-flash-image-preview`.
- Lines 371-489 and 4045-4104: image-editing examples with the same model.

### Official-Google-Pricing

Source: https://ai.google.dev/gemini-api/docs/pricing

Current official developer pricing facts captured on 2026-04-19:

- `gemini-3.1-flash-image-preview`:
  - Free tier: not available on image pricing rows.
  - Standard image output: $0.045 for 0.5K, $0.067 for 1K, $0.101 for 2K, $0.151 for 4K.
  - Search grounding can add query charges.
- `gemini-3-pro-image-preview`:
  - Free tier: not available on image pricing rows.
  - Standard image output: $0.134 for 1K/2K and $0.24 for 4K.
  - Batch/Flex rows show lower image output pricing.
- `gemini-2.5-flash-image`:
  - Standard output: $0.039 per image.
  - Batch/Flex output: $0.0195 per image.

Relevant web lines captured:

- Pricing lines 357-378: `gemini-3.1-flash-image-preview` image output prices and no free-tier row.
- Pricing lines 458-506: `gemini-3-pro-image-preview` image output prices and no free-tier row.
- Pricing lines 708-743: `gemini-2.5-flash-image` image output prices.

### Official-Google-Launches

Sources:

- https://blog.google/innovation-and-ai/technology/developers-tools/build-with-nano-banana-2/
- https://cloud.google.com/blog/products/ai-machine-learning/nano-banana-pro-available-for-enterprise
- https://blog.google/products-and-platforms/products/gemini/updated-image-editing-model/
- https://blog.google/innovation-and-ai/products/gemini-app/personal-intelligence-nano-banana/

Observed facts:

- 2025-08-26: Google Gemini app update introduced the upgraded image-editing model branded as Nano Banana, emphasizing likeness preservation, blending, multi-turn editing, and SynthID/watermarking.
- 2025-11-20: Google Cloud announced Nano Banana Pro / Gemini 3 Pro Image for Vertex AI, Google Workspace, and Gemini Enterprise trajectory; developer route is Vertex AI Gemini API.
- 2026-02-26: Google announced Nano Banana 2 / Gemini 3.1 Flash Image for Google AI Studio and Gemini API. The post says a paid API key is required to use the model on Google AI Studio.
- 2026-04-16: Google announced Gemini app personalization features using Nano Banana 2 and Google Photos for eligible Google AI Plus/Pro/Ultra subscribers in the US.

Relevant web lines captured:

- Nano Banana 2 launch lines 250-308 and 334-340.
- Nano Banana Pro Cloud launch lines 80-87 and 132-137.
- Gemini app Nano Banana update lines 294-312.
- Personal Intelligence update lines 318-333.

### Official-Google-Deprecations

Source: https://ai.google.dev/gemini-api/docs/deprecations

Observed facts:

- `gemini-3.1-flash-image-preview`: release date 2026-02-26, no shutdown date announced.
- `gemini-3-pro-image-preview`: release date 2025-11-20, no shutdown date announced.
- `gemini-2.5-flash-image`: release date 2025-10-02, earliest shutdown date 2026-10-02, recommended replacement `gemini-3.1-flash-image-preview`.
- `gemini-2.5-flash-image-preview`: shut down 2026-01-15, recommended replacement `gemini-2.5-flash-image`.

Relevant web lines captured:

- Deprecations lines 192-200 for Gemini 3 image preview model status.
- Deprecations lines 209-218 for Gemini 2.5 Flash image status.

## Browser SERP Evidence

### SERP-main

Query: `nano banana`

Clean capture: yes.

Visible top structure:

- Ads: Artlist "Nano Banana Pro by Gemini 3", ChatGPT image ad, Adobe Firefly Nano Banana 2 ad, and `nanobananaprolabs.com`.
- Organic #1: Google Gemini `gemini.google/overview/image-generation/`, titled around "Nano Banana 2 - Gemini AI image generator & photo editor".
- Organic #2: `nanobanana.io`, "Nano Banana: Free Online AI Image Editor".
- PAA:
  - What exactly is Nano Banana?
  - Is Google Nano Banana free?
  - Why is Nano Banana so famous?
  - Does Nano Banana cost anything?
- Video block:
  - "48 POWERFUL ways to use Nano Banana 2!" (2 days ago)
  - "New Nano Banana Update: How to Use Nano Banana 2" (2 weeks ago)
  - "Nano Banana 2 is Here! Full Review & Testing Results" (1 month ago)
- Additional organic results visible while scrolling:
  - Google Blog Gemini app Nano Banana update.
  - AI Studio model page for `Gemini 3.1 Flash Image (aka Nano Banana 2)`.
  - Google DeepMind Gemini Image page.
  - `nano-banana.com`.
  - Artlist model page.
- Related searches / people also search for:
  - Nano Banana 2 Pro
  - Nano Banana free use
  - Nano Banana AI
  - Gemini Nano Banana 2
  - Nano Banana 3
  - Nano Banana Gemini
  - Nano Banana English
  - Nano Banana Google

Interpretation:

- Naked head term is mixed product/app/tool/tutorial/free intent.
- Google official surfaces are strong, but the SERP also rewards third-party online editor pages, videos, and ads.
- A generic new "what is Nano Banana" article is unlikely to be the best LaoZhang network entry point.

### SERP-variant-api

Query: `nano banana API`

Clean capture: yes.

Visible top structure:

- Ads: API/wrapper providers and general AI image products.
- Organic #1: Google AI Developers `ai.google.dev/gemini-api/docs/image-generation`, "Nano Banana image generation - Google AI for Developers".
- Organic #2: `nanobananaapi.ai`, "Nano Banana 2 & Nano Banana Pro API".
- PAA:
  - Can nano bananas be used via API?
  - Is Google Nano Banana API free?
  - What is the nano banana API?
  - Can I use nano banana images commercially?
- Additional visible results:
  - AI Studio model page for `gemini-3.1-flash-image`.
  - Google Blog "Build with Nano Banana 2".
  - Reddit pricing/API discussion.
  - Google Cloud Nano Banana Pro enterprise/API page.
  - Fal.ai and GitHub free/pro API pages.
- Related searches:
  - Nano Banana API pricing
  - Nano Banana API key
  - Nano Banana API key free
  - Nano Banana API documentation
  - Nano Banana API Python
  - Nano Banana cost per image
  - Nano Banana tutorial

Interpretation:

- API intent is high-conversion and official-docs-led.
- The gap is translation from market nickname to model ID, price, endpoint, and LaoZhang route.

### SERP-variant-pricing

Query: `nano banana pricing`

Clean capture: yes.

Visible top structure:

- AI Overview summarizes pricing, but values should be treated as volatile and rechecked against official pricing.
- Organic/winner types:
  - `nanobanana.io/pricing`
  - `nanobanana.im/pricing`
  - Reddit pricing breakdown
  - Google Gemini overview
  - Chase Jarvis pricing page
  - `nanobanana.org`
  - EvoLink pricing guide
  - Google AI Developers Forum pricing discussion
- Related searches:
  - Nano Banana API pricing
  - Nano Banana pricing reddit
  - Nano Banana pricing USA
  - Nano Banana 2 price
  - Nano Banana Pro pricing
  - How to buy Nano Banana Pro
  - Nano Banana 2 Pro free
  - Nano Banana plans

Interpretation:

- Pricing SERP is fragmented between official pricing, wrapper subscription pages, Reddit, and forum content.
- Winning content must avoid "one price" answers and split by model, route, resolution, and consumer-vs-API surface.

### SERP-variant-tutorial

Query: `nano banana tutorial`

Clean capture: yes.

Visible top structure:

- Video-heavy SERP:
  - Kevin Stratvert tutorial
  - AI Master tutorial
  - The AI Advantage tutorial
  - other YouTube walkthroughs
- Other results:
  - Reddit official prompt guide.
  - Google Gemini overview.
  - Google Cloud "Ultimate prompting guide for Nano Banana".
  - DEV Community Nano Banana Pro tutorial.
  - Google DeepMind prompt guide.
- Related searches:
  - tutorial step-by-step
  - beginners
  - how to use free
  - AI free
  - Nano Banana 2
  - prompt techniques
  - copy paste
  - demo

Interpretation:

- Tutorial intent is creator/workflow-led and video-friendly.
- It fits `yingtu.ai` and blog tutorials more than docs reference pages.

### SERP-variant-vs

Query: `nano banana vs`

Clean capture: yes.

Visible top structure:

- AI Overview compares Nano Banana Pro against Flux, Midjourney, ChatGPT-style image products, and describes quality/4K/text rendering.
- Organic examples:
  - Imagine.Art model comparison.
  - Higgsfield "Flux.2 vs Nano Banana Pro".
  - Reddit "Nano Banana Pro or Banana 2: Which one do you prefer?"
  - Labellerr Pro vs Standard.
  - Artlist Pro vs Standard.
  - Midlibrary Midjourney comparison.
  - WaveSpeed Nano Banana 2 vs Pro.
  - Google Gemini overview.
- PAA:
  - Anything better than Nano Banana?
  - Flux 2 vs Nano Banana?
  - ChatGPT vs Nano Banana?
  - Is Gemini the same as Nano Banana?
- Related searches:
  - Nano Banana 2
  - Nano Banana Pro
  - Nano Banana vs Pro
  - Nano Banana vs Nano Banana 2
  - Nano Banana vs Midjourney
  - Nano Banana vs Flux

Interpretation:

- Comparison intent is active, but the phrase "Nano Banana" is ambiguous.
- Pages must normalize which model is being compared before giving a winner.

### SERP-zh-tutorial

Query: `nano banana 教程`

Clean capture: yes.

Visible top structure:

- Zhihu: "Nano-banana 完整使用指南：教程、案例、白嫖网站".
- Bilibili tutorial/video result.
- YouTube Chinese/TW videos.
- GitHub prompt/creation repo.
- University blog and Zhihu "Nano Banana Pro 完全指南".
- Google Gemini TW overview.
- Tencent Cloud guide.
- Google Codelab "使用 Gemini Nano Banana 生成一致的图像".
- `nano-banana.cn` guide.
- Related:
  - Pro 使用教程
  - 本地部署
  - 破解版
  - 入口
  - Pro 免费使用
  - 是哪个公司
  - 越狱
  - 提示词

Interpretation:

- Chinese tutorial SERP has heavy community/video/third-party guide presence.
- There is noise around "破解/越狱"; avoid direct targeting.

### SERP-zh-pricing

Query: `nano banana 价格`

Clean capture: yes.

Visible top structure:

- Top pages include `nanobanana.io/zh/pricing`, `nano-banana.cn/pricing`, Reddit pricing breakdown, Zhihu API pricing, `nanobanana.im/zh/pricing`, 36Kr/Sina price-drop coverage.
- `docs.laozhang.ai/api-capabilities/nano-banana-pro-image` appears in the visible result set with a $0.09/张 price angle.
- Tencent Cloud domestic access guide appears.
- Related:
  - 中文官网
  - 图像生成器
  - 免费使用
  - 2价格
  - 中国
  - 在线使用
  - 免登录
  - 官网

Interpretation:

- LaoZhang docs already has live visibility in Chinese pricing SERP.
- This is a strong reason to fix docs canonical/model drift before creating more pages.

## Google Trends Evidence

### Trends-us

Source: Google Trends browser capture, US, past 12 months, Web Search.

Observed interest over time:

- Zero/near-zero until mid-August 2025.
- Aug 24 2025: 45.
- Aug 31 2025: 66.
- Nov 23 2025: 100 peak.
- Nov 30 2025: 77.
- Dec 7 2025: 58.
- Jan 2026: mid-30s.
- Mar 1 2026: 51.
- Apr 19 2026: 26.

Top subregions:

- California 100
- Washington 83
- Massachusetts 73
- District of Columbia 70
- New York 62

Related topics rising:

- Gemini
- Nano Banana
- API
- Text-to-image model
- Pricing

Related queries rising:

- `banana nano pro`
- `banana nano ai`
- `google banana nano`
- `google nano`
- `google banana`

Interpretation:

- US demand is below launch/Pro spike but still material.
- API and pricing are explicit related topics, supporting a commercial/API route.

### Trends-worldwide

Source: Google Trends browser capture, worldwide, past 12 months, Web Search.

Observed interest over time:

- Near-zero until mid-August 2025.
- Aug 24 2025: 45.
- Aug 31 2025: 86.
- Sep 7 2025: 100 peak.
- Sep 14 2025: 81.
- Nov 23 2025: 70.
- Nov 30 2025: 57.
- Dec 7 2025: 44.
- Feb 22 2026: 34.
- Mar 1 2026: 37.
- Apr 19 2026: 22.

Top regions:

- China 100
- Sri Lanka 35
- Hong Kong 26
- Nigeria 25
- Pakistan 25

Related topics rising:

- Nano Banana
- Gemini
- API
- Google AI
- Google AI Studio

Related queries rising:

- `gemini nano`
- `banana gemini`
- `gemini`
- `gemini nano banana`
- `nano banana ai google`

Interpretation:

- Worldwide interest has decayed from the early viral peak but remains live.
- China/Hong Kong signal supports Chinese pricing/domestic-access and API relay angles.

## Google Suggest Evidence

Suggest data was fetched from Google Suggest API (`client=chrome`) during this run.

### Suggest-en-root

Root: `nano banana`

- `nano banana pro`
- `nano banana 2`
- `nano banana ai`
- `nano banana gemini`
- `nano banana prompt`
- `nano banana api`
- `nano banana 2 pro`
- `nano banana free`
- `nano banana pro api`
- `nano banana pro free`
- `nano banana pro price`
- `nano banana google`
- `nano banana pro prompt`
- `nano banana 3`
- `nano banana ai free`

### Suggest-api

Root: `nano banana api`

- `nano banana api key`
- `nano banana api price`
- `nano banana api free`
- `nano banana api documentation`
- `nano banana api key free`
- `nano banana api cost per image`
- `nano banana api free tier`
- `nano banana api key price`
- `nano banana api access`
- `nano banana api status`
- `nano banana api url`
- `nano banana api google`
- `nano banana api call`
- `nano banana api endpoint`
- `nano banana api ai`

### Suggest-pricing

Root: `nano banana pricing`

- `nano banana pricing api`
- `nano banana pricing plans`
- `nano banana pricing google`
- `nano banana pricing per image`
- `nano banana pricing gemini`
- `nano banana pricing video`
- `nano banana pricing pro`
- `nano banana price subscription`
- `nano banana 2 pricing`
- `nano banana pro pricing api`
- `nano banana pro pricing google`

### Suggest-tutorial

Root: `nano banana tutorial`

- `nano banana tutorial for beginners`
- `nano banana tutorial architecture`
- `nano banana tutorial video`
- `nano banana tutorial pdf`
- `nano banana tutorial for interior design`
- `nano banana tutorial youtube`
- `nano banana tutorial prompt`
- `nano banana tutorial google`
- `nano banana tutorial photoshop`
- `nano banana tutorial for architects`
- `nano banana tutorial reddit`
- `nano banana guide`
- `nano banana guide google`
- `nano banana guide prompt`
- `nano banana guide pdf`

### Suggest-free

Root: `nano banana free`

- `nano banana free use`
- `nano banana free ai`
- `nano banana free trial`
- `nano banana free image generator`
- `nano banana free unlimited`
- `nano banana free video generator`
- `nano banana free version`
- `nano banana free api`
- `nano banana free prompts`
- `nano banana free download`
- `nano banana free no sign up`
- `nano banana free no credits`
- `nano banana freepik`
- `nano banana free limit`
- `nano banana free tier`

### Suggest-models-and-comparison

Root: `nano banana pro`

- `nano banana prompt`
- `nano banana pro api`
- `nano banana pro free`
- `nano banana pro price`
- `nano banana pro prompt`
- `nano banana pro 2`
- `nano banana pro gemini`
- `nano banana prompt github`
- `nano banana prompt library`
- `nano banana pro limit`
- `nano banana prompt gallery`
- `nano banana pro unlimited`
- `nano banana prompt guide`
- `nano banana pro ai`
- `nano banana pro free unlimited`

Root: `nano banana 2`

- `nano banana 2 pro`
- `nano banana 2 api`
- `nano banana 2 vs pro`
- `nano banana 2 free`
- `nano banana 2 price`
- `nano banana 2.5`
- `nano banana 2 ai`
- `nano banana 2 gemini`
- `nano banana 2.0`
- `nano banana 2 prompts`
- `nano banana 2 pro free`
- `nano banana 2 free unlimited`
- `nano banana 2 or pro`
- `nano banana 2 unlimited`
- `nano banana 2 google`

Root: `nano banana vs`

- `nano banana vs nano banana pro`
- `nano banana vs midjourney`
- `nano banana vs chatgpt`
- `nano banana vs imagen`
- `nano banana vs imagen 4`
- `nano banana vs gemini`
- `nano banana vs veo 3`
- `nano banana vs sora`
- `nano banana vs seedream`
- `nano banana vs chatgpt image generation`
- `nano banana vs nano banana 2`
- `nano banana vs veo`
- `nano banana vs grok`
- `nano banana vs flux`
- `nano banana vs dalle`

### Suggest-problem-and-developer

Root: `nano banana cost`

- `nano banana cost per image`
- `nano banana cost api`
- `nano banana cost in india`
- `nano banana cost uk`
- `nano banana cost per month`
- `nano banana cost google`
- `nano banana cost photoshop`
- `nano banana cost per generation`
- `nano banana cost gemini`
- `nano banana cost reddit`
- `nano banana cost calculator`
- `nano banana cost per token`

Root: `nano banana rate limit`

- `nano banana rate limit api`
- `nano banana rate limit exceeded`
- `nano banana pro rate limit`
- `gemini nano banana rate limit`
- `nano banana 2 rate limit`
- `google nano banana rate limit`
- `google ai studio nano banana rate limit`
- `gemini nano banana api rate limit`
- `nano banana you've reached your rate limit`

Root: `nano banana error`

- `nano banana error 13`
- `nano banana error message`
- `nano banana error reddit`
- `nano banana error 429`
- `nano banana error 500`
- `nano banana error pasting image`
- `nano banana error 503`
- `nano banana error 422`
- `nano banana problem`
- `nano banana problem with gemini`
- `nano banana failure`
- `nano banana pro error`
- `nano banana internal error`

Root: `nano banana not working`

- `nano banana not working today`
- `nano banana not working in gemini`
- `nano banana not working in photoshop`
- `nano banana not working reddit`
- `nano banana not working properly`
- `nano banana stopped working`
- `nano banana not showing in gemini`
- `nano banana not showing in photoshop`

Root: `nano banana python`

- `nano banana python api`
- `nano banana python code`
- `nano banana python sdk`
- `nano banana python github`
- `nano banana python example`
- `nano banana pro python`
- `gemini nano banana python`
- `google nano banana python api`
- `nano banana 2 python`

### Suggest-zh

Root: `nano banana 国内`

- `nano banana 国内 使用`
- `nano banana 国内 api`
- `nano banana 国内 怎么 用`
- `nano banana 国内 代理`
- `nano banana 国内 版`
- `nano banana 国内 平 替`
- `nano banana pro 国内`
- `nano banana pro api 国内`
- `nano banana 2 国内`

Root: `nano banana 教程`

- `nano banana pro 官方 教程`
- `nano banana pro 使用 教程`
- `nano banana 官方 教程`
- `nano banana 使用 教程`
- `nano banana pro 教程`
- `nano banana prompt 教程`
- `nano banana 提示 词 教程`
- `nano banana 2 教程`
- `nano banana 科研 绘图 教程`
- `nano banana ppt 教程`

Root: `nano banana 价格`

- `google nano banana 价格`
- `nano banana pro api 价格`
- `nano banana 2 价格`
- `nano banana token价格`
- `nano banana pro 的 价格`
- `nano banana pro 4k 价格`
- `nano banana 生 图 价格`
- `nano banana 2 api 价格`
- `nano banana 官方价格`
- `gemini nano banana 价格`

Root: `nano banana 免费`

- `nano banana 免费api`
- `nano banana 免费吗`
- `nano banana 免费 版`
- `nano banana 免费 使用`
- `nano banana 免费 入口`
- `nano banana pro 免费 api`
- `nano banana pro 免费 用`
- `nano banana 免费 使用 方法`
- `nano banana 可以 免费 使用 吗`
- `免费 使用 nano banana 的 网站`

Root: `nano banana API 中转`

- `nano banana api 中转站`
- `nano banana pro api 中转`
- `nano banana 2 api 中转`

## Community Evidence

Sources discovered through browser SERP and web search:

- Reddit pricing/API discussion visible on `SERP-variant-api`.
- Reddit pricing breakdown visible on `SERP-variant-pricing`.
- Reddit "Nano Banana Pro or Banana 2" comparison visible on `SERP-variant-vs`.
- Suggest problem clusters for 429/500/503, request denied, rate limit, no image, not working, not showing, and quality complaints.
- Google AI Developers Forum pricing result visible on `SERP-variant-pricing`.
- GitHub "Free Nano Banana Pro API" result visible on `SERP-variant-api`.

Extracted pain points:

- Naming confusion: Nano Banana vs Nano Banana 2 vs Nano Banana Pro vs official model IDs.
- API route confusion: Gemini API, AI Studio, Vertex AI, OpenAI-compatible proxies, and wrappers.
- Pricing confusion: consumer plan, official API price, Batch/Flex, resolution, and wrapper credits.
- Free-tier confusion: app/AI Studio trial-like use vs production API billing.
- Reliability issues: rate limits, overloaded/503, 429, no-image/text-only returns, request denied.
- Quality issues: small text, face/character consistency, Pro vs 2 downgrade perception, output resolution.
- Compliance issues: watermark removal and "free unlimited" claims.

## Owned Asset Evidence

### Owned-docs-local

Repo: `/Users/laozhang/Projects/docs`

Observed current docs:

- `docs.json` lines 12-14: banner says `Nano Banana 调价：Pro $0.09，Banana2 $0.055`.
- `docs.json` lines 154-187: navigation has image API groups for Standard, Banana2, and Pro.
- `api-capabilities/nano-banana-image.mdx`:
  - Title: Nano Banana 文生图.
  - Lines 52-55: maps Standard to `gemini-2.5-flash-image`.
  - Lines 73-80: price table includes Standard $0.025, Banana2 $0.055, Pro $0.09.
- `api-capabilities/nano-banana2-image.mdx`:
  - Lines 2-6: page title/description targets Nano Banana2 / Gemini 3.1 Flash / $0.055.
  - Lines 50-54: maps Nano Banana2 to `gemini-3.1-flash-image-preview`.
  - Lines 56-63: comparison table across Pro / Banana2 / Standard.
  - Lines 171-185: FAQ explains Pro vs Banana2 and migration.
- `api-capabilities/nano-banana-pro-image.mdx`:
  - Lines 2-6: Pro title/description and $0.09 positioning.
  - Lines 50-52: maps Pro to `gemini-3-pro-image-preview`.
  - Lines 97-104: comparison table includes Pro, Banana2, Standard.
- `en/api-capabilities/gemini-flash-image.mdx`:
  - Lines 2-5: title says Nano Banana 2 API but description/og maps to Pro price/model.
  - Lines 13-18 and 56-80: stale mapping says Nano Banana 2 = `gemini-3-pro-image-preview`, which now conflicts with official API docs and current Chinese Banana2 page.
- `public/sitemap.xml`:
  - Lines 48-61: still lists `https://docs.laozhang.ai/api-capabilities/gemini-flash-image` and `/en/api-capabilities/gemini-flash-image` under a Nano Banana 2 high-priority SEO comment.

Key risk:

- Current navigation points to `/api-capabilities/nano-banana2-image`, while sitemap still pushes old `gemini-flash-image` URLs. The old English page maps Banana2 to Pro. This creates canonical/semantic drift exactly in the high-value API/pricing cluster.

### Owned-blog-laozhang-local

Repo: `/Users/laozhang/Projects/blog-laozhang`

Local Nano Banana / Gemini image coverage is dense. Examples:

- `data/posts/en/nano-banana-2-api-pricing-guide/...`
- `data/posts/en/nano-banana-2-free-trial/...`
- `data/posts/en/nano-banana-2-free-unlimited/...`
- `data/posts/en/nano-banana-ai-image-generation-api/...`
- `data/posts/en/nano-banana-pro-api-guide/...`
- `data/posts/en/nano-banana-pro-4k-guide/...`
- `data/posts/en/nano-banana-pro-errors-troubleshooting-hub/...`
- `data/posts/en/gemini-3-1-flash-image-preview/...`
- `data/posts/en/gemini-3-pro-image-api-pricing/...`
- `data/posts/en/gemini-image-common-errors-fix/...`

Role fit:

- Strong for technical tutorials, model comparisons, pricing explainers, error diagnostics, and exact long-tail API problems.
- Avoid duplicating a docs reference/hub article as a blog article.

### Owned-blog-local

Repo: `/Users/laozhang/Projects/blog`

Local Nano Banana / Gemini image coverage includes:

- `content/blog/en/nano-banana-api-pricing/...`
- `content/blog/en/gemini-3-1-flash-image-preview-api/...`
- `content/blog/en/gemini-3-pro-flash-nano-banana-comparison/...`
- `content/blog/en/gemini-3-pro-4k-image-cost/...`
- `content/blog/en/how-to-use-nano-banana-pro/...`
- `content/blog/en/nano-banana-pro-best-prompts/...`
- `content/blog/en/nano-banana-pro-rate-limits/...`
- `content/blog/en/nano-banana-pro-troubleshooting/...`
- `content/blog/zh/gemini-nano-banana-tutorial/...`
- `content/blog/zh/nano-banana-free/...`

Role fit:

- Already covers many creator/developer long tails.
- Treat as supporting blog cluster, not the primary docs canonical.

### Owned-yingtu-local

Repo: `/Users/laozhang/Projects/yingtuai`

Observed local coverage:

- `src/lib/models.ts` contains Nano Banana, Nano Banana 2 (`gemini-3.1-flash-image-preview`), and Nano Banana Pro (`gemini-3-pro-image-preview`); default selected model is Nano Banana 2 from prior local context.
- Blog/content coverage includes cheap API credits, Pro pricing/quota, prompt guides, comparison guides, China guide, free/paid comparisons, and tutorial content.

Role fit:

- Best for image workflow, prompt, app experience, online generator, and creator comparison queries.
- Should not own the canonical API pricing/model-ID answer if docs is available.

### Owned-aifreeapi-web

No local repo found under `/Users/laozhang/Projects`. Site search found existing Nano Banana coverage:

- `https://www.aifreeapi.com/en/posts/nano-banana-free-use`
- `https://www.aifreeapi.com/en/posts/gemini-2-5-flash-image-replacement`
- `https://www.aifreeapi.com/en/posts/nano-banana-pro-api-key-free-trial`
- `https://www.aifreeapi.com/en/posts/nano-banana-ai-image-generator`
- `https://www.aifreeapi.com/en/posts/nano-banana-api-key-free`
- `https://www.aifreeapi.com/zh/posts/nano-banana2-china-direct`

Important caution:

- Some snippets from older/free-focused pages may conflict with current official pricing rows. Use aifreeapi for free/cheap route pages only after refreshing official pricing and availability facts.

## Volatile Facts To Recheck Before Publishing

- Google API pricing and Batch/Flex/Priority rows.
- Free tier availability for image models.
- Gemini app subscriber quotas and eligible countries.
- `gemini-2.5-flash-image` deprecation schedule.
- LaoZhang public prices: Standard $0.025, Banana2 $0.055, Pro $0.09.
- Docs sitemap/canonical/redirect behavior for `gemini-flash-image`.
- Whether AI Studio still requires a paid API key for Nano Banana 2 usage.

## Evidence Gaps

- No paid keyword volume or keyword difficulty from Ahrefs, Semrush, Google Ads Keyword Planner, or GSC.
- Browser SERP captures are search-time snapshots; rankings and AI Overview content can change.
- Google Suggest is locale/device sensitive.
- Some owned-site web snippets may be stale; local repo or live page verification is required before publishing edits.
