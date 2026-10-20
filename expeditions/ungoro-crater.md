---
zone: 1449   # Un'Goro Crater
client: both
# the spots, pinned by the data (scripts/expeditions.py resolves them): object (every spawn of it on
# this map), creature (one that stands still, or found by targeting it), trigger (a quest's exploration
# trigger) or area (a sub-area of the game's; its hint placed by its map overlay, or an anchor inside
# it: a creature, an object, a graveyard). gestures: the emotes it accepts, the story's own first.
riddles:
  - id: ungoro-crater-simone
    tier: off
    gestures: [WAVE, HELLO, GREET, SMILE]
    creature: 14527   # Simone the Inconspicuous, with Precious (14528): from Golakka Hot Springs (dump 34.3, 40.8) south and back
    found: target   # she keeps walking
    hint_area: { x: 35.0, y: 45.0, r: 5 }
    danger: "Deadly if provoked (she answers a blow with blows that fell a hero), otherwise quiet"
    sources: "the dump's spawn, path and words; the client's display tables (a troll); the WoWWiki archive's Simone the Inconspicuous page (the succubus beneath, Precious, Fool's Plight)"
  - id: ungoro-crater-lakkari
    tier: near
    gestures: [PEER, LOOK, GAZE]
    area: Lakkari Tar Pits   # placed: the client's overlay
    hint_area: { x: 49.5, y: 21.5, r: 9 }
    danger: "Perilous (tar elementals, to level 54)"
    quest_overlap: [4504]
    quest_context: "Super Sticky asks for tar from the elementals of the pits. Yonder asks only a look at what the tar has kept, with no kill and no quest."
    sources: "warcraft.wiki.gg's Lakkari Tar Pits page (the lakes of black tar south of Marshal's Refuge, the bones of hundreds of beasts jutting from the surface, scavengers waiting for the tar's prey); the dump's spawns (Tar Beasts, Creepers, Lurkers and Lords: elementals); the client's AreaTable and overlay"
quarry:
  id: 6584   # King Mosh
  sources: "the WoWWiki archive's King Mosh page (the infamous devilsaur of the north-west); https://www.wowhead.com/classic/npc=6584/king-mosh (period accounts of fear); the pinned dump's path and creature_ai_scripts (14100 Terrifying Roar); the dump's loot (raptor skulls and feathers)"
---
## ungoro-crater-simone
By the hot springs in the crater's west, a troll woman walks with her wolf
and finds everything lovely: the steam, the ferns, the beasts that would eat her.
Be pleasant to her, and only pleasant.
? Golakka Hot Springs, in western Un'Goro. She walks south from there and back. Wave to the troll woman as she passes.
= Simone the Inconspicuous, with Precious, her wolf: 'What a wonderful day to be alive! Look at the beauty that surrounds you, friend.'
+ She is not what she seems: hunters on the trail of an ancient bow know her as Simone the Seductress, a succubus. Strike her as she is, and she answers with blows that fell a hero in one.

## ungoro-crater-lakkari
South of the explorers' refuge, the floor of the crater turns to black lakes
that keep whatever walks into them.
The bones of hundreds of beasts still break their surface,
and what rises from the tar is tar too. Go and see what it has kept.
? The Lakkari Tar Pits, just south of Marshal's Refuge: look out over the tar from its shore.
= The Lakkari Tar Pits: lakes of thick black tar that trap whatever wanders in, the bones of hundreds of beasts jutting from the surface, and elementals of the tar rising out of it.
+ The scavengers know the pits too. They wait at the edges for the tar to catch their next meal.

## quarry
Between the river and the great lakes of the crater's north-west,
the king of the devilsaurs walks.
The crater shakes for him.
= King Mosh, the infamous devilsaur of Un'Goro's north-west.
+ Raptor skulls and feathers are most of what is found on him.
