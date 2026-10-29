# Design system — Work + Quilted Health

Extends Vinta's updated identity (homepage, AI Fast-track, Building Blocks). Full rationale in T09 (Log #1). All tokens live in `:root` of `src/site-template.html`.

## Principles
1. Healthcare first, breadth visible. 2. Evidence beside the claim (Delivered / In progress / Planned always in words). 3. Hierarchy by scale, space and color. 4. Strongest color accent reserved for the final CTA. 5. Motion explains or answers, and stops with reduced motion.

## Color
| Token | Hex | Role |
|---|---|---|
| `--blue-600` | #0050FF | Primary buttons, links, selected states, key words |
| `--blue-700` | #0040CC | Hover, focus ring |
| `--ink-900` | #050842 | Headings, deep-blue sections |
| `--ink-700` | #33415F | Body text |
| `--label-500` | #465A78 | Labels, captions |
| `--surface` / `--white` | #FDFDFE / #FFF | Page / cards |
| `--tint-050` / `--tint-100` | #EEF3FF / #DCE7FF | Soft panels, pills |
| `--cyan-600` | #0893B3 | Gradient accent (large text/graphics only) |
| `--grad` | #186DFF → #0893B3 | One part of a heading, big numbers |
| Status | #0B5B3C/#E3F3EC · #6B4A00/#FFF3D6 · #465A78/#EEF1F7 | Delivered · In progress · Planned |

Contrast checked to WCAG AA (body ≥ 4.5:1). Focus: 3px `--blue-700` ring with 2px white offset; white ring on dark.

## Typography
Inter 300/400/500/600 (self-hosted). Display `clamp(40px,5.6cqi,82px)` 300 −0.045em · H2 `clamp(31px,3.7cqi,53px)` 300 · H3 20–24px · Lead 17–19px · Body 16px/1.55 · Small 13.5px · Label 12px 600 uppercase 0.1em. Key words in **500** and/or blue; one gradient fragment per heading.

## Spacing, radius, elevation, motion
Spacing 4px base (4–80px), sections `clamp(64px,8cqi,120px)` top. Container 1180px, gutter `clamp(20px,3vw,40px)`. Radius 10 (controls) · 14 · 20 (cards) · 28 (bands) · pill. Shadows: hover, float, chip (navy-tinted). Motion: 300ms fast, 600ms base, `cubic-bezier(.2,.8,.2,1)`, transform/opacity only, all disabled under `prefers-reduced-motion`. Layout uses **container queries** (1023px / 767px).

## Components (shared)
Header with nav capsule · Primary/secondary buttons · Action button (`.abtn`) · "Read the case" button (`.rbtn`) · Tag · Status label · Sector label · Fact chip · Image frame with fixed ratio · Project cover (photo + navy overlay + logo bottom-left) · Project card · Quote card · Stats strip (icon + gradient number) · Deep-blue panel · Booking CTA (`.cta3`) · Footer.

### Action button (`.abtn`)
The one secondary action style for in-page links ("Explore all our services", "See our Building Blocks", "Talk to us about your care model", "← Back to all work").
- Pill, `min-height:44px`, 15px/500 text, 1px `--line-200` border on white, label + 28px arrow circle (`.ra`, blue-600 fill, white arrow, `aria-hidden`).
- Hover: border and text go blue-600, arrow moves 3px; transform only.
- `.abtn.dk` on deep-blue panels (white 12% fill, white text, white ring on focus). `.abtn.back` puts the arrow first and points left.
- Always its own line (never inline inside a sentence), so the tap target stays 44 px tall.

### "Read the case" button (`.rbtn`)
Same shape and arrow as `.abtn`; sits at the bottom of every project card (`.card .bd` is a flex column, `.rbtn{margin-top:auto}`), so buttons align across a row. Accessible name keeps the visible words first: "Read the case: Quilted Health" (client name in `.sr`).

### Booking CTA (`.cta3`)
Closing block on both pages. Two columns on desktop, stacked under 1023px.
- Left (deep blue gradient): eyebrow "Let’s talk", H2 "Book a 30-minute call" (cyan fragment), one bold page-specific line (Work: "Tell us about your care model."; Quilted: "Planning a rebuild or migration?"), body, and a chip "30 min · A conversation with our team".
- Right (white card): "What happens next", three numbered steps, full-width primary button "Let’s talk →" and the note "Opens our contact page to book the call."
- No calendar widget, dates or time slots: there is no public scheduling link, so the button goes to vintasoftware.com/contact. Swap the `href` when a booking link exists.

### Sector label (`.sector`)
12px/600 blue-600 label above quote attributions and CEO cards, format "Industry · Client" ("Healthcare · Quilted Health", "Edtech · PlusPlus"). Healthcare quotes come first.

### Focus, targets, contrast
- Focus: `box-shadow:0 0 0 2px #fff,0 0 0 5px #0040CC` on light surfaces; white 3 px ring on blue/dark surfaces (`.dark`, `.svc-panel`, `.cta3-l`, timeline).
- Every link and button is at least 44 × 44 px (chips, header button, tabs, segmented control, slider buttons included).
- Dimmed states use color, not opacity (patch column: `--label-500` text on `#F4F6FA`, dashed border; unlit timeline items keep full-opacity text and dim only the border/background), so text stays AA.

### Motion and progressive enhancement
- An inline head script adds `.js` to `<html>`; hidden-until-revealed styles only apply under `.js`. If the main script does not finish within 2.5 s (`window.__vok`), the class is removed and everything is shown.
- Anything that animates in has its space reserved (gallery `min-height`), so CLS stays 0.
- `prefers-reduced-motion: reduce` shows final states (reveals, services map, timeline) with no transitions.

## Work-specific
Hero pill with screen-reader separators · Project gallery (drag/arrows below the row, short specialty tag at the bottom, all 32) · Group segmented control + sub-filter chips + challenge pill disclosure (`#chBtn` toggles a chip row with counts, `aria-expanded`/`aria-pressed`, state in URL) · Tag note under the chips · Count "Showing 9 of N projects" while collapsed · Services stepper (horizontal on desktop, vertical list under 767px) · Building Blocks tabs (one row of five on desktop, one scroll row with snap below 1023px) with a "Planned in discovery" status · Client quote carousel · CEO portrait cards.

## Quilted-specific
Hero with tool-icon orbit · Key facts strip (neutral ink for "Medplum" and "In progress") · At a glance band (`section` with H2 + `dl` of 7 pairs) · Video on click · Care-model two-column panel · 63% statistic with source · Patch/rebuild toggle · Why Medplum cards (text always visible, icon tile on top) · Delivery timeline (deep blue, scroll-lit) · Before/after slider · Record cards by status · Transferable patterns · Services map (line draws in, cards rise in sequence, chips follow; hover lifts 6px).
