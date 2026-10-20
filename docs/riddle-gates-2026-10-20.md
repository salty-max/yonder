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

## Waiting on you (5)

The resolver still fails on these, so `data/expeditions.json` can't be
rebuilt until they're settled. Nothing is pushed.

1. **blasted-lands-tainted-scar.** An arrival ("Find his ground, and do not
   linger"), and Suppression (7583) sends players into the Scar to bind a
   Doomguard Commander. The Stones That Bind Us (2681) frees a servant
   there, and Warrior Kinship (8423) hunts its Helboar. Doing the quest
   solves the riddle in passing.
   *Recommendation:* make it a look at the scar from its edge (LOOK, GAZE,
   PEER: "look upon his ground, and do not linger"), new verse and hint in
   four languages, then the overlap [2681, 7583, 8423] with a context.
2. **stranglethorn-vale-emperors-tomb.** An arrival ("Find it"), and the
   tomb itself (object 54) is the chest of Kurzen's Mystery (207): the
   Fourth Troll Legend drops from it. Every Alliance player on that quest
   solves the riddle.
   *Recommendation:* a gesture of respect at the tomb (BOW, KNEEL), and the
   overlap [207]: "Kurzen's Mystery takes the fourth troll legend from the
   tomb. Yonder asks only a bow to the emperor, with no quest."
3. **the-barrens-tidus-stair.** An arrival ("Set foot on the stair")
   anchored on Mahren Skyseer, who gives and ends Isha Awak (873) and is
   the destination of Mahren Skyseer (874, "Speak with Mahren Skyseer").
   The Merchant Coast's pirate quests (887, 888, 895, 1963, 2381, and
   Forever's 92706 and 97253) fall inside its 405-yard circle too.
   *Recommendation:* a gesture on the stair (PEER or LOOK down where it goes
   under the sea, as the margin's drowned city invites), then the overlap
   with a context. A smaller hint circle doesn't help: at r 2, Southsea
   Freebooters (17 of the 24 brigands) and Plundering the Plunderers are
   still there. The pirates camp at the stair's foot.
4. **tanaris-gadgetzan.** Bera Stonehammer (7823), the Alliance's gryphon
   master, stands within 10 yards of the book, and her faction attacks the
   Horde. The data can't say whether she pulls (her flags are PvP and immune
   to NPCs, nothing on aggression).
   *Recommendation:* name her in the danger line, in four languages, e.g.
   "Quiet, but for the Horde, Bera Stonehammer, the Alliance's gryphon
   master, stands close". Worth a look with a Horde character either way.
5. **westfall-aegwynn.** Salma Saldean (235, level 20) stands by the shelf
   at Saldean's Farm and attacks the Horde.
   *Recommendation:* the danger line, in four languages: "Quiet for the
   Alliance. For the Horde, the Saldeans defend their farm". `faction:
   alliance` would take a book from Horde readers for one farmer.

## Drafted for your review (27)

Each one is now in its file (commit `0bf0662`, easy to drop) with a drafted
`quest_context`. Two are worth a second look:

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
| loch-modan-valley-of-kings | 224, 1526 and 94467 (Forever) | troggs, Forever's dwarf shaman Call of Fire |
| mulgore-rolling-plains | 99080 (Forever) | Galak centaurs |
| searing-gorge-blackchar | 3906, 4262 | Overmaster Pyron killed near the cave |
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

## Answered by the rule

- **silverpine-forest-wallace**: the Haggard and Sickly Refugees attack the
  Horde, and its danger line already says "Guarded for the Horde (the
  refugees...)".
