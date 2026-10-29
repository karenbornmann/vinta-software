# Performance: before × after

## Before — current vintasoftware.com pages
PageSpeed Insights (Lighthouse 13.5, Chrome 153), 3 runs per profile, 28 Oct 2026. Median (range).

| Page | Mobile perf. | Mobile LCP | Desktop perf. | Desktop LCP |
|---|---|---|---|---|
| /work | 64 (60–64) | 8.7 s (8.7–9.2) | 87 (81–87) | 1.5 s (1.3–1.9) |
| /work/quilted-health | 55 (50–57) | 11.4 s | 73 (63–74) | 2.2 s (2.1–2.7) |

## After — production build (dist/)
Lighthouse 12.8.2 CLI, default mobile and desktop presets (simulated throttling), headless Chromium, local static server **without compression**, 3 runs per profile, 29 Oct 2026. Variation between runs: 0 points.

| Page | Mobile perf. | Mobile LCP | Desktop perf. | Desktop LCP | TBT | CLS | Transfer (mobile) |
|---|---|---|---|---|---|---|---|
| /work/ | 98 | 2.1 s | 100 | 0.8 s | 0 ms | 0.000 | 424 KB |
| /work/quilted-health/ | 93 | 3.1 s | 100 | 0.6 s | 0 ms | 0.001 | 381 KB |

Accessibility 98 / 95, Best practices 96. SEO 66 is expected: pages are intentionally `noindex` (duplicate of the live site).

## Conditions and limits — read before comparing
- Different tool versions and environments (PSI remote vs. local CLI). The fair comparison is PageSpeed Insights on the Netlify URLs with the same 3-run protocol; record it here after deploy.
- Locally, third-party requests (Vinta CDN logos/screens, YouTube thumbnail) were blocked by the sandbox network, so they are not counted: after-numbers are optimistic for those items. Netlify adds gzip/brotli, which the local server did not.
- These are lab results. They do not measure conversion or commercial impact.

## What changed to get there
Self-hosted Inter with preload (no render-blocking Google Fonts), WebP images sized for their slot with fixed aspect ratios (no layout shift), lazy loading below the fold, one page per route with only its own script, no framework or third-party scripts (no Webflow runtime, no Calendly embed), YouTube/demo video only loaded on click.

## Single-file review preview (for reference)
The review file embeds all images as base64 (1.7 MB) and scored 56 mobile / LCP 11.0 s — a review format, not what is deployed.
