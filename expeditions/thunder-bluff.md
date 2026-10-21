---
zone: 1456   # Thunder Bluff
home: horde   # a capital: its riddles are its faction's alone
client: both
# the spots, pinned by the data (scripts/expeditions.py resolves them): object (every spawn of it on
# this map), creature (one that stands still, or found by targeting it), trigger (a quest's exploration
# trigger) or area (a sub-area of the game's; its hint placed by its map overlay, or an anchor inside
# it: a creature, an object, a graveyard). gestures: the emotes it accepts, the story's own first.
riddles:
  - id: thunder-bluff-mak
    tier: near
    creature: 3008   # Mak, Journeyman Leatherworker, dump 42.1, 43.5, beside Tarn (11084) and Una (3007); Wowhead's points alike
    found: target   # in the city: only by speaking to him
    hint_area: { x: 43.5, y: 42.0, r: 4 }
    danger: "Quiet"
    sources: "Mak's own words (his gossip); the dump's spawns (Cairne Bloodhoof at 60.3, 51.7, on the same rise); the WoWWiki archive's Mak page"
  - id: thunder-bluff-white-stag
    tier: off
    reading: The White Stag and the Moon
    object: 177208   # dump 78.7, 26.6; Wowhead's page alike
    hint_area: { x: 74.7, y: 26.4, r: 8 }
    danger: "Quiet"
    sources: "object 177208's text"
  - id: thunder-bluff-nibbles
    tier: hidden
    gestures: [PET, PAT, SOOTHE, HELLO, GREET, WAVE]
    creature: 12383   # Nibbles, Prairie Dog, dump 62.1, 57.8, beside Halpa (8401)
    hint_area: { x: 61.5, y: 57.5, r: 3 }
    danger: "Quiet"
    sources: "the dump's spawns and Halpa's wares (the prairie dog whistle)"
# no quarry: a capital has riddles alone
---
## thunder-bluff-mak
On the bluff where the High Chieftain keeps his lodge, a leatherworker is making him a gift.
He has only heard that Cairne lives here. He means to go and see for himself
when the work is fine enough to give, and perhaps hear a word of wisdom.
It is a short walk across the rise. Ask him how the work is going.
? Thunder Bluff's central rise, among the leatherworkers on its western side. Speak to the journeyman.
= Mak, a journeyman leatherworker: 'Cairne himself lives here, they say. Once I have finished crafting a fitting gift, I will seek him out. Perhaps he will have words of wisdom for me.'
+ Cairne Bloodhoof's lodge stands at the other end of the same rise. Mak has not crossed it yet.

## thunder-bluff-white-stag
On the rise of the elders, a tale tells of a white stag
whose antlers tangled in the stars as he fled the hunters,
and of the moon, who freed him for his love. Find the tale.
? Elder Rise. Read the tale of the stag and the moon.
= The White Stag and the Moon: Apa'ro, whom the night elves call Malorne.
+ Their child was Cenarius, who 'would walk the starry path between the waking world and the kingdom of the heavens'.

## thunder-bluff-nibbles
By the chieftain's lodge, a tauren sells prairie dogs to keep as friends,
and keeps one of his own beside his stall, with a name.
Make its acquaintance.
? Thunder Bluff, by the prairie dog seller's stall near Cairne's lodge. Pet the prairie dog with a name of its own.
= Nibbles, Halpa's own prairie dog, beside his stall: Halpa sells prairie dog whistles to anyone who wants a friend of their own.
+ Nibbles is not for sale.
