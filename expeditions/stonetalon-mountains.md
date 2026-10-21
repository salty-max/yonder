---
zone: 1442   # Stonetalon Mountains
client: both
# the spots, pinned by the data (scripts/expeditions.py resolves them): object (every spawn of it on
# this map), creature (one that stands still, or found by targeting it), trigger (a quest's exploration
# trigger) or area (a sub-area of the game's; its hint placed by its map overlay, or an anchor inside
# it: a creature, an object, a graveyard). gestures: the emotes it accepts, the story's own first.
riddles:
  - id: stonetalon-mountains-nizzik
    tier: off
    creature: 4085   # Nizzik, Venture Armor Salesman, dump 62.7, 40.2, on the Cragpool Lake waterwheel; Wowhead's point alike
    found: target   # among the company's workers: only by speaking to him
    hint_area: { x: 61.5, y: 41.5, r: 4 }
    danger: "Guarded (Venture Co. engineers, builders and machine smiths, levels 20 to 22)"
    sources: "the dump's spawns, faction (friendly to all) and wares; the client's display tables (a goblin); the WoWWiki archive's Nizzik page (the far platform of the Cragpool Lake waterwheel); object 19569 (the sign on the Webwinder Path)"
  - id: stonetalon-mountains-sun-rock
    tier: town
    faction: horde   # its town's: for that faction alone
    creature: 11074   # Hgarth, Artisan Enchanter, dump 49.2, 57.2
    found: target   # in the town: only by speaking to him
    hint_area: { x: 48.0, y: 58.0, r: 3 }
    danger: "Quiet"
    sources: "the dump's spawn and his words (the one whose skill exceeds his own)"
  - id: stonetalon-mountains-smiling-log
    tier: off
    gestures: [SMILE]
    name: The smiling log
    landmark: stonetalon-smiling-log   # the client's own placement of the log, read from its map files
    radius: 12
    hint_area: { x: 58.1, y: 67.8, r: 1.5 }
    danger: "Quiet (the Alliance camp across the road attacks the Horde)"
    sources: "the pinned client's map files: stonetreelog02.m2 (file 202634), unique id 230720, in kalimdor_31_30_obj0.adt, placed the same on Forever (wow-data landmark stonetalon-smiling-log, source client-map, bin/placements.ts); the log's end texture (file 198335), two knots for eyes and the rings mirrored into a smile; the WoWWiki archive's Easter eggs page (the Webwinder Path's fallen trees, one end adorned with smiley faces, screenshot Webwinder smile.jpg, 2008); the same three log models, with the same texture, at Windshear Crag and along the Blackwolf River; the dump's spawns near it (a rabbit, Gaxim Rustfizzle at 78 yards and Kaela Shadowspear at 98, both attacking the Horde)"
quarry:
  id: 4030   # Vengeful Ancient
  sources: "the WoWWiki archive's Vengeful Ancient page (a treant roaming the Charred Vale); the dump's spawn and the flame spirits and burning destroyers of the vale"
---
## stonetalon-mountains-nizzik
In the stone mountains, the Venture Company fells the forest and works the lake,
and its workers take every visitor for a thief.
Out on the company's great wheel, one of its own sells armour to all comers.
Business is business. Find the salesman.
? Windshear Crag, at Cragpool Lake. Cross to the far platform of the Venture Co.'s waterwheel and speak to the goblin selling armour.
= Nizzik, the Venture Co.'s armour salesman, on the waterwheel at Cragpool Lake: friendly to every traveller, among company workers who attack them all.
+ Down the Webwinder Path, the company has signposted where its claim stops: 'End of Venture Co. Lands'.

## stonetalon-mountains-sun-rock
In the Horde's retreat among the stone mountains, an enchanter teaches,
and he is as good as any in the world but one.
Those he has taught all he knows, he sends on to her. Ask him who she is.
? Sun Rock Retreat. Speak to the enchanting trainer about his teacher.
= Hgarth, Artisan Enchanter, at Sun Rock Retreat: 'There is only one whose skills exceed my own... She is Annora, and you may find her... in Uldaman.'
+ Annora keeps to the halls of Uldaman, under the Badlands, among its troggs and its dead: a strange home for the best enchanter in the world.

## stonetalon-mountains-smiling-log
On the spider-haunted path that winds down out of the stone mountains,
a fallen tree lies by the road, across from a small camp, sawn clean through.
Its cut end has two knots for eyes, and the rings beneath them turn up at the corners.
Show it the same face.
? The Webwinder Path, across the road from the small Alliance camp halfway down it. Find the fallen log on the road's west side and smile at its sawn end.
= The smiling log, on the Webwinder Path: a fallen tree of the stone mountains whose sawn end wears two knots for eyes and a smile in its rings.
+ It is not the only one. The logs the Venture Co. leaves at Windshear Crag wear the same face.

## quarry
In the vale the fire took, some of the trees still walk.
Among the charred ancients,
seek the one whose name promises an answer to the burning.
= The Vengeful Ancient, a treant of the Charred Vale, among its charred ancients.
+ The vale burns still: flame spirits and burning destroyers roam it, and the ancients walk among them.
