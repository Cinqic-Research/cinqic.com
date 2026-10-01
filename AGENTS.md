# Cinqic website instructions

Keep this site static, fast, accessible, and honest. Cinqic is a small software
and research company. Juniper is the flagship product, `/apps/` groups
Cinqic's software, `/research/` groups research, and `/privacy/` explains the
website and product-documentation boundaries. Keep `/juniper/`, `/calculator/`, and `/privacy/`
working as public routes.

GitHub is canonical for product facts. Active repositories live in the
`Cinqic-Research` organization; link there. Retired projects keep links to the
archived repositories where they actually live. Before publishing copy, distinguish
current implementation, development candidates, published releases, research
targets, and retired work. Never claim a release, performance result,
availability, privacy guarantee, certification, partner, social account, or
download without current repository or release evidence. Do not advertise
uncommitted work from another repository.

AAA is the active research project. Juniper Encoder and Juniper Math 1 are
retired historical research and must not be presented as active model projects
or as released models. Retired projects removed from active public surfaces
stay removed unless explicit new site policy reverses that decision.

AAA and Juniper LM 1 are the current public research projects. Private
repositories, including Juniper Reference 4B, are not described or linked on
this site without a separate publication decision.

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
