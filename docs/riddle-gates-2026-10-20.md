# Riddle gates, 20 October 2026

`scripts/expeditions.py` now runs two checks the 20 October review made by
hand, over all 127 riddles on Classic Era and Forever (piece C of
`addon-kit/docs/harness.md`):

- **Quest ties.** A quest of either game that gives, ends or asks for the
  riddle's subject (its creature or object, companions, anchor, or an item
  the subject drops on the quest), or asks for what stands at the riddle's
  place, must be in `quest_overlap` with a `quest_context`.
- **Keepers and guards.** On a riddle open to both sides, a creature within
  10 yards of the spot (or the area's anchor) that attacks one side only must
  be answered by `faction:` or by a danger line naming it (its name, or its
  kind: "the refugees").

The tests (`scripts/expeditions_test.py`) undo the review's four fixes and
get all five findings back: Thel'danis at Uther's plaque, 1424 and 1475 at
the Pool of Tears, 4504 at the Lakkari Tar Pits, 5245 at Kel'Theril.

## Where I left the spec, and why

- **A spot riddle's place is where it is solved, plus 10 yards, not its hint
  circle.** The circles are vague on purpose: the Ratchet book's covers about
  800 yards of the Barrens, so every Merchant Coast pirate quest was "tied" to
  a book on a shelf. Hint circles for every riddle gave 239 ties, this gives
  67. An area riddle keeps its hint circle, as the spec says. There the
  circle stands for the area, and that is where the review's three quest
  findings were.
- **A quest asks for what is at the place only when half the zone's spawns
  of its target are there.** Without it, every yeti quest in Winterspring
  was Kel'Theril's.
- **Item ties count quest-only drops** (the Classic database's negative
  chances, Questie's quest items). Counting every drop gave 6,448 ties:
  linen cloth from every humanoid, herbs from every node.
- **A Classic spawn belongs to a zone only where Questie or Wowhead place it
  in that zone too.** A zone's map rectangle also holds what lies beneath
  it: Overmaster Pyron, deep in Blackrock Mountain, came out as a neighbour
  of Searing Gorge's Blackchar Cave (the reviewer caught it).

Not covered: 2,452 of Forever's new creatures have neither a faction
template in the data nor Questie's friendly sides, so the keepers check
can't judge them. No source we have gives them (the 736 Questie does give
are judged). Zephras Isle's people are all friendly to both, or unknown.

## Settled with the user (5)

These five failed the first run, and the user chose on 20 October 2026:

1. **blasted-lands-tainted-scar**: an arrival that Suppression (7583) solved
   in passing. Now a long look over Kazzak's ground from just inside its
   edge (GAZE, LOOK, PEER), with the overlap [2681, 7583, 8423].
2. **stranglethorn-vale-emperors-tomb**: an arrival at Kurzen's Mystery's
   own chest (207). Now a bow at the tomb (BOW, KNEEL), with the overlap
   [207]. The sim's arrival test moved to the Badlands' hidden crypt.
3. **the-barrens-tidus-stair**: an arrival on Mahren Skyseer, the
   destination of his own quest (874). Now a look down where the stair goes
   (PEER, LOOK, GAZE), with all nine quests in the overlap. A narrower hint
   wouldn't have helped: the pirates camp at the stair's foot.
4. **tanaris-gadgetzan**: Bera Stonehammer (7823), the Alliance's gryphon
   master, stands by the book. Her danger line names her in all four
   languages ("Guarded for the Horde (Bera Stonehammer...), quiet for the
   Alliance"). Whether she actually pulls is still worth a look in game.
5. **westfall-aegwynn**: Salma Saldean (235) stands by the shelf at
   Saldean's Farm. Now the Alliance's riddle (`faction: alliance`).

Verses and hints changed in English, French, German and Spanish, each
translation restamped (the Spanish Tidus Stair note also lost a typo,
"Lal Escalon").

## Drafted for your review (26)

Each one is now in its file (commits `0bf0662` and `bbf6aa8`, easy to drop)
with a drafted `quest_context`. Two are worth a second look:

- **the-barrens-fallen-warrior**: all seven quests are inside its 608-yard
  circle, none at the shrine. Tried on a copy: at r 3 (about 300 yards)
  none is left, so narrowing the hint and dropping the context is cleaner.
  Your call, since it's the hint's vagueness.
- **tirisfal-glades-stillwater**: Forever's Harvesting the Harvesters
  (92909, 92911) is a Westfall quest, but its isosprings also drop from the
  Decrepit Harvesters Forever put by the pond.

The rest are a separate deed at a quest's place, kept as the rules allow:

| Riddle | Quests | What the quests do there |
|---|---|---|
| blasted-lands-dark-portal | 2681, 7602, 8423 | servants freed, fel essence, Helboar |
| darnassus-darianna | 97950 (Forever) | Camping 101: Tailoring, Trianna near her |
| durotar-tiragarde | 784 | Lieutenant Benedict killed by the book |
| duskwood-twilight-grove | 8735 | the Twilight Corrupter's fragment |
| dustwallow-marsh-theramore | 558 | Jaina's Autograph (Children's Week) |
| eastern-plaguelands-mirador | 5742 | Tirion's Redemption, beside his horse |
| elwynn-forest-heroes-vigil | 1786, 1787, 5545, 91724 (Forever) | paladin's Tome of Divinity, wood, Defias wizards |
| feralas-the-maul | 5247 | a vial from the Dire Pool |
| hillsbrad-foothills-tarren-mill | 1536 | shaman's Call of Water at the well |
| hillsbrad-foothills-zixil | 9389 | Midsummer's Flame of Hillsbrad on his road |
| loch-modan-valley-of-kings | 224, 1526 and 94467 (Forever) | troggs, both Call of Fire quests' fire and brazier on Forever |
| mulgore-rolling-plains | 99080 (Forever) | Galak centaurs |
| silithus-glibb | 8304 | Dearest Natalia's two dwarves |
| stranglethorn-vale-booty-bay | 2843 | Scooty's transponder |
| teldrassil-tree-on-watch | 95998, 96101, 96604-96608, 96634 (Forever) | The Great Outdoors' campfire, Zarrin |
| the-barrens-ratchet-book | 65593 | warlock's Hearts of the Lovers, Isaac Pearson |
| the-hinterlands-seradane | 8735 | the Verdantine's fragment |
| tirisfal-glades-bulwark | 5344 | The Last Barov |
| tirisfal-glades-faols-rest | 1113, 99156 (Forever) | Hearts of Zeal, Riptear |
| tirisfal-glades-terrace | 1113 | Hearts of Zeal |
| tirisfal-glades-whispering-gardens | 1113, 99156 (Forever) | Hearts of Zeal, Riptear |
| ungoro-crater-lakkari | 4642 added to 4504 | Melding of Influences' ooze |
| wetlands-menethil | 1249 | The Missing Diplomat's brawl |
| zephras-isle-swimmers | 92679 (Forever) | Blood Tithe starts beside Swimmers |

## Fixed by the run

- **swamp-of-sorrows-pool-of-tears**: The Temple of Atal'Hakkar (1445) was
  missing. Within the Swamp proper, its Fetish of Hakkar drops only from the
  Atal'ai at the Pool (11 of the zone's 19). Added to the overlap, and its
  context gained one clause.

## Answered by the rule

- **silverpine-forest-wallace**: the Haggard and Sickly Refugees attack the
  Horde, and its danger line already says "Guarded for the Horde (the
  refugees...)".
