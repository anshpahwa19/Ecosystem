"""Inline the logo files into the proposal and write the single-file builds.

One source, three builds. Direction A or B styles the glimpse slides (07a-07f); the set picks the slides:
  web,    direction A  "One language"      dist/bloom-digital-ecosystem.html,   Bloom-Digital-Ecosystem-Proposal.html
  web,    direction B  "Drawn from Bloom"  dist/bloom-digital-ecosystem-b.html, Bloom-Digital-Ecosystem-Proposal-B.html
  mobile, direction B  mobile apps only    dist/bloom-mobile-apps.html,         Bloom-Mobile-Apps.html
The mobile set (05e-05g, 07g-07i) is tagged data-set="mobile" in the source. Set "all" builds both sets as one deck.

dist/*.html are page fragments for the Claude artifact; the root files are standalone documents that open straight from disk.
"""
import base64
import pathlib

ROOT = pathlib.Path(__file__).parent
ASSETS = {
    "{{IMG_EDITION}}": "assets/the-abu-dhabi-edition.png",
    "{{IMG_MARRIOTT}}": "assets/marriott.png",
    # Bloom wordmark lifted from the Bloom Universal screen as an alpha mask (slides 07a-07f)
    "{{IMG_WORDMARK}}": "assets/bloom-wordmark-alpha.png",
    # Product screens supplied by the Bloom team (slides 05a-05c); Bloom@Go is the live employee platform
    "{{SHOT_HOME}}": "screens/home-buying-platform.webp",
    "{{SHOT_PARTNERS}}": "screens/bloom-partners-requests.webp",
    "{{SHOT_GO}}": "screens/bloom-go-home.webp",
    "{{SHOT_MASTERPLAN}}": "screens/al-metlaa-master-plan.webp",
    "{{SHOT_UNIVERSAL}}": "screens/bloom-universal.webp",
}
# App home screens supplied by the Bloom team (slides 05e-07i), inlined as supplied (no re-compression) and only into
# builds that carry the mobile set.
APP_ASSETS = {
    "{{APP_PARTNERS}}": "screens/bloom-partners-app.webp",
    "{{APP_HOMES}}": "screens/home-buying-app.jpg",
    "{{APP_COMMUNITY}}": "screens/bloom-community-app.webp",
}
MIME = {".png": "image/png", ".webp": "image/webp", ".jpg": "image/jpeg"}
# name: (direction, set, artifact fragment, standalone file)
BUILDS = {"a": ("a", "web", "bloom-digital-ecosystem.html", "Bloom-Digital-Ecosystem-Proposal.html"),
          "b": ("b", "web", "bloom-digital-ecosystem-b.html", "Bloom-Digital-Ecosystem-Proposal-B.html"),
          "mobile": ("b", "mobile", "bloom-mobile-apps.html", "Bloom-Mobile-Apps.html")}


def inline(page, assets):
    for token, name in assets.items():
        path = ROOT / "src" / name
        data = base64.b64encode(path.read_bytes()).decode()
        page = page.replace(token, f"data:{MIME[path.suffix]};base64,{data}")
    return page


source = inline((ROOT / "src" / "proposal.html").read_text(encoding="utf-8"), ASSETS)
assert "{{IMG_" not in source and "{{SHOT_" not in source and source.count("{{DIR}}") == 1 and source.count("{{SET}}") == 1

(ROOT / "dist").mkdir(exist_ok=True)
for name, (direction, slides, fragment, standalone_name) in BUILDS.items():
    page = source.replace("{{DIR}}", direction).replace("{{SET}}", slides)
    if slides == "web":  # the mobile slides are dropped at runtime; leave their screens out
        for token in APP_ASSETS:
            page = page.replace(f"url({token})", "none")
    else:
        page = inline(page, APP_ASSETS)
    assert "{{APP_" not in page, f"unfilled app screen in build {name}"
    if slides == "mobile":  # its own name in the artifact gallery and the browser tab
        page = page.replace("<title>Bloom Digital Ecosystem</title>", "<title>Bloom Mobile Apps</title>", 1)
    (ROOT / "dist" / fragment).write_text(page, encoding="utf-8")
    # Same skeleton the artifact host wraps around the fragment.
    standalone = (
        '<!doctype html><html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        "<style>:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}"
        "body{margin:0}img{max-width:100%}[hidden]:not([hidden=until-found i]){display:none!important}</style>"
        "</head><body>\n" + page + "\n</body></html>\n"
    )
    (ROOT / standalone_name).write_text(standalone, encoding="utf-8")
    print(f"{name}: direction {direction}, {slides} set, built {len(page):,} bytes -> {standalone_name}")
