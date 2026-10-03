"""Dependency-free verification for the static Cinqic site."""

from html.parser import HTMLParser
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
PAGES = [
    ROOT / "index.html",
    ROOT / "juniper/index.html",
    ROOT / "apps/index.html",
    ROOT / "research/index.html",
    ROOT / "calculator/index.html",
    ROOT / "privacy/index.html",
    ROOT / "404.html",
]
REQUIRED = [
    ROOT / "CNAME",
    ROOT / "robots.txt",
    ROOT / "sitemap.xml",
    ROOT / "site.webmanifest",
    ROOT / "favicon.svg",
    ROOT / "assets/css/site.css",
    ROOT / "assets/js/company.js",
    ROOT / "assets/js/site.js",
    ROOT / "assets/img/cinqic-social.svg",
]
PUBLIC_ROUTES = [
    "/",
    "/juniper/",
    "/apps/",
    "/research/",
    "/calculator/",
    "/privacy/",
]
NAV_LINKS = ["/juniper/", "/apps/", "/research/", "/privacy/"]
CURRENT_MARKERS = {
    "juniper/index.html": 'href="/juniper/" aria-current="page"',
    "apps/index.html": 'href="/apps/" aria-current="page"',
    "research/index.html": 'href="/research/" aria-current="page"',
    "calculator/index.html": 'href="/apps/" aria-current="page"',
    "privacy/index.html": 'href="/privacy/" aria-current="page"',
}


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links: list[str] = []

    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if tag in {"a", "link", "script", "img"} and key in {"href", "src"} and value:
                self.links.append(value)


def fail(message: str) -> int:
    print(f"FAIL: {message}")
    return 1


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def check_internal_links(page: Path, text: str) -> str | None:
    parser = Links()
    parser.feed(text)
    for link in parser.links:
        if link.startswith(("https://", "http://", "mailto:", "tel:", "#", "data:")):
            continue
        path = link.split("#", 1)[0].split("?", 1)[0]
        if not path:
            continue
        target = ROOT / path.lstrip("/")
        if path == "/":
            target = ROOT / "index.html"
        elif path.endswith("/"):
            target = target / "index.html"
        if not target.is_file():
            return f"{relative(page)} -> {link}"
    return None


