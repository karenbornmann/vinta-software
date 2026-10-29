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
Header with nav capsule · Primary/secondary buttons · "Read the case" pill button · Tag · Status label · Fact chip · Image frame with fixed ratio · Project cover (photo + navy overlay + logo bottom-left) · Project card · Quote card · Stats strip (icon + gradient number) · Deep-blue panel · CTA band with "What happens next" card · Footer.

## Work-specific
Project gallery (drag/arrows, all 32) · Group segmented control + sub-filter chips + challenge select (state in URL) · Services stepper (auto-advance, stacked layers) · Building Blocks tabs with "What we built in this area" card · Client quote carousel · CEO portrait cards.

## Quilted-specific
Hero with tool-icon orbit · At a glance axis (client ↔ Vinta) · Video on click · Care-model two-column panel · 63% statistic with source · Patch/rebuild toggle · Why Medplum reveal cards · Delivery timeline (deep blue, scroll-lit) · Before/after slider · Record cards by status · Transferable patterns · Services map.
