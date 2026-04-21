# SEO Evidence Ledger: gemini image

- Seed keyword: `gemini image`
- Run date: 2026-04-19 17:51 CST, Asia/Shanghai
- Target locale: US/English first; Chinese variants checked as secondary
- Artifact path: `.codex/reports/seo/2026-04-19-gemini-image/`
- Skill used: `docs-seo-research`

## Capture Status

### Computer Use SERP capture

- Status: blocked.
- Attempted tools:
  - `mcp__computer_use__.list_apps`
  - `mcp__computer_use__.get_app_state` for `Google Chrome`
  - `mcp__computer_use__.get_app_state` for `Safari`
- Result: all returned `Apple event error -10000: Sender process is not authenticated`.
- User then confirmed permission was allowed, but the same error persisted after retry.
- Consequence: no clean Computer Use browser screenshot or accessibility-tree SERP capture could be produced in this run.
- Evidence strength: degraded. SERP analysis below uses fallback sources and direct Google request blockers are recorded separately.

### Direct Google Search fallback

- Query URL attempted: `https://www.google.com/search?q=gemini%20image&hl=en&gl=us&pws=0`
- Result: HTML challenge/degraded Google Search page requiring JS/session flow. It did not expose normal result blocks.
- Key blocker text: Google returned a page with an access retry/challenge flow instead of readable SERP structure.
- Evidence group: `SERP-main-google-direct-blocked`

### Google Trends fallback

- Query URL attempted: `https://trends.google.com/trends/explore?date=today%2012-m&geo=US&q=gemini%20image`
- Result: Google returned `Error 429 (Too Many Requests)`.
- Evidence group: `Trends-fallback`
- Consequence: no quantified Trends chart or related-query table was available. Trend judgment is inferred from fresh official launches, Google Suggest density, and search-result freshness, and should be treated as indirect.

## Exact Queries Used

### High-value SERP intents

- `gemini image`
- `gemini image api`
- `gemini image pricing`
- `gemini image tutorial`
- `gemini image vs chatgpt image generation comparison 2026`
- `gemini image vs midjourney 2026`
- `gemini image not working 429 503 reddit`
- `gemini image generation API GitHub issue 429 503`

### Chinese variants

- `Gemini 图片生成 教程 Nano Banana 2`
- `Gemini 图片生成 API 价格 2026`
- `Gemini 图片生成 国内 使用 API 中转`
- `Gemini 图片生成 免费 次数 限制`

### Owned-asset searches

- `site:laozhang.ai gemini image API`
- `site:docs.laozhang.ai gemini image nano banana`
- `site:blog.laozhang.ai gemini image api`
- `site:aifreeapi.com gemini image`
- `site:yingtu.ai gemini image api nano banana`
- `site:yingtu.ai "Gemini 3 Pro Image"`
- `site:yingtu.ai "Nano Banana 2"`
- `site:laozhang.ai "Gemini 3 Pro Image"`

## Official And Current-Product Evidence

### `Official-google-image-generation`

Source URLs:

- https://ai.google.dev/gemini-api/docs/image-generation
- https://ai.google.dev/gemini-api/docs/image-generation#gemini-image-generation-models
- https://ai.google.dev/pricing
- https://ai.google.dev/gemini-api/docs/rate-limits
- https://support.google.com/gemini/answer/16275805?hl=en&ref_topic=13194540
- https://cloud.google.com/vertex-ai/generative-ai/docs/image/overview
- https://cloud.google.com/vertex-ai/generative-ai/pricing

Extracted facts used:

- Google AI docs now present multiple Gemini image-generation routes, not one generic `Gemini image` product.
- Google model naming currently includes `gemini-2.5-flash-image` for Nano Banana, `gemini-3-pro-image-preview` for Nano Banana Pro, and `gemini-3.1-flash-image-preview` for Nano Banana 2.
- Google pricing is model and resolution dependent. Official pricing needs source refresh before any publish-layer price claim because this is volatile.
- Google support distinguishes consumer Gemini App generation, Nano Banana 2 usage, and "Redo with Nano Banana Pro" usage limits by account/plan.
- Vertex AI and Gemini Developer API are different routes. A reader searching `gemini image api` often needs route choice first: Gemini API, Vertex AI, consumer Gemini App, or third-party OpenAI-compatible gateway.

