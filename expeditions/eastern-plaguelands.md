---
zone: 1423   # Eastern Plaguelands
client: both
# the spots, pinned by the data (scripts/expeditions.py resolves them): object (every spawn of it on
# this map), creature (one that stands still, or found by targeting it), trigger (a quest's exploration
# trigger) or area (a sub-area of the game's; its hint placed by its map overlay, or an anchor inside
# it: a creature, an object, a graveyard). gestures: the emotes it accepts, the story's own first.
riddles:
  - id: eastern-plaguelands-mirador
    tier: off
    gestures: [PET, PAT, SOOTHE, COMFORT]
    creature: 11710   # Mirador, dump 7.4, 43.5, outside Tirion Fordring's cottage
    hint_area: { x: 9.0, y: 45.0, r: 4 }
    danger: "Quiet"
    quest_overlap: [5742]
    quest_context: "Redemption, and the chain after it, is Tirion Fordring's story, told beside his horse. Yonder asks only a hand on Mirador, with no quest."
    sources: "the WoWWiki archive's Mirador page; Of Blood and Honor (2001: Tirion, Eitrigg, the exile); the dump's spawn"
  - id: eastern-plaguelands-pestilent-scar
    tier: off
    gestures: [PEER, LOOK, STARE, SHIVER]
    area: Pestilent Scar   # placed: the client's overlay: 74.1, 62.5
    hint_area: { x: 72.0, y: 60.0, r: 6 }
    danger: "Perilous (the Scourge and the scar's oozes, levels 54 to 60)"
    sources: "the client's AreaTable and overlay; the dump's spawns (living decay and rotting sludge in the scar); the WoWWiki archive's Pestilent Scar page (a natural gorge unlike the Infectis Scar, perhaps a lake the plague dried up, oozes, a fatal fall)"
  - id: eastern-plaguelands-adon
    tier: hidden
    gestures: [BOW, SALUTE, GREET, WAVE, HELLO, HAIL]
    creature: 11706   # Adon, dump 58.4, 16.9, at the road north to Quel'Thalas
    hint_area: { x: 57.0, y: 19.0, r: 4 }
    danger: "Perilous (the Scourge of the north road)"
    sources: "the WoWWiki archive's Adon and Quel'Lithien Lodge pages; the dump's spawn and faction (friendly to all)"
quarry:
  id: 10821   # Hed'mush the Rotting
  sources: "the WoWWiki archive's Hed'mush the Rotting page (an undead ogre, glowing green); the pinned dump's spawns (three towers, one at a time) and creature_ai_scripts (16577 Disease Cloud); the dump's loot (Corruptor's Scourgestone, 100%)"
---
## eastern-plaguelands-mirador
Where the river runs between the two plaguelands, an old knight lives in exile in a cottage,
and outside it his horse waits, as if a war might call any day.
Make a friend of the horse.
? The Thondroril River, at the Eastern Plaguelands' western edge, by a cottage. Pet the horse waiting outside the cottage.
= Mirador, the horse of Tirion Fordring, outside the cottage where his master lives in exile.
+ Tirion lost his lands and his title for saving the life of an orc, Eitrigg, who had once spared his own.

## eastern-plaguelands-pestilent-scar
In the plagued east, the earth falls away into a deep gorge,
older than the plague, its floor long dry.
Only oozes live at its bottom now.
Find its edge, mind your footing, and let your eyes follow the drop all the way down.
? The Pestilent Scar, in the Eastern Plaguelands' south-east. From its edge, peer down into it.
= The Pestilent Scar: a deep pitfall in the blighted earth. Unlike the Infectis Scar, it seems the land's own: a natural gorge, perhaps a lake the plague dried up.
+ Its oozes are the plague's own kind: living decay and rotting sludge, at the bottom of the fall.

## eastern-plaguelands-adon
At the dead country's northern end, where the road climbs toward the elves' kingdom,
one of them stands alone at the way north, and says nothing at all.
Nobody gets past him, and nobody is sent to him. Pay him your respects all the same.
? The Eastern Plaguelands' northern edge, where the road goes on toward Quel'Thalas. Bow to the silent elf.
= Adon, a high elf, alone at the road north to Quel'Thalas: he has no wares, no orders and no words.
+ Close by, at Quel'Lithien Lodge, the last high elves of these lands keep a hunting lodge.

## quarry
An ogre that died and did not stay dead walks the dead country, glowing green.
Seek him by one of three old towers:
the north pass, the eastern wall, or the crown guard in the south-west.
= Hed'mush the Rotting, an undead ogre, by Northpass Tower, Eastwall Tower or Crown Guard Tower.
+ He always carries a Corruptor's Scourgestone, the rarest of the stones the Argent Dawn takes from the Scourge's dead.
