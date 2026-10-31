---
zone: 1432   # Loch Modan
client: both
# the spots, pinned by the data (scripts/expeditions.py resolves them): object (every spawn of it on
# this map), creature (one that stands still, or found by targeting it), trigger (a quest's exploration
# trigger) or area (a sub-area of the game's; its hint placed by its map overlay, or an anchor inside
# it: a creature, an object, a graveyard). gestures: the emotes it accepts, the story's own first.
riddles:
  - id: loch-modan-valley-of-kings
    tier: near
    gestures: [BOW, SALUTE, KNEEL]
    area: Valley of Kings   # placed: the client's overlay: 20.5, 73.7, half-size 5.5 by 13.8
    hint_area: { x: 22.0, y: 71.0, r: 14 }
    danger: "Quiet"
    quest_overlap: [224, 1526, 94467]
    quest_context: "In Defense of the King's Lands hunts the Stonesplinter troggs in the valley. On Forever, Questie places the Minor Manifestation of Fire and the Brazier of the Dormant Flame of both Call of Fire quests (1526, 94467) there too. Yonder asks only a bow to the stone kings, with no kill and no quest."
    sources: "the Codex's valley-of-kings page; object 175739's text"
  - id: loch-modan-stonewrought-dam
    tier: off
    gestures: [AWE, AMAZE, GAZE, LOOK]
    area: Stonewrought Dam   # placed: the client's overlay: 47.9, 12.7
    hint_area: { x: 51.0, y: 13.0, r: 4 }
    danger: "Guarded for the Horde (the dam's mountaineers and Chief Engineer Hinderweir VII, level 40), Dark Iron saboteurs for everyone"
    quest_overlap: [250, 280, 283, 1558]
    quest_context: "A Dark Threat Looms sends the Alliance from Chief Engineer Hinderweir VII to a suspicious barrel and an explosive charge on the dam, set by the Dark Irons. Children's Week's The Stonewrought Dam brings an orphan to the middle of the dam once a year, to see the waterfall. Yonder asks for a look over the loch at any time, with no quest, no barrel and no orphan."
    sources: "the client's AreaTable and overlay; the dump's spawns (the dam's mountaineers and engineer, the Dark Iron insurgents and sappers); the WoWWiki archive's Stonewrought Dam page (Lands of Conflict, p. 78: the snowmelt of Ironforge's mountain, the loch more than doubled, Franclorn Forgewright, a Dark Iron, its architect)"
  - id: loch-modan-horde-runners
    tier: hidden
    faction: horde   # its keeper attacks the other side: this side's alone
    creature: 2478   # Haren Swifthoof, who runs with Gradok (2477) and Thragomm (7170): dump 55.5, 67.1, a path up the east shore and back
    found: target   # they never stop running
    hint_area: { x: 60.0, y: 60.0, r: 9 }
    danger: "Deadly to the Alliance (three elites, levels 19 to 21), friends to the Horde"
    sources: "the dump's spawns and their path; the client's display tables (two orcs of one face, a tauren); the WoWWiki archive's Gradok page"
  - id: loch-modan-thelsamar
    tier: town
    faction: alliance   # its town's: for that faction alone
    reading: Ironforge - the Awakening of the Dwarves
    object: 175736   # dump 35.5, 49.0; Wowhead's page alike
    hint_area: { x: 33.4, y: 45.6, r: 8 }
    danger: "Quiet"
    sources: "object 175736's text"
quarry:
  id: 1398   # Boss Galgosh
  sources: "the WoWWiki archive's Boss Galgosh page (the platform, the title); quest 217's text (Grawmug); the dump's spawns"
---
## loch-modan-valley-of-kings
Of three great hammers, two were set in stone.
In life they shared no hall and shared no throne.
Their sons set them together by the road,
facing the south, where once the third one's fires glowed.
? In the lake country's south-west, two great figures guard a pass. Bow before the two stone kings.
= Bronzebeard and Wildhammer, side by side, raised by their sons. Their peoples parted ways later. The statues did not.
+ The whole war is in a dwarven history, War of the Three Hammers: Thaurissan's summoning woke Ragnaros, and the statues were meant as a warning to all who would attack the dwarven kingdoms, and a reminder of what the Dark Irons paid.

## loch-modan-stonewrought-dam
At the head of the loch, the dwarves have shut a valley with a wall of stone
and kept the mountain's snowmelt behind it.
The lake they made is more than twice the one they found.
Their wall is counted among the wonders of the world. Climb onto it and see why.
? The Stonewrought Dam, at Loch Modan's northern end. From the dam, look out over the loch in awe.
= Stonewrought Dam, the dwarves' wall across the head of Loch Modan: it holds back the snowmelt of Ironforge's mountain, and more than doubled the loch.
+ Few know it, but the dam is a Dark Iron's work: Franclorn Forgewright, a master architect before the War of the Three Hammers. 'Stonewrought' was the name given to his works.

## loch-modan-horde-runners
Three of the Horde run the Loch's eastern shore,
from the hills south of the water to the foot of the dam and back,
round and round, in the very middle of the dwarves' country.
Two of them are orcs. It is the third you want.
? The east shore of the Loch, anywhere from the southern hills to the dam: they keep running. Speak to the tauren among the runners.
= Haren Swifthoof, a tauren, Horde Runner, with Gradok and Thragomm: three elite runners of the Horde, lapping the shore of an Alliance lake.
+ Gradok and Thragomm share one face: the same orc, twice over.

## loch-modan-thelsamar
The lake-road inn keeps an account of stone becoming flesh.
Seek the sleepers who woke beneath the earth and found themselves mortal.
The vault lies south of this lake.
? Thelsamar's inn. Open the history of the dwarves' awakening.
= Ironforge - the Awakening of the Dwarves, in Thelsamar. The vault it names, Uldaman, lies south of the Loch, in the Badlands.
+ The dwarves named their land Khaz Modan for the Titan Khaz'goroth, and built a forge for him in the heart of the mountain. The city grew around it.

## quarry
The troggs who took the League's dig in the Loch's south-east
answer to a chieftain who stands on the excavation's platform,
among his diggers and a berserk one.
He calls himself the boss, and none of his tribe argues.
= Boss Galgosh, Stonesplinter Chieftain, on the platform of the dig in the Loch's south-east. Magosh, the tribe's shaman and as rare a sight, keeps the same dig, a little east of him.
+ The mountaineers' scouts send the bold after another trogg, Grawmug, in a cave south-west of the Loch.
