# Bloom Digital Ecosystem — stakeholder proposal

The glimpse slides (07a–07f) come in two design directions. Everything else in the deck is identical.

| Direction | Idea | Standalone file | Artifact build |
| --- | --- | --- | --- |
| A · One language | One shared UI language, an accent per audience | `Bloom-Digital-Ecosystem-Proposal.html` | `dist/bloom-digital-ecosystem.html` |
| B · Drawn from Bloom | A symbol traced from the wordmark's letter o, colours sampled from Bloom's own screens and photography, serif-led type | `Bloom-Digital-Ecosystem-Proposal-B.html` | `dist/bloom-digital-ecosystem-b.html` |

- `src/proposal.html` — the single source for both. Slides and notes tagged `data-dir="a"` or `data-dir="b"` only appear in that direction's build. Logos live in `src/assets/`, product screens in `src/screens/`; the build inlines them.

Rebuild after editing the source:

```sh
python3 build.py
```

Open either standalone file in a browser. Navigate with the arrow keys, the chapter menu at the top, or by swiping. Every figure links to its source; the full list is in the Sources drawer and the appendix.

## Direction B, in brief

- **Symbol.** Five copies of the wordmark's first o (traced from `src/assets/bloom-wordmark-alpha.png`, outline smoothed to within 0.5% of the glyph), each touching one centre and woven over its neighbour. The petal paths are the `#b-p0`–`#b-p4` paths in the SVG sprite. The wordmark itself is unchanged.
- **Colour.** Eight base colours, each sampled from something Bloom already owns: Oxblood `#932A23` (wordmark), Ink `#1C1A19` (Bloom Partners headings), Paper `#F6F4F0` (Bloom Multiverse), White, Sandstone `#85674B`, Garden `#4B5715` and Dusk `#A79DBF` (Bloom Universal photography), Navy `#0B1641` (Bloom Multiverse). Sample points are recorded in `WINS` in the source.
- **Type.** Cormorant Garamond for headlines, Plus Jakarta Sans for interface text, lining figures throughout.
