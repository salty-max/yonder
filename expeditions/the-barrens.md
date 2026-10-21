---
zone: 1413   # The Barrens
client: both
# the spots, pinned by the data (scripts/expeditions.py resolves them): object (every spawn of it on
# this map), creature (one that stands still, or found by targeting it), trigger (a quest's exploration
# trigger) or area (a sub-area of the game's; its hint placed by its map overlay, or an anchor inside
# it: a creature, an object, a graveyard). gestures: the emotes it accepts, the story's own first.
riddles:
  - id: the-barrens-ratchet-book
    tier: near
    reading: Exile of the High Elves
    object: 175731   # dump 61.9, 38.7; Wowhead 62.0, 38.7
    hint_area: { x: 63.4, y: 42.4, r: 8 }
    danger: "Quiet"
    quest_overlap: [65593]
    quest_context: "Hearts of the Lovers, a warlock's quest, takes Isaac Pearson's heart in Ratchet, near the shelf. Yonder asks only that the book be read, with no kill and no quest."
    sources: "object 175731's text"
  - id: the-barrens-lizzarik
    tier: near
    creature: 3658   # Lizzarik, Weapon Dealer: from Ratchet (dump 61.8, 38.3) to the Crossroads and back, Jorb (3659) his bodyguard
    found: target   # he never stops walking
    hint_area: { x: 56.0, y: 35.0, r: 4 }
    danger: "Quiet on the road"
    sources: "the dump's spawn, path and wares; the WoWWiki archive's Lizzarik page (his road, Jorb)"
  - id: the-barrens-tidus-stair
    tier: off
    gestures: [PEER, LOOK, GAZE]
    area: The Tidus Stair   # placed: Mahren Skyseer, who fishes on it (creature 3388), dump 65.8, 43.9
    anchor: { creature: 3388 }   # what places its hint: the area has no overlay of its own
    hint_area: { x: 65.0, y: 45.0, r: 4 }
    danger: "Quiet on the stairs, deep water below"
    quest_overlap: [873, 874, 887, 888, 895, 1963, 2381, 92706, 97253]
    quest_context: "Mahren Skyseer, who fishes from the stair, gives Isha Awak and ends Mahren Skyseer. The pirate camp and the coast at its foot are the errand of Southsea Freebooters, Stolen Booty, WANTED: Baron Longshore, The Shattered Hand, Plundering the Plunderers, and Forever's WANTED: Bruuz and Parts and Pieces. Yonder asks only a look down where the stair goes, with no kill and no quest."
    sources: "Warcraft: The Roleplaying Game, p. 192 (the stairs beneath the waves, the legend, the divers); the client's AreaTable"
  - id: the-barrens-pooka
    tier: off
    faction: horde   # its keeper attacks the other side: this side's alone
    gestures: [WAVE, HELLO, GREET, SMILE]
    creature: 14909   # Pooka, dump 47.8, 8.8, at the Mor'shan Rampart; Mogg (14908), her son, playing outside
    hint_area: { x: 47.5, y: 10.0, r: 3 }
    danger: "Quiet for the Horde, the rampart's guards for the Alliance"
    sources: "the WoWWiki archive's Pooka page (her son Mogg); the dump's spawns"
  - id: the-barrens-northwatch
    tier: off
    reading: Lethargy of the Orcs
    object: 175751   # dump 61.9, 55.2, in Northwatch Hold; Wowhead 61.8, 55.1 (another copy in Elwynn's Eastvale Logging Camp)
    hint_area: { x: 61.0, y: 54.0, r: 4 }
    danger: "Guarded (Theramore's marines and preservers, levels 15 to 17, who attack the Horde)"
    sources: "object 175751's text; object 175752's text (The New Horde: Thrall's shamanism, a new spiritual identity); the dump's spawns of the hold (Gilthares Firebough, the captive of the Horde's Free From the Hold, 17 yards off, beyond the gates' reach); the WoWWiki archive's Northwatch Hold page"
  - id: the-barrens-fallen-warrior
    tier: hidden
    gestures: [SALUTE, BOW]
    area: Shrine of the Fallen Warrior   # placed: Koiter, dump 47.4, 29.7; Wowhead 47.4, 29.6
    anchor: { creature: 12034 }   # what places its hint: the area has no overlay of its own
    hint_area: { x: 49.9, y: 28.1, r: 6 }
    danger: "Quiet"
    quest_overlap: [871, 959, 1486, 1491, 1503, 1525, 94466]
    quest_context: "The hint's wide circle takes in the Razormane camps (Disrupt the Attacks, Call of Fire's Fire Tar), Lushwater Oasis and the caverns' outer cave (Deviate Hides, Smart Drinks, Trouble at the Docks) and Forged Steel's bars. None is the shrine's own. Yonder asks only a salute at the fallen warrior's grave, with no kill and no quest."
    sources: "the wiki's Shrine of the Fallen Warrior; Koiter (creature 12034) places the hint"
