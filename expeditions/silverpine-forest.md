---
zone: 1421   # Silverpine Forest
client: both
# the spots, pinned by the data (scripts/expeditions.py resolves them): object (every spawn of it on
# this map), creature (one that stands still, or found by targeting it), trigger (a quest's exploration
# trigger) or area (a sub-area of the game's; its hint placed by its map overlay, or an anchor inside
# it: a creature, an object, a graveyard). gestures: the emotes it accepts, the story's own first.
riddles:
  - id: silverpine-forest-wallace
    tier: off
    gestures: [HELLO, HAIL, GREET]
    creature: 3534   # Wallace the Blind, dump 46.5, 86.5, among the refugees under the Greymane Wall
    hint_area: { x: 45.0, y: 84.0, r: 5 }
    danger: "Guarded for the Horde (the refugees, levels 18 to 20, are Lordaeron's own), quiet for the Alliance"
    sources: "the dump's spawns and factions (Wallace friendly to all, the refugees to the Alliance alone); the WoWWiki archive's Greymane Wall and Wallace the Blind pages; Warcraft II: Beyond the Dark Portal's manual (the wall)"
  - id: silverpine-forest-sepulcher
    tier: town
    faction: horde   # its town's: for that faction alone
    creature: 5886   # Gwyn Farrow <Mushroom Merchant>, dump 44.0, 39.8; Wowhead alike
    found: target   # in the town: only by speaking to her
    hint_area: { x: 43.4, y: 40.6, r: 3 }
    danger: "Quiet"
    sources: "the dump's spawn and her wares (npc_vendor: Forest Mushroom Cap, Red-speckled Mushroom, Spongy Morel, Delicious Cave Mold, Raw Black Truffle, Dried King Bolete); warcraft.wiki.gg's Gwyn Farrow and The Sepulcher pages (a graveyard along the road across Silverpine, the old crypt the Forsaken took for their base)"
  - id: silverpine-forest-bates
    tier: town
    faction: horde   # its town's: for that faction alone
    gestures: [SHIVER, SCARED]
    creature: 6739   # Innkeeper Bates, dump 43.2, 41.3, in the Sepulcher; Wowhead's point alike
    hint_area: { x: 43.0, y: 42.0, r: 2 }
    danger: "Quiet"
    sources: "the dump's spawn and his gossip; the WoWWiki archive's In-jokes and references, Eastern Kingdoms page (Innkeeper Norman in the Undercity and Innkeeper Bates in the Sepulcher, Psycho's Norman Bates); Wowhead's point"
  - id: silverpine-forest-fenris-isle
    tier: off
    gestures: [GAZE, LOOK, PONDER]
    area: Fenris Isle   # the sub-area's name: the overlay it shares with the Dawning Isles centres on 71.9, 28.8
    hint_area: { x: 69.0, y: 27.0, r: 6 }
    danger: "Guarded (Rot Hide gnolls and Vile Fin murlocs, levels 17 to 24, and Thule Ravenclaw in the keep)"
    quest_overlap: [460, 461, 491, 442, 443, 368, 451, 91860, 91862]
    quest_context: "Fenris Isle is the ground of the Forsaken's quests against the Rot Hide gnolls, Thule Ravenclaw and the Vile Fin murlocs, and of The Hidden Niche's grave and shelf. On Forever, two new quests send travellers there after an Earthen Ring party and Lumina Windsinger. Yonder asks only that the reader look out from the island and see what the ring of islands once was."
    sources: "the WoWWiki archive's Fenris Isle page (with the Dawning Isles, a broken circle of dry land in Lordamere Lake, once the rim of an ancient volcano long since eroded); the client's map files (Fenris Isle's chunks at 62 to 72, 18 to 36, the Dawning Isles' at 75 to 82, 15 to 35); the dump's spawns (the Rot Hide gnolls, Thule Ravenclaw in the keep)"
quarry:
  id: 1948   # Snarlmane
  sources: "the WoWWiki archive's Snarlmane page; Warcraft III: The Frozen Throne, 'The Dark Lady' (Snarlmane possessed); the dump's spawn"
---
## silverpine-forest-wallace
At the forest's southern end, a wall of grey stone shuts a kingdom in.
Under it, the plague's refugees wait for a gate that does not open,
and among them a smith sells blades to anyone at all:
he cannot see which side you are on. Don't bother waving.
? Under the Greymane Wall, at the south end of Silverpine, among the refugees. Say hello to the smith. A wave is no use to a blind man.
= Wallace the Blind, weaponsmith to Horde and Alliance alike, under the Greymane Wall: Gilneas keeps its gate shut on the refugees at its foot.
+ Gilneas raised the wall after the Second War, when Genn Greymane quit the Alliance over the cost of the orcs' internment camps.

## silverpine-forest-sepulcher
Where the road through the pines passes a graveyard, the dead have made a town of it.
One of them keeps a stall of nothing but mushrooms, molds and truffles,
from the caves and from the forest floor.
Ask her what she has.
? The Sepulcher, among its merchants: speak to the one who sells mushrooms.
= Gwyn Farrow, the Sepulcher's mushroom merchant. Her stall holds fungi only: Forest Mushroom Cap, Red-speckled Mushroom, Spongy Morel, Delicious Cave Mold, Raw Black Truffle and Dried King Bolete.
+ The Sepulcher was nothing more than a graveyard by the road across Silverpine before the Forsaken took its old crypt for their base in the forest.

## silverpine-forest-bates
In the Forsaken's crypt among the pines, the innkeeper offers every traveller a bed.
In another world, a man with his name kept a quiet motel off a lonely road,
and some of his guests never checked out.
Call at his counter, and let him see what the name does to you.
? The Sepulcher, in Silverpine. Find the innkeeper and shiver.
= Innkeeper Bates, of the Sepulcher: 'Rest your weary bones for a spell.'
+ The Undercity's innkeeper is called Norman. Together, they make one name.

## silverpine-forest-fenris-isle
In the middle of the great lake, a ruined keep stands on an island, and the island is not alone:
with its smaller sisters it makes a broken ring on the water.
Long before the keep, before the lake had its name, that ring was something else.
Set foot on it and find out what.
? Fenris Isle, in Lordamere Lake, east of Silverpine. Gaze out over the ring the islands make.
= Fenris Isle and the Dawning Isles: a broken ring of land on Lordamere Lake, the rim of an ancient volcano worn down by the ages.
+ The rest of the ring is the Dawning Isles, a scatter of islets to Fenris Isle's east.

## quarry
On the isle in the lake, the Rot Hide dead hold an old keep.
Down in its cellar, one of them still has a name,
and a gnoll of that name once led a living pack in the Glades,
until the Dark Lady needed it more than he did.
= Snarlmane, a dead gnoll of the Rot Hide, in the cellar of Fenris Keep.
+ In the Third War, Sylvanas set a banshee in the mind of a gnoll chieftain called Snarlmane, and spent his pack against the dreadlord Varimathras. If this is he, someone raised him again.
