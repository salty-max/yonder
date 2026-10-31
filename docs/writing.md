# Writing Yonder

The voices and the rules of the text (moved from CLAUDE.md on 20 October
2026).

- Voice: a naturalist of the Explorers' League (a colleague of Archesonus,
  the Codex's Royal Historian: the League is the city's, not her order):
  observant, dry, fond of the creatures it describes. Two to four
  short paragraphs per family: what they are, where and how they live, what a
  traveller should know. The player's own numbers follow the note on the page.
- No semicolons in prose, in any language (the user's rule, 14 October
  2026): two sentences, or a comma, or a rewrite for a list. The gender
  tokens' own `;` stay. Research notes (`sources:`) may keep theirs.
- A gesture's verse suggests the action through its story, without naming
  the emote. Its paid hint helps with the action as well as the place and
  may name one accepted gesture in ordinary words. Keep the League's voice,
  not a list of possible answers. The riddle page explains emotes and, for
  creatures, proximity and targeting. Do not repeat those mechanics in each
  hint. Avoid false requirements to wait, fight, buy an item or operate a
  portal. Read changed passages in context in English, French and German
  before release: passing interaction tests does not check the writing.
  `scripts/riddle-solutions.test.ts` checks every authored solution against
  all twelve client language files, including group keepers, through both
  emote APIs and the event hooks. Its small game is
  `addon/test/riddle-game.lua`, independent of `sim.lua`'s narrative.
  GUID kinds are protocol tokens, never translated UI words.
- Lore scope as the Codex (loosened on 12 October 2026): the past up to the
  vanilla era from any source (the games, novels, comics, RPG books,
  Chronicle), nothing anachronic to vanilla or Forever; Forever-only families
  may use Forever's own texts. Original wording. Plain ASCII (the build
  rejects others).
- Classic and Forever are separate accounts of the world. In family notes,
  Atlas notes and herb/fish notes, prefix a paragraph with `[classic]` or
  `[forever]` when the accounts differ. Unmarked paragraphs belong to both.
  Selection happens at build time; markers and the other world's paragraphs
  never reach the installed book. Each available note must retain text in
  both games. Use Forever's quests and announcements for its additions;
  a new map name alone does not establish new history.
- The Atlas has a dwarf surveyor's voice: terrain, routes, landmarks and the
  experience of crossing them. Keep its work distinct from the naturalist's
  creatures and Archesonus's history in the Codex. Herb and fish notes complement
  the location lists already shown by the book; they need not repeat them.
- Material notes use that same naturalist's voice. Review the English
  against the existing fish and herb notes before translating it. Give
  each item its own observation, grounded in its sources or uses. Avoid
  repeated inventory advice and a forced witty ending on every entry.
  Translate the observation and dry humour naturally, rather than copying
  the English sentence structure or making the notes sound like tooltips.
  Explain the material itself as well as its uses. Include physical or
  magical properties, preparation, cultural associations or a short piece
  of history where the game's text supports them. A location and a recipe
  list alone are not the aim. Attribute a character's opinions and claims.
  A finished item's effects do not establish the raw material's properties.
- No spoilers: families appear once met; no totals of what remains.

## The riddle's form

Written from the 166 riddles and 39 quarry posters shipped on 31 October 2026
(`expeditions/*.md`), not invented. The League's voice is the naturalist's
above, speaking of one place at a time. A riddle section has four parts, in
this order, each a different job.

- **The verse.** Three or four lines, rarely five (166 riddles: 102 of four,
  59 of three, 5 of five). Unrhymed and unmetred, ordinary sentences broken
  at the line (median 12 words a line, 43 words in all, 26 to 65). It tells
  the place and its story in the third person and usually ends on an
  instruction to the traveller in the imperative (about one last line in four opens with
  Find, Ask or Give), which carries the
  action without naming the emote ("Follow their example", "Honour the post,
  whoever keeps it", "Find her among them: she will tell you herself"). The
  rest end on the story's last image. Plain words, no archaic
  thee and thou, no puzzle for its own sake: the story points, the hint helps.
  One deliberate exception: the Valley of Kings (`loch-modan-valley-of-kings`)
  rhymes in couplets, a dwarven ballad for the dwarves' own monument (the
  user's call, 31 October 2026). It stays the only one: a new riddle never
  rhymes. Its translations need not rhyme.
- **The hint (`? `).** Usually two sentences (one to four), 16 words at the median (7 to 29).
  Where the place is, in the traveller's own terms (a road, a town's square,
  a house), then what to do, in ordinary words, one accepted gesture at most.
  It is paid for, so it is plain where the verse is oblique. Never a slash
  command.
