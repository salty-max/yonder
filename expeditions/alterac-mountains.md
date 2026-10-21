---
zone: 1416   # Alterac Mountains
client: both
# the spots, pinned by the data (scripts/expeditions.py resolves them): object (every spawn of it on
# this map), creature (one that stands still, or found by targeting it), trigger (a quest's exploration
# trigger) or area (a sub-area of the game's; its hint placed by its map overlay, or an anchor inside
# it: a creature, an object, a graveyard). gestures: the emotes it accepts, the story's own first.
riddles:
  - id: alterac-mountains-rizz
    tier: off
    creature: 2684   # Rizz Loosebolt, Engineering Supplies, dump 47.3, 35.2, caged in the Crushridge ogres' hollow; Wowhead's point alike
    found: target   # behind bars: only by speaking to him
    hint_area: { x: 46.5, y: 36.5, r: 4 }
    danger: "Guarded (Crushridge ogres and brutes, levels 34 to 36)"
    sources: "the dump's spawns, faction (friendly to all) and wares (Schematic: Ice Deflector, sold by no one else); the client's display tables (a gnome); the WoWWiki archive's Rizz Loosebolt page (in a cage in Slaughter Hollow, no quest or other way to free him) and Slaughter Hollow page (the Crushridge ogres' mound)"
  - id: alterac-mountains-simone
    tier: hidden
    gestures: [PRAISE, COMMEND, APPLAUD]
    creature: 7324   # Simone Cantrell, Landscape Architect, dump 83.8, 79.8, at Ravenholdt Manor
    hint_area: { x: 82.8, y: 77.5, r: 7 }
    danger: "Quiet"
    sources: "the dump's spawns (Simone, Winstone Wolfe, Salome); the client's display tables (a night elf); the WoWWiki archive's Simone Cantrell and Salome pages"
quarry:
  id: 14222   # Araga
  sources: "the WoWWiki archive's Araga page (among the mountain lions); the dump's spawns; the WoWWiki archive's Araga page (her own skin: a slight mane, a striped tail); Petopia Classic (a tameable mountain lion)"
---
## alterac-mountains-rizz
The Crushridge ogres keep a hollow in the hills for whatever they drag home,
and one of the things they dragged home still talks, and still trades.
A small engineer sells the tools of his craft through the bars.
Find him, and see what he has to offer.
? In the middle of Alterac, the Crushridge ogres' hollow. In their cave, speak to the gnome in the cage.
= Rizz Loosebolt, a gnome engineer in a Crushridge cage, still selling flux, tubes, blasting powder and parts, and the only plans in the world for an Ice Deflector.
+ No quest frees him. Travellers buy what they need through the bars, and leave him to the ogres.

## alterac-mountains-simone
In the hills above the foothills, a manor hides from all who do not know the way,
a hall for those who work unseen.
And yet someone there works in plain sight, with a title to prove it:
Find the one who keeps the grounds of this most secret house, and let them hear how fine the work is.
? Ravenholdt Manor, up a mountain path north-west of Durnholde Keep. The groundskeeper deserves a little praise.
= Simone Cantrell, a night elf, Landscape Architect to Ravenholdt Manor, hall of the Assassin's League.
+ Near the master stands Winstone Wolfe, whom the manor calls The Wolf. And a housecat, Salome, has the run of the place.

## quarry
Mountain lions own the southern hills of Alterac.
Among them, a lone female has a name of her own.
Search from the yetis' hills down toward the naze.
= Araga, a mountain lion of Alterac's southern hills, from west of the yetis' cave down to Gavin's Naze.
+ Her coat is her own: a slight mane and a striped tail, worn by no other cat.
