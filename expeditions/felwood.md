---
zone: 1448   # Felwood
client: both
# the spots, pinned by the data (scripts/expeditions.py resolves them): object (every spawn of it on
# this map), creature (one that stands still, or found by targeting it), trigger (a quest's exploration
# trigger) or area (a sub-area of the game's; its hint placed by its map overlay, or an anchor inside
# it: a creature, an object, a graveyard). gestures: the emotes it accepts, the story's own first.
riddles:
  - id: felwood-morlos-aran
    tier: off
    gestures: [PONDER, THINK, MOURN, SIGH]
    area: Morlos'Aran   # placed: the client's overlay: 57.6, 87.9, half-size 3.7 by 4.1
    hint_area: { x: 57.0, y: 87.0, r: 4 }
    danger: "Guarded (felpaw wolves, angerclaw bears and ironbeak owls, levels 47 and 48)"
    sources: "the WoWWiki archive's Morlos'Aran page (its sister ruins); the dump's spawns"
  - id: felwood-talonbranch
    tier: town
    faction: alliance   # its town's: for that faction alone
    gestures: [PET, PAT, SOOTHE, COMFORT]
    creature: 11181   # Shi'alune <Kaerbrus' Pet>, dump 61.8, 23.7; Wowhead 61.4-62.6, 23.4-23.8, about Kaerbrus <Hunter Trainer> (5501)
    found: target   # it walks about its master: only by targeting it near
    hint_area: { x: 62.4, y: 24.4, r: 3 }
    danger: "Quiet"
    sources: "the dump's spawns (Shi'alune <Kaerbrus' Pet>, the Elder Shadowmaw Panther's model; Kaerbrus <Hunter Trainer> and his words, 'Welcome to the Cenarion Circle'; Golhine the Hooded <Druid Trainer>; Nalesette Wildbringer <Pet Trainer>); warcraft.wiki.gg's Shi'alune page (a nightsaber, Kaerbrus its master)"
quarry:
  id: 7137   # Immolatus
  sources: "https://wowwiki-archive.fandom.com/wiki/Immolatus (Knock Away, original level 56 rare elite); the pinned dump's path and creature_ai_scripts (10101 Knock Away); the dump's loot (Lifeless Stone, Deeprock Salt, Core of Earth)"
---
## felwood-morlos-aran
At the southern edge of the poisoned wood, the stones of an elven town still stand,
and its name ends as theirs did on the dark shore and in the forest to the south.
Remember the towns whose names it echoes, and grieve for what has become of this one.
? Morlos'Aran, at Felwood's southern edge. Among the ruins, ponder what became of the town.
= Morlos'Aran, one of the old night elf settlements whose names end alike: Ameth'Aran and Bashal'Aran in Darkshore, Ordil'Aran in Ashenvale, Tethris Aran in Desolace.
+ A druid of the Emerald Circle keeps watch by the ruins. The wood around him is still sick.

## felwood-talonbranch
At the edge of the corrupted forest, three teachers of the wild keep a glade together:
one for druids, one for hunters, one for the beasts that hunters keep.
The hunters' teacher never works alone. A great cat keeps at his side.
It has earned the kindness he teaches others to show their own.
? Talonbranch Glade, by the hunters' trainer: pet the nightsaber at his side.
= Shi'alune, the nightsaber Kaerbrus keeps as his own companion while he trains the hunters of Talonbranch Glade, whom he welcomes to the Cenarion Circle.
+ Talonbranch Glade has all three teachers of the wild in one camp: Golhine the Hooded for druids, Kaerbrus for hunters, and Nalesette Wildbringer for the hunters' pets.

## quarry
In the scarred vale where fire once fell on the forest,
an infernal still burns.
Seek the named demon among the forest's wounds.
= Immolatus, an elite infernal of Shatter Scar Vale.
+ When the fire goes out of him, stone is what remains: lifeless stone mostly, sometimes salt from deep rock or a core of earth.
