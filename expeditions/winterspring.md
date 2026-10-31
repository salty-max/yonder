---
zone: 1452   # Winterspring
client: both
# the spots, pinned by the data (scripts/expeditions.py resolves them): object (every spawn of it on
# this map), creature (one that stands still, or found by targeting it), trigger (a quest's exploration
# trigger) or area (a sub-area of the game's; its hint placed by its map overlay, or an anchor inside
# it: a creature, an object, a graveyard). gestures: the emotes it accepts, the story's own first.
riddles:
  - id: winterspring-farflinger
    tier: near
    creature: 14742   # Zap Farflinger, Unbalanced Engineer, in Everlook
    found: target   # his invention is described in his gossip
    hint_area: { x: 61.0, y: 38.0, r: 3 }
    danger: "Quiet"
    sources: "https://www.wowhead.com/classic/npc=14742/zap-farflinger; https://warcraft.wiki.gg/wiki/Zap_Farflinger (gossip, added in 1.5.0); the dump's gossip menu 6092 and npc_text 7249/7250 (the imploder, the explosion, goblin engineering), spawn and lack of quest relations"
  - id: winterspring-jack-sterling
    tier: near
    creature: 11546   # Jack Sterling, dump 61.6, 38.3, in Everlook; Wowhead 61.4, 38.2
    found: target   # in the town: only by finding him
    hint_area: { x: 61.0, y: 37.5, r: 3 }
    danger: "Quiet"
    quest_overlap: [5163]
    quest_context: "Are We There, Yeti? is given by Legacki, who stands beside Jack in Everlook. Yonder asks only that Jack be found, with no yeti and no quest."
    sources: "the dump's spawn (no quest, no wares, no word); the WoWWiki archive's Jack Sterling page (a human in Everlook who offers no quests or services; the dump has three more humans in Everlook, so the riddle names him by what he lacks) and In-jokes and references, Kalimdor page (Everlook and the Overlook Hotel, Jack Sterling and Jack Torrance)"
  - id: winterspring-kel-theril
    tier: off
    gestures: [MOURN, KNEEL, PRAY, CRY]
    area: The Ruins of Kel'Theril   # placed: the Remorseful Highborne (10684), dump 56.1, 44.4; Wowhead 56.0, 44.6
    anchor: { creature: 10684 }   # what places its hint: the area has no overlay of its own
    hint_area: { x: 54.5, y: 43.5, r: 5 }
    danger: "Perilous (the Highborne's tormented spirits, to level 56, and for the Horde the Remorseful Highborne)"
    quest_overlap: [5245, 5248, 5252]
    quest_context: "Troubled Spirits of Kel'Theril asks for the relic fragments scattered in the ruins, and Tormented By the Past and Remorseful Highborne go on with the spirit who stands among them. Yonder asks only a moment's mourning for the city, with no fragment and no quest."
    sources: "warcraft.wiki.gg's Ruins of Kel'Theril page (a night elven city destroyed in the Great Sundering, haunted by the Highborne's tormented spirits); the dump's spawns (Suffering and Anguished Highborne); World of Warcraft: Chronicle, volume 1 (the Highborne, Azshara's court, the Legion drawn into the world, the Sundering)"
quarry:
  id: 10200   # Rak'shiri
  sources: "https://www.wow-petopia.com/classic/look.php?id=ridingtigerskinaqua (Rak'shiri and Shy-Rotam share the aqua coat); the dump's path near Frostsaber Rock"
---
## winterspring-farflinger
In the goblins' town in the snow, an engineer has finished a machine
and is waiting for someone else to try it.
Find the inventor whose title gives you reason to hesitate.
? Everlook. Speak to the engineer. Trying his machine is another matter.
= Zap Farflinger, Unbalanced Engineer. His plan for instant transport begins by blowing the traveller to pieces, then reassembling the particles at Everlook.
+ He teaches skilled goblin engineers to build the ripper that connects to his machine. His answer to doubts about safety is that survival comes second to engineering.

## winterspring-jack-sterling
In the snowbound town where goblins keep the only lodging for miles,
a man named Jack is spending the winter.
Nobody has seen him at work, or at play.
Find him.
? Everlook, in Winterspring. Find Jack, the man with nothing to sell and nothing to say, and get close enough to target him.
= Jack Sterling, of Everlook. He offers no work, no wares and no word.
+ Another snowbound hotel, in another world's tale, had a Jack too. It did not end well.

## winterspring-kel-theril
By a lake in the north, an elven city stood before the world was broken.
The Sundering left it in ruins, and the winter came after.
Its people never left. They walk it still, and they are not at peace.
They are owed a moment's grief.
? The Ruins of Kel'Theril, on the shore of the lake: mourn the city's dead.
= The Ruins of Kel'Theril, a night elven city of the Highborne, destroyed in the Great Sundering. Its tormented spirits, the Suffering Highborne and the Anguished Highborne, still haunt it.
+ The Highborne were Queen Azshara's nobles. Their reckless magic drew the Burning Legion into the world and ended in the Sundering that broke their own city.

## quarry
Below Frostsaber Rock, a saber's coat puts a little colour into the snow:
aqua beneath the stripes, among the white and lavender of its neighbours.
Search the slopes and the ground beside the frozen lake.
= Rak'shiri, an aqua-coated saber of Winterspring, near Frostsaber Rock.
+ Only one other cat wears the aqua coat: Shy-Rotam.
