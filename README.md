# Vinta · Work + Quilted Health redesign

Redesign of two pages for Vinta's web design challenge, positioning Vinta as a product and engineering partner for healthcare:

| Page | Route | Live |
|---|---|---|
| Clients / Work | `/work/` | https://karenbornmann-vinta-challenge.netlify.app/work/ |
| Quilted Health case study | `/work/quilted-health/` | https://karenbornmann-vinta-challenge.netlify.app/work/quilted-health/ |

`/` redirects to `/work/`. Unknown routes show `404.html`.

## Run locally

Requirements: **Python 3.9+** (standard library only). No Node packages are needed to build.

```bash
python3 scripts/build.py                          # builds dist/
python3 -m http.server 8080 --directory dist      # open http://localhost:8080/work/
```

or `npm run preview` (does both).

## Deploy (Netlify)

`netlify.toml` already sets `command = "python3 scripts/build.py"` and `publish = "dist"`.
In Netlify: **Add new site → Import an existing project → GitHub → this repository → Deploy**. Site name used: `karenbornmann-vinta-challenge`.

## Project structure

```
src/site-template.html   Reviewed single-file source (both pages, design tokens, components, data, JS)
scripts/build.py         Splits the source into two independent static pages for production
public/assets/img/       Optimized images (WebP), face-aware crops for project covers
public/assets/fonts/     Inter 300/400/500/600, self-hosted (SIL OFL, license included)
public/404.html          Not-found page
netlify.toml             Build, redirect and cache/robots headers
docs/DESIGN-SYSTEM.md    Foundations and components used on both pages
docs/PERFORMANCE.md      Before/after measurements and conditions
docs/ai-logs/            AI conversation logs (Log #1 Claude chat, Log #2 Claude Code)
docs/preview/            The single-file review preview used for design decisions (with review toolbar)
```

## Technical decisions

- **Static HTML/CSS/vanilla JS instead of Astro.** The R05 plan suggested Astro. The pages were designed and reviewed as one self-contained file (fast iteration with the reviewer), so the production build splits that reviewed source into two static pages with a dependency-free Python script. Output is plain pre-rendered HTML (content readable without JS except interactive widgets), no framework runtime. With more time: port components to Astro for maintainability.
- **One source, two pages.** Shared tokens, header, footer, cards and buttons live once in the source; each page receives only its own `<main>`, and page-specific JS runs only on its page.
- **Images:** generated/edited context photos (labelled illustrative), cropped around detected faces (OpenCV) so people stay in frame and the logo corner stays free. Product screens, client logos, portraits of Marko and the demo/testimonial videos load from Vinta's public CDN / YouTube / Cloudinary.
- **Fonts:** Inter self-hosted with preload (Moderat license not available; Inter is the homepage's declared fallback).
- **Indexing:** pages are `noindex` (meta + header) because they duplicate content from vintasoftware.com; this lowers the Lighthouse SEO score on purpose. Titles, descriptions, canonical, Open Graph, `lang`, one H1 per page are in place.

## Known limitations

- Assets loaded from third parties (Vinta CDN logos and screens, YouTube, Cloudinary demo) depend on those hosts.
- 16 of 32 projects have no published logo in the sources: the client name is shown in white text instead.
- Carlos Montes, Peter Thulson and Ben Yoon appear with initials (no approved portrait). Carlos's title is shown as "Quilted Health" only, because sources differ.
- Before/after slider assumes the two Quilted screens show comparable tasks (not confirmed).
- The 63% statistic is attributed to athenahealth as industry context; exact wording/date to re-check.
- "13 years" ages over time; confirm before any real publication.
- Image re-processing (crops/focal points) used Pillow + OpenCV in the authoring environment; the processed files are committed, so the build itself needs only Python.

## Time spent (approx.)

T10–T15 with Claude Code: ~7 h (setup and asset collection 1.5 h, preview v1 1.5 h, three review rounds 3 h, production build/QA/deploy 1 h). Planning, research, copy and design system (T01–T09): see Log #1.

## Next priorities with more time

Port to Astro components; responsive `srcset` for hero images (Quilted mobile LCP 3.1 s lab); real portraits for remaining quotes; confirm open content points above with Vinta; PageSpeed field data after a few days online.
