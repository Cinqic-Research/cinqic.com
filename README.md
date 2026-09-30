# Cinqic.com

The official static website for Cinqic, a small software and research company.
The information architecture keeps Juniper as the flagship, groups standalone
software under Apps, and keeps the research record separate from product
routes.

## Stack and commands

Plain HTML, CSS, and minimal vanilla JavaScript. There are no package
dependencies or build step.

```powershell
python scripts/verify_site.py
python scripts/verify_release_links.py --include-android
python -m http.server 8000 --directory .
```

`verify_site.py` checks the local site structure, metadata, navigation, route
invariants, internal links, and durable content guardrails, and CI runs it on
every push and pull request. Release-link
verification depends on GitHub being reachable and checks every release URL
advertised in the HTML.

## Information architecture

- `/` — Cinqic overview, with Juniper as the flagship attraction.
- `/juniper/` — current Juniper implementation, published-release state, and
  platform limitations.
- `/apps/` — Juniper and Cinqic Calculator.
- `/research/` — AAA and Juniper LM 1 (current), and completed research.
- `/calculator/` — Cinqic Calculator downloads and product details.
- `/privacy/` — website and product-privacy boundaries.

## Maintenance

Shared company facts and current project metadata live in `assets/js/company.js`.
Shared navigation behavior lives in `assets/js/site.js`; pages remain authored
HTML rather than JavaScript-generated content. Shared design tokens and
responsive styling are in `assets/css/site.css`.

When updating product copy, inspect the canonical repository README, current
version sources, release documentation, and actual GitHub Releases. Keep
development candidates separate from published downloads, and do not invent
platform support, release dates, screenshots, integrations, or capabilities.

## Deployment

GitHub Pages serves `main` from the repository root. `CNAME` must remain exactly
`cinqic.com`. DNS, the Pages configuration, and the certificate are external to
the repository; verify the deployed URLs after a merge.
