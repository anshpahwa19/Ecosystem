"""Inline the logo files into the proposal and write the single-file builds.

One source, two design directions for the glimpse slides (07a-07f):
  direction A  "One language"      dist/bloom-digital-ecosystem.html,   Bloom-Digital-Ecosystem-Proposal.html
  direction B  "Drawn from Bloom"  dist/bloom-digital-ecosystem-b.html, Bloom-Digital-Ecosystem-Proposal-B.html

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
MIME = {".png": "image/png", ".webp": "image/webp"}
BUILDS = {"a": ("bloom-digital-ecosystem.html", "Bloom-Digital-Ecosystem-Proposal.html"),
          "b": ("bloom-digital-ecosystem-b.html", "Bloom-Digital-Ecosystem-Proposal-B.html")}

source = (ROOT / "src" / "proposal.html").read_text(encoding="utf-8")
for token, name in ASSETS.items():
    path = ROOT / "src" / name
    data = base64.b64encode(path.read_bytes()).decode()
    source = source.replace(token, f"data:{MIME[path.suffix]};base64,{data}")
assert "{{IMG_" not in source and "{{SHOT_" not in source and source.count("{{DIR}}") == 1

(ROOT / "dist").mkdir(exist_ok=True)
for direction, (fragment, standalone_name) in BUILDS.items():
    page = source.replace("{{DIR}}", direction)
    if direction == "b":  # its own name in the browser tab and the artifact gallery
        page = page.replace("<title>Bloom Digital Ecosystem</title>", "<title>Bloom Ecosystem Direction B</title>", 1)
        assert "<title>Bloom Ecosystem Direction B</title>" in page[:8192]
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
    print(f"direction {direction}: built {len(page):,} bytes -> {standalone_name}")
