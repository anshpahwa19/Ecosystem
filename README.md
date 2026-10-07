# Bloom Digital Ecosystem — stakeholder proposal

The glimpse slides (07a–07f) come in two design directions. Everything else in the deck is identical.

| Direction | Idea | Standalone file | Artifact build |
| --- | --- | --- | --- |
| A · One language | One shared UI language, an accent per audience | `Bloom-Digital-Ecosystem-Proposal.html` | `dist/bloom-digital-ecosystem.html` |
| B · Drawn from Bloom | A symbol traced from the wordmark's letter o, colours sampled from Bloom's own screens and photography, serif-led type | `Bloom-Digital-Ecosystem-Proposal-B.html` | `dist/bloom-digital-ecosystem-b.html`, published privately at https://claude.ai/artifact/GQNGMTPC3BzjuaKt34UyVy |

- The employee platform shown is **Bloom@Go**, live today (`src/screens/bloom-go-home.webp`, stitched from two screenshots of its home page). It replaces Bloom Multiverse throughout; the concepts name it Bloom Go.
- `src/proposal.html` — the single source for both. Slides and notes tagged `data-dir="a"` or `data-dir="b"` only appear in that direction's build. Logos live in `src/assets/`, product screens in `src/screens/`; the build inlines them.

Rebuild after editing the source:

```sh
python3 build.py
```

Open either standalone file in a browser. Navigate with the arrow keys, the chapter menu at the top, or by swiping. Every figure links to its source; the full list is in the Sources drawer and the appendix.

## Direction B, in brief

- **Symbol.** Five copies of the wordmark's first o (traced from `src/assets/bloom-wordmark-alpha.png`, outline smoothed to within 0.5% of the glyph), each touching one centre and woven over its neighbour. The petal paths are the `#b-p0`–`#b-p4` paths in the SVG sprite. The wordmark itself is unchanged.
- **Colour.** Eight base colours, each sampled from something Bloom already owns: Oxblood `#932A23` (wordmark), Ink `#1C1A19` (Bloom Partners and Bloom@Go headings), Paper `#F8F8F8` (Bloom@Go page), White, Sandstone `#85674B`, Garden `#4B5715` and Dusk `#684FA1` (deepened from the evening sky `#A79DBF`) and Marina `#47699E` (deepened from the marina sky `#7C8DA9`), all from Bloom Universal photography. Sample points are recorded in `WINS` in the source.
- **Type.** Cormorant Garamond for headlines, Plus Jakarta Sans for interface text, lining figures throughout.
- **Symbol rules.** The symbol only signs: whole, in one colour (oxblood, or white on a dark field), in lockups, app icons and favicons. It is never recoloured in parts, never a chart, tracker or loader, and never a bullet in text.
- **Product views.** One Bloom, five views: no new marks. Each product is a crop of the same flower (`VIEWS` in the source): Universal the whole flower, Homes one petal's arch, Community the centre where all five meet, Partners two Bloom o's woven together, Go written with a G cut from the Bloom o and the o itself. App icons show the view white on oxblood; lockup rows end with the same view, oxblood on cream.