## Fallback SERP Evidence

Because Computer Use and direct Google SERP access were blocked, the following are web-search fallback snapshots rather than clean Google SERP captures.

### `SERP-main`

Query: `gemini image`

Observed result mix:

- Official Google/Gemini surfaces and help content.
- Third-party exact-match image generator tools, including pages branded around "Gemini Image AI" or "Gemini AI image generator".
- SEO articles and tool pages using `Nano Banana`, `Gemini 3 Pro Image`, `Gemini 3.1 Flash Image`, and `Gemini image generator` interchangeably.
- User-intent split: generate image online, edit image online, find API, understand pricing/limits, compare with ChatGPT/Midjourney/Imagen.

Implication:

- The exact keyword is ambiguous and brand/tool-heavy. A generic page titled only `Gemini Image` would compete with official Google pages and thin tool pages while failing to satisfy API, free, prompt, and troubleshooting sub-intents at once.

### `SERP-variant-api`

Query: `gemini image api`

Observed result mix:

- Official Google Gemini API docs.
- Google AI Studio / Vertex AI references.
- LaoZhang/docs and blog pages covering Nano Banana, Nano Banana Pro, Nano Banana2, image endpoint setup, code examples, and gateway routes.
- Third-party API guide pages with price and route claims.

Implication:

- This is the strongest business-fit branch for `docs.laozhang.ai` and `laozhang.ai`: users are closer to implementation and need exact model IDs, endpoint format, price, and route choice.

### `SERP-variant-pricing`

Query: `gemini image pricing`

Observed result mix:

- Official Google pricing pages.
- Third-party pricing guides comparing Gemini 2.5 Flash Image, Gemini 3 Pro Image, Gemini 3.1 Flash Image, Imagen, and OpenAI image models.
- LaoZhang network already has multiple price-specific pages, including Gemini 3 Pro Image API cost and Gemini 3.1 Flash Image pricing pages.

Implication:

- Pricing is commercially valuable but cannibalization risk is high. Existing pages should be refreshed and internally routed before new pages are created.

### `SERP-variant-tutorial`

Query: `gemini image tutorial`

Observed result mix:

- How-to guides for Gemini App and Google AI Studio.
- API tutorials using Python, Node.js, REST/cURL, and n8n/ComfyUI workflows.
- Prompt-tutorial content for portraits, product images, editing, and viral templates.

Implication:

- Tutorial intent should be split by route: consumer app and prompts fit `yingtu.ai`; API implementation fits `blog.laozhang.ai`; reference docs and endpoint examples fit `docs.laozhang.ai`.

### `SERP-variant-vs`

Queries:

- `gemini image vs chatgpt image generation comparison 2026`
- `gemini image vs midjourney 2026`

Observed result mix:

- Comparison guides around Gemini/Nano Banana vs ChatGPT Images, Midjourney, Imagen, Flux, and Grok.
- Search terms often use consumer names while the actual product boundary is model specific.

Implication:

- Comparison pages need corrected comparator naming. Avoid a generic `Gemini Image vs X`; use `Gemini 3.1 Flash Image vs ChatGPT Images`, `Gemini 3 Pro Image vs Imagen 4`, etc.

### `SERP-variant-error-community`

Queries:

- `gemini image not working 429 503 reddit`
- `gemini image generation API GitHub issue 429 503`

Observed result mix:

- Google AI Developers Forum threads around quota, overload, safety, Lambda/deployment failures, and image-generation output errors.
- Reddit/community pages around 429/503 spikes and consumer-app generation failures.
- Existing LaoZhang/aifreeapi pages cover 429, 503, quota exceeded, permission denied, and common Gemini image errors.

Implication:

- Troubleshooting is a strong GEO citation angle because users ask long-form symptom questions. Existing pages already cover much of it; consolidation and refresh are more valuable than broad new pages.

### `SERP-zh`

Queries:

- `Gemini 图片生成 教程 Nano Banana 2`
- `Gemini 图片生成 API 价格 2026`
- `Gemini 图片生成 国内 使用 API 中转`
- `Gemini 图片生成 免费 次数 限制`

