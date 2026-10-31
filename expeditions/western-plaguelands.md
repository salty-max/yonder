---
zone: 1422   # Western Plaguelands
client: both
# the spots, pinned by the data (scripts/expeditions.py resolves them): object (every spawn of it on
# this map), creature (one that stands still, or found by targeting it), trigger (a quest's exploration
# trigger) or area (a sub-area of the game's; its hint placed by its map overlay, or an anchor inside
# it: a creature, an object, a graveyard). gestures: the emotes it accepts, the story's own first.
riddles:
  - id: western-plaguelands-chillwind
    tier: town
    faction: alliance   # its town's: for that faction alone
    creature: 11609   # Alexia Ironknife, dump 42.9, 84.0
    found: target   # in the camp: only by speaking to her
    hint_area: { x: 43.5, y: 83.0, r: 3 }
    danger: "Quiet"
    sources: "the dump's spawn and her words"
  - id: western-plaguelands-uther
    tier: off
    faction: alliance   # High Priest Thel'danis (1854), level 62, Stormwind's, stands at the plaque and attacks the Horde
    reading: Uther the Lightbringer
    object: 2082   # the plaque at Uther's Tomb, dump 52.1, 83.3; Wowhead 52.1, 83.2; before the statue (1323)
    hint_area: { x: 51.2, y: 82.0, r: 5 }
    danger: "Guarded (ghouls and skeletons, to level 52)"
    quest_overlap: [8149, 8414, 8416]
    quest_context: "Honoring a Hero (the Harvest Festival) asks for an offering at the statue, and High Priest Thel'danis, the tomb's caretaker, ends Dispelling Evil and gives Inert Scourgestones beside it. Yonder asks only that the plaque be read, with no quest, offering or festival."
    sources: "the plaque's own words (readable object 2082, the dump's page_text 292); warcraft.wiki.gg's Uther's Tomb page (the great tomb south of Andorhal where his soldiers buried him, High Priest Thel'danis its caretaker, Arthas taking King Terenas's urn from his master's body)"
  - id: western-plaguelands-darrowmere
    tier: hidden
    gestures: [GAZE, LOOK, PEER, STARE]
    area: Darrowmere Lake   # placed: the client's overlay: 68.4, 73.7 (the island in its middle)
    hint_area: { x: 68.5, y: 74.5, r: 8 }
    danger: "Perilous (the Scourge's lands, levels 55 to 60)"
    sources: "the client's AreaTable and overlay; the WoWWiki archive's Darrowmere Lake page (the largest lake of the Eastern Kingdoms, Caer Darrow and the House of Barov, the Scholomance below; the eastern side's breeze off the Hinterlands' peaks, the plague mist thinnest there of all the Plaguelands, blue sky seen in the lake) and Caer Darrow page"
quarry:
  id: 1851   # The Husk
  sources: "the WoWWiki archive's The Husk and The Weeping Cave pages; the pinned dump's spawn and creature_ai_scripts (17230 Infected Wound); the dump's loot (Living Essence, 96%; Firebloom, Icecap, Sungrass)"
---
## western-plaguelands-chillwind
In the Alliance's camp at the plague's southern edge, a traveller rests before Hearthglen,
and passes on what she has heard: the Crusade once had a mage making bows and guns,
and killed him before his work ever left the town. Ask her about it.
? Chillwind Camp. Speak to the traveller resting in the camp.
= Alexia Ironknife, resting at Chillwind before Hearthglen: the Crusade's own weapon-maker, she has heard, was killed by the Crusade.
+ At the Bulwark, the Horde's camp, a traveller tells the same tale, and adds that the wizard finished a remarkable weapon first.

## western-plaguelands-uther
South of a city the plague emptied, on a hill named for sorrow,
the first of the Light's knights lies where his soldiers buried him.
He taught a prince, and the prince cut him down.
His stone has something to say to whoever stops to read it.
? Uther's Tomb, on Sorrow Hill south of Andorhal: read the plaque before the statue.
= The plaque of Uther the Lightbringer, First Paladin and Founder of the Order of the Silver Hand, who lived and died to defend Lordaeron and was betrayed by his most beloved student. It is signed: Anonymous.
+ Uther had King Terenas's urn with him when his student killed him. The prince took it from his master's body.

## western-plaguelands-darrowmere
In the fallen kingdom lies the greatest lake of these lands,
and in its middle an island town, and a noble family's house,
and under the house a school that teaches the raising of the dead.
From its shore, fix your eyes on the island across the water.
? Darrowmere Lake, in the Western Plaguelands' south-east. From its shore, gaze across at the island.
= Darrowmere Lake, the largest lake of the Eastern Kingdoms. On the island at its heart stand Caer Darrow and the House of Barov, with the Scholomance deep beneath them.
+ On its eastern side, a wind off the Hinterlands' peaks keeps the plague mist thinner than anywhere else in the Plaguelands, and the water still shows the blue of the sky.

## quarry
In a cave above the river at the plague's eastern edge,
bog beasts and oozes keep the dark.
Among them, seek a bog beast with a dead thing's name.
= The Husk, a bog beast of level 62, at the Weeping Cave.
+ Herbs take root on him: Firebloom, Icecap and Sungrass come away when he falls, and a living essence nearly always.
