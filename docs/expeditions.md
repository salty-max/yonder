# Yonder's expeditions: the riddle files and the resolver

The format of `expeditions/<zone>.md`, what the resolver checks and what it
writes (moved from CLAUDE.md on 20 October 2026). How a riddle is written:
`docs/writing.md`. The hard rules: CLAUDE.md.

- `expeditions/<zone>.md` (named as the atlas's, top level: build.ts reads
  every `content/` folder as a Bestiary section): a zone's riddles (the
  Expeditions): front matter in YAML (`zone`, `home` for a starting
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
  (the choices behind them are at the end), then `## <id>` sections: the verse, `? ` the
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

## The gates' choices (20 October 2026)

`scripts/expeditions.py` runs two checks the 20 October review made by hand,
over every riddle on Classic Era and Forever (`scripts/expeditions_test.py`
undoes the review's four fixes and gets all five findings back). Where the
spec was left, and why:

- **A spot riddle's place is where it is solved, plus 10 yards, not its hint
  circle.** The circles are vague on purpose: the Ratchet book's covers about
  800 yards of the Barrens, so every Merchant Coast pirate quest was "tied" to
  a book on a shelf. Hint circles for every riddle gave 239 ties, this gives
  67. An area riddle keeps its hint circle: there the circle stands for the
  area.
- **A quest asks for what is at the place only when half the zone's spawns
  of its target are there.** Without it, every yeti quest in Winterspring
  was Kel'Theril's.
- **Item ties count quest-only drops** (the Classic database's negative
  chances, Questie's quest items). Counting every drop gave 6,448 ties:
  linen cloth from every humanoid, herbs from every node.
- **A Classic spawn is another zone's when Questie or Wowhead don't place
  the thing in this zone, and a map they do place it on holds the spawn.** A
  zone's map rectangle also holds what lies beneath it and the cities inside
  it: Overmaster Pyron, deep in Blackrock Mountain, came out as a neighbour
  of Searing Gorge's Blackchar Cave. A book copied in several inns stays
  where it is, even where Questie lists only the other inns.
- A keeper within 10 yards of the spot (or the area's anchor) that attacks
  one side only must be answered by `faction:` or a danger line naming it
  (its name, or its kind: "the refugees").

Not covered: 2,452 of Forever's new creatures have neither a faction template
in the data nor Questie's friendly sides, so the keepers check cannot judge
them (the 736 Questie does give are judged). Zephras Isle's people are all
friendly to both, or unknown.

## Rules kept from the October 2026 plan

(Cut from `PLAN.md` on 30 October 2026, the rest is in git's history.)

- **How many.** The first plan's ceiling, not a quota: a zone one riddle for
  every four places its map reveals (its WorldMapOverlay entries), rounded up,
  a capital three, a faction town in a contested zone one for its own faction
  alone. Later decisions and the user's asks moved it either way: fewer when
  the land has nothing untied to show (a zone keeps one riddle or none, a town
  loses its riddle), more where a thin zone had untied things (Stormwind and
  Undercity have four). A zone's riddles climb: near the road, off the road, hidden (never behind an exploit
  or off the playable map).
- **Whose ground.** A zone's own riddles lie on ground both factions can walk,
  never inside a faction's guarded town, neutral towns welcome. A capital's
  riddles are its own faction's alone. The six starting zones are kept the
  same way (`home:`): Elwynn, Dun Morogh and Teldrassil for the Alliance,
  Durotar, Mulgore and Tirisfal for the Horde.
- **What solves a riddle.** Never from a taxi, nor as a ghost, nor in combat.
  A gesture is the emote's token (`C_ChatInfo.PerformEmote` hooked), never the
  text. The reader guesses it from the story, so a riddle accepts every
  gesture that means the same there (grief at a grave, cheer at a feast) and
  never one that does not.
- **Never the same discovery twice in a zone.** Different places may share an
  arrival, a reading, a conversation or a gesture. Each riddle needs its own
  subject and observation: the resolver refuses a reused subject (a group's
  companion keepers included) and overlapping passive arrival footprints.
  Never a kill: a creature a riddle asks for is no foe of the side that may
  solve it.
- **Danger.** Each riddle and quarry says how dangerous its place is, from the
  pinned spawns within about 60 yards (highest level, elites): "Quiet",
  "Guarded (to level 32)", "Perilous (elites)", "the other faction's land". A
  Hardcore character is never sent blind into an elite camp.
- **Forever's quests.** The resolver flags a new quest that gives, ends or
  asks for a riddle's subject, names it, or sends players within 4% of a
  passive arrival. Only the quest ids named in `quest_overlap` are exempt, so
  later quest changes still surface. Passing the resolver does not replace
  editorial review of the action and the note.
- **Sources** beyond the quests: the dump's props, inscriptions, gossip and
  scripted lines, the WoWWiki archive (its later expansions' lines set
  aside), Warcraft III, Lands of Conflict, the Warcraft RPG, Chronicle for the
  old past, the client's display tables (who a keeper is) and the data's own
  oddities. Cross-media lore is welcome when it is not anachronic to the
  original game or Forever.
- **Never a famous leader or a capital's front gate.** The overlooked, as
  CLAUDE.md's table says.
