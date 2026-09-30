"""Verify the pinned GitHub release links used on the website are live.

This is deliberately separate from verify_site.py: local site structure
should always be checkable offline, but these checks depend on GitHub being
reachable and should not block normal local development.
"""

import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

DESKTOP_TAG = "v1.1.0"
ANDROID_TAG = "android-v1.1.0"
JUNIPER_TAG = "v0.3.0-rc.33"
JUNIPER_VERSION = JUNIPER_TAG.lstrip("v")

# Pinned to specific release tags, not /releases/latest/..., so publishing
# one platform's release can never break the other platform's download
# links (GitHub's "latest" always points at whichever tag was published
# most recently, regardless of which platform it's for). Windows and Linux
# now ship from one desktop tag, so they share DESKTOP_TAG.
RELEASE_URLS = [
    f"https://github.com/Cinqic-Research/Cinqic-Calculator/releases/download/{DESKTOP_TAG}/Cinqic-Calculator-Windows-x64-Setup.exe",
    f"https://github.com/Cinqic-Research/Cinqic-Calculator/releases/download/{DESKTOP_TAG}/Cinqic-Calculator-Windows-x64-Portable.zip",
    f"https://github.com/Cinqic-Research/Cinqic-Calculator/releases/download/{DESKTOP_TAG}/Cinqic-Calculator-Linux-x86_64.tar.gz",
    f"https://github.com/Cinqic-Research/Cinqic-Calculator/releases/download/{DESKTOP_TAG}/SHA256SUMS.txt",
    f"https://github.com/Cinqic-Research/Cinqic-Calculator/releases/tag/{DESKTOP_TAG}",
    "https://github.com/Cinqic-Research/Cinqic-Calculator",
    f"https://github.com/Cinqic-Research/Juniper-App/releases/tag/{JUNIPER_TAG}",
    f"https://github.com/Cinqic-Research/Juniper-App/releases/download/{JUNIPER_TAG}/Juniper-{JUNIPER_VERSION}-windows-x86_64.msi",
    f"https://github.com/Cinqic-Research/Juniper-App/releases/download/{JUNIPER_TAG}/Juniper-{JUNIPER_VERSION}-android-universal.apk",
    f"https://github.com/Cinqic-Research/Juniper-App/releases/download/{JUNIPER_TAG}/Juniper-{JUNIPER_VERSION}-linux-x86_64.AppImage",
    f"https://github.com/Cinqic-Research/Juniper-App/releases/download/{JUNIPER_TAG}/Juniper-{JUNIPER_VERSION}-linux-x86_64.deb",
    f"https://github.com/Cinqic-Research/Juniper-App/releases/download/{JUNIPER_TAG}/SHA256SUMS.txt",
    "https://github.com/Cinqic-Research/Juniper-App",
]

# Checked only if present in ANDROID_RELEASE_URLS at call time (see main());
# kept as a separate, optional list so this script still passes before the
# Android release exists.
ANDROID_RELEASE_URLS = [
    f"https://github.com/Cinqic-Research/Cinqic-Calculator/releases/download/{ANDROID_TAG}/Cinqic-Calculator-Android.apk",
    f"https://github.com/Cinqic-Research/Cinqic-Calculator/releases/download/{ANDROID_TAG}/SHA256SUMS-Android.txt",
    f"https://github.com/Cinqic-Research/Cinqic-Calculator/releases/tag/{ANDROID_TAG}",
]


def check_url(url: str) -> tuple[bool, str]:
    request = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "cinqic-site-verify"})
    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            return True, f"{response.status}"
    except urllib.error.HTTPError as exc:
        return False, f"HTTP {exc.code}"
    except urllib.error.URLError as exc:
        return False, str(exc.reason)


SITE_ROOT = Path(__file__).resolve().parent.parent

# Any GitHub release URL the site actually links to. Discovered from the HTML
# rather than hardcoded, so a new product page cannot ship a dead release link
# without this check noticing it.
RELEASE_LINK_PATTERN = re.compile(
    r"https://github\.com/Cinqic(?:-Research)?/[^\"'\s]*/releases(?:/[^\"'\s]*)?"
)


def discover_release_links() -> list[str]:
    found = set()
    for page in SITE_ROOT.rglob("*.html"):
        found.update(RELEASE_LINK_PATTERN.findall(page.read_text(encoding="utf8")))
    return sorted(found)


def main():
    urls = list(RELEASE_URLS)
    if "--include-android" in sys.argv:
        urls += ANDROID_RELEASE_URLS
    for url in discover_release_links():
        if url not in urls:
            urls.append(url)

    failures = []
    for url in urls:
        ok, detail = check_url(url)
        status = "OK" if ok else "FAIL"
        print(f"{status}  {detail:<20}  {url}")
        if not ok:
            failures.append(url)

    if failures:
        print(f"\n{len(failures)} release link(s) failed.", file=sys.stderr)
        return 1
    print("\nAll release links are reachable.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