def main() -> int:
    for path in PAGES + REQUIRED:
        if not path.is_file():
            return fail(f"missing {relative(path)}")

    if (ROOT / "CNAME").read_text(encoding="utf-8").strip() != "cinqic.com":
        return fail("CNAME must be exactly cinqic.com")

    page_text = {relative(page): page.read_text(encoding="utf-8") for page in PAGES}
    text_assets = [
        ROOT / "CNAME",
        ROOT / "robots.txt",
        ROOT / "sitemap.xml",
        ROOT / "site.webmanifest",
        ROOT / "assets/css/site.css",
        ROOT / "assets/js/company.js",
        ROOT / "assets/js/site.js",
    ]
    public = "\n".join(page_text.values()) + "\n" + "\n".join(
        path.read_text(encoding="utf-8") for path in text_assets
    )

    forbidden = [
        "http://cinqic.com",
        "Planned launch:",
        "Juniper Baby",
        "Constitutional AI",
        "Juniper 120M",
        "19,863,936",
        "juniper-math-social.svg",
    ]
    retired_reference_terms = [
        " ".join(("Juniper", "Auto")),
        "-".join(("Juniper", "Auto")),
        "/" + "-".join(("juniper", "auto")) + "/",
        "https://github.com/" + "/".join(("Cinqic", "Juniper" + "-" + "Auto")),
        "".join(("juniper", "Auto")),
    ]
    for term in forbidden + retired_reference_terms:
        if term.lower() in public.lower():
            return fail(f"obsolete or insecure public text: {term}")

    # Cinqic Notes was removed from the site on 2026-09-30. Reintroducing it
    # requires an explicit site-policy change, not an accidental edit.
    for term in ["Cinqic Notes", "Cinqic-Notes", "/notes/"]:
        if term.lower() in public.lower():
            return fail(f"Cinqic Notes is not part of the site: {term}")
    if (ROOT / "notes").exists():
        return fail("the /notes/ route must not exist")

    # Private repositories are not published through the site.
    for term in [
        "Juniper-Reference-4B",
        "Juniper Reference 4B",
        "Juniper-LM-1.1",
        "Juniper LM 1.1",
    ]:
        if term.lower() in public.lower():
            return fail(f"private project referenced on the public site: {term}")

    # Active repositories live in Cinqic-Research; only archived historical
    # repositories that genuinely remain in the old organization may be linked there.
    historical_old_org = ("Juniper-Encoder", "juniper-math-1")
    for match in re.finditer(r"github\.com/Cinqic/([A-Za-z0-9._-]+)", public):
        if match.group(1) not in historical_old_org:
            return fail(f"stale organization link: {match.group(0)}")

    for route in PUBLIC_ROUTES:
        if route not in (ROOT / "sitemap.xml").read_text(encoding="utf-8"):
            return fail(f"missing sitemap route: {route}")

    for name, text in page_text.items():
        if "<title>" not in text or "<main" not in text:
            return fail(f"missing title or main: {name}")
        if 'name="description"' not in text:
            return fail(f"missing description metadata: {name}")
        if name != "404.html" and 'rel="canonical"' not in text:
            return fail(f"missing canonical metadata: {name}")
        if name != "404.html" and ('property="og:title"' not in text or 'property="og:description"' not in text):
            return fail(f"missing Open Graph metadata: {name}")
        if name != "404.html" and 'name="twitter:title"' not in text:
            return fail(f"missing Twitter metadata: {name}")
        if name != "404.html":
            canonical_start = text.find('rel="canonical"')
            canonical_end = text.find(">", canonical_start)
            canonical_tag = text[canonical_start:canonical_end]
            if "https://cinqic.com/" not in canonical_tag:
                return fail(f"canonical must use HTTPS Cinqic URL: {name}")
        for nav_link in NAV_LINKS:
            if f'href="{nav_link}"' not in text:
                return fail(f"missing shared nav link {nav_link}: {name}")
        if (problem := check_internal_links(ROOT / name, text)) is not None:
            return fail(f"broken internal link {problem}")

    for name, marker in CURRENT_MARKERS.items():
        if marker not in page_text[name]:
            return fail(f"missing aria-current marker: {name}")

    apps = page_text["apps/index.html"]
    required_apps = ["Juniper", "Cinqic Calculator"]
    positions = [apps.find(value) for value in required_apps]
    if any(position < 0 for position in positions):
        return fail("Apps page is missing an expected active application")
    if positions != sorted(positions):
        return fail("Apps page must feature Juniper before Calculator")
    if "flagship" not in page_text["index.html"].lower() or 'href="/juniper/"' not in page_text["index.html"]:
        return fail("homepage must keep Juniper represented as the flagship")
    research = page_text["research/index.html"]
    if "Current research" not in research or "https://github.com/Cinqic-Research/AAA" not in research:
        return fail("Research page must present AAA as current research")
    if "aaa.python.v1" not in research or "moving dot on a line and a three-parameter learner" in research:
        return fail("Research page must describe AAA's current Python phase, not the dot era as current")
    if "https://github.com/Cinqic-Research/Juniper-LM-1" not in research or "No Juniper LM 1 checkpoint has been trained or released" not in research:
        return fail("Research page must present Juniper LM 1 with its untrained status")
    if "remains a separate GPT-2 modernization research study" not in research:
        return fail("Research page must describe Juniper LM 1 as separate research")
    if "intended to become AAA" in research.lower():
        return fail("Research page contains the obsolete Juniper LM 1 to AAA plan")
    if "Retired research" not in research or "Juniper Encoder" not in research:
        return fail("Research page must present Juniper Encoder as retired research")
    if "Completed research" not in research or "Juniper Math 1" not in research:
        return fail("Research page must keep Juniper Math 1 as completed research")
    print("PASS: pages, metadata, navigation, routes, links, sitemap, flagship hierarchy, research status, and removed, private, and retired-project guardrails.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
