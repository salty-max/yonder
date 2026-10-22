---
zone: 1418   # Badlands
client: both
# the spots, pinned by the data (scripts/expeditions.py resolves them): object (every spawn of it on
# this map), creature (one that stands still, or found by targeting it), trigger (a quest's exploration
# trigger) or area (a sub-area of the game's; its hint placed by its map overlay, or an anchor inside
# it: a creature, an object, a graveyard). gestures: the emotes it accepts, the story's own first.
riddles:
  - id: badlands-hidden-crypt
    tier: hidden
    name: The crypt above the diggers
    object: 144181
    position_check: questie
    hint_area: { x: 57.0, y: 40.5, r: 3 }
    danger: "Guarded (the Badlands approach)"
    sources: "Sword of the Barbarian King (144181), Classic world spawn and Questie 57.25, 40.03; https://www.wowhead.com/tbc/object=144181/sword-of-the-barbarian-king#comments, firsthand crypt visits; https://wowwiki-archive.fandom.com/wiki/Crypt_(Badlands), ordinary path and seated armoured skeleton"
  - id: badlands-apocryphans-rest
    tier: off
    gestures: [GAZE, AWE, AMAZE, PONDER, THINK, LOOK, PEER, STARE]
    area: Apocryphan's Rest   # placed: the client's overlay: 15.7, 61.8, half-size 5.7 by 7.9
    hint_area: { x: 16.0, y: 60.0, r: 8 }
    danger: "Guarded (giant buzzards, coyotes and ridge stalkers, levels 39 and 40)"
    sources: "the WoWWiki archive's Apocryphan's Rest and Badlands pages; the dump's spawns"
  - id: badlands-funeral-ground
    tier: hidden
    gestures: [MOURN, PRAY, KNEEL]
    name: The funeral ground above the road
    landmark: badlands-funeral-ground   # the client's own placement of the middle pyre, read from its map files
    radius: 20
    hint_area: { x: 8.5, y: 54.5, r: 1.5 }
    danger: "Quiet"
    sources: "the pinned client's map files: funeralpyre01.m2 (file 202295), unique id 355310, in azeroth_36_44_obj0.adt, among tauren and troll mummies, tiki masks, tauren kites and orc weapons, placed the same on Forever (wow-data landmark badlands-funeral-ground, source client-map); the dump's spawns near it (the Spirit Healer some 15 yards off, a Ridge Stalker Patriarch at 45)"
quarry:
  id: 2850   # Broken Tooth
  sources: "the WoWWiki archive's Broken Tooth page (asleep in the sun; the quickest claws); the dump's spawns; https://www.wow-petopia.com/classic/attackspeed.php (Classic's fastest cat)"
---
## badlands-hidden-crypt
Above the dwarves who dig in the red waste,
an unmarked path climbs where their work does not.
Under stone, an armoured figure still has a seat.
Find the chamber whose occupant has outlasted his flesh.
? Above Sigrun Ironhew's camp, southeast of Hammertoe's Digsite. Follow the unmarked path uphill and enter the crypt, as far as the throne.
= A crypt above the dwarves' camp in the Badlands. An armoured skeleton sits on a stone throne, with a sword close by.
+ The blade is called the Sword of the Barbarian King. It offers a title, though hardly an account of who occupied this chamber.

## badlands-apocryphans-rest
South of the Horde's stockade on the western cliffs,
something died that was bigger than a keep, and it lies where it fell:
a cage of ribs the vultures have long since picked clean.
It has a name on the maps, and nothing more. Take in what remains among its bones.
? South of Kargath, on the Badlands' western side. Among the bones, look at how big they are.
= Apocryphan's Rest: the skeleton of a dragon, south of Kargath. Whose bones they were, nobody in the Badlands says.
+ The black dragonflight still keeps a ravine of its own, at the waste's far eastern edge.

## badlands-funeral-ground
South of the Horde's hold in the red waste, a ledge above the road keeps the Horde's dead:
tauren wrapped for the pyre, trolls under their masks, orc blades laid beside them.
Most who come here arrive as spirits, looking for the way back.
Come while you are breathing, and pay your respects.
? The ledge south of Kargath, at the Badlands' graveyard. Mourn among the pyres.
= The funeral ground above the road: three pyres on a ledge south of Kargath, tauren and troll dead wrapped for burning, their weapons and offerings beside them.
+ The Spirit Healer at its edge raises those who fall in the Badlands. Those on the pyres are past raising.

## quarry
In the north of the waste, a cougar with a broken fang
lies about in the sun, and seems to be asleep.
His stillness is a poor guide to the speed of his claws.
= Broken Tooth, a cougar of the Badlands, sunning himself in the north, around Angor Fortress and Hammertoe's Digsite and up to the Maker's Terrace.
+ Tamed, he keeps the speed of those claws, which makes him a prize among hunters.