Observed result mix:

- Chinese/Taiwan wording uses `Gemini 图片生成`, `指令`, `次数`, `限制`, `中文字体`, `图片生成不出来`, `国内使用`, `API 中转`.
- Consumer-app and prompt intent is much stronger in Chinese autocomplete than pure developer API intent.
- `国内使用/API 中转` is commercially relevant for LaoZhang gateway content, but needs factual boundary around official Google route vs third-party route.

Implication:

- Chinese content should not simply translate `gemini image API`. It should split into `Gemini 图片生成怎么用`, `Gemini 图片生成次数/限制`, and `Gemini 图片生成 API 国内怎么接入`.

## Google Suggest Evidence

### `Suggest-en-root`

Root: `gemini image`

- `gemini image generation`
- `gemini image to video`
- `gemini image editor`
- `gemini image creator`
- `gemini image prompt`
- `gemini image ai`
- `gemini image creation`
- `gemini imagenes`
- `gemini image editing`
- `gemini image generator prompt`
- `gemini image generator ai`
- `gemini image generation limit`
- `gemini image watermark remover`
- `gemini image gen`
- `gemini image search`

### `Suggest-en-api-pricing-free`

Root: `gemini image api`

- `gemini image api pricing`
- `gemini image api key`
- `gemini image api free`
- `gemini image api docs`
- `gemini image api models`
- `gemini image api url`
- `gemini image api documentation`
- `gemini image api python`
- `gemini image api call`
- `gemini image api n8n`
- `gemini image api endpoint`
- `gemini image api base url`
- `gemini api image generation`
- `gemini api image input`
- `gemini api image upload`

Root: `gemini image pricing`

- `gemini image pricing api`
- `gemini pricing image generation`
- `gemini pricing image input`
- `gemini image costs`
- `gemini flash image pricing`
- `gemini image gen pricing`
- `gemini image model pricing`
- `gemini pro image pricing`
- `gemini 3 image pricing`
- `gemini 2.5 image pricing`
- `google gemini image pricing`
- `gemini ai image pricing`
- `gemini image understanding pricing`
- `gemini image token pricing`
- `gemini image analysis pricing`

Root: `gemini image free`

- `gemini image free online`
- `gemini image free download`
- `gemini image free limit`
- `gemini image free api`
- `gemini image free tier`
- `gemini image free prompt`
- `gemini free image generator`
- `gemini free image generation limit`
- `gemini free image editor`
- `gemini free image upload limit`
- `gemini free image generator api`
- `gemini free image creation limit`
- `gemini free image generation model`

### `Suggest-en-tutorial-vs-prompt-error`

Root: `gemini image tutorial`

- `gemini image guide`
- `gemini image generation tutorial`
- `gemini ai image tutorial`
- `gemini image prompt tutorial`
- `gemini 2.5 flash image tutorial`
- `gemini image generation api tutorial`
- `gemini ai image editing tutorial`
- `google gemini image generation tutorial`

Root: `gemini image vs`

- `gemini image vs chatgpt`
- `nano banana vs gemini image`
- `gemini image vs imagen`
- `gemini images vs sora`
- `gemini vs image fx`
- `gemini image generation vs chatgpt`
- `gemini image generation vs midjourney`
- `gemini image generation vs imagen`

Root: `gemini image edit`

- `gemini image editing`
- `gemini image editing request denied`
- `gemini image editing not supported`
- `gemini image editor`
- `gemini image editor free`
- `gemini image edit prompt`
- `gemini image editor online`
- `gemini image editing api`
- `gemini image editing pricing`

Root: `gemini image not working`

- `gemini image generator not working`
- `gemini image upload not working`
- `gemini image editing not working`
- `gemini image creation not working`
- `gemini image generator not working reddit`
- `gemini image download not working`

Root: `gemini image rate limit`

- `gemini image generation rate limit`
- `gemini flash image rate limit`
- `gemini 2.5 flash image rate limit`
- `gemini-3-pro-image rate limit`
- `gemini 3 pro image preview rate limit`
- `gemini increase limits`

### `Suggest-zh`

Root: `gemini 图片`

