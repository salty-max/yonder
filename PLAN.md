# Yonder: what is open

The design decisions of the Bestiary, the Atlas, the Expeditions, the Finds
and the Plants and Fish (October 2026) are built and released, and are written
where they are kept: the hard rules in CLAUDE.md, the riddle files, their
gates and the rules of the October plan in `docs/expeditions.md`, the voices in `docs/writing.md`, the files in
`docs/architecture.md`. The old plan (60 KB, dated 5 to 17 October, naming
`/journal` and the CMaNGOS list) was cut down to this on 30 October 2026:
`git log -- PLAN.md` has it.

## Open

- **After Forever's launch (4 November 2026):** Forever's new zones, creatures
  and rares reach the Bestiary and the Atlas as wow-data's databases fill; new
  riddles for them follow the gates (`docs/expeditions.md`).
- **The FieldJournal handover** (`addon/FieldJournal/`: its TOCs and
  `YonderHandover.lua`): players may still hold `FieldJournalChar`. Keep it
  one more release cycle, then remove it with the user's go.
- **The TBC and Italian sweep**, one wave across the family after the launch:
  `Yonder_TBC.toc`, `Text_itIT.lua`, `i18n/itIT/`, with the kit's resync.
- **Two checks**: a test pinning the hand milestone ids in `Achievements.lua`
  (NIGHTMARE, PAGLE, SCHOOLED) against wow-data, and a short-circuit of the
  1-second riddle tick in `Expeditions.lua` when no journal is loaded or
  nothing is open in the zone.
- **Hand tables for wow-data**: `data/peoples.json` (Yonder's own taxonomy,
  arguably authored) and `Creatures.lua`'s BEAST_NAMES (wow-data has
  `creature_family` in every language).
