---
zone: 1458   # Undercity
home: horde   # a capital: its riddles are its faction's alone
client: both
# the spots, pinned by the data (scripts/expeditions.py resolves them): object (every spawn of it on
# this map), creature (one that stands still, or found by targeting it), trigger (a quest's exploration
# trigger) or area (a sub-area of the game's; its hint placed by its map overlay, or an anchor inside
# it: a creature, an object, a graveyard). gestures: the emotes it accepts, the story's own first.
riddles:
  - id: undercity-kelthuzad-book
    tier: near
    reading: Kel'Thuzad and the Forming of the Scourge
    object: 175754   # dump 56.2, 51.0; Wowhead's page alike
    hint_area: { x: 52.5, y: 49.6, r: 8 }
    danger: "Quiet"
    sources: "object 175754's text"
  - id: undercity-theresa
    tier: off
    gestures: [PITY, SHUDDER, SIGH, COMFORT, HUG]
    creature: 5697   # Theresa, Gerard's Mindslave, dump 52.7, 34.7; Gerard Abernathy (5696) beside her
    hint_area: { x: 52.0, y: 35.5, r: 3 }
    danger: "Quiet"
    sources: "the dump's spawns and the scene's words (broadcast texts 1994-2014); the WoWWiki archive's Theresa and Gerard Abernathy pages"
  - id: undercity-terenas
    tier: hidden
    gestures: [KNEEL, BOW, MOURN]
    object: 175659   # dump 66.0, 43.9; Wowhead 65.9, 43.4
    hint_area: { x: 68.6, y: 40.9, r: 8 }
    danger: "Quiet"
    sources: "object 175659's text; the Codex's fall-of-lordaeron page"
  - id: undercity-edward-tyler
    tier: near
    faction: horde   # a Horde capital
    gestures: [SILENCE]
    creature: 5654   # Edward, dump 51.9, 22.5, in the War Quarter; Tyler (5653) fighting him; Wowhead's points alike
    companions: [5653]
    hint_area: { x: 52.5, y: 23.0, r: 2 }
    danger: "Quiet"
    quest_overlap: [92401]
    quest_context: "Forever's new quest in the Ruins of Lordaeron names its own Edward, Edward Heartweaver, another man. Yonder asks only for silence by the two who fight."
    sources: "the dump's spawns (Edward and Tyler, facing each other, fighting without end); the WoWWiki archive's In-jokes and references, Eastern Kingdoms page (Fight Club, Edward Norton, who played the narrator, and Tyler Durden, his other half); Wowhead's points for both"
# no quarry: a capital has riddles alone
---
## undercity-kelthuzad-book
In the city beneath the ruins, seek a preacher whose master spoke from the frozen north.
He promised the poor equality and a life that would never end.
His congregation's story stands among the herbalists' books.
? In the Undercity, by the herbalists: the Alliestars' shop. Read the book about the preacher and his cult.
= Kel'Thuzad and the Forming of the Scourge. The former archmage founded the Cult of the Damned to serve Ner'zhul, and named the undead rising from the plague the Scourge.
+ 'It was surprisingly easy for Kel'Thuzad to achieve his goal: namely, to transfer the citizens' faith in the Holy Light into belief in Ner'zhul's dark shadow.'

## undercity-theresa
In the quarter of the city's soldiers, three of the Forsaken stand around a living woman,
and one of them is very proud of her. He sends her across the bridge on errands,
and she always comes back. Let her see that someone still feels for her.
? The War Quarter, in the Undercity. Show the living woman a little pity.
= Theresa, Gerard Abernathy's mindslave: 'Theresa, take this to Father Lankester.' 'Yes My Lord.'
+ 'I managed to discover that certain parts of the brain when removed or stimulated will make a subject much more docile.' Even his companions ask him how he did it.

## undercity-terenas
Above the city, in what is left of the palace garden, the last true king
of the land lies under a stone that asks for his son's deeds
not to be laid at his feet. Pay him the respect his son did not.
? In the gardens of the Ruins of Lordaeron, above the Undercity. Kneel beside the king's tomb.
= 'Here lies King Terenas Menethil II -- Last True King of Lordaeron. Great were his deeds -- long was his reign -- unthinkable was his death.'
+ 'May the Father lie blameless for the deeds of the son. May the bloodied crown stay lost and forgotten.'

## undercity-edward-tyler
In the dead city's war quarter, two men have been fighting since long before you came,
and will be fighting long after you leave. Nobody stops them. Nobody asks why.
There is a rule about fights like theirs, and it is the first one.
Keep it.
? The War Quarter, in the Undercity. By the two men who never stop fighting, call for silence.
= Edward and Tyler, fighting without end in the Undercity's War Quarter.
+ In another world's tale, one of their names belongs to the man who played its narrator, the other to the narrator's other half. The first rule of their fight is that nobody talks about it.