- `gemini 图片跑不出来`
- `gemini 图片 浮水印`
- `gemini 图片生成指令`
- `gemini 图片指令`
- `gemini 图片上限`
- `gemini 图片解析度`
- `gemini 图片转影片`
- `gemini 图片去浮水印`
- `gemini 图片无法生成`
- `gemini 图片去背`
- `gemini 图片 尺寸`
- `gemini 图片生成影片`
- `gemini 图片生成 没有图片`
- `gemini 图片翻译`

Root: `gemini 图片生成`

- `gemini 图片生成指令`
- `gemini 图片生成影片`
- `gemini 图片生成不出来`
- `gemini 图片生成上限`
- `gemini 图片生成 没有图片`
- `gemini图片生成失败`
- `gemini 图片生成 教学`
- `gemini 图片生成次数`
- `gemini 图片生成 中文字`
- `gemini 图片生成 prompt`
- `gemini 图片生成额度`
- `gemini 图片生成风格`
- `gemini 图片生成咒语`
- `gemini 图片生成提示词`
- `gemini 图片生成 限制`

## Community And Problem Evidence

### `Community-forum`

Source examples:

- Google AI Developers Forum threads surfaced in search around Gemini image 503/429, AWS Lambda failures, `IMAGE_OTHER`, permission errors, and quota exhaustion.
- Reddit results surfaced for `gemini image not working`, `gemini 3 image API spamming 503 and 429`, and Gemini image generator behavior.

Recurring user problems:

- API route mismatch: Gemini Developer API vs Vertex AI vs third-party OpenAI-compatible gateway.
- Model-name mismatch: `nano banana`, `Nano Banana Pro`, `Gemini 3 Pro Image`, `Gemini 3.1 Flash Image`, `Imagen 4`.
- Quota/rate-limit confusion: free tier, paid tier, project tier, consumer app limits.
- Runtime errors: 429, 403, 503, safety refusal, no image returned, upload/download failures.
- Prompt/use-case questions: image editing, people restrictions, text rendering, Chinese text, 4K output, image-to-video.

## Owned-Asset Evidence

### `Owned-docs-laozhang`

Local repo: `/Users/laozhang/Projects/docs`

Relevant current pages:

- `api-capabilities/nano-banana-image.mdx`: Chinese Nano Banana text-to-image page. SEO title targets `Gemini 2.5 Flash 图像生成 API`.
- `api-capabilities/nano-banana-pro-image.mdx`: Chinese Nano Banana Pro page. Claims Gemini 3 Pro image generation, 4K, LaoZhang price.
- `api-capabilities/nano-banana2-image.mdx`: Chinese Nano Banana2 page. Claims Gemini 3.1 Flash, text-to-image plus image editing, 4K.
- `en/api-capabilities/nano-banana-image.mdx`: English Nano Banana page, includes migration notice.
- `en/api-capabilities/nano-banana-pro-image.mdx`: English Nano Banana Pro page.
- `en/api-capabilities/nano-banana2-image.mdx`: English Nano Banana2 page.
- `en/api-capabilities/gemini-flash-image.mdx`: English page titled `Nano Banana 2 API Image Generation`, but frontmatter/body still map Nano Banana 2 to `gemini-3-pro-image-preview`. This conflicts with the current owned `nano-banana2-image` page and current official model naming.
- `en/api-capabilities/gemini-flash-image-edit.mdx`: English editing page also maps Nano Banana 2 to `gemini-3-pro-image-preview`.
- `docs.json`: navigation already has groups for Nano Banana Standard, Nano Banana2, and Nano Banana Pro in both Chinese and English.
- `public/sitemap.xml`: includes a high-priority Nano Banana 2 image-generation page.

Key drift:

- The docs site has correct newer Nano Banana2 pages, but older `gemini-flash-image*` English pages still risk telling search users the wrong model boundary.

### `Owned-blog-laozhang`

Local repo: `/Users/laozhang/Projects/blog-laozhang`

Scan result:

