# Bloom Digital Ecosystem — stakeholder proposal

The glimpse slides (07a–07f) come in two design directions. Everything else in the deck is identical. The mobile apps have their own slides, built as a separate deck for now.

| Direction | Idea | Standalone file | Artifact build |
| --- | --- | --- | --- |
| A · One language | One shared UI language, an accent per audience | `Bloom-Digital-Ecosystem-Proposal.html` | `dist/bloom-digital-ecosystem.html` |
| B · Drawn from Bloom | A symbol traced from the wordmark's letter o, colours sampled from Bloom's own screens and photography, serif-led type | `Bloom-Digital-Ecosystem-Proposal-B.html` | `dist/bloom-digital-ecosystem-b.html`, published privately at https://claude.ai/artifact/GQNGMTPC3BzjuaKt34UyVy |
| Mobile apps · direction B | The three apps today (05e–05g) and as one Bloom (07g–07i) | `Bloom-Mobile-Apps.html` | `dist/bloom-mobile-apps.html`, published privately at https://claude.ai/artifact/WCkCVhQCUfD2djTRbpsGUn |

- The employee platform shown is **Bloom@Go**, live today (`src/screens/bloom-go-home.webp`, stitched from two screenshots of its home page). It replaces Bloom Multiverse throughout; the concepts name it Bloom Go.
- `src/proposal.html` — the single source for all three. Slides and notes tagged `data-dir="a"` or `data-dir="b"` only appear in that direction's build. Slides tagged `data-set="mobile"` only appear in the mobile build; untagged slides are the web deck. Logos live in `src/assets/`, product screens in `src/screens/`; the build inlines them.
- **Combining the decks.** Set a build's set to `"all"` in `BUILDS` in `build.py`: the mobile slides then sit after 05d and 07f, numbered 05e–05g and 07g–07i, with source 17 and the mobile notes in the appendix.

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
- **Product views.** One Bloom, five views: no new marks. Each product is a crop of the same flower (`VIEWS` in the source): Universal the whole flower, Homes one petal's arch, Community the centre where all five meet, Partners two Bloom o's woven together, Go written with a G drawn from the Bloom o's own strokes, beside the o itself. App icons show the view white on oxblood; lockup rows end with the same view, oxblood on cream.

## Mobile apps

- **Screens.** Home screens supplied by the Bloom team: Bloom Partners (`src/screens/bloom-partners-app.webp`, a 269 px wide capture, so its colours are approximate), the home-buying app (`home-buying-app.webp`) and the Bloom Community App (`bloom-community-app.webp`, straightened out of a promotional device frame, its bezel corners painted over). In the phone frames the content scrolls while each app's fixed parts stay pinned: status bars, Partners' tab bar and the floating Book Appointment.
- **05e–05g, today.** The three apps in phone frames; the same jobs side by side (Bloom in view, greeting, main action, navigation, colour); and what it means: 1 app with the wordmark in view, 3 greeting styles, 3 navigation patterns, 5 reds and none on a main action.
- **07g–07i, direction B.** One app shell shared by every app (app bar signed by the symbol and wordmark, serif greeting, cards, one accent, one oxblood action docked above the tab bar) and tuned per app: Partners in Dusk, Homes in Sandstone, Community in Garden. Concept screens are drawn at 390 × 844 (`MOBILE` in the source) with content from today's screens and the Bloom Community App page.
