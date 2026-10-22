# Yonder's expeditions: the riddle files and the resolver

The format of `expeditions/<zone>.md`, what the resolver checks and what it
writes (moved from CLAUDE.md on 20 October 2026). How a riddle is written:
`docs/writing.md`. The plan and the decisions: `PLAN.md` (Reworked, After
the first test).

- `expeditions/<zone>.md` (named as the atlas's, top level: build.ts reads
  every `content/` folder as a Bestiary section): a zone's riddles (the
  Expeditions, PLAN.md): front matter in YAML (`zone`, `home` for a starting
  zone or capital, `riddles`: id, tier, `faction` (a town's, or the side a
  keeper doesn't attack), `gestures`
  (emote tokens) or `reading`, `night`, `companions` (other creature ids
  accepted by a group gesture, such as either musical frog or either
  gryphon), the spot: `object`, `creature`,
  `trigger`, `area` (with an `anchor` where the area has no map overlay),
  or `landmark: <text-id>` for explicitly reviewed scenery from wow-data's
  `landmark` table. A landmark needs its own `name` and a `radius` of 10 to
  100 yards. Its provenance stays in wow-data (`owner-report`, the owner's
  look in the game or at the client's map in a viewer, or `client-map`, a placement in the client's own map
  files, read with wow-data's `bin/placements.ts`), and it never borrows an
  NPC's spawn or invents a game object. Shared riddles require matching landmark
  coordinates in both databases. A radius is the journal's detection
  tolerance, not a claim that the full scene boundary has been surveyed.
  `found: target` for a keeper met by speaking to it or one that walks,
  `found: place` with `radius` (10 to 100 yards) for a gesture in a stationary
  creature's surroundings or an arrival, with no live creature or target
  needed and no companion keepers. A named place may use a hostile creature
  only as a fixed positional anchor, never as a required meeting.
  `found: patrol` for a gesture that needs both the nearby creature targeted
  and the selected spawn's recorded patrol corridor, preventing another
  creature with the same ID elsewhere from substituting for that scene.
  Do not gate a solution on `IsIndoors`: a roof or cave in the story does not
  establish how the client classifies it. An assumed indoor flag in a test
  is not live geometry evidence. The remaining fields are
  `hint_area`, `danger`, `sources`; `quarry: { id, sources }` in a zone with
  rares, never a capital (a creature of Forever's own, which the data doesn't
  know, adds its `name`, `level`, `rank` and `model`); `client: forever` for a
  zone of Forever's own (Zephras Isle: creatures and sub-areas only);
  quest locations allowed for a distinct experience, never a copied objective
  or a temporary quest prop. A reviewed overlap records `quest_overlap: [ids]`
  and `quest_context` explaining the separate discovery. Never a kill, never
  the same discovery twice in a zone. New unreviewed Forever quest overlaps
  still fail, as do either game's quests tied to the subject or the place (an
  area's hint circle, a spot's solving radius and NEAR yards about: half the
  zone's spawns of what they ask for there), and a creature by the spot of a
  riddle open to both that attacks one side, unless `faction:` or the danger
  line names it (`--dry [folder]`, `scripts/expeditions_test.py`)
  (the resolver checks these safeguards:
  PLAN.md, Reworked and After the first test), then `## <id>` sections: the verse, `? ` the
  first hint, `= ` the note, `+ ` the margin; `## quarry`: its poster (verse,
  note, margin, no hint); plain ASCII.
  `scripts/expeditions.py` resolves the spots from the game's data into
  `data/expeditions.json` (committed): an object's spawns (dump and Wowhead
  alike, inside the hint circle), a creature's spawn (and whether it walks),
  a trigger, a sub-area's ids; a quarry's haunts (its spawns that Wowhead
  places too, and the paths they walk, gathered into circles); each zone's
  size in yards and sub-areas; the client's emote tokens. A zone of Forever's
  own is placed on Forever's client tables, its creatures from Questie's
  Forever (no license: credited) where Wowhead's Forever database places them
  too. Wowhead's points (the cross-check of every spot, a quarry's
  sightings) are frozen in wow-data (`bun ../wow-data/bin/wowhead-points.ts`:
  a new riddle's creature or object fetched there first). For a Classic world
  record, `position_check: questie` explicitly uses Questie's independent
  coordinates for an object or creature when Wowhead has no points for the
  relevant zone, still requiring agreement with the
  Classic world spawn. Record the evidence in `sources:`. Rerun it after changing a spot or a hint circle (the
  build refuses a stale one). `scripts/expeditions.ts` (for build.ts) checks
  every riddle and writes the answers as fingerprints only (salted FNV-1a of
  5-yard cells, sub-areas, the keeper, the gestures), the texts read once
  solved veiled. Spots, hint circles and haunts are written in Classic's map
  percent. Four shared zones have a different map on Forever (a retail
  map's bounds: Stormwind with its harbour, Mulgore, Redridge, the Eastern
  Plaguelands): the resolver gives each Forever's size and the line from
  Classic's percent to Forever's (checked against Forever's own creature
  points), and the build moves Data_Forever.lua's cells, circles and haunts
  by it. A landmark in one of them is refused until its map is settled.
