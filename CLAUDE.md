# Yonder

A World of Warcraft addon: an Explorers' League field journal that fills in as
a character travels. The **Expeditions** first (each zone's riddles, solved
on the spot, and its quarry, a rare to track down), the **Bestiary**, the
**Atlas**, **Finds** (fish, plants, ores and gems, cloth and leather) and the
**Milestones**. Called Explorer's Field Journal (folder `FieldJournal`)
until 0.8.0, renamed on 13 October 2026; `addon/FieldJournal` is the
handover that brings old journals over. Classic Era (11509), TBC
Anniversary (20506) and Forever (16001), one package; salty-max/yonder.
Sister project: Lorekeeper's Codex (same engineering and voice). Read the
family's CLAUDE.md (`../CLAUDE.md`) first.

## Where things are

| What | Where |
|---|---|
| The journal file by file: the handover, the data files, notes, families, the build, the package, every Lua file, languages, the sim, the daily job, releases | `docs/architecture.md` |
| The riddle files (`expeditions/<zone>.md`): fields, spots, `found:`, quests and keepers, what `scripts/expeditions.py` resolves and refuses | `docs/expeditions.md` |
| The voices (naturalist, surveyor), riddle verses and hints, lore scope, `[classic]`/`[forever]` | `docs/writing.md` |
| The plan and the decisions (Expeditions: Reworked, After the first test) | `PLAN.md` |
| Finds' research and the translations' notes | `docs/finds-*.md` and the other tracked files in `docs/` |
| The store page | `addon/CURSEFORGE.md` |

A few local review notes in `docs/` are excluded (`.git/info/exclude`):
absent from git and from a worktree. Everything else there is tracked, the
docs above included.

## Commands

```bash
bun run build | check | package
bun scripts/root.ts --run addon-kit/q.ts check -- bun run check   # the check, quiet, stamping the tree for the push
python3 scripts/expeditions.py [--dry [folder]]   # resolve the riddles' spots into data/expeditions.json; --dry: the checks alone
bun scripts/root.ts --run wow-data/bin/card.ts <npc|object|place> <id or name> [--game forever]  # a riddle's subject, before writing it
bun run creatures          # regenerate data/creatures.json (pinned database)
python3 scripts/rare_zones.py    # then data/rare-zones.json (each rare's zone)
bun scripts/build.ts --verbose   # per-family counts, overlaps, unsorted
bun run kit:sync           # after a change to the kit (Kit.lua, Media, scripts/root.ts and root.py)
scripts/release.sh [--version X.Y.Z] [--hold] NOTES.md   # check, tag, push; Actions publish
```

Writing or vetting a riddle: the `wow-riddles` skill (the root's
`.claude/skills/`).

## Hard rules

- Riddles: never a kill, never the same discovery twice in a zone. A quest
  place only for a distinct experience, never a copied objective or a
  temporary quest prop; a reviewed overlap records `quest_overlap` and
  `quest_context`. A keeper that attacks one side, on a riddle open to
  both, is answered by `faction:` or the danger line. The resolver
  (`expeditions.py`) checks these; rerun it after changing a spot or a hint
  circle (the build refuses a stale one).
- A landmark never borrows an NPC's spawn or invents a game object. Never
  gate a solution on `IsIndoors`. A verse suggests a gesture without naming
  the emote. Answers ship as fingerprints only.
- The journal keeps ids only, never a game name (a player's excepted); the
  game names things by id in the client's language. A regenerated table
  keeps every id a journal may hold.
- No spoilers: families appear once met, no totals of what remains.
- The voices: the League's naturalist (Bestiary, herbs, fish, materials),
  a dwarf surveyor (Atlas). Plain ASCII in the English files, no semicolons
  in prose in any language. Use full Opus and read `docs/writing.md` before
  writing.
- The game's data comes from wow-data only (scripts/, through
  `scripts/root.ts` and `root.py`); Wowhead's points are frozen in wow-data
  (a new riddle's thing fetched there first). Generated files (`Data_*.lua`,
  `data/*.json`, the name files) are never edited by hand. A new generator
  goes into `game-data.yml` too.
- Dropping the FieldJournal handover is the user's call.
- `Kit.lua`, `scripts/root.ts` and `scripts/root.py` are the kit's copies:
  edit addon-kit, then `bun run kit:sync`.
- Conventional Commits, lowercase subjects, no AI trailers. Commit locally;
  ask before any push, release or deploy. The pre-push hook wants a check
  stamp on the tree (q), which `release.sh` makes after the version bump.
