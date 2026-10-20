---
zone: 1435   # Swamp of Sorrows
client: both
# the spots, pinned by the data (scripts/expeditions.py resolves them): object (every spawn of it on
# this map), creature (one that stands still, or found by targeting it), trigger (a quest's exploration
# trigger) or area (a sub-area of the game's; its hint placed by its map overlay, or an anchor inside
# it: a creature, an object, a graveyard). gestures: the emotes it accepts, the story's own first.
riddles:
  - id: swamp-of-sorrows-stonard
    tier: town
    faction: horde   # its town's: for that faction alone
    reading: The New Horde
    object: 175752   # dump 47.6, 55.0; Wowhead's page alike
    hint_area: { x: 51.2, y: 53.2, r: 8 }
    danger: "Quiet"
    sources: "object 175752's text"
  - id: swamp-of-sorrows-pool-of-tears
    tier: off
    gestures: [PEER, LOOK, GAZE]
    area: Pool of Tears   # placed: the client's overlay
    hint_area: { x: 70.0, y: 51.5, r: 9 }
    danger: "Guarded (dragonkin and sawfin frenzies, to level 45)"
    quest_overlap: [1424, 1445, 1475]
    quest_context: "Pool of Tears and Into The Temple of Atal'Hakkar ask for artifacts and tablets from the temple's stones around the lake, and The Temple of Atal'Hakkar for fetishes from the Atal'ai who haunt it. Yonder asks only a look into the water, with no item and no quest."
    sources: "warcraft.wiki.gg's Temple of Atal'Hakkar page (the Atal'ai's temple for Hakkar's return, Ysera smashing it beneath the marshes, her dragons guarding the ruins, the sinking leaving the rituals undisturbed); the client's AreaTable and overlay"
quarry:
  id: 14445   # Lord Captain Wyrmak
  sources: "the WoWWiki archive's Lord Captain Wyrmak and Sorrowmurk pages (the dragonspawn, the acid breath); the dump's path"
---
## swamp-of-sorrows-stonard
In the stone fortress above the mire, seek a child's name that meant a lifetime in chains.
A warden chose it for the orphan he raised.
The story did not end as he intended.
? Stonard. Read the account of the Horde's new beginning. The name belongs to its story.
= The New Horde, in Stonard: Aedelas Blackmoore and the orphan he called Thrall.
+ Doomhammer fell freeing one of the camps. Thrall took up his warhammer and his black plate, and became warchief of the Horde.

## swamp-of-sorrows-pool-of-tears
In the east of the swamp, trolls who served a blood god raised him a temple,
and a dragon who dreams, learning whom they meant to call back, broke it beneath the marsh.
A lake has lain over it ever since,
and it keeps what it covers from all but the most attentive eye.
? The Pool of Tears, in the east of the swamp: peer into the lake.
= The Pool of Tears, over the sunken Temple of Atal'Hakkar. The Atal'ai trolls built the temple for the return of Hakkar the Soulflayer, and Ysera, learning of their plans, smashed it beneath the marshes. Her green dragons keep watch over the ruins.
+ The sinking did not end the rituals. Under the water, the Atal'ai went on with them undisturbed.

## quarry
East of the sunken temple, dragonspawn hold the Sorrowmurk,
captains and elders among them, and above the captains walks one with a lord's title.
He keeps a long round, from the Pool of Tears down the marsh's eastern edge and back.
= Lord Captain Wyrmak, an elite dragonspawn, walking the Sorrowmurk and the shores of the Pool of Tears.
+ His breath is acid, and it builds on you, up to ten times over if you stay in it.