- **The note (`= `).** What the traveller found, once it is found: the
  subject's name and one or two facts, 22 words at the median (3 to 54). A
  delivery, not a flourish.
- **The margin (`+ `).** One fact the naturalist adds in the margin, 23 words
  at the median (5 to 60): a detail of the place, its history or the creature.
  No closing quip.
- **A quarry's poster** is the same without a hint: three or four lines of
  verse (28 posters of three lines, 10 of four, one of five: 21 to 57 words, 34 at the median) that describe the rare and where it keeps, then `= `
  the name and haunt, then `+ ` one fact (loot, place, coat, a plain
  mechanic). The poster says where to look and never that it is a kill.
- Spelling is British (honour, grey, traveller), game names as the game
  spells them (a few riddles still say "center" and "gray", to be corrected
  with their translations under their own card). The build checks that the
  parts are there (two lines of verse or more, one hint, note and margin, no
  hint on a quarry, no gesture named) and the resolver the content rules
  (`docs/expeditions.md`), not the length or the tone: those are read.

Two real riddles, as `expeditions/duskwood.md` has them:

```
## duskwood-unseen
The village on the hill of ravens was left to its dead,
and most of its houses stand empty, or seem to.
In one of them, a household keeps both floors, hidden from an unaided eye.
Study the empty rooms, and leave their occupants undisturbed.
? Raven Hill, at the village's northern edge: a house of two floors, and no one in it. Inside, peer into the empty rooms.
= The Unseen: invisible wraiths, of a strength far beyond Duskwood's. Two keep this house. Others keep the rest of Raven Hill's.
+ A warlock's Detect Invisibility reveals them. Their invisibility is not a rogue's stealth: an eye trained to find the latter may miss an entire household here.
```

```
## quarry
Beneath the cemetery on the hill of ravens, a dead commander keeps his post.
Strike him down and he stands again, whole, while you watch:
the spell is his own, and he casts it as he falls.
Finish him before he finishes it.
= Commander Felstrom, of the Dawning Wood Catacombs under Raven Hill Cemetery. Lord Malathrom, a ghoul who calls up two foul servants, Sloth and Sludge, keeps the same dark.
+ Each copy that rises fights as long as the last. Fail to stop the spell, and the hunt has no end.
```

## Registers and examples, by language

English is the base (British spelling, plain ASCII, no semicolons, short
sentences). The League's voice speaks to the traveller in the imperative in
every language: French **vous** ("Trouvez-la parmi eux"), German **du**
("Finde sie unter ihnen", the Codex's "Euch" is not Yonder's), Spanish **tú**
("Encuéntrala entre ellos"), never "vosotros". Real riddle, `duskwood-darkshire`
(`expeditions/duskwood.md`, translations in `i18n/<locale>/expeditions/`):

> Find her among them: she will tell you herself.
> Trouvez-la parmi eux : elle vous le dira elle-même.
> Finde sie unter ihnen: Sie wird es dir selbst erzählen.
> Encuéntrala entre ellos. Te lo contará ella misma.

and the hint (`?`) of `duskwood-unseen`:

> Raven Hill, at the village's northern edge: a house of two floors, and no one in it. Inside, peer into the empty rooms.
> Colline-aux-Corbeaux, à la lisière nord du village : une maison à deux étages, et personne dedans. À l'intérieur, scrutez les pièces vides.
> Rabenflucht, am nördlichen Rand des Dorfes: ein Haus mit zwei Stockwerken, und niemand darin. Spähe drinnen in die leeren Räume.
> Cerro del Cuervo, en el extremo norte del pueblo: una casa de dos plantas sin nadie dentro. Ya dentro, escudriña las habitaciones vacías.
