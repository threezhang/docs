---
name: docs-seo-research
description: "Run Codex-native SEO/GEO keyword research for the LaoZhang site network. Use when the user asks for /seo-style keyword research, search intent analysis, SERP opportunity evaluation, GEO/content planning, site allocation across laozhang.ai, blog.laozhang.ai, aifreeapi.com, and yingtu.ai, or migration of the legacy .claude/commands/seo.md workflow."
---

# Docs SEO Research

Use this skill to turn a seed keyword into an evidence-led SEO/GEO opportunity report.

The legacy `.claude/commands/seo.md` logic is preserved, but the execution model is Codex-native:

- live search evidence first
- Computer Use live-browser SERP capture first, explicit blocker/fallback when blocked
- batched web search instead of Claude sub-agent assumptions
- Google Suggest API fetched directly
- owned-asset scan across the four-site network
- a durable report artifact by default

## Default Output

Unless the user asks for chat-only output, write the result under:

```text
.codex/reports/seo/{YYYY-MM-DD}-{keyword-slug}/
```

Use this file layout:

- `01-evidence.md`: raw evidence, capture methods, source URLs, volatile facts, and owned-asset findings
- `02-report.md`: final Chinese SEO/GEO report using `references/report-template.md`

In the final chat response, give the verdict, the recommended first action, and the artifact paths.

## Inputs

Minimum input:

- seed keyword

Optional inputs:

- target locale or language
- target site preference
- whether the user wants a full report or a quick triage
- whether external search should be skipped

If the keyword is English, keep the keyword and English variants in English. Write analysis and recommendations in Chinese unless the user asks otherwise.

## Site Network Rules

Route opportunities by business fit before writing article ideas:

| Site | Role | Default Fit |
| --- | --- | --- |
| `laozhang.ai` | AI API gateway main site | product, docs, pricing, gateway route, account or console pages |
| `blog.laozhang.ai` | AI API technical blog | API tutorials, model comparisons, benchmarks, developer practice |
| `aifreeapi.com` | free and cheap AI API resource site | free tier, quota, cheap API, low-cost routes, savings |
| `yingtu.ai` | AI image generation tool and image-content site | image generation, image editing, image model reviews, prompts |

Use existing coverage first. If one site already owns the topic, recommend optimizing that page before creating a duplicate on another site.

## Tool Mapping

Map the old Claude workflow to Codex tools as follows:

| Legacy step | Codex-native implementation |
| --- | --- |
| Claude in Chrome SERP capture | Use Computer Use to control a real browser and capture Google SERP structure. This is the primary path, not an optional enhancement. |
| WebSearch agents | After Computer Use captures the high-value SERPs, use batched `web.search_query` calls for breadth and fallback coverage. Spawn sub-agents only when the user explicitly authorizes parallel agents. |
| WebFetch Google Suggest | Fetch `https://suggestqueries.google.com/complete/search?...&client=chrome` with shell, JS, or browser fetch. |
| Google Trends | Use Computer Use to open and inspect Google Trends first. If blocked or unreadable, search for trend descriptions and mark as fallback. |
| Owned-asset scan | Combine Google `site:` searches with local repo scans such as `docs.json`, `public/sitemap.xml`, `llms.txt`, and MDX frontmatter when the relevant repo is local. |

Do not claim a clean Google SERP capture unless the Computer Use browser capture actually happened. If Google blocks, say what blocked and what fallback data was used.

## Computer Use SERP Contract

For a full report, use Computer Use before text-only search for:

- the seed keyword Google SERP
- 3-4 critical English variants: `vs`, `API`, `pricing` or `cost`, `tutorial` or `how to use`
- 1-2 high-value Chinese variants selected from early evidence
- Google Trends for the seed keyword

For each browser capture, record:

- exact query, locale, and URL
- capture time
- browser title and final browser URL
- whether the result page was clean, blocked, partial, or degraded
- visible top results, snippets, PAA, related searches, ads, videos/images/news, and other feature blocks
- screenshot path or equivalent browser evidence when available

Allowed fallback reasons:

- Google CAPTCHA, `sorry` page, or bot challenge
- page loads but result structure cannot be read
- Trends graph or related queries are not extractable
- Computer Use tool is unavailable in the current environment

