# Project memory — Vinta challenge (Karen Bornmann)

Karen's practical challenge for Vinta's **Senior Marketing Web Designer (AI-Driven)** role: redesign and implement /work and /work/quilted-health with healthcare positioning.

## Working rules
- Reply to Karen in Brazilian Portuguese. Code, copy and docs stay in English.
- No invented data (clients, quotes, results, metrics, availability or time slots). Quotes stay word for word; flag missing evidence instead of filling it.
- Keep CLS at 0, respect `prefers-reduced-motion`, WCAG AA contrast, visible focus (3 px #0040CC ring on light, white on blue), touch targets ≥ 44 × 44 px.
- Source of truth is `src/site-template.html`; `python3 scripts/build.py` writes `dist/` (see README.md, docs/DESIGN-SYSTEM.md, docs/DECISIONS.md, docs/PERFORMANCE.md).

## Status (Nov 2026)
- **Submitted.** Everything is in one Google Drive folder, in EN and PT versions:
  - project ZIP;
  - the Netlify pages;
  - design system documentation;
  - AI logs: Log #1 is the Claude chat, Log #2 is this Claude Code session;
  - a presentation (diagnosis, design decisions, iterations, validation).
- **Published pages:**
  - Work: https://karenbornmann-vinta-challenge.netlify.app/work/
  - Quilted Health: https://karenbornmann-vinta-challenge.netlify.app/work/quilted-health/
- **Portfolio:** https://karenbornmann.vercel.app/
- **Next stage (approved):** a final interview with Vinta's Head of Growth and CEO.
  - Karen presents the delivery, then answers questions.
  - She must explain and defend her decision process, the reasoning behind her choices, and the trade-offs at each step.
  - The conversation may switch between English and Portuguese.

## The challenge brief (as received)

Senior Marketing Web Designer (AI-Driven)
Practical challenge · Website redesign with AI
About the challenge
Vinta is strengthening its positioning as a product and engineering partner for healthcare. We continue to build custom software for other markets, but healthcare should take a more prominent role in how we communicate our expertise.
Our Clients and case study pages serve two purposes: helping inbound leads understand who we work with and what we do, and supporting the sales pipeline with relevant examples and evidence. We want these pages to make the breadth of our healthcare experience easier to recognize, including our clients’ segments, profiles, and challenges.
The challenge
Vinta is evolving from a generalist custom software development company into a specialized product and engineering partner for healthcare.
Our goal is not simply to showcase more healthcare projects, but to demonstrate a deeper understanding of clinical workflows, care delivery models, and the technical challenges healthcare organizations face.
This evolution is reflected in our new homepage, our healthcare-focused services, and our Building Blocks approach, where we accelerate development by starting with proven, reusable healthcare software and tailoring it to each client's specific needs.
Our healthcare positioning spans a broad range of specialties, care models, and operational needs, including:

* Chronic Disease Management
* Weight & Metabolic Health
* Maternal & Prenatal Care
* Behavioral & Mental Health
* Wellness & Longevity
* Pediatric & Family Care
* Oncology & Cancer Care
* Dermatology
* Care Navigation & Clinic Operations
* Orthopedic Care

These audiences are an important part of our go-to-market strategy. We want prospective clients across these segments to recognize that Vinta understands their specific challenges and has the technical expertise to help address them.
We want our portfolio to support this positioning. Rather than simply displaying projects we've delivered, it should help potential clients understand what problems we're experienced in solving, where our expertise is strongest, and how that experience connects to what we offer today.
Your challenge is to redesign and implement new versions of two existing pages:

* Clients / Work: https://www.vintasoftware.com/work
* Quilted Health case study: https://www.vintasoftware.com/work/quilted-health

1. Clients / Work
Reimagine this page to reflect Vinta's healthcare specialization while preserving visibility into our broader custom software experience.
Consider how visitors can discover our work through different perspectives, including healthcare specialties, and the types of solutions we've delivered.
Our target audiences should inform your thinking about how the portfolio is organized and presented. The goal is to help prospective clients from these healthcare segments quickly recognize relevant experience, even when a project doesn't belong to their exact specialty but addresses similar workflows or technical challenges.
Our current services, including EHR Development & Modernization, Medplum Development, Healthcare Integration & Interoperability, and Fast-track Builds, should inform how you think about the relationship between our portfolio and what we offer today.
Our Building Blocks approach is also an important part of this positioning. Consider how our previous experience can reinforce the credibility behind this approach without implying that current Building Blocks were used in historical projects.

2. Quilted Health case study
Redesign this case study to communicate Vinta's healthcare expertise and the value of our contribution more effectively.
Make the client's care delivery context, the challenges they faced, Vinta's contribution, and the available evidence of impact easy to understand.
Consider how this story can demonstrate our ability to navigate complex healthcare requirements, work with clinical and technical stakeholders, and deliver solutions tailored to specific workflows.
Think about how the case study can resonate not only with organizations in maternal and prenatal care, but also with potential clients in other healthcare segments facing comparable challenges.
Prioritize concrete evidence over generic claims. Use the available project information to communicate the challenges, decisions, technical work, and outcomes without inventing results or overstating our contribution.
What we're looking for
We want to see how you translate business positioning, target audiences, and existing content into thoughtful, strategic design decisions.
Explore our new homepage, healthcare services, Building Blocks landing page, and target audiences to develop your own hypotheses about Vinta's strategic direction, going beyond simply understanding or applying our visual identity.
Think critically about how these two pages can strengthen our healthcare positioning, establish credibility, showcase our expertise, and connect relevant experience with the services we offer today.
You're encouraged to challenge the current information architecture, content hierarchy, navigation, and visual presentation. We expect you to articulate your interpretation of our healthcare strategy, explain how your design decisions support that interpretation, identify the problems you're trying to solve, and discuss the hypotheses and trade-offs behind your choices.

What you’ll do

* Analyze the current pages and the updated visual references. Explain what you would preserve, adapt, or improve, considering positioning, content, visual hierarchy, navigation, and performance.
* Consider using AI to analyze Vinta’s own website, identify opportunities, and compare alternatives. Review its recommendations critically and explain which you adopted or rejected and why.
* Use the updated pages, including the new homepage provided for this exercise, to guide your visual direction. Explain how your choices extend that identity and justify any departures.
* Define a basic design system covering typography, colors, spacing, and reusable components. Apply it consistently across both pages and document it in your preferred format.
* Use Claude Code to implement and refine both pages. You may use other tools to support research, exploration, asset creation, and validation. Make clear how each tool contributed.
* Deliver working, responsive pages with attention to visual detail, accessibility, SEO, and loading performance. Check navigation, links, and any interactions you introduce.
* You may reorganize and edit the existing content to improve clarity. Preserve factual accuracy; do not invent clients, testimonials, project results, or metrics. Flag missing evidence rather than filling it with unsupported claims.
* Explain your design and performance hypotheses and how you checked them. Where you claim a technical improvement, include comparable measurements and their conditions. Distinguish measured results from expected commercial impact.
* Deploy the pages independently on [Netlify](https://www.netlify.com/), a platform that offers a free hosting tier. There will be no cost in deploying and hosting these pages. Use Claude Code and Netlify’s documentation to work through setup and deployment, and verify that all published pages are fully functional and publicly accessible.


What you’ll submit

* Project ZIP: include the source code, required assets, dependency information, and a README with instructions to install, run, and build the project. Include any known limitations and omit generated dependency folders and credentials.
* Published pages: provide working Netlify URLs for both pages so our team can review them online before the interview.
* Basic design system: include its documentation in the project or your presentation, showing the foundations and components used across the two pages.
* AI conversation logs: export the complete conversations used for this exercise, including prompts, responses, follow-ups, and iterations from Claude Code and any other conversational AI tools. Organize them for review and remove credentials or unrelated private information, noting any redactions.
* Presentation: use the format you prefer, such as slides, a document, or a Claude artifact. Cover your diagnosis, hypotheses, visual references, design decisions, and workflow. Show how you guided and refined AI output, what you discarded, how you validated the pages.


What we’ll evaluate

* Strategic clarity: how clearly the pages establish healthcare as the priority, communicate the breadth of our experience, and support both inbound discovery and sales conversations.
* Visual judgment: typography, composition, hierarchy, spacing, responsiveness, and consistency with the updated Vinta identity.
* Content and reasoning: how well you organize information, present credible evidence, and connect your decisions to visitor needs and business goals.
* Use of AI: how effectively you direct the tools, evaluate their suggestions, and improve the output through your own judgment.
* Execution and ownership: the quality of the working pages, reuse of the basic design system, validation, deployment, and clarity of the handoff.

Practical details
The following pages reflect Vinta’s new visual identity and should serve as the primary design references for this exercise:

* Homepage: https://vinta-webdesign-challenge-homepage.netlify.app/homepage
* AI Fast-track: https://vinta-webdesign-challenge-fast-track.netlify.app/ai-fast-track/v1
* Building Blocks: https://www.vintasoftware.com/building-blocks

Use these pages to understand the visual language, design patterns, and overall direction of Vinta’s updated identity.
Keep the scope focused on the two pages and the shared foundations needed to build them. Document your assumptions, approximate time spent, and any work you would prioritize with more time.

Deadline and submission
You have 5 business days from receiving this challenge to submit your work. If you need more time to polish things up, just let us know before the deadline and we’ll be glad to discuss an extension.
To submit, reply to this email with the deliverables listed above, addressed to the Vinta hiring team (Diogo and Felipe).
Please also include links to your resume and portfolio in your reply.

Next steps
Our team will review the project, published pages, conversation logs, and presentation before deciding whether to invite you to the next interview.
If you move forward, you’ll present both pages and walk us through your decisions and workflow. Be ready to discuss how you used AI, why you chose your direction, how you validated the result, and what you would improve next.
