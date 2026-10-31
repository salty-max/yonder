---
zone: 1437   # Wetlands
client: both
# the spots, pinned by the data (scripts/expeditions.py resolves them): object (every spawn of it on
# this map), creature (one that stands still, or found by targeting it), trigger (a quest's exploration
# trigger) or area (a sub-area of the game's; its hint placed by its map overlay, or an anchor inside
# it: a creature, an object, a graveyard). gestures: the emotes it accepts, the story's own first.
riddles:
  - id: wetlands-dun-modr
    tier: near
    creature: 3180   # the Dark Iron Entrepreneur, Speciality Goods, dump 46.6, 18.4, in Dun Modr's inn; Wowhead's points alike
    found: target   # among his kin: only by speaking to him
    hint_area: { x: 47.5, y: 19.5, r: 4 }
    danger: "Perilous (Dark Iron elites, levels 28 to 31)"
    sources: "the dump's spawns, faction (friendly to all) and wares; the client's display tables (a dwarf); the WoWWiki archive's Dark Iron Entrepreneur page (the inn) and Dun Modr page (Lands of Conflict, p. 80: the Dark Irons kill anything that enters their territory; Warcraft II: Tides of Darkness, the battle to retake Dun Modr from the Horde)"
  - id: wetlands-sundown-marsh
    tier: off
    faction: alliance   # its keeper attacks the other side: this side's alone
    gestures: [HELLO, GREET, WAVE, HAIL, BOW]
    creature: 2679   # Wenna Silkbeard, dump 25.6, 25.8; Fradd Swiftgear (2682) beside her
    hint_area: { x: 24.0, y: 28.0, r: 6 }
    danger: "Guarded (crocolisks, bog beasts and raptors all round)"
    sources: "the WoWWiki archive's Sundown Marsh page (the stone house, the windmill); the dump's spawns and wares (one piece at a time); the client's display tables (a dwarf, a gnome); https://www.wowhead.com/classic/item=4381/minor-recombobulator (dispels Polymorph, restores health and mana)"
  - id: wetlands-terl
    tier: hidden
    faction: alliance   # its keeper attacks the other side: this side's alone
    creature: 2153   # Terl Arakor, dump 27.4, 41.2
    found: target
    hint_area: { x: 29.0, y: 39.0, r: 5 }
    danger: "Guarded (mottled raptors), and for the Horde, Terl himself"
    sources: "the dump's spawn, his words and his faction (the Alliance's, hostile to the Horde)"
  - id: wetlands-menethil
    tier: town
    faction: alliance   # its town's: for that faction alone
    reading: The Battle of Grim Batol
    object: 175750   # dump 10.8, 60.8; Wowhead's page alike
    hint_area: { x: 9.0, y: 64.4, r: 8 }
    danger: "Quiet"
    quest_overlap: [1249]
    quest_context: "The Missing Diplomat ends in a brawl with Tapoke Jahn by the shelf. Yonder asks only that the book be read, with no quest."
    sources: "object 175750's text"
quarry:
  id: 1140   # Razormaw Matriarch
  sources: "the WoWWiki archive's Razormaw Matriarch and Raptor Ridge pages (her brood, the cavern); the dump's path"
---
## wetlands-dun-modr
On the road north to the great bridge, the Dark Irons hold a fallen dwarven town,
and they kill whoever comes up the road.
One of them has found a better use for strangers.
Find him at the inn, open for business.
? Dun Modr, on the road to the Thandol Span. In the ruined town's inn, speak to the Dark Iron who sells instead of fighting.
= The Dark Iron Entrepreneur, in Dun Modr's inn: friendly to every traveller, among kin who are friendly to none. He sells heavy dynamite, a red firework, and whatever fine gear has come his way.
+ Dun Modr was a dwarven town before the Dark Irons claimed it. In the Second War, the Alliance fought here to take it back from the Horde.

## wetlands-sundown-marsh
Deep in the marsh, where the crocolisks own the water,
a dwarf and a gnome keep a stone house with a windmill,
and sell what they come by: fine belts and leggings, one of each at a time,
and two gnomish plans, one copy of each.
Call at their door.
? Sundown Marsh, the Wetlands' north-west, west of Ironbeard's Tomb. Say hello to the dwarf among the merchants.
= Wenna Silkbeard, a dwarf, and Fradd Swiftgear, a gnome, in their stone house in Sundown Marsh. Fradd's plans: a Lovingly Crafted Boomstick and a Minor Recombobulator.
+ Fradd's smaller device restores some health and mana, but its particular talent is turning a sheep back into a traveller. An engineer need not wait for the mage's spell to wear off.

## wetlands-terl
North of the old dig, out in the marsh where the raptors hunt,
a man stands alone, and he is not going anywhere.
Ask him what he is doing there. He has an answer, and he will shout it.
? Black Channel Marsh's north edge, north of Whelgar's Excavation Site. Speak to the man standing alone in the marsh.
= Terl Arakor, alone in the marsh: 'This is MY WAGON! MINE!'
+ He stands with the Alliance: a Horde traveller gets no answer from him, only a fight.

## wetlands-menethil
The harbour keeps an account of a prison high above the marsh.
Its captive could burn an army, yet her captors forced her to serve them.
Find the page that tells how she was freed.
? Menethil Harbor. Read the account of the dragon queen's captivity.
= The Battle of Grim Batol, in Menethil Harbor. The Dragonmaw orcs held Alexstrasza captive in the mountain at the Wetlands' eastern edge. Once free, she and the other great dragons destroyed their fortress.
+ Grim Batol was a Wildhammer stronghold first, 'some say cursed'. A small band led by the mage Rhonin destroyed the Demon Soul and freed Alexstrasza.

## quarry
In the Wetlands' east, a ridge of raptors has a cavern.
Seek the matriarch among the Highland and Elder brood.
Their mother does not keep an empty house.
= The Razormaw Matriarch, of level thirty-one, in the cavern of Raptor Ridge, with her Highland and Elder Razormaws.
+ She never strays far from her brood: the cavern, and the slope before it.