When falling back, keep the fallback explicit in `01-evidence.md`; do not blend browser and text-search evidence as if they had the same strength.

## Workflow

### 1. Start The Run

Record in `01-evidence.md`:

- seed keyword
- run date and timezone
- target locale
- exact search queries used
- Computer Use capture methods, evidence, and blockers
- all source URLs used for claims

Normalize a `keyword-slug` for the artifact path, but do not normalize the keyword in the report title if the market uses the noisy or English form.

### 2. Collect Evidence

Collect evidence before strategy. Do not draft conclusions from memory.

Minimum evidence set for a full report:

- Main SERP for the seed keyword, captured with Computer Use unless blocked: top 10 results, domain types, snippets, SERP features, PAA, related searches, ads if visible.
- Critical variant SERPs, captured with Computer Use unless blocked: `{keyword} vs`, `{keyword} API`, `{keyword} pricing` or `{keyword} cost`, `{keyword} tutorial` or `{keyword} how to use`.
- Broader variant searches: free, free tier, subscription, alternative, SDK, integration, rate limit, review, benchmark, error, not working, latest, changelog, current year.
- Chinese variant searches: 教程, 怎么用, 国内使用, 国内访问, API 中转, 免费, 价格, 对比, 替代方案, 最新.
- Google Suggest data for the full keyword, short roots, English modifiers, a-z expansions, and Chinese suggestions.
- Competitor discovery from search results, then freshness verification for competitor names and versions.
- Community evidence from Reddit, GitHub issues, Stack Overflow, forums, or equivalent user-problem sources.
- Owned-asset scan across `laozhang.ai`, `blog.laozhang.ai`, `aifreeapi.com`, and `yingtu.ai`.
- Google Trends signal from Computer Use, or a clearly marked fallback if Trends cannot be read.

For AI models, pricing, limits, availability, and competitor relationships, use current sources. Do not rely on training knowledge.

### 3. Analyze

Convert evidence into decisions in this order:

1. Timeliness check: verify model/product names, versions, pricing, limits, and competitor status. Mark unverified or stale claims.
2. Keyword merge: combine Suggest, PAA, related searches, title reverse-extraction, competitor coverage, community questions, owned assets, and Trends queries.
3. Clustering: core, commercial, scenario, comparison, alternative, tutorial, API/developer, review, question, and programmatic/template terms.
4. Opportunity tiering: `优先做`, `可做但不优先`, `不建议做`. A full report should include at least 30 total keywords, at least 10 priority keywords, and at least 5 rejected keywords unless the evidence is too sparse.
5. SERP preference: summarize page types, domain mix, result title patterns, snippets, special elements, ads, and content formats Google appears to reward.
6. Content gap: identify what current winners repeat, what they do not answer, and which community pain points remain under-served.
7. Business fit: classify each worthwhile angle as direct conversion, indirect conversion, brand support, GEO citation, or not relevant.
8. Site allocation: assign every `优先做` and `可做但不优先` keyword to one recommended site.

Every material judgment in `02-report.md` must point back to specific evidence in `01-evidence.md`.

### 4. Write The Report

Use `references/report-template.md` for the final report structure.

Keep the report direct and decision-heavy:

- conclusion first
- explicit site recommendation
- clear tradeoffs
- no inflated scores
- no generic SEO filler
- no unsupported price/model/version claims

Preserve raw appendices for:

- autocomplete results
- reverse-extracted title terms
- competitor coverage
- community questions
- owned assets
- Trends data or fallback

### 5. Quality Gate

Before finishing, check:

- `01-evidence.md` exists and contains capture methods, source URLs, and blockers/fallbacks.
- Main Google SERP evidence comes from Computer Use, or the report states a concrete blocker and fallback.
- `02-report.md` includes all required sections from the template.
- Every priority and secondary keyword has a recommended site.
- Site allocation follows the network rules and avoids cross-site cannibalization.
- All volatile facts have current evidence or a visible warning.
- The report contains a real no-go list, not only positive opportunities.
- The final content matrix has at least 5 article/page ideas for a full report.

If any requirement cannot be met, state the limitation in the report instead of filling the gap with guesses.
