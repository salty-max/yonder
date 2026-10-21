---
zone: 1429   # Elwynn Forest
home: alliance   # a starting zone: its riddles are its faction's alone
client: both
# the spots, pinned by the data (scripts/expeditions.py resolves them): object (every spawn of it on
# this map), creature (one that stands still, or found by targeting it), trigger (a quest's exploration
# trigger) or area (a sub-area of the game's; its hint placed by its map overlay, or an anchor inside
# it: a creature, an object, a graveyard). gestures: the emotes it accepts, the story's own first.
riddles:
  - id: elwynn-forest-cats
    tier: near
    gestures: [MEOW, PURR]
    name: Donni Anthania's Cats
    creature: 6367   # Donni Anthania, dump 44.2, 53.4, in her house: her four cats at her feet (Bombay 7385, Wowhead places none of them)
    companions: [7381, 7382, 7384, 7385]   # Silver Tabby, Orange Tabby, Cornish Rex, Bombay
    hint_area: { x: 45.0, y: 52.5, r: 4 }
    danger: "Quiet"
    sources: "the dump: Donni Anthania <Crazy Cat Lady> and her four cats in her house, and who sells cats (npc_vendor: her four carriers, forty silver each; Lil Timmy's White Kitten, one at a time); warcraft.wiki.gg's Donni Anthania page"
  - id: elwynn-forest-goldshire-children
    tier: off
    gestures: [SHIVER, SCARED, COWER, CRINGE, GASP, NERVOUS]
    name: The children's room
    creature: 805   # Cameron, Questie 46.2, 61.9: the six spawn on his spot, upstairs in the house of Goldshire's skinner and leatherworker, and stand in a ring around it
    found: place   # the room is the subject: the children walk out and come back, the room stays
    radius: 15
    position_check: questie   # no Wowhead point: Questie's 46.2, 61.9 against the dump's spawn
    hint_area: { x: 45.5, y: 61.0, r: 3 }
    danger: "Quiet"
    quest_overlap: [91746, 91751, 97922, 97924]
    quest_context: "Forever's Camping 101: Leatherworking and Camping 101: Skinning send new players to Adele Fielder and Helene Peltskinner, downstairs in the same house, and Helene gives Rough Wolf Pelts and takes Elmpaw's Head. Yonder asks for a shiver upstairs, by the children's ring, with no trainer and no quest."
    sources: "the dump's spawn group 19989 ('Elwynn Forest - Goldshire - Creepy Goldshire Children - Day RP'): Cameron, Dana, John, Lisa, Aaron and Jose (805, 804, 806, 807, 810, 811) in one formation, spawned only while game event 401 runs (condition 9110: 'DayTime 7AM to 12AM'), their path round Goldshire and back, dbscripts_on_creature_movement 80503 (each child to a place around Cameron, upstairs) and the path's last wait of five hours; Questie's coordinates (no Wowhead point); the WoWWiki archive's Children of Goldshire page (the house with the skinning and leatherworking trainers, the second floor, the pentagram, silent and unmoving, Cameron always in the middle; first reported in 2008, and scripted in the game this journal is played on)"
  - id: elwynn-forest-terry-palin
    tier: off
    gestures: [SING]
    creature: 1650   # Terry Palin, Lumberjack, dump 83.0, 63.3, at the Eastvale Logging Camp; Wowhead 82.8, 63.2
    hint_area: { x: 82.0, y: 62.5, r: 3 }
    danger: "Quiet"
    sources: "the dump's spawn; the WoWWiki archive's In-jokes and references, Eastern Kingdoms page (Terry Palin: Terry Jones and Michael Palin, who wrote the Lumberjack Song)"
  - id: elwynn-forest-heroes-vigil
    tier: hidden
    gestures: [SALUTE, BOW, KNEEL, MOURN, PRAY]
    area: Heroes' Vigil   # placed: the Stone of Remembrance, dump 74.5, 51.7 (no Wowhead position: the area solves, the stone places the hint)
    anchor: { object: 20923 }   # what places its hint: the area has no overlay of its own
    hint_area: { x: 75.0, y: 55.7, r: 8 }
    danger: "Guarded (the Defias Rogue Wizards)"
    quest_overlap: [1786, 1787, 5545, 91724]
    quest_context: "The Tome of Divinity, a paladin's quest, raises Henze Faulk nearby and takes a Defias Script from the Rogue Wizards about Stone Cairn Lake, A Bundle of Trouble gathers wood about it, and Forever's Delicate Instruments hunts the same wizards. Yonder asks only a salute to the fallen named on the stone, with no kill and no quest."
    sources: "the WoWWiki archive's Heroes' Vigil, Stone of Remembrance and Stone Cairn Lake pages; object 20923"
