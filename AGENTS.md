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

AAA is the active research project. Juniper Encoder and Juniper Math 1 are
retired historical research and must not be presented as active model projects
or as released models. Retired projects removed from active public surfaces
stay removed unless explicit new site policy reverses that decision.

AAA is the active public research project. Juniper LM 1 is retired historical
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
