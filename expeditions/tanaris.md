---
zone: 1446   # Tanaris
client: both
# the spots, pinned by the data (scripts/expeditions.py resolves them): object (every spawn of it on
# this map), creature (one that stands still, or found by targeting it), trigger (a quest's exploration
# trigger) or area (a sub-area of the game's; its hint placed by its map overlay, or an anchor inside
# it: a creature, an object, a graveyard). gestures: the emotes it accepts, the story's own first.
riddles:
  - id: tanaris-gadgetzan
    tier: near
    reading: Old Hatreds - The Colonization of Kalimdor
    object: 175763   # dump 51.0, 29.4, in Gadgetzan
    hint_area: { x: 51.5, y: 28.5, r: 3 }
    danger: "Guarded for the Horde (Bera Stonehammer, the Alliance's gryphon master, level 55, stands close), quiet for the Alliance"
    sources: "object 175763's text"
  - id: tanaris-buzzek
    tier: near
    creature: 8736   # Buzzek Bracketswing, Master Engineer, dump 52.3, 27.7, in Gadgetzan by the mailbox; Wowhead 52.2, 27.6
    found: target   # in the town: only by speaking to him
    hint_area: { x: 53.0, y: 26.5, r: 3 }
    danger: "Quiet"
    sources: "Buzzek Bracketswing's own words (his gossip); the client's display tables (a goblin); the WoWWiki archive's Buzzek Bracketswing page (in front of the middle hut, by the mailbox); Gadgetzan's faction (the Steamwheedle Cartel's)"
  - id: tanaris-zalashji
    tier: off
    gestures: [WAVE, HELLO, GREET, BOW, HAIL]
    creature: 8617   # Zalashji, dump 67.7, 32.2, at his den
    hint_area: { x: 67.0, y: 33.0, r: 3 }
    danger: "Guarded (Wastewander bandits and steeljaw snappers nearby)"
    sources: "the WoWWiki archive's Zalashji page (friendly, no purpose anyone knows); the dump's spawn and faction (friendly to all)"
  - id: tanaris-oreily
    tier: off
    gestures: [DOUBT, SURPRISED, CONFUSED]
    creature: 15520   # O'Reily, a white owl, dump 65.4, 19.0, flying a path round Narain Soothfancy's hut at Steamwheedle Port
    found: patrol   # the owl targeted, along the circle it flies
    position_check: questie
    hint_area: { x: 66.0, y: 19.5, r: 3 }
    danger: "Quiet"
    sources: "the dump's spawn and path; Wowhead's points; the WoWWiki archive's In-jokes and references, Kalimdor page (the white owl round Narain Soothfancy's hut, the O RLY owl, and the auctioneers O'reely and Yarly)"
  - id: tanaris-winkey
    tier: hidden
    gestures: [WINK, SMILE, BLUSH]
    creature: 7770   # Winkey, dump 65.7, 64.2, alone on an islet
    hint_area: { x: 64.0, y: 63.0, r: 4 }
    danger: "Guarded (surf gliders and coast striders, level 48, in the shallows)"
    sources: "the WoWWiki archive's Winkey and Southbreak Shore pages; the dump's spawn and words; quest 3823's text (Oralius and his 'Winky')"
  - id: tanaris-jhordy
    tier: near
    gestures: [EYE, SUSPICIOUS, PEER]
    creature: 14743   # Jhordy Lapforge, Engineer, dump 52.3, 26.9, in Gadgetzan; Wowhead 52.2, 26.8
    hint_area: { x: 52.0, y: 26.0, r: 2 }
    danger: "Quiet"
    sources: "the dump's spawn; his gossip and its second page for engineers (broadcast text 9998, the matter transporter and the evil selves); the WoWWiki archive's In-jokes and references (games, TV and movies) page, Star Trek: The Next Generation (Geordi La Forge, chief engineer), and its Kalimdor page (his goggles or visor and yellow shirt); the client's display (a gnome); Wowhead's point"
  - id: tanaris-rocket-car
    tier: off
    gestures: [SURPRISED, CONFUSED, GASP, DOUBT]
    name: The car through the mountain
    landmark: tanaris-rocket-car-wreck   # the client's own placement of the wreck, read from its map files
    radius: 15
    hint_area: { x: 48.5, y: 26.0, r: 1.5 }
    danger: "Guarded (Starving Blisterpaws and Scorpid Tail Lashers close by, levels 41 to 44)"
    sources: "the pinned client's map files: crashedgnomerc.m2 (file 197705), unique id 397465, in kalimdor_38_45_obj0.adt, placed the same on Forever (wow-data landmark tanaris-rocket-car-wreck, source client-map); the WoWWiki archive's In-jokes and references (games, TV and movies) page, The Adventures of Buckaroo Banzai (skid marks into the mountain in Thousand Needles, out of it just west of Gadgetzan, to a crashed rocket car); the dump's spawns near it (a Starving Blisterpaw at 39 yards, a Scorpid Tail Lasher at 56)"
