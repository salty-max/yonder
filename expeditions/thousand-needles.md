---
zone: 1441   # Thousand Needles
client: both
# the spots, pinned by the data (scripts/expeditions.py resolves them): object (every spawn of it on
# this map), creature (one that stands still, or found by targeting it), trigger (a quest's exploration
# trigger) or area (a sub-area of the game's; its hint placed by its map overlay, or an anchor inside
# it: a creature, an object, a graveyard). gestures: the emotes it accepts, the story's own first.
riddles:
  - id: thousand-needles-raceway
    tier: near
    gestures: [CHEER, APPLAUD, CLAP]
    creature: 4507   # Daisy, Race Starter Girl, dump 79.5, 76.9; Fobeed (4620) and Zuzubee (4707) announce
    hint_area: { x: 79.0, y: 77.5, r: 5 }
    danger: "Quiet"
    sources: "the dump's spawns (Daisy, Fobeed, Zuzubee); the WoWWiki archive's Daisy and Fobeed pages"
  - id: thousand-needles-freewind
    tier: town
    faction: horde   # its town's: for that faction alone
    gestures: [PET, PAT, SOOTHE, COMFORT]
    creature: 10582   # Dog <Sire>, dump 45.1, 50.4, by Montarr the Lorekeeper's stall (4878); Wowhead 45.2, 50.4 and 50.6
    found: target   # he paces at the stall: only by targeting him near
    hint_area: { x: 45.6, y: 50.0, r: 3 }
    danger: "Quiet"
    quest_overlap: [4821]
    quest_context: "warcraft.wiki.gg says the Young Arikara hatched at Alien Egg's turn-in (Hagar Lightninghoof's quest) kills him, though the dump's turn-in script only spawns the hatchling. Yonder asks a kindness to the post's dog while he stands there, needing no quest or egg."
    sources: "Wowhead's tooltip (Dog <Sire>, level 10, Thunder Bluff; Freewind Post 45.2, 50.4 and 50.6); the dump: the only creature in the game titled Sire, beside Montarr <Lorekeeper>; warcraft.wiki.gg's Dog (Thousand Needles) and Freewind Post pages (the mesa, out of the centaur warbands' reach, its wooden lifts and rope bridges)"
quarry:
  id: 5933   # Achellios the Banished
  sources: "the WoWWiki archive's Achellios the Banished page (his three hounds); the dump's path"
---
## thousand-needles-raceway
On the salt flats, gnomes and goblins race their machines,
an ogre calls the races, and a barmaid sends them off with a flag.
Every race needs a crowd. Be one.
? The Mirage Raceway, on the Shimmering Flats. Cheer on the race beside the flag-bearer.
= Daisy, the race starter girl of the Mirage Raceway, with Fobeed, the ogre, and Zuzubee calling the races.
+ The racers come and go. The flag, the ogre's voice and the salt stay.

## thousand-needles-freewind
High on a mesa the tauren keep a post above the needles,
and beside its lorekeeper's stall lives a resident no merchant pays.
He answers to the plainest name there is, and his title makes him a father,
though no pup of his is to be seen at the post.
A good dog is owed a kind hand.
? Freewind Post, by Montarr the lorekeeper's stall. Pet the dog.
= Dog, titled Sire, the father of pups: no other creature in Kalimdor or the Eastern Kingdoms carries that title. He keeps to Montarr's stall in Freewind Post.
+ The tauren built their towns on the tallest mesas, out of reach of the centaur warbands, and joined them with wooden lifts and rope bridges.

## quarry
A centaur called the Banished circles the plateaus of the canyons' west,
between the wyverns' heights and the screeching canyon.
Three hounds keep at his heels.
= Achellios the Banished, a centaur, circling the plateaus between Highperch and the Screeching Canyon with three Galak Packhounds.
+ The Galak's hounds still follow him, whoever it was that banished him.
