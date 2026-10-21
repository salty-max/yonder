---
zone: 1434   # Stranglethorn Vale
client: both
# the spots, pinned by the data (scripts/expeditions.py resolves them): object (every spawn of it on
# this map), creature (one that stands still, or found by targeting it), trigger (a quest's exploration
# trigger) or area (a sub-area of the game's; its hint placed by its map overlay, or an anchor inside
# it: a creature, an object, a graveyard). gestures: the emotes it accepts, the story's own first.
riddles:
  - id: stranglethorn-vale-booty-bay
    tier: near
    reading: Wrath of Soulflayer
    object: 175856   # dump 27.8, 77.3, in Booty Bay
    hint_area: { x: 27.0, y: 76.0, r: 4 }
    danger: "Quiet"
    quest_overlap: [2843]
    quest_context: "Gnomer-gooooone! waits on Scooty and his transponder beside the shelf. Yonder asks only that the book be read, with no quest."
    sources: "object 175856's text"
  - id: stranglethorn-vale-brikk
    tier: near
    creature: 2836   # Brikk Keencraft, Master Blacksmith, dump 29.0, 75.6, in Booty Bay's smithy; Wowhead 29.0, 75.4
    found: target   # in the town: only by speaking to him
    hint_area: { x: 28.0, y: 74.5, r: 3 }
    danger: "Quiet"
    sources: "Brikk Keencraft's own words (his gossip: a stranger's, a novice's, an artisan's); Saru Steelfury's words to an artisan smith in Orgrimmar ('I do not like Goblins but his knowledge of the secret of steel is unmatched by any I know of'); the client's display tables (a goblin); the WoWWiki archive's Brikk Keencraft page"
  - id: stranglethorn-vale-emperors-tomb
    tier: hidden
    gestures: [BOW, KNEEL]
    object: 54   # dump 24.7, 8.9; Wowhead 24.7, 9.0
    hint_area: { x: 26.6, y: 12.4, r: 8 }
    danger: "Perilous (the Bloodscalp)"
    quest_overlap: [207]
    quest_context: "Kurzen's Mystery takes the Fourth Troll Legend from the tomb. Yonder asks only a bow to the emperor, with no item and no quest."
    sources: "object 54 (its name); the Codex's gurubashi-empire and zulgurub pages"
  - id: stranglethorn-vale-janeiro
    tier: hidden
    gestures: [HUG]
    area: Janeiro's Point   # the islet's own sub-area: the embrace counts anywhere on it
    anchor: { creature: 1493 }   # what places its hint: Mok'rash, the sea giant who keeps the islet (dump 23.3, 72.1), never a meeting
    hint_area: { x: 24.0, y: 71.0, r: 3 }
    danger: "Perilous (Mok'rash, a sea giant, elite, level 50)"
    quest_overlap: [6571]
    quest_context: "Warsong Supplies sends the Horde after scattered Warsong shipments, one of them on the islet. Yonder asks for an embrace of the statue, with no quest and no crate."
    sources: "the WoWWiki archive's Janeiro's Point page (a great statue on the islet outside Booty Bay, a beacon to all travellers, Mok'rash's abode) and In-jokes and references, Eastern Kingdoms page (Christ on Corcovado); the dump's spawn of Mok'rash; the client's AreaTable"
  - id: stranglethorn-vale-gromgol
    tier: town
    faction: horde   # its town's: for that faction alone
    creature: 3149   # Nez'raz, Zeppelin Master, dump 31.4, 29.9, atop the tower
    found: target   # in the town: only by speaking to him
    hint_area: { x: 32.0, y: 28.0, r: 3 }
    danger: "Quiet"
    sources: "the dump's spawn and his words"
quarry:
  id: 14490   # Rippa
  sources: "the WoWWiki archive's Rippa page (a frenzy with a name); the dump's paths (round the southern tip, into Booty Bay's harbour) and loot (Raw Bristle Whisker Catfish, 39%)"
---
## stranglethorn-vale-booty-bay
A god's appetite emptied a jungle kingdom.
In the pirates' port, find the account of his worshippers' answer
when they could no longer pay what he demanded.
? Booty Bay. Open the book about the hungry god and his followers.
= Wrath of Soulflayer, in Booty Bay. The Gurubashi fed souls to Hakkar, then drove out the blood god and the priests who still served him. Those priests fled north to the swamps.
+ The Darkspear were among the tribes that went their own way after that war. And some spoke of a prophecy, that Hakkar would one day be reborn and consume the world whole.

## stranglethorn-vale-brikk
In the goblins' port at the jungle's end, a goblin keeps the smithy,
and the master of Orgrimmar's forge, who likes no goblin, sends his best pupils to him all the same.
Not everyone who walks in believes he is the smith.
Ask him.
? Booty Bay, in the smithy. Speak to the goblin master blacksmith.
= Brikk Keencraft, Master Blacksmith of Booty Bay: 'Yeah? Of course I'm a smith. What, you think Dwarves are the only ones worth their weight in anvils? Fine, be that way. Go get a dwarf to help you!'
+ Saru Steelfury, who sends him his pupils from Orgrimmar: 'I do not like Goblins but his knowledge of the secret of steel is unmatched by any I know of.'

## stranglethorn-vale-emperors-tomb
In the north-western ruins of the troll empire that ruled the south
before there were kingdoms of men, a tomb is all that is left
of one of its emperors. Find it, and pay him the homage his subjects once owed.
? The Ruins of Zul'Kunda, in Stranglethorn's north-west. Bow before the tomb.
= The Emperor's Tomb, at Zul'Kunda.
+ The Gurubashi empire once stretched across the south. Its descendants hold its ruins now, and Hakkar is back in Zul'Gurub.

## stranglethorn-vale-janeiro
Off the goblins' port, on a rock in the sea, a great statue spreads its arms
to every ship that sails in, as if in welcome.
A giant of another kind has made the rock his home.
Swim out, and answer those open arms.
? Janeiro's Point, the islet north-west of Booty Bay's harbour mouth. On the rock, hug the statue, and mind the sea giant.
= Janeiro's Point, and its great statue, arms open, a beacon to every traveller who sails into Booty Bay.
+ Its pose is borrowed from another world's great statue, which watches over a harbour city from a mountain.

## stranglethorn-vale-gromgol
At the top of the Horde's tower in the jungle, a goblin sees the airships off to Orgrimmar,
and has been left at the wrong end of the route.
He would give a great deal for a decent meal from home. Ask him.
? Grom'gol Base Camp, at the top of the zeppelin tower. Speak to the goblin. He will talk without being fed.
= Nez'raz, Zeppelin Master at Grom'gol: his brother talked him into the trade route, and left him the jungle end of it.
+ 'If you come back this way on the Zeppelin, could you bring me something to eat? ... I sure could use something that didn't die weeks before it stopped moving.'

## quarry
In the warm shallows round the jungle's southern tip,
the frenzies are many and small.
Seek the one big enough to have a name.
= Rippa, a frenzy of the shore around Booty Bay: a fish with a name, of all things.
+ It feeds as it swims: a raw bristle whisker catfish is often found inside it.