- Thousands of hits around Gemini image/Nano Banana content.
- Representative pages include:
  - `data/posts/en/gemini-image-generation-complete-guide/...`
  - `data/posts/en/gemini-image-api-guide-2026/...`
  - `data/posts/en/gemini-image-model-comparison/...`
  - `data/posts/en/gemini-3-1-flash-image-preview/...`
  - `data/posts/en/gemini-3-pro-image-api-pricing/...`
  - `data/posts/en/gemini-image-429-rate-limit/...`
  - `data/posts/en/gemini-image-common-errors-fix/...`
  - `data/posts/en/gemini-flash-image-comfyui-integration-tutorial/...`
  - `data/posts/en/gemini-flash-image-vs-gpt-image-vs-flux/...`

Implication:

- `blog.laozhang.ai` already owns many developer/tutorial/comparison/troubleshooting branches. A new generic `gemini image` blog post is likely cannibalistic unless it is a hub refresh or a very narrow missing branch.

### `Owned-aifreeapi`

Local repo: `/Users/laozhang/Projects/blog`

Scan result:

- Strong existing coverage around free/cheap/limits:
  - `data/md/zh/gemini-image-generation-limits.mdx`
  - `data/posts/en/gemini-3-1-flash-image-preview-api-free/...`
  - `data/posts/en/gemini-image-generation-error-429-fix/...`
  - `data/posts/en/google-gemini-api-free-tier/...`
  - `data/posts/en/gemini-3-pro-image-preview-pricing/...`
  - `data/posts/en/gemini-3-pro-image-preview-cost-per-image/...`

Implication:

- `aifreeapi.com` should keep the free/cheap/quota branch. It should not duplicate docs/product route pages.

### `Owned-yingtu`

Local repo: `/Users/laozhang/Projects/yingtuai`

Scan result:

- Model selector currently has:
  - `nano-banana` => `gemini-2.5-flash-image`
  - `nano-banana-2` => `gemini-3.1-flash-image-preview`
  - `nano-banana-pro-legacy` => `gemini-3-pro-image-preview`
- `DEFAULT_MODEL = MODELS[1]`, Nano Banana 2.
- Blog/content hits include prompt, API, pricing, quota, and Nano Banana Pro access clusters.

Implication:

- `yingtu.ai` is the best fit for online image-generation, prompt, template, visual examples, and consumer route content.

## Source URL Index

Official:

- https://ai.google.dev/gemini-api/docs/image-generation
- https://ai.google.dev/pricing
- https://ai.google.dev/gemini-api/docs/rate-limits
- https://support.google.com/gemini/answer/16275805?hl=en&ref_topic=13194540
- https://cloud.google.com/vertex-ai/generative-ai/docs/image/overview
- https://cloud.google.com/vertex-ai/generative-ai/pricing

Search and Suggest:

- https://suggestqueries.google.com/complete/search?client=chrome&hl=en&q=gemini%20image
- https://suggestqueries.google.com/complete/search?client=chrome&hl=en&q=gemini%20image%20api
- https://suggestqueries.google.com/complete/search?client=chrome&hl=en&q=gemini%20image%20pricing
- https://suggestqueries.google.com/complete/search?client=chrome&hl=en&q=gemini%20image%20free
- https://suggestqueries.google.com/complete/search?client=chrome&hl=en&q=gemini%20image%20tutorial
- https://suggestqueries.google.com/complete/search?client=chrome&hl=en&q=gemini%20image%20vs
- https://suggestqueries.google.com/complete/search?client=chrome&hl=zh-CN&q=gemini%20%E5%9B%BE%E7%89%87
- https://suggestqueries.google.com/complete/search?client=chrome&hl=zh-CN&q=gemini%20%E5%9B%BE%E7%89%87%E7%94%9F%E6%88%90

Owned local files:

- `/Users/laozhang/Projects/docs/api-capabilities/nano-banana-image.mdx`
- `/Users/laozhang/Projects/docs/api-capabilities/nano-banana-pro-image.mdx`
- `/Users/laozhang/Projects/docs/api-capabilities/nano-banana2-image.mdx`
- `/Users/laozhang/Projects/docs/en/api-capabilities/gemini-flash-image.mdx`
- `/Users/laozhang/Projects/docs/en/api-capabilities/gemini-flash-image-edit.mdx`
- `/Users/laozhang/Projects/docs/docs.json`
- `/Users/laozhang/Projects/docs/public/sitemap.xml`
- `/Users/laozhang/Projects/yingtuai/src/lib/models.ts`