quarry:
  id: 471   # Mother Fang
  sources: "the WoWWiki archive's Mother Fang page (the inner mine, the hunter's pet, the meat); https://classic.warcraftdb.com/data/spell/12023 (Web, cast by Mother Fang); the pinned dump's spawn and creature_ai_scripts"
---
## elwynn-forest-cats
In a house on the road between the abbey and the gold town,
a woman lives with four cats, and her title says what the neighbours make of it.
The cats have the run of the place.
Address them in their own tongue.
? Donni Anthania's house, on the road from Northshire down to Goldshire. Answer one of the cats in its own tongue. A meow will do.
= Donni Anthania, the Crazy Cat Lady, and her four cats: a Bombay, a Cornish Rex, an Orange Tabby and a Silver Tabby. Every one of them is for sale, at forty silver a carrier.
+ They are four of the five cats anyone in the world will sell you. The fifth, a white kitten, is carried about Stormwind by a boy called Lil Timmy, and sold one at a time.

## elwynn-forest-goldshire-children
In the town at the forest's crossroads, six children walk the roads together,
always in the same order, and always back to the same house.
Upstairs, of a morning, they stand in a ring around one of them, silent, for hours.
Climb to their room, if you have the nerve, and see how it feels.
? Goldshire, the house on its north-east side by the lake, where the skinner and the leatherworker keep shop. Upstairs, in the morning, by the children's ring, let yourself shiver.
= The children of Goldshire: Cameron in the middle of the ring, Dana, John, Lisa, Aaron and Jose around him. They walk out together, and they always come back to this room.
+ They come out in the morning, walk their round once, and stand in their room until noon. Then they are gone.

## elwynn-forest-terry-palin
In the logging camp at the forest's eastern edge, a lumberjack keeps the stores.
Somewhere far away there is a song about men like him,
about the trees they fell and the nights they sleep so soundly.
He has never heard it. Be the first to give it to him.
? The Eastvale Logging Camp, in Elwynn's east. Sing to the lumberjack who keeps the camp's stores.
= Terry Palin, Lumberjack, of the Eastvale Logging Camp.
+ His name joins two men of another world, who wrote a famous song about a lumberjack.

## elwynn-forest-heroes-vigil
In a lake shaped like a ring, an island holds a ring of stones
and a stone raised so that heroes would be remembered.
Renegade wizards hold the island now, gone over to the bandits.
Cross the water, and give the stone what it was raised for.
? The ring-shaped lake north of the road to Eastvale has an island in its middle. Heroes are honoured there. Kneel by the memorial stone.
= Heroes' Vigil, and its Stone of Remembrance: a cairn for the dead of the First War, when the orcs sacked Goldshire and the lands around it. The lake takes its name from the cairn.
+ The lake was a place of pilgrimage once. The Defias' renegade wizards have made it a dangerous one.

## quarry
East of the gold town, in the mine the kobolds dig,
a mother of spiders hunts the inner galleries.
Her hunting ground lies beyond the kobolds' workings.
Go past the kobolds, and keep going.
= Mother Fang, a spider of the Jasperlode Mine. A hunter can tame her: a fair first companion, if a demanding one, for she eats only meat.
+ Her web holds whoever she catches for a few seconds, long enough for her bite.
