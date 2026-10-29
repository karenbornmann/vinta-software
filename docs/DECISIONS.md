# Design decisions — Karen Bornmann

The decisions I made while redesigning /work and /work/quilted-health, in the order they came up in review. Each one says what I chose and why.

## Positioning and content
- **I lead with healthcare without hiding the rest.** The hero says "Software shaped around how you work. See what we’ve built." The lead names Vinta as a product and engineering partner and lets people explore by healthcare specialty, by industry or by the challenge we solved. Healthcare buyers see themselves first, and the other 21 projects are still one click away.
- **I don't invent data.** Every number, client name, status and quote comes from Vinta's published pages or the challenge material. Quotes stay word for word. Where a fact was missing, I left it out instead of filling the gap.
- **I keep status honest.** On Quilted, the proof of concept is delivered and the production build and migration are in progress. "Build for production" is shown as delivery work, not as a promise of a finished result. A roadmap item that only exists as a plan is labeled "Planned in discovery".
- **Tags are ours, and I say so.** Specialty, industry and challenge tags are our own classification of published projects, and a note under the filters says that.
- **Healthcare voices come first in proof.** The quote carousel starts with healthcare clients. Every quote and CEO card carries a sector label, so a reader knows which industry is speaking.

## Navigation and interaction
- **No automatic scrolling in the hero.** The gallery moves only when people drag it or use the arrows. Clicking a cover goes straight to that project.
- **Covers are thumbnails that put people first.** I made the covers smaller. Each crop keeps the people and the main action in frame, with the client logo in the corner, and no cut-off heads.
- **One filter bar, three ways in.** A group control (healthcare / other industries), sub-filter chips and a challenge pill that opens a chip row with counts. The filter state lives in the URL, so a filtered view can be shared.
- **The count tells the truth while collapsed.** It reads "Showing 9 of N projects" until someone opens the full list.
- **On mobile, the services stepper becomes a vertical list.** Five steps in a row don't fit in 360 px, and a vertical list is easier to read and tap.

## Visual system
- **One secondary button style.** "Read the case" felt too plain, so I asked for a refined button. That shape (pill, label, arrow circle) became the shared action button for every in-page link, including "← Back to all work".
- **One booking CTA on both pages.** "Book a 30-minute call", with a "What happens next" card. There is no public scheduling link, so I don't show fake dates or time slots: the button opens the contact page, and the note under it says so.
- **Color, not opacity, for dimmed states.** Faded text failed contrast, so the dimmed "Keep patching" column and the unlit timeline steps now dim through color and borders. Their text keeps AA contrast.
- **Why Medplum text is always visible.** Cards no longer hide their text behind hover. The icon is a small tile on top, and spacing keeps text clear of icons and borders.
- **Neutral color for neutral facts.** "Medplum" and "In progress" in the key facts use ink, not the blue gradient, so emphasis stays on the outcomes.

## Quality bar
- **Layout shift stays at zero.** Anything that animates in has its space reserved, and I check this with a slow-network test and Lighthouse mobile after every round.
- **Motion is optional.** With `prefers-reduced-motion` or without JavaScript, every section shows its final state.
- **Accessible by default.** WCAG AA contrast, a visible 3 px #0040CC focus ring (white on blue), and touch targets of at least 44 × 44 px.
- **Fast pages over effects.** Self-hosted fonts, sized WebP images, no third-party scripts, and video loaded only on click.