quarry:
  id: 8201   # Omgorn the Lost
  sources: "the WoWWiki archive's Omgorn the Lost page (one of three camps, a great axe); the pinned dump's spawns and creature_ai_scripts (16856 Mortal Strike)"
---
## tanaris-gadgetzan
In the desert's goblin town, find a daughter who chose the peace her father had come to break.
Their quarrel crossed an ocean before it ended.
The town keeps the account among its books.
? Gadgetzan. Read the account of the daughter and her father's war.
= Old Hatreds - The Colonization of Kalimdor, in Gadgetzan: Durotar named for Thrall's father, and Jaina Proudmoore against her father, the Grand Admiral.
+ He died before she could reconcile with him. For her loyalty, the orcs let her forces go home to Theramore in peace.

## tanaris-buzzek
In the goblins' town in the desert, an engineer has a grand idea:
to carry oil under the ground from one great city to the next.
Everyone he tells answers him with the same two words.
Ask him what they are.
? Gadgetzan, in front of the middle hut, by the mailbox. Speak to the master engineer.
= Buzzek Bracketswing, Master Engineer of Gadgetzan: 'I've been working on a way to transport oil underground between major cities, but everyone tells me it's a pipe dream.'
+ Gadgetzan belongs to the Steamwheedle Cartel, as Booty Bay, Ratchet and Everlook do.

## tanaris-zalashji
East of the goblins' town, a naga keeps a den in the rocks,
and wants nothing at all from you: no war, no treasure, no blood.
Be friendly, for once.
? Zalashji's Den, east of Gadgetzan. Bow to the naga. He is willing to leave you in peace.
= Zalashji, a naga at home in his den: friendly to all, and wanting nothing from anyone.
+ Horde and Alliance alike may walk up to him unharmed, as to few naga anywhere.

## tanaris-oreily
At the goblins' port on the desert coast, a fortune-teller keeps a hut,
and a white owl circles it day and night, as if it had heard every prophecy and believed none of them.
Whatever it seems to ask you, answer it in kind.
? Steamwheedle Port, in Tanaris' north-east. Target the white owl circling the seer's hut, and look doubtful.
= O'Reily, a white owl, circling Narain Soothfancy's hut at Steamwheedle Port.
+ Its namesakes keep the auction houses: Auctioneer O'reely in Booty Bay, Auctioneer Yarly in the Undercity.

## tanaris-winkey
Off the quiet beach south of the pirates' cove, a little island holds one gnome, alone,
sunning herself as if the whole sea were her garden.
She has one request for whoever swims out to her. Let your face answer hers.
? An islet off Southbreak Shore, south of Lost Rigger Cove. Answer the sunbathing gnome with a wink.
= Winkey, a gnome alone on her islet off Southbreak Shore: 'Hey there, cutie! Mind rubbing some lotion on my exposed areas?'
+ Far away in the Burning Steppes, a dwarf at Morgan's Vigil grabs at the air and shouts at someone called Winky who isn't there. Whether he means her, nobody can say.

## tanaris-jhordy
In the goblins' desert town, a gnome engineer with a visor over his eyes
has built a machine that sends a traveller across the world in an instant,
nearly always in one piece, and nearly always the same traveller.
Make sure its maker is still himself.
? Gadgetzan, in Tanaris: the gnome engineer with the visor, by the transporter pad. Eye him suspiciously.
= Jhordy Lapforge, Gadgetzan's engineer, and his Matter Transporter.
+ To engineers who can build its beacon, he admits the rest: 'There have been some reported problems with transportees being replaced by their evil selves from an alternate universe, but I'm sure we will have that worked out soon...'

## tanaris-rocket-car
West of the goblins' desert town, a little rocket car lies wrecked at the foot of the mountains.
Its skid marks run back into the rock behind it, as though the range were no wall at all,
and on the far side, by the salt flats, the same marks lead in.
Find where it came out, and see if you can believe it.
? Just west of Gadgetzan, at the foot of the mountains. Find the crashed rocket car, and show your surprise.
= The car through the mountain: a crashed gnome rocket car west of Gadgetzan, its skid marks starting on the far side of the range, by the Shimmering Flats.
+ In another world's tale, a scientist drove a rocket car straight through a mountain, across salt flats very like the Shimmering Flats.

## quarry
The ogres of the southern desert hold three camps among old troll ruins.
An ogre with a great axe may be found at any one of them.
Lost, they call him. He has company enough wherever he turns up.
= Omgorn the Lost, a Dunemaul ogre, in the Dunemaul Compound, the Eastmoon Ruins or the Southmoon Ruins.
+ His axe leaves wounds that resist healing.
