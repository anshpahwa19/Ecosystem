"""Inline the logo files into the proposal and write two single-file builds.

dist/bloom-digital-ecosystem.html   page fragment published to the Claude artifact
Bloom-Digital-Ecosystem-Proposal.html  standalone document that opens straight from disk
"""
import base64
import pathlib

ROOT = pathlib.Path(__file__).parent
ASSETS = {
    "{{IMG_EDITION}}": "the-abu-dhabi-edition.png",
    "{{IMG_MARRIOTT}}": "marriott.png",
    "{{IMG_MARK}}": "bloom-multiverse-mark.png",
}

page = (ROOT / "src" / "proposal.html").read_text(encoding="utf-8")
for token, name in ASSETS.items():
    data = base64.b64encode((ROOT / "src" / "assets" / name).read_bytes()).decode()
    page = page.replace(token, f"data:image/png;base64,{data}")
assert "{{IMG_" not in page

(ROOT / "dist").mkdir(exist_ok=True)
(ROOT / "dist" / "bloom-digital-ecosystem.html").write_text(page, encoding="utf-8")

# Same skeleton the artifact host wraps around the fragment.
standalone = (
    '<!doctype html><html lang="en"><head><meta charset="utf-8">'
    '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
    "<style>:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}"
    "body{margin:0}img{max-width:100%}[hidden]:not([hidden=until-found i]){display:none!important}</style>"
    "</head><body>\n" + page + "\n</body></html>\n"
)
(ROOT / "Bloom-Digital-Ecosystem-Proposal.html").write_text(standalone, encoding="utf-8")
print(f"built {len(page):,} bytes")
