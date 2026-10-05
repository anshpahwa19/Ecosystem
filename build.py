"""Inline the logo files into the proposal and write two single-file builds.

dist/bloom-digital-ecosystem.html   page fragment published to the Claude artifact
Bloom-Digital-Ecosystem-Proposal.html  standalone document that opens straight from disk
"""
import base64
import pathlib

ROOT = pathlib.Path(__file__).parent
ASSETS = {
    "{{IMG_EDITION}}": "assets/the-abu-dhabi-edition.png",
    "{{IMG_MARRIOTT}}": "assets/marriott.png",
    "{{IMG_MARK}}": "assets/bloom-multiverse-mark.png",
    # Product screens supplied by the Bloom team (slides 05a-05c)
    "{{SHOT_HOME}}": "screens/home-buying-platform.webp",
    "{{SHOT_PARTNERS}}": "screens/bloom-partners-requests.webp",
    "{{SHOT_MULTIVERSE}}": "screens/bloom-multiverse-home.webp",
    "{{SHOT_MASTERPLAN}}": "screens/al-metlaa-master-plan.webp",
    "{{SHOT_UNIVERSAL}}": "screens/bloom-universal.webp",
}
MIME = {".png": "image/png", ".webp": "image/webp"}

page = (ROOT / "src" / "proposal.html").read_text(encoding="utf-8")
for token, name in ASSETS.items():
    path = ROOT / "src" / name
    data = base64.b64encode(path.read_bytes()).decode()
    page = page.replace(token, f"data:{MIME[path.suffix]};base64,{data}")
assert "{{IMG_" not in page and "{{SHOT_" not in page

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
