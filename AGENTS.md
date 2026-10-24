# Cinqic website instructions

Keep this site static, fast, accessible, and honest. Cinqic is a small software
and research company. Juniper is the flagship product, `/apps/` groups
Cinqic's software, `/research/` groups research, and `/privacy/` explains the
website and product-documentation boundaries. Keep `/juniper/`, `/calculator/`, and `/privacy/`
working as public routes.

GitHub is canonical for product facts. Active repositories live in the
`Cinqic-Research` organization; link there. Link to a retired research
repository only while it remains public. Before publishing copy, distinguish
current implementation, development candidates, published releases, research
targets, and retired work. Never claim a release, performance result,
availability, privacy guarantee, certification, partner, social account, or
download without current repository or release evidence. Do not advertise
uncommitted work from another repository.

AAA is Cinqic's current research program; its research is paused (see
below). Juniper Encoder and Juniper Math 1 are retired historical research and must not be presented as active model projects
or as released models. Retired projects removed from active public surfaces
stay removed unless explicit new site policy reverses that decision.

AAA is Cinqic's current public research program. Its research is temporarily
paused while Cinqic focuses on Juniper and its other software; it is not
retired, and its published results and limits stand as recorded. Do not
describe new AAA experiments as under way unless the owner resumes the
research. Juniper 1 Base is a released base model, separate from AAA and from
the Juniper app: its R&D closed on 2026-10-16 and it was published on
2026-10-17 (US Eastern). Juniper LM 1 is retired historical
research and may appear on `/research/` only as a concise summary of facts that
were already public. Do not link its private repository or publish private
repository contents. Other private research repositories, including Juniper
Reference 4B, are not described or linked without a separate publication
decision.

Cinqic Notes is not part of the site. Do not add it back to any page, route,
sitemap entry, or navigation unless site policy explicitly changes; the
verifier enforces this. Removing it from the site does not change the archived
repository's own status.

Use semantic HTML, keyboard-accessible interactions, visible focus states,
responsive layouts, and reduced-motion support. Do not add trackers, ads,
external fonts, cookies, secret material, fake contact details, or
dependency-heavy frameworks. Preserve `CNAME` exactly as `cinqic.com` and keep
GitHub Pages deployment files intact.

Run `python scripts/verify_site.py` after changes and
`python scripts/verify_release_links.py --include-android` when release links
or product copy change. Review all internal links and metadata before commit.

## Review roles

From 2026-10-24, by the owner's direction (the 2026-10-16 assignment named
Claude Fable 5.1 as reviewer):

- **Implementer: Claude Opus 5.5.** Builds, tests, and documents changes, and
  prepares the evidence. It may fix defects, but it never certifies its own
  work as independently reviewed.
- **Independent technical reviewer: GPT-6.1 Sol,** in a separate session
  with a fresh context. It reviews the exact head and the primary evidence
  itself, and may reject work, require changes, or withhold approval. If it
  authored, repaired, or directed the exact change, it says so and the change
  stays pending review.
- **Owner: Markus Gillyard.** Decides direction, funding, releases,
  irreversible operations, and policy exceptions. A technical approval is not
  owner authorization.

A named reviewer is an assignment, not evidence that a review took place;
only a recorded review of the exact head counts. Earlier reviews (Claude
Fable 5.1, GPT-6 Luna, GPT-6 and GPT-5.6 Sol, Codex) remain historical
records under their original attribution. This section does not change any
review gate.

Publication still needs the owner's decision. A technical review checks
factual accuracy, privacy, and accessibility against the actual releases.