quarry:
  id: 5828   # Humar the Pridelord
  sources: "the WoWWiki archive's Humar the Pridelord page (the ring of lions round his tree, his roar, his black coat and tameability); the dump's spawn; the WoWWiki archive's Araga page (Humar's one spot under the tree)"
---
## the-barrens-ratchet-book
The elves in this account answered a ban on magic with a storm.
Find the page in the goblins' port that tells what became of them.
Their punishment began a voyage.
? Ratchet, on the Barrens' coast. Open the book about the exiled elves.
= Exile of the High Elves, in Ratchet. Banished for their refusal to abandon arcane magic, the Highborne sailed east and founded Quel'Thalas. The goblins keep their history. It is not for sale.
+ Dath'Remar mocked the druids as cowards. They could not bring themselves to put so many of their kin to death, and exiled them instead.

## the-barrens-lizzarik
On the road between the goblins' port and the orcs' crossroads,
a goblin peddler walks back and forth with weapons and potions to sell,
and an ogre walks behind him, far too strong for these plains.
Catch the peddler on the road.
? The road from Ratchet to the Crossroads. He walks it end to end. Ask the peddler to show you his wares. There is no need to buy.
= Lizzarik, a goblin weapon dealer of Ratchet, walking the road to the Crossroads and back with Jorb, his ogre bodyguard.
+ Jorb is of level thirty-seven, on a road most travellers walk at fifteen.

## the-barrens-tidus-stair
South of the goblins' port, great steps of ancient stone come up out of the sea,
or go down into it: the waves cover all but the highest of them.
Two tauren fish from them, as if nothing were strange about it.
Stand on the stair, and try to see where it leads.
? South-east of Ratchet, on the coast. From the stair, peer down into the water.
= The Tidus Stair: a giant's stairway of ancient stone, from the beach down beneath the waves.
+ Some say it goes down to a kaldorei city the sea took when the Well of Eternity was destroyed. Those who have dived as deep as they could found only more stairs.

## the-barrens-pooka
At the rampart on the northern road, where the Horde watches the elves' forest,
a mother keeps house in the middle of the war camp,
and her small son plays outside her door. Be friendly.
? The Mor'shan Rampart, at the Barrens' northern edge. Greet the child with a wave.
= Pooka and her son Mogg, at the Mor'shan Rampart: a family, in a war camp.
+ Of the boy's father, the rampart says nothing.

## the-barrens-northwatch
On the plains' southern coast, Theramore's soldiers hold a fort against the Horde,
and inside it the Alliance keeps its own account of the camps where it once held the orcs,
and of the sickness no warden could explain.
Find the page that says what kind of cure it would take.
? Northwatch Hold, on the coast south of Ratchet. Inside the fort, read the account of the orcs' lethargy.
= Lethargy of the Orcs, in Northwatch Hold. Antonidas of Dalaran judged the lethargy no disease but the orcs' withdrawal from the demonic magic in their blood, and concluded that their cure would have to be a spiritual one.
+ It was. Thrall, raised a slave in Durnholde, studied his people's forgotten shamanism and gave them 'a new spiritual identity', as the Horde's own account, The New Horde, tells it.

## the-barrens-fallen-warrior
Not far from the busiest road of the plains, a short trail climbs a hill
to a shrine raised for a warrior who fell,
and a spirit healer waits before it, as if for him.
Few find it. Honour him as one warrior honours another.
? West of the Crossroads, follow a ridge up a small hill. Salute the warrior at his shrine.
= The Shrine of the Fallen Warrior, and its own spirit healer, Koiter.
+ It remembers Michel Koiter, who worked on this world and died before it was finished. The spirit healer bears his name, and the orc of the shrine was his own character.

## quarry
North-west of the goblins' port, beyond the hills, lions lie in a ring around a tree,
and the one at the middle has a coat unlike theirs.
He roars when he is hurt, and the ring comes running.
= Humar the Pridelord, an elite lion, under his tree north-west of Ratchet, his pride around him.
+ He never leaves that tree, so hunters who want the black coat for a companion have learned to wait beneath it.
