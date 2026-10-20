# Writing Yonder

The voices and the rules of the text (moved from CLAUDE.md on 20 October
2026).

- Voice: a naturalist of the Explorers' League (the Codex's archivist's
  colleague): observant, dry, fond of the creatures it describes. Two to four
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
  creatures and the Codex archivist's history. Herb and fish notes complement
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
