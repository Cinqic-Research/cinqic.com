# Content maintenance

## Source of truth

GitHub is canonical. Before changing public copy, fetch and inspect the
current `main` state of the relevant repository, then check its published
GitHub Releases and downloadable assets. Only merged or otherwise canonical
remote state may be advertised; do not copy another worker's uncommitted
implementation into release or availability language.

Keep these distinctions visible:

- current implementation on `main`;
- development or release-candidate versions;
- the latest actually published release;
- future plans and research targets;
- completed or retired work.

## Site structure

`index.html` is the Cinqic overview and keeps Juniper as the flagship.
`apps/index.html` is the software catalog (Juniper and Cinqic Calculator).
`research/index.html` summarizes current research (AAA, Juniper LM 1) and
completed research. `juniper/index.html` and
`calculator/index.html` hold detailed product information.
`privacy/index.html` describes website and product privacy boundaries.

Shared company facts and project metadata live in `assets/js/company.js`.
Keep it descriptive and small; do not turn it into a client-side content
management system or generate page copy from it. Shared menu behavior belongs
in `assets/js/site.js`.

## Release and product updates

When a release changes, update only the claims and pinned links supported by
the current GitHub Release. Keep independently versioned platform releases
independent, especially for Cinqic Calculator. For Juniper, separate the
current source candidate from the latest published prerelease; open pull
requests are not shipped behavior. For research, summarize the current phase
and its limits from the repository's own README and research log, and never
upgrade a result (for example, a development result to a confirmation, or a
plan to an implementation). Cinqic Notes is not presented on the site, and
private repositories are not linked or described.

## Metadata and verification

Every indexable page needs a title, description, canonical HTTPS URL, Open
Graph metadata, and Twitter metadata. Update `sitemap.xml` when adding a
public route. Do not add a route to the sitemap until its `index.html` exists.

Run:

```powershell
python scripts/verify_site.py
python scripts/verify_release_links.py --include-android
```

Also serve the root locally and inspect every public page at desktop and
narrow mobile widths. Confirm keyboard focus, mobile menu behavior, internal
links, images, and visible release boundaries before committing.
