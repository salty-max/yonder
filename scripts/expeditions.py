#!/usr/bin/env python3
"""Where each riddle of expeditions/*.md is solved: data/expeditions.json.

  python3 scripts/expeditions.py
  python3 scripts/expeditions.py --dry [folder]   the checks alone, nothing
                   written: expeditions/, or another folder of riddle files

A riddle names its spot by what the game's data pins down:

  object: <id>     a game object of the CMaNGOS Classic database (wow-data's
                   database, its spawns): every spawn of it on the zone's
                   map, each checked against Wowhead's points (frozen in
                   wow-data: bin/wowhead-points.ts): within 0.6% of one
  creature: <id>   a creature: its spawns inside the hint circle, Wowhead's
                   alike; found where it stands still (no further than 10
                   yards from its spawn: the dump's wandering radius or its
                   path), and, one of a kind, by targeting it near (anywhere
                   it walks); `found: target` for one found only by talking
                   to it (in a town, where passing by would solve it), or
                   one that walks: its path crossing the hint circle will do.
                   `found: place` with `radius: <yards>` anchors a gesture or
                   arrival to fixed surroundings, never a live creature.
                   `found: patrol` requires the nearby creature targeted and
                   a player position along the selected spawn's recorded path
  trigger: <id>    a quest's exploration trigger (the client's AreaTrigger)
  area: <name>     a sub-area of the zone (the client's AreaTable, under the
                   zone's own area): every id of that name
  landmark: <id>  reviewed scenery in wow-data's landmark table. Its recorded
                   map position, with radius in yards, never an NPC proxy

For an object or creature without Wowhead map data, position_check: questie explicitly
checks its Classic world spawn against Questie's independent zone coordinates.
The same agreement tolerance applies. It never uses player observer sightings.

The world positions go on the zone's map by the client's UiMapAssignment
(Classic Era's, wow-data's database: ../wow-data). The hint circle (hint_area,
in percent of the map's width) must hold the spot (an area's: its overlay's
centre, or its anchor's); an object's spawns outside it are other copies (a
history book stands in more than one inn), not the riddle's. Each zone also gets its size in yards
(the addon's cells are yards) and every sub-area id under it (the addon finds
the one it stands in by name; the riddles' own are not singled out). The
client's emote tokens (EmotesText) go with them, for the build to check the
gestures. An area
with no overlay of its own names an anchor inside it for its hint
(`anchor: { creature: <id> }`, `{ object: <id> }`, or `{ grave: <id> }`: a
graveyard the server names, world_safe_locs).

Wowhead's position: its object or NPC page's map data where a browser saved
it (every copy, by zone; its site refuses scripts), else its tooltip (the
zone with the most), frozen in wow-data's data/wowhead/<game>/points.json
(bun ../wow-data/bin/wowhead-points.ts: a new riddle's thing fetched there
first) and read from its databases (spawns of source wowhead).

A zone's quarry (`quarry: { id, sources }`): every spawn of the creature on
the zone's map (its own, or one that may take its place: creature_spawn_entry,
spawn groups) that Wowhead places there too, and the places Wowhead's
players met it, gathered into its haunts: the points within HAUNT percent of
each other, each a circle around them wide enough for its wandering (the
dump's radius or path), HAUNT_MIN at least.

A zone of Forever's own (`client: forever`, Zephras Isle) is placed on
Forever's client tables (wow-data's database), its creatures from Questie's
Forever (its in-game recorder's traces, merged: wow-data's database; percent
of the zone's map), each point kept only
where Wowhead's Forever database (its tooltip) places the creature too: a
creature or a sub-area, and a quarry the data doesn't know (its name, level,
rank and model given in the file).

Then the riddles are checked as a reader meets them:

  - never a kill: a creature asked for is no foe of the side that may solve
    it (the client's FactionTemplate; a riddle of one side's says so:
    `faction:`, on any tier);
  - never the same discovery twice for either side: distinct subjects and
    no overlapping passive arrivals. Different places may share a deed;
  - flag Forever's own new quests' road (its quests no Classic one is:
    Questie's Forever, wow-data's database): no new quest gives, ends or
    asks for the riddle's creature or object (by kind: an item's id is no
    creature's), none names it in its title or its objectives, and none
    sends a player (its giver, its ender, what it asks for, where Questie
    places them) within FOREVER_NEAR of a riddle solved by arriving. An exact
    quest_overlap list and quest_context acknowledge a reviewed separate experience;
  - its twin for every quest of both games (Classic's are Forever's too):
    none gives, ends or asks for the riddle's subject (or an item it drops
    on the quest), and none asks for what stands at the riddle's place (a
    creature, an object, or an item they drop on the quest, SHARE of the
    zone's spawns of it there at least): an area's place is its hint circle,
    a spot's where it is solved and NEAR yards about. A spawn of the Classic
    database's is the zone's only where Questie or Wowhead place the thing
    in the zone too, or on no map that holds it (a zone's map holds
    Blackrock Mountain under Searing Gorge). The same exact quest_overlap
    and quest_context answer it;
  - keepers and guards: on a riddle open to both sides, no creature within
    NEAR yards of its spot (or its area's anchor) attacks one side only (by
    its faction template, else, for Forever's new creatures, which have none
    in the data, by the sides Questie says it is friendly to), unless the
    riddle is that side's riddle no more (faction:) or its danger line names
    it (its name, or its kind: "the refugees").

Anything that fails is printed and nothing is written (--dry: the checks
alone, on expeditions/ or another folder of riddle files).
"""
import collections, json, math, os, re, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
from root import family_path  # noqa: E402  (scripts/root.py, the kit's copy: the family folder, from a worktree too)

try:  # (wowdata is imported only when a database is opened: CI's tests run without the family folder)
    sys.path.insert(0, family_path("wow-data", "py"))
except RuntimeError:
    pass

EXPEDITIONS = os.path.join(ROOT, "expeditions")
DRY = "--dry" in sys.argv
if DRY and sys.argv[-1] != "--dry":
    EXPEDITIONS = os.path.abspath(sys.argv[-1])
OUT = os.path.join(ROOT, "data", "expeditions.json")

# How near the spot counts, in yards: an object or a creature stood beside
# (a statue's base can be a few yards from its centre), a trigger by its own
# radius (never less).
NEAR = 10
# Dump and Wowhead must agree within this, in percent of the map (a quarry's
# spawn within AGREE_HAUNT: Wowhead's points are sightings of a creature that
# moves, and its haunt is a circle of HAUNT_MIN at least).
AGREE, AGREE_HAUNT = 0.6, 2.0
# The map art's height over its width (1002 by 668): a hint circle's radius is
# in percent of the width.
ASPECT = 668 / 1002
# A quarry's haunts: spawns this near each other (percent of the width) are
# one, a circle never smaller than HAUNT_MIN.
HAUNT, HAUNT_MIN = 6, 3
# Wowhead's sightings of a quarry count within this of a spawn the two agree
# on (further out, they are another place's, or noise).
ROAM = 10
# A new quest of Forever's this near an arrival's spot (percent of the map's
# width) sends its players through it.
FOREVER_NEAR = 4


def db(game):
    """Load the data dependency only for queries, not pure authoring checks."""
    from wowdata import db as open_db
    return open_db(game)


def table(name, game="classic"):
    """a client table of the game (wow-data's database, the pinned build)"""
    from wowdata import client
    return client(game, name)


def traces(kind):
    """Forever's creatures (kind "Npc") or objects as Questie places them
    (wow-data's Forever database): {id: {"name", "spawns": {zone area id:
    [(x, y)]}}}, x and y in percent of the zone's map."""
    out = {}
    k = "creature" if kind == "Npc" else "object"
    for id, name in db("forever").execute(f"SELECT e.id, n.name FROM {k} e LEFT JOIN name n ON n.kind = '{k}' AND n.id = e.id AND n.locale = 'enUS'"):
        out[id] = {"name": name, "spawns": {}}
    for id, area, x, y in db("forever").execute(
        "SELECT entity_id, area_id, ux, uy FROM spawn WHERE kind = ? AND source = 'questie' AND area_id IS NOT NULL AND ux IS NOT NULL ORDER BY rowid", (k,)
    ):
        if id in out:
            out[id]["spawns"].setdefault(area, []).append((x, y))
    return out


def forever_quests(classic):
    """Forever's own new quests (none of Classic's ids): {id: {"text": its
    title and objectives, lower case, "ids": the creatures, objects and items
    that give, end or are asked for by it, by kind ((kind, id): an item's id
    is no creature's), "points": []}} (wow-data's Forever database: where
    they stand is their spawns, by traces())."""
    out = collections.defaultdict(lambda: {"text": "", "ids": set(), "points": []})
    f = db("forever")
    for (q,) in f.execute("SELECT id FROM quest ORDER BY id"):
        if q in classic:
            continue
        d = out[q]
        for (t,) in f.execute(
            """SELECT name FROM name WHERE kind = 'quest' AND id = ?1 AND locale = 'enUS'
               UNION ALL SELECT text FROM quest_text WHERE quest_id = ?1 AND locale = 'enUS' AND field = 'objectives'
               UNION ALL SELECT text FROM quest_objective WHERE quest_id = ?1 AND text IS NOT NULL""",
            (q,),
        ):
            d["text"] += " " + t.lower()
        d["ids"] |= set(f.execute("SELECT kind, entity_id FROM quest_relation WHERE quest_id = ?", (q,)))
        d["ids"] |= {("item" if k == "source" else k, i) for k, i in f.execute("SELECT kind, target_id FROM quest_objective WHERE quest_id = ? AND target_id > 0", (q,))}
    return out


def quest_index(c):
    """What a game's quests touch (wow-data's database c, every source's rows):
    "gives" {(kind, id): {quest}}, a creature or object that starts or ends
    it; "asks" {(kind, id): {quest}}, a creature, object or item its
    objectives ask for; "drops" {(kind, id): {item}}, the quest items a
    creature or object yields: the Classic database's loot by the entity's
    templates, its references followed, where it drops only on its quest (a
    negative chance: an item dropped by every humanoid, cloth, a herb, sends
    nobody anywhere); Questie's and Wowhead's (a quest item's sources) by the
    entity's own id; "sources" {item: {(kind, id)}}, the same the other way;
    "names" {quest: its English title}."""
    gives, asks, drops = (collections.defaultdict(set) for _ in range(3))
    for q, kind, i in c.execute("SELECT quest_id, kind, entity_id FROM quest_relation WHERE kind IN ('creature', 'object')"):
        gives[(kind, i)].add(q)
    for q, kind, i in c.execute("SELECT quest_id, kind, target_id FROM quest_objective WHERE kind IN ('creature', 'object', 'item') AND target_id > 0"):
        asks[(kind, i)].add(q)
    wanted = {i for k, i in asks if k == "item"}
    # a Classic template (its loot kind, its id): the creatures and objects it is
    owners = collections.defaultdict(set)
    for i, loot, skin, pick in c.execute("SELECT id, loot_id, skin_loot_id, pick_loot_id FROM creature"):
        for k, t in (("creature", loot), ("skinning", skin), ("pickpocket", pick)):
            if t:
                owners[(k, t)].add(("creature", i))
    for i, t in c.execute("SELECT id, loot_id FROM object WHERE loot_id"):
        owners[("object", t)].add(("object", i))
    rows = collections.defaultdict(list)
    for kind, src, item, ref, chance, source in c.execute(
        "SELECT kind, source_id, item_id, ref_id, chance, source FROM loot WHERE kind IN ('creature', 'object', 'skinning', 'pickpocket', 'reference')"
    ):
        template = source == "classicdb"
        if ref or not template or (chance or 0) < 0:
            rows[(kind, src, template)].append((item, ref))

    def items(key, seen=frozenset()):
        out = set()
        for item, ref in rows.get(key, ()):
            if item in wanted:
                out.add(item)
            if ref and ("reference", ref, True) not in seen:
                out |= items(("reference", ref, True), seen | {key})
        return out

    for (kind, src, template) in list(rows):
        got = kind != "reference" and items((kind, src, template))
        if got:
            for owner in owners[(kind, src)] if template else [("object" if kind == "object" else "creature", src)]:
                drops[owner] |= got
    sources = collections.defaultdict(set)
    for owner, got in drops.items():
        for item in got:
            sources[item].add(owner)
    names = dict(c.execute("SELECT id, name FROM name WHERE kind = 'quest' AND locale = 'enUS'"))
    return {"gives": gives, "asks": asks, "drops": drops, "sources": sources, "names": names}


def wowhead(kind, id, area, game="classic"):
    """Wowhead's points of an object or a creature in a zone (its area id), on
    Classic or Forever: its players' sightings, frozen in wow-data
    (bin/wowhead-points.ts, spawns of source wowhead), in Wowhead's order. None
    when Wowhead doesn't place it there."""
    k = "creature" if kind == "npc" else kind
    rows = db(game).execute(
        "SELECT ux, uy FROM spawn WHERE kind = ? AND entity_id = ? AND area_id = ? AND source = 'wowhead' ORDER BY rowid",
        (k, int(id), area),
    ).fetchall()
    return [(x, y) for x, y in rows] or None


# ── the riddle files ───────────────────────────────────────────────────────
def value(s):
    """A front-matter value: { k: v, ... }, [a, b], "quoted", a number or plain text."""
    s = s.strip()
    if s.startswith("{"):
        return {k.strip(): value(v) for k, v in (p.split(":", 1) for p in s[1:-1].split(","))}
    if s.startswith("["):
        return [value(p) for p in s[1:-1].split(",") if p.strip()]
    if s.startswith('"'):
        return s[1:-1]
    if s in ("true", "false"):
        return s == "true"
    if re.fullmatch(r"-?\d+(\.\d+)?", s):
        return float(s) if "." in s else int(s)
    return s


def riddle_files():
    for f in sorted(os.listdir(EXPEDITIONS)):
        if not f.endswith(".md"):
            continue
        src = open(os.path.join(EXPEDITIONS, f)).read()
        head = src.split("\n---\n", 1)[0]
        zone, client, riddles, quarry, block = None, "both", [], None, None
        for raw in head.split("\n")[1:]:
            line = re.sub(r"\s+#\s.*$", "", raw)
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            m = re.match(r"^(\s*)(- )?(\w+):\s*(.*)$", line)
            if not m:
                sys.exit(f"{f}: can't read {raw!r}")
            indent, item, key, val = m.groups()
            if not indent:
                block = key
                if key == "zone":
                    zone = int(val)
                elif key == "client":
                    client = val
                elif key == "quarry":
                    quarry = {"id": int(val)} if val else {}
            elif block == "quarry" and len(indent) == 2:
                quarry[key] = value(val)
            elif item:
                riddles.append({key: value(val)})
            elif len(indent) == 4 and riddles:
                riddles[-1][key] = value(val)
        yield f, zone, client, riddles, quarry


def reviewed_quests(r, known):
    """An explicit editorial review, not permission to copy a quest objective.
    Exact ids keep a future quest from inheriting an unrelated exemption.
    """
    ids, reason = r.get("quest_overlap", []), r.get("quest_context", "")
    if "quest_overlap" not in r and "quest_context" not in r:
        return set()
    if (not isinstance(ids, list) or not ids
        or any(type(q) is not int or q not in known for q in ids)
        or len(ids) != len(set(ids))
        or not isinstance(reason, str) or not reason.strip()):
        raise ValueError("quest_overlap needs distinct known quest ids and quest_context explaining the separate discovery")
    return set(ids)


def repeated_sites(rs, resolved, width, height):
    """Repeated actions are fine at different discoveries. Reusing a subject,
    or overlapping two passive arrival footprints, is not a new discovery.
    The caller passes only the riddles available to one faction.
    """
    errors, occupied = [], {}
    for r in rs:
        subjects = [(kind, r[kind]) for kind in ("object", "creature", "trigger", "area", "landmark") if kind in r]
        subjects += [("creature", n) for n in r.get("companions", [])]
        for subject in subjects:
            if subject in occupied:
                errors.append(f"{r['id']} reuses {subject[0]} {subject[1]} from {occupied[subject]}")
            else:
                occupied[subject] = r["id"]
    arrivals = [r for r in rs if not r.get("gestures") and "reading" not in r and r.get("found") != "target"]
    for i, a in enumerate(arrivals):
        sa = resolved.get(a["id"], {})
        for b in arrivals[i + 1:]:
            sb = resolved.get(b["id"], {})
            reach = sa.get("r", 0) + sb.get("r", 0) + 5  # the runtime's five-yard cells
            if any(math.hypot((x - u) * width / 100, (y - v) * height / 100) <= reach
                   for x, y in sa.get("spots", []) for u, v in sb.get("spots", [])):
                errors.append(f"{a['id']} and {b['id']} have overlapping arrival footprints")
    return errors


# A quest asks for what stands at a riddle's place when at least this share
# of the things in the zone that answer it (its creature or object, or every
# one that drops the item it asks for) spawn there: the place is its errand,
# not a corner of a zone-wide hunt (the yetis of all Winterspring).
SHARE = 0.5


def quest_ties(subject, inside, total, index):
    """The quests a riddle is tied to, {quest: why}: one that gives, ends or
    asks for its subject (the (kind, id) of its creature or object, its
    companions, its anchor) or an item the subject drops on it, and one that
    asks for what stands at the riddle's place, SHARE of it at least (inside
    and total: the spawns of each (kind, id) there and on the zone's map).
    index: quest_index()'s. Each must be a reviewed quest_overlap, as
    Forever's new quests are."""
    gives, asks, drops, sources = index["gives"], index["asks"], index["drops"], index["sources"]
    out = {}
    for k, i in subject:
        for q in gives.get((k, i), ()):
            out.setdefault(q, f"gives or ends at the riddle's {k} {i}")
        for q in asks.get((k, i), ()):
            out.setdefault(q, f"asks for the riddle's {k} {i}")
        for item in sorted(drops.get((k, i), ())):
            for q in asks.get(("item", item), ()):
                out.setdefault(q, f"asks for item {item}, which the riddle's {k} {i} drops")
    wanted = {t for s in inside for t in [s] + [("item", item) for item in drops.get(s, ())] if t in asks}
    for t in sorted(wanted):
        answers = [t] if t[0] != "item" else sorted(sources.get(t[1], ()))
        there = sum(inside.get(s, 0) for s in answers)
        n = max(there, sum(total.get(s, 0) for s in answers))
        if there and there >= SHARE * n:
            for q in asks[t]:
                out.setdefault(q, f"asks for {t[0]} {t[1]}: {there} of the zone's {n} spawns {'dropping it ' if t[0] == 'item' else ''}are at the riddle's place")
    return out


# The players' sides: their FactionGroup bit, their races' and capitals' factions.
SIDES = {"alliance": (2, {469, 72, 47, 54, 69, 1}), "horde": (4, {67, 76, 81, 68, 530, 2})}


def attacks(t, side):
    """A creature of this faction template (the client's FactionTemplate row)
    attacks the side's players."""
    group, factions = SIDES[side]
    enemies = {int(t[k]) for k in t if k.startswith("Enemies_")}
    friends = {int(t[k]) for k in t if k.startswith("Friend_")}
    if friends & factions:
        return False
    return bool(int(t["EnemyGroup"]) & (1 | group)) or bool(enemies & factions)


def names_it(danger, name):
    """A danger line names a creature: its whole name, or its kind, the name's
    last word, alone or in the plural ("the refugees": a Haggard Refugee)."""
    said = (danger or "").lower()
    return bool(name) and (name.lower() in said or bool(re.search(r"\b" + re.escape(name.split()[-1].lower()) + r"(e?s)?\b", said)))


def zones_own(maps, uimap, holds):
    """A spawn of the Classic database's on this zone's map (uimap) is the
    zone's: Questie and Wowhead place the thing on no map (maps), or on this
    one, or on none that holds the spawn (holds(u): map u holds it). A map
    that holds it is another zone's under this one's rectangle, or a city's
    inside it. A copy they list only elsewhere (an inn's book) stays."""
    return not maps or uimap in maps or not any(holds(u) for u in maps)


def unanswered_keepers(sides, danger, near):
    """The creatures near a riddle's spot that attack one side's players, on a
    riddle open to both, that its danger line doesn't name: [(id, name,
    side)]. sides: the sides that may solve it; near: [(id, name, the sides it
    attacks)]. A riddle answers one with faction: (then one side alone may
    solve it) or by naming it in its danger line."""
    if len(sides) < 2:
        return []
    return [(i, n, next(iter(a))) for i, n, a in near if len(a) == 1 and not names_it(danger, n)]


# ── placing on a zone's map ────────────────────────────────────────────────
def game_names(kind, id, english):
    """An answer's name in every other language, the game's own (Forever's,
    else Classic's, wow-data's databases), when the answer is the thing's own
    name: never a riddle's own ("Roger and Jamin"), which its translations give.
    An area's by the first of its ids."""
    if kind not in ("object", "creature", "area") or not isinstance(id, int):
        return None
    plain = lambda s: s.replace("\u2019", "'").replace("\u201c", '"').replace("\u201d", '"')
    out = {}
    for game in ("forever", "classic"):
        rows = {loc: plain(n) for loc, n in db(game).execute("SELECT locale, name FROM name WHERE kind = ? AND id = ?", (kind, id))}
        if rows.get("enUS") != english:
            continue
        for loc, n in rows.items():
            if loc not in ("enUS", "enGB"):
                out.setdefault(loc, n)
    return dict(sorted(out.items())) or None


def landmark_position(identifier, uimap, games=("classic", "forever")):
    """Shared riddles require the same reviewed location in each game's DB.
    Provenance lives with the landmark, never in a fabricated spawn row.
    """
    rows = []
    for game in games:
        c = db(game)
        if not c.execute("SELECT 1 FROM sqlite_master WHERE name='landmark'").fetchone():
            raise ValueError(f"{game} wow-data lacks landmarks: rebuild its database")
        row = c.execute("SELECT ui_map_id, ux, uy, evidence FROM landmark WHERE id=?", (identifier,)).fetchone()
        if not row or row[0] != uimap or not row[3]:
            raise ValueError(f"landmark {identifier}: no reviewed location on map {uimap} in {game}")
        rows.append([float(row[1]), float(row[2])])
    if any(p != rows[0] for p in rows):
        raise ValueError(f"landmark {identifier}: game positions differ, use separate client content")
    return rows[0]


def main():
    cdb = db("classic")
    # the Classic database's world (wow-data's database): its objects and
    # creatures, their spawns and the paths they walk
    otypes = {i: kind for i, kind in cdb.execute("SELECT id, type FROM object WHERE data IS NOT NULL")}
    names = {}
    for kind in ("object", "creature"):
        for i, n in cdb.execute(f"SELECT e.id, n.name FROM {kind} e JOIN name n ON n.kind = '{kind}' AND n.id = e.id AND n.locale = 'enUS'"):
            names[(kind, i)] = n
    # a creature's face (its display id), shown once its riddle is solved
    faces = {i: int(m.split(",")[0]) for i, m in cdb.execute("SELECT id, display_ids FROM creature WHERE display_ids IS NOT NULL")}
    objects = collections.defaultdict(list)
    for i, m, x, y in cdb.execute("SELECT entity_id, map_id, x, y FROM spawn WHERE kind = 'object' AND source = 'classicdb' ORDER BY rowid"):
        objects[i].append((m, x, y))
    creatures, spawn = collections.defaultdict(list), {}
    for guid, i, m, x, y, move, dist in cdb.execute(
        """SELECT spawn_id, entity_id, map_id, x, y, movement_type, wander_distance FROM spawn
           WHERE kind = 'creature' AND source = 'classicdb' ORDER BY rowid"""
    ):
        spawn[guid] = {"guid": guid, "id": i, "map": m, "position_x": x, "position_y": y, "MovementType": str(move), "spawndist": dist}
        creatures[i].append((m, x, y, spawn[guid]))
    # the spawns a creature may take (a spawn's other entries, its group's), as scripts/rare_zones.py
    takes = collections.defaultdict(set)
    for guid, i in cdb.execute(
        """SELECT spawn_id, entity_id FROM spawn_entry WHERE kind = 'creature'
           UNION SELECT s.spawn_id, e.entity_id FROM spawn_group_spawn s JOIN spawn_group_entry e ON e.group_id = s.group_id
           JOIN spawn_group g ON g.id = s.group_id WHERE g.kind = 'creature'"""
    ):
        takes[i].add(guid)
    for c, rows in list(creatures.items()):
        takes[c] |= {s["guid"] for *_, s in rows}
    # the paths creatures walk: a spawn's own (by guid), else its kind's (by entry)
    paths = collections.defaultdict(list)
    for owner, i, x, y in cdb.execute("SELECT owner, owner_id, x, y FROM path WHERE source = 'classicdb' ORDER BY owner, owner_id, path_id, point"):
        paths[(owner, i)].append((x, y))
    graves = {i: (m, x, y) for i, m, x, y in cdb.execute("SELECT id, map_id, x, y FROM graveyard")}

    def path(d):
        """The points a spawn walks through (world x, y), if it walks a path."""
        if d["MovementType"] != "2":
            return []
        return paths[("spawn", d["guid"])] or paths[("creature", d["id"])]

    def wanders(d):
        """How far a spawn goes from where it stands, in yards."""
        if d["MovementType"] == "1":
            return float(d["spawndist"])
        x, y = float(d["position_x"]), float(d["position_y"])
        return max((((a - x) ** 2 + (b - y) ** 2) ** 0.5 for a, b in path(d)), default=0)

    assignments = collections.defaultdict(list)
    for a in table("UiMapAssignment"):
        assignments[int(a["UiMapID"])].append(a)
    areas = {int(r["ID"]): r for r in table("AreaTable")}
    children = collections.defaultdict(list)
    for i, r in areas.items():
        children[int(r["ParentAreaID"])].append(i)
    triggers = {int(r["ID"]): r for r in table("AreaTrigger")}
    overlays = overlay_centres(areas)

    def on(uimap, m, x, y):
        """A world position on the zone's map, in percent (None if off it)."""
        for a in assignments[uimap]:
            if int(a["MapID"]) != m:
                continue
            x0, y0, x1, y1 = (float(a[k]) for k in ("Region_0", "Region_1", "Region_3", "Region_4"))
            if x0 <= x <= x1 and y0 <= y <= y1:
                u0, v0, u1, v1 = (float(a[k]) for k in ("UiMin_0", "UiMin_1", "UiMax_0", "UiMax_1"))
                return (u0 + (u1 - u0) * (y1 - y) / (y1 - y0)) * 100, (v0 + (v1 - v0) * (x1 - x) / (x1 - x0)) * 100

    def size(uimap):
        """The zone's map in yards: width, height."""
        a = assignments[uimap][0]
        x0, y0, x1, y1 = (float(a[k]) for k in ("Region_0", "Region_1", "Region_3", "Region_4"))
        u0, v0, u1, v1 = (float(a[k]) for k in ("UiMin_0", "UiMin_1", "UiMax_0", "UiMax_1"))
        return (y1 - y0) / (u1 - u0), (x1 - x0) / (v1 - v0)

    def zone_area(uimap):
        ids = collections.Counter(int(a["AreaID"]) for a in assignments[uimap] if int(a["AreaID"]))
        return ids.most_common(1)[0][0]

    def under(area):
        out, todo = [], list(children[area])
        while todo:
            i = todo.pop()
            out.append(i)
            todo += children[i]
        return sorted(out)

    def agreed(kind, id, uimap, points, tolerance=AGREE, source="wowhead"):
        """The dump's points on the zone's map that Wowhead places in the zone
        too (the maps overlap at their edges, a city lies inside its zone's
        rectangle: a point of the dump alone is another place's)."""
        if source == "questie":
            theirs = list(cdb.execute("SELECT ux, uy FROM spawn WHERE kind=? AND entity_id=? AND area_id=? AND source='questie'",
                                     ("creature" if kind == "npc" else kind, id, zone_area(uimap))))
        else:
            theirs = wowhead(kind, id, zone_area(uimap)) or []
        return [(x, y) for x, y in points if any(abs(x - a) <= tolerance and abs(y - b) <= tolerance for a, b in theirs)]

    def haunts(uimap, id, w):
        """A quarry's haunts on the zone's map: [[x, y, r]] (percent of the width).
        A spawn that walks a path haunts its path: each of its points is one."""
        found = []
        for g in sorted(takes[id]):
            d = spawn[g]
            p = on(uimap, int(d["map"]), float(d["position_x"]), float(d["position_y"]))
            if p:
                found.append((p, d))
        kept = set(agreed("npc", id, uimap, [p for p, _ in found], AGREE_HAUNT))
        # where players met it, as Wowhead records them (a creature that roams
        # further than its spawn says), near a spawn the two agree on
        near = lambda p: any(((p[0] - q[0]) ** 2 + ((p[1] - q[1]) * ASPECT) ** 2) ** 0.5 <= ROAM for q in kept)
        points = [(tuple(p), 0) for p in (wowhead("npc", id, zone_area(uimap)) or []) if near(p)]
        for p, d in found:
            if p not in kept:
                continue
            walk = [q for q in (on(uimap, int(d["map"]), a, b) for a, b in path(d)) if q]
            points += [(p, 0)] + [(q, 0) for q in walk] if walk else [(p, wanders(d))]
        out = []
        for p, far in points:
            for c in out:
                cx, cy = sum(q[0] for q, _ in c) / len(c), sum(q[1] for q, _ in c) / len(c)
                if ((p[0] - cx) ** 2 + ((p[1] - cy) * ASPECT) ** 2) ** 0.5 <= HAUNT:
                    c.append((p, far))
                    break
            else:
                out.append([(p, far)])
        circles = []
        for c in out:
            cx, cy = sum(q[0] for q, _ in c) / len(c), sum(q[1] for q, _ in c) / len(c)
            reach = max(((q[0] - cx) ** 2 + ((q[1] - cy) * ASPECT) ** 2) ** 0.5 + far / w * 100 for q, far in c)
            circles.append([round(cx, 1), round(cy, 1), round(max(HAUNT_MIN, reach + 1.5), 1)])
        return circles

    errors, zones, riddles, quarries = [], {}, {}, {}
    placed = []  # (file, uiMap, riddle, its points on the map), for the checks below
    for f, uimap, client, rs, quarry in riddle_files():
        if client == "forever":
            forever_zone(f, uimap, rs, quarry, errors, zones, riddles, quarries)
            continue
        if uimap not in assignments:
            errors.append(f"{f}: no uiMap {uimap}")
            continue
        w, h = size(uimap)
        mine = under(zone_area(uimap))
        zones[str(uimap)] = {"w": round(w, 1), "h": round(h, 1), "areas": mine}
        if quarry:
            id = quarry.get("id")
            spots = id and haunts(uimap, id, w)
            if not spots:
                errors.append(f"{f}: quarry {id}: no spawn on the map that the dump and Wowhead agree on")
            else:
                quarries[str(uimap)] = {"id": id, "name": names.get(("creature", id)), "haunts": spots}
                if game_names("creature", id, names.get(("creature", id))):
                    quarries[str(uimap)]["names"] = game_names("creature", id, names.get(("creature", id)))
        for r in rs:
            id, out, where = r["id"], {"zone": uimap}, f"{f}: {r['id']}"
            if "position_check" in r and (r["position_check"] != "questie" or not any(k in r for k in ("object", "creature"))):
                errors.append(f"{where}: position_check: questie is for a Classic object or creature's independent map position")
                continue
            if r.get("found") == "place" and (r.get("reading") or r.get("companions")
                or type(r.get("radius")) is not int or not 10 <= r["radius"] <= 100):
                errors.append(f"{where}: found: place needs no reading or companions and a radius of 10 to 100 yards")
                continue
            if r.get("found") == "patrol" and (not r.get("gestures") or r.get("companions")):
                errors.append(f"{where}: found: patrol needs a gesture and no companions")
                continue
            if "landmark" in r and (not r.get("name") or r.get("found") or r.get("reading")
                or type(r.get("radius")) is not int or not 10 <= r["radius"] <= 100):
                errors.append(f"{where}: landmark needs its own name, a radius of 10 to 100 yards, no found mode or reading")
                continue
            if "indoors" in r:
                errors.append(f"{where}: indoors is not a verified solution condition")
                continue
            # what it was resolved from: the build refuses a file changed since
            kind = next((k for k in ("object", "creature", "trigger", "area", "landmark") if k in r), None)
            out["of"] = f"{kind}:{r[kind]}" if kind else None
            if "anchor" in r:
                out["of"] += " " + ",".join(f"{k}:{v}" for k, v in r["anchor"].items())
            if r.get("found"):
                out["of"] += f" found:{r['found']}"
            if r.get("position_check"):
                out["of"] += f" position_check:{r['position_check']}"
            if r.get("hint_area"):
                out["hint"] = [r["hint_area"][k] for k in ("x", "y", "r")]
            # its name, once solved: the file's, else the game's (the object's,
            # the creature's, the area's)
            out["name"] = r.get("name") or names.get((kind, r.get(kind))) or (r["area"] if kind == "area" else None)
            if game_names(kind, r.get(kind), out["name"]):
                out["names"] = game_names(kind, r.get(kind), out["name"])
            if not out["name"]:
                errors.append(f"{where}: no name: give the riddle's own (name:)")
            if kind == "landmark":
                try:
                    point = landmark_position(r["landmark"], uimap, ("classic", "forever") if client == "both" else (client,))
                except ValueError as e:
                    errors.append(f"{where}: {e}")
                    continue
                points = [point]
                out.update(spots=points, r=r["radius"])
            elif "object" in r:
                check_source = r.get("position_check", "wowhead")
                points = agreed("object", r["object"], uimap, [p for p in (on(uimap, *s) for s in objects[r["object"]]) if p], source=check_source)
                if not points:
                    errors.append(f"{where}: object {r['object']}: no spawn on the map that the dump and {check_source} agree on")
                    continue
                out.update(spots=points, r=NEAR)
                # a reading: a text object, which opens the game's reader (a
                # quest's poster opens the quest window), and its own title
                if "reading" in r and (otypes.get(r["object"]) != 9 or names[("object", r["object"])] != r["reading"]):
                    errors.append(f"{where}: reading: object {r['object']} is no text object titled {r['reading']!r}")
            elif "creature" in r:
                # its spawns inside the hint circle (a kind standing in more
                # than one place, the Unseen: those the riddle means), the
                # dump's and Wowhead's alike
                ha = r.get("hint_area") or {}
                held = lambda p: ha and (p[0] - ha["x"]) ** 2 + ((p[1] - ha["y"]) * ASPECT) ** 2 <= ha["r"] ** 2
                # one found by targeting may be met anywhere it walks: its path counts
                follows = r.get("found") in ("target", "patrol")
                walks = lambda d: [q for q in (on(uimap, int(d["map"]), x, y) for x, y in path(d)) if q] if follows else []
                found = [(on(uimap, *s[:3]), s[3]) for s in creatures[r["creature"]]]
                # one found by targeting is placed only to the hint's measure: the haunts' tolerance
                tol = AGREE_HAUNT if follows else AGREE
                check_source = r.get("position_check", "wowhead")
                found = [(p, d) for p, d in found if p and agreed("npc", r["creature"], uimap, [p] + walks(d), tol, source=check_source)]
                spawns = [(p, d) for p, d in found if held(p) or any(held(q) for q in walks(d))]
                if not spawns:
                    errors.append(f"{where}: creature {r['creature']}: no spawn inside the hint circle (nor a path through it, found by targeting) that the dump and Wowhead agree on")
                    continue
                # found by targeting it near: one of a kind, or one only so found
                if r.get("found") != "place" and (len(found) == 1 or follows):
                    out["npc"] = r["creature"]
                if faces.get(int(r["creature"])):
                    out["face"] = faces[int(r["creature"])]
                still = [(p, wanders(d)) for p, d in spawns if wanders(d) <= NEAR]
                if not follows and still:
                    out.update(spots=[p for p, _ in still], r=NEAR + math.ceil(max(far for _, far in still)))
                if r.get("found") == "place":
                    if not still:
                        errors.append(f"{where}: found: place needs a stationary anchor")
                        continue
                    out["r"] = r["radius"]
                if r.get("found") == "patrol":
                    if not any(walks(d) for _, d in spawns):
                        errors.append(f"{where}: found: patrol needs a recorded path")
                        continue
                    # Sample whole path segments, not only waypoint circles.
                    # A player and guard can meet between two distant points.
                    samples = []
                    for p, d in spawns:
                        trail = [p] + walks(d)
                        for a, b in zip(trail, trail[1:] + trail[:1]):
                            distance = math.hypot((a[0] - b[0]) / 100 * w, (a[1] - b[1]) / 100 * h)
                            steps = max(1, math.ceil(distance / NEAR))
                            samples.extend([[a[0] + (b[0] - a[0]) * i / steps, a[1] + (b[1] - a[1]) * i / steps] for i in range(steps)])
                    out.update(spots=samples, r=NEAR + 5, bounded=True)
                points = [q for p, d in spawns for q in ([p] if held(p) else [q for q in walks(d) if held(q)])]
            elif "trigger" in r:
                t = triggers.get(r["trigger"])
                p = t and on(uimap, int(t["ContinentID"]), float(t["Pos_0"]), float(t["Pos_1"]))
                if not p:
                    errors.append(f"{where}: trigger {r['trigger']} is not on the map")
                    continue
                out.update(spots=[p], r=max(NEAR, round(float(t["Radius"]))))
            elif "area" in r:
                ids = [i for i in mine if areas[i]["AreaName_lang"].strip() == r["area"]]
                if not ids:
                    errors.append(f"{where}: no sub-area {r['area']!r} in this zone")
                    continue
                out["areas"] = ids
                if game_names("area", min(ids), out["name"]):
                    out["names"] = game_names("area", min(ids), out["name"])
                if "anchor" in r:
                    (kind, n), = r["anchor"].items()
                    found = {"grave": [graves[n]] if n in graves else [], "object": objects[n], "creature": creatures[n]}.get(kind, [])
                    points = [p for p in (on(uimap, *s[:3]) for s in found) if p][:1]
                    if not points:
                        errors.append(f"{where}: the anchor {r['anchor']} is not on the map")
                        continue
                else:
                    points = [overlays[i] for i in ids if i in overlays][:1]
                    if not points:
                        errors.append(f"{where}: the area has no overlay on the map: give an anchor inside it")
                        continue
            else:
                errors.append(f"{where}: no spot (object, creature, trigger or area)")
                continue
            if "reading" in r and "object" not in r:
                errors.append(f"{where}: a reading is an object's")
            if "spots" in out:
                points = out["spots"]
            ha = r.get("hint_area")
            inside = ha and [(x, y) for x, y in points if (x - ha["x"]) ** 2 + ((y - ha["y"]) * ASPECT) ** 2 <= ha["r"] ** 2]
            if not ha:
                errors.append(f"{where}: no hint_area")
            elif not inside:
                errors.append(f"{where}: the hint circle {ha} doesn't hold the spot {points[0]}")
            elif "spots" in out:
                # the copies of a book elsewhere in the zone are other riddles' (or none)
                out["spots"] = [[round(x, 2), round(y, 2)] for x, y in inside]
            riddles[id] = out
            placed.append((f, uimap, r, inside or points))

    # ── as a reader meets them ──────────────────────────────────────────────
    ct = {i: {"Faction": faction or 0, "Name": names.get(("creature", i))} for i, faction in cdb.execute("SELECT id, faction_id FROM creature")}
    ft = {int(d["ID"]): d for d in table("FactionTemplate")}

    def hostile(template, side, templates=None):
        """A creature of this faction template attacks the side's players."""
        t = (ft if templates is None else templates).get(template)
        return bool(t) and attacks(t, side)

    def deed(r):
        if "reading" in r:
            return "reading"
        if r.get("gestures"):
            return "gesture"
        return "speaking" if r.get("found") == "target" else "arrival"

    homes = {f: (re.search(r"^home: (\w+)", open(os.path.join(EXPEDITIONS, f)).read(), re.M) or [None, None])[1] for f, *_ in placed}
    for f, uimap, r, _ in placed:
        sides = [r["faction"]] if r.get("faction") else ([homes[f]] if homes[f] else list(SIDES))
        c = "creature" in r and ct.get(int(r["creature"]))
        for side in sides:
            # A place anchor is never a creature the player must meet.
            # Its fixed position survives death, absence or movement.
            place_only = r.get("found") == "place" and r.get("name") and not r.get("gestures")
            if c and not place_only and hostile(int(c["Faction"]), side):
                errors.append(f"{f}: {r['id']}: {c['Name']} attacks the {side}'s players: a riddle never asks for a kill (or give it to the other side: faction:)")
    files = list(riddle_files())
    # A group named in a verse must not silently mean just its first keeper.
    # Companions are real, non-hostile creatures too, and participate in the
    # same quest-road checks as the primary creature below.
    for f, uimap, client, rs, _ in files:
        for r in rs:
            ids = r.get("companions", [])
            if not ids:
                continue
            if (not isinstance(ids, list) or not r.get("gestures") or not r.get("creature")
                or any(type(i) is not int or i <= 0 or i == r["creature"] for i in ids)
                or len(set(ids)) != len(ids)):
                errors.append(f"{f}: {r['id']}: companions: distinct other creature ids for a gesture's group")
                continue
            sides = [r["faction"]] if r.get("faction") else ([homes.get(f)] if homes.get(f) else list(SIDES))
            for game in (["forever"] if client == "forever" else ["classic", "forever"]):
                templates = {int(t["ID"]): t for t in table("FactionTemplate", game)}
                for i in ids:
                    creature = db(game).execute("SELECT faction_id FROM creature WHERE id = ?", (i,)).fetchone()
                    if not creature:
                        errors.append(f"{f}: {r['id']}: no companion creature {i} in {game}")
                    elif any(hostile(int(creature[0] or 0), side, templates) for side in sides):
                        errors.append(f"{f}: {r['id']}: companion {i} attacks a side that may solve the riddle in {game}")
            if r["id"] in riddles:
                riddles[r["id"]]["companions"] = ids
    for f, *_ in files:
        if f not in homes:
            homes[f] = (re.search(r"^home: (\w+)", open(os.path.join(EXPEDITIONS, f)).read(), re.M) or [None, None])[1]
    for f, uimap, client, rs, _ in files:
        for side in SIDES:
            mine = [r for r in rs if (not homes[f] or homes[f] == side) and r.get("faction", side) == side]
            size = zones.get(str(uimap), {})
            for error in repeated_sites(mine, riddles, size.get("w", 0), size.get("h", 0)):
                errors.append(f"{f}: the {side}'s reader: {error}")

    classic = {i for (i,) in cdb.execute("SELECT id FROM quest")}
    new = forever_quests(classic)
    known_quests = classic | {i for (i,) in db("forever").execute("SELECT id FROM quest")}
    norm = lambda x: re.sub(r"[^a-z]", "", x.lower())
    zone_names = {int(z["ID"]): z["Name_lang"] for z in table("UiMap")}
    npcs, objs = traces("Npc"), traces("Object")
    # (Forever's own zones: their riddles' creatures and objects, against its quests too)
    own = [(f, uimap, r, []) for f, uimap, client, rs, _ in files if client == "forever" for r in rs]
    told = set()  # (riddle, quest): Forever's new quests already said, not said twice below
    for f, uimap, r, points in placed + own:
        where = f"{f}: {r['id']}"
        try:
            reviewed = reviewed_quests(r, known_quests)
        except ValueError as e:
            errors.append(f"{where}: {e}")
            reviewed = set()
        subject = [(k, int(r[k])) for k in ("creature", "object") if k in r]
        subject += [("creature", i) for i in r.get("companions", [])]
        subject += [(k, int(v)) for k, v in (r.get("anchor") or {}).items() if k in ("creature", "object")]
        named = {n for n in [r.get("name"), r.get("area"), r.get("reading")] + [names.get(s) or ((npcs if s[0] == "creature" else objs).get(s[1]) or {}).get("name") for s in subject] if n and len(n) > 4}
        for q, d in sorted(new.items()):
            if q in reviewed:
                continue
            hit = [i for i in subject if i in d["ids"]]
            if hit:
                errors.append(f"{where}: Forever's new quest {q} gives, ends or asks for {hit[0][0]} {hit[0][1]}")
                told.add((r["id"], q))
            said = [n for n in named if re.search(r"\b" + re.escape(n.lower()) + r"\b", d["text"])]
            if said:
                errors.append(f"{where}: Forever's new quest {q} names {said[0]!r}")
                told.add((r["id"], q))
            if deed(r) != "arrival" or not points:
                continue
            near = lambda x, y: any(((x - a) ** 2 + ((y - b) * ASPECT) ** 2) ** 0.5 <= FOREVER_NEAR for a, b in points)
            mine = [(x, y) for m, x, y in d["points"] if norm(m) == norm(zone_names.get(uimap, ""))]
            area = zone_area(uimap)
            for k, i in d["ids"]:
                t = npcs.get(i) if k == "creature" else objs.get(i) if k == "object" else None
                mine += (t or {}).get("spawns", {}).get(area, [])
            close = [(x, y) for x, y in mine if near(x, y)]
            if close:
                errors.append(f"{where}: arriving here is Forever's new quest {q}'s road (a point at {close[0][0]:.1f}, {close[0][1]:.1f})")
                told.add((r["id"], q))

    # ── each game's quests tied to a riddle, and who keeps its spot ─────────
    # The Forever road's twin for every quest of both games (Classic's are
    # Forever's too): one that gives, ends or asks for the riddle's subject,
    # or asks for what stands at its place. And on a riddle open to both
    # sides, a creature by its spot (or its area's anchor) that attacks one.
    games = ("classic", "forever")
    indexes = {g: quest_index(db(g)) for g in games}
    templates = {g: {int(t["ID"]): t for t in table("FactionTemplate", g)} for g in games}
    kin = {g: dict(db(g).execute("SELECT id, faction_id FROM creature")) for g in games}
    # the sides Questie says a creature is friendly to (A, H, AH): Forever's
    # new creatures have no faction template in the data, only this
    friendly = {g: dict(db(g).execute("SELECT id, friendly FROM creature WHERE friendly IS NOT NULL")) for g in games}
    cnames = {g: dict(db(g).execute("SELECT id, name FROM name WHERE kind = 'creature' AND locale = 'enUS'")) for g in games}
    may_be = collections.defaultdict(set)  # a spawn's guid: every creature it may be
    for c, guids in takes.items():
        for g in guids:
            may_be[g].add(c)
    forever_maps = collections.defaultdict(list)
    for a in table("UiMapAssignment", "forever"):
        forever_maps[int(a["UiMapID"])].append(a)
    world, seen = {}, {}
    # the maps Questie and Wowhead place each thing on: its zones' (by their
    # area ids, the client's UiMapAssignment), else, where they name no zone,
    # the continent's. A spawn of the Classic database's on a zone's map is
    # another's when they don't place the thing in this zone and a map they
    # do place it on holds the spawn: a zone's rectangle holds what lies under
    # it (Overmaster Pyron, whom they place on the continent alone, in
    # Blackrock Mountain under Searing Gorge) and the cities inside it
    # (Darnassus's wisps), never a copy elsewhere (an inn's book)
    maps_of = collections.defaultdict(set)
    for u, rows in assignments.items():
        for a in rows:
            if int(a["AreaID"]):
                maps_of[int(a["AreaID"])].add(u)
    placed_on = collections.defaultdict(set)
    for k, i, area, ui in cdb.execute("SELECT DISTINCT kind, entity_id, area_id, ui_map_id FROM spawn WHERE source IN ('questie', 'wowhead')"):
        placed_on[(k, i)] |= maps_of.get(area, set()) if area else {ui}

    def world_on(uimap):
        """The Classic database's creatures and objects on the zone's map (one
        world on both games): {(kind, id, x, y, far, at its spawn)}, each
        creature a spawn may be, at its spawn and along its path; far: how far
        it wanders, in yards. Not one Questie and Wowhead place in another
        zone that holds the spawn."""
        if uimap not in world:
            out = set()

            def ours(k, i, m, x, y):
                return zones_own(placed_on.get((k, i)), uimap, lambda u: on(u, m, x, y))

            for a in assignments[uimap]:
                m = int(a["MapID"])
                x0, y0, x1, y1 = (float(a[k]) for k in ("Region_0", "Region_1", "Region_3", "Region_4"))
                for kind, i, guid, x, y in cdb.execute(
                    "SELECT kind, entity_id, spawn_id, x, y FROM spawn WHERE source = 'classicdb' AND map_id = ? AND x BETWEEN ? AND ? AND y BETWEEN ? AND ?",
                    (m, x0, x1, y0, y1),
                ):
                    p = on(uimap, m, x, y)
                    if not p:
                        continue
                    if kind == "object":
                        if ours("object", i, m, x, y):
                            out.add(("object", i, *p, 0, True))
                        continue
                    d = spawn[guid]
                    far = float(d["spawndist"] or 0) if d["MovementType"] == "1" else 0
                    walk = [(q, False) for q in (on(uimap, m, u, v) for u, v in path(d)) if q]
                    for q, at in [(p, True)] + walk:
                        out |= {("creature", c, *q, far, at) for c in may_be[guid] | {i} if ours("creature", c, m, x, y)}
            world[uimap] = out
        return world[uimap]

    def traced(game, area):
        """The game's Questie and Wowhead points in a zone (its area id): {(kind, id, x, y, 0, True)}."""
        if (game, area) not in seen:
            seen[(game, area)] = {(k, i, x, y, 0, True) for k, i, x, y in db(game).execute(
                "SELECT kind, entity_id, ux, uy FROM spawn WHERE source IN ('questie', 'wowhead') AND area_id = ? AND ux IS NOT NULL", (area,))}
        return seen[(game, area)]

    told_on = lambda gs: " and ".join({"classic": "Classic Era", "forever": "Forever"}[g] for g in gs)
    gated = [(f, uimap, "both", r, points) for f, uimap, r, points in placed]
    gated += [(f, uimap, "forever", r, None) for f, uimap, r, _ in own]
    for f, uimap, client, r, points in gated:
        where, ha = f"{f}: {r['id']}", r.get("hint_area")
        if not ha or str(uimap) not in zones:
            continue  # said above
        try:
            reviewed = reviewed_quests(r, known_quests)
        except ValueError:
            reviewed = set()  # said above
        held = lambda x, y: (x - ha["x"]) ** 2 + ((y - ha["y"]) * ASPECT) ** 2 <= ha["r"] ** 2
        if client == "forever":
            on_games, mine = ("forever",), set()
            area = collections.Counter(int(a["AreaID"]) for a in forever_maps[uimap] if int(a["AreaID"])).most_common(1)[0][0]
        else:
            on_games, mine, area = games, world_on(uimap), zone_area(uimap)
        on_map = {(k, i) for k, i, *_ in mine}
        subject = [(k, int(r[k])) for k in ("creature", "object") if k in r]
        subject += [("creature", i) for i in r.get("companions", [])]
        subject += [(k, int(v)) for k, v in (r.get("anchor") or {}).items() if k in ("creature", "object")]
        spots = points or (riddles.get(r["id"]) or {}).get("spots") or [
            (x, y) for k, i, x, y, _, _ in traced("forever", area) if (k, i) == ("creature", r.get("creature")) and held(x, y)]
        w, h = zones[str(uimap)]["w"], zones[str(uimap)]["h"]
        yards = lambda x, y: min((math.hypot((x - u) * w / 100, (y - v) * h / 100) for u, v in spots), default=math.inf)
        # the riddle's place: an area's is its hint circle; a spot's, where it
        # is solved and NEAR yards about (a wide hint circle holds far more)
        reach = ((riddles.get(r["id"]) or {}).get("r") or NEAR) + NEAR
        there = held if "area" in r else lambda x, y: yards(x, y) <= reach
        ties = {}
        for game in on_games:
            # the spawns on the zone's map and at the place: the Classic
            # database's, else (a thing it doesn't place here: one of
            # Forever's, or moved by Forever) the game's points
            zone = collections.Counter((k, i, x, y) for k, i, x, y, _, at in mine if at)
            zone.update((k, i, x, y) for k, i, x, y, _, _ in traced(game, area) if (k, i) not in on_map)
            total, inside = collections.Counter(), collections.Counter()
            for (k, i, x, y), n in zone.items():
                total[(k, i)] += n
                if there(x, y):
                    inside[(k, i)] += n
            for q, why in quest_ties(subject, inside, total, indexes[game]).items():
                if q not in reviewed and (r["id"], q) not in told:
                    ties.setdefault(q, (why, []))[1].append(game)
        for q, (why, gs) in sorted(ties.items()):
            errors.append(f"{where}: quest {q} ({indexes[gs[0]]['names'].get(q)}) {why}, on {told_on(gs)}: a reviewed quest_overlap with its quest_context")
        # who keeps the spot: a keeper the riddle asks for is the never-a-kill check's above
        sides = [r["faction"]] if r.get("faction") else ([homes[f]] if homes.get(f) else list(SIDES))
        place_only = r.get("found") == "place" and r.get("name") and not r.get("gestures")
        asked = set(r.get("companions", [])) | ({r["creature"]} if "creature" in r and client != "forever" and not place_only else set())
        keep = {}
        # an area placed by its overlay has no spot to stand by: its overlay's centre is the map's
        for game in on_games if len(sides) > 1 and ("area" not in r or "anchor" in r) else ():
            near = set()
            for k, i, x, y, far, _ in mine | {t for t in traced(game, area) if t[:2] not in on_map}:
                if k == "creature" and i not in asked and yards(x, y) <= NEAR + far:
                    near.add(i)
            def attacked(i):
                t = templates[game].get(kin[game].get(i) or 0)
                if t:
                    return {s for s in SIDES if attacks(t, s)}
                # friendly to one side only: a keeper of that side's
                return {"A": {"horde"}, "H": {"alliance"}}.get(friendly[game].get(i), set())
            near = [(i, cnames[game].get(i), attacked(i)) for i in sorted(near)]
            for i, n, side in unanswered_keepers(sides, r.get("danger"), near):
                keep.setdefault(i, (n, side, []))[2].append(game)
        for i, (n, side, gs) in sorted(keep.items()):
            errors.append(f"{where}: {n} ({i}), by the spot, attacks the {side}'s players on {told_on(gs)}: faction: (the other side's riddle), or a danger line that names it")

    if errors:
        print("\n".join(f"x {e}" for e in errors))
        sys.exit(1)
    if DRY:
        print(f"{len(riddles)} riddles pass, nothing written (--dry)")
        return
    with open(OUT, "w") as f:
        f.write("{\n")
        f.write(' "zones": {\n' + ",\n".join(f'  "{k}": {json.dumps(v)}' for k, v in sorted(zones.items(), key=lambda kv: int(kv[0]))) + "\n },\n")
        f.write(' "riddles": {\n' + ",\n".join(f'  "{k}": {json.dumps(v)}' for k, v in sorted(riddles.items())) + "\n },\n")
        f.write(' "quarries": {\n' + ",\n".join(f'  "{k}": {json.dumps(v)}' for k, v in sorted(quarries.items(), key=lambda kv: int(kv[0]))) + "\n },\n")
        f.write(f' "emotes": {json.dumps(sorted(r["Name"] for r in table("EmotesText")))}\n}}\n')
    kinds = collections.Counter("areas" in v and "area" or "spot" for v in riddles.values())
    print(f"{len(riddles)} riddles in {len(zones)} zones ({kinds['spot']} spots, {kinds['area']} areas), {len(quarries)} quarries -> data/expeditions.json")


def overlay_centres(areas, client="classic"):
    """A sub-area's centre on its zone's map, in percent, from the map overlay
    that names it (WorldMapOverlay on the map art, 1002 by 668)."""
    out = {}
    for o in table("WorldMapOverlay", client):
        t, b, l, r = (float(o[k]) for k in ("HitRectTop", "HitRectBottom", "HitRectLeft", "HitRectRight"))
        if b <= t or r <= l:
            l, t = float(o["OffsetX"]), float(o["OffsetY"])
            r, b = l + float(o["TextureWidth"]), t + float(o["TextureHeight"])
        for k in ("AreaID_0", "AreaID_1", "AreaID_2", "AreaID_3"):
            a = int(o[k])
            if a and a in areas:
                out.setdefault(a, ((l + r) / 2 / 10.02, (t + b) / 2 / 6.68))
    return out


def forever_zone(f, uimap, rs, quarry, errors, zones, riddles, quarries):
    """A zone of Forever's own: its map from Forever's client tables, its
    creatures' points from Questie's Forever (wow-data's database), each kept only where Wowhead's
    Forever database places the creature too (they share the zone's map)."""
    assignments = [a for a in table("UiMapAssignment", "forever") if int(a["UiMapID"]) == uimap]
    if not assignments:
        errors.append(f"{f}: no uiMap {uimap} on Forever")
        return
    areas = {int(r["ID"]): r for r in table("AreaTable", "forever")}
    children = collections.defaultdict(list)
    for i, r in areas.items():
        children[int(r["ParentAreaID"])].append(i)
    a = assignments[0]
    x0, y0, x1, y1 = (float(a[k]) for k in ("Region_0", "Region_1", "Region_3", "Region_4"))
    u0, v0, u1, v1 = (float(a[k]) for k in ("UiMin_0", "UiMin_1", "UiMax_0", "UiMax_1"))
    w, h = (y1 - y0) / (u1 - u0), (x1 - x0) / (v1 - v0)
    zone = collections.Counter(int(a["AreaID"]) for a in assignments if int(a["AreaID"])).most_common(1)[0][0]
    mine, todo = [], list(children[zone])
    while todo:
        i = todo.pop()
        mine.append(i)
        todo += children[i]
    mine.sort()
    zones[str(uimap)] = {"w": round(w, 1), "h": round(h, 1), "areas": mine}
    npcs = traces("Npc")
    overlays = overlay_centres(areas, "forever")

    def agreed(id, tolerance):
        """The traces' points of a creature that Wowhead's Forever places too, and Wowhead's."""
        theirs = wowhead("npc", id, zone, "forever") or []
        ours = (npcs.get(id) or {}).get("spawns", {}).get(zone, [])
        return [p for p in ours if any(abs(p[0] - a) <= tolerance and abs(p[1] - b) <= tolerance for a, b in theirs)], theirs

    yards = lambda p, q: (((p[0] - q[0]) / 100 * w) ** 2 + ((p[1] - q[1]) / 100 * h) ** 2) ** 0.5
    if quarry:
        id = quarry.get("id")
        kept, theirs = agreed(id, AGREE_HAUNT) if id else ([], [])
        near = lambda p: any(((p[0] - q[0]) ** 2 + ((p[1] - q[1]) * ASPECT) ** 2) ** 0.5 <= ROAM for q in kept)
        circles = []
        for p in kept + [p for p in theirs if near(p)]:
            for c in circles:
                cx, cy = sum(q[0] for q in c) / len(c), sum(q[1] for q in c) / len(c)
                if ((p[0] - cx) ** 2 + ((p[1] - cy) * ASPECT) ** 2) ** 0.5 <= HAUNT:
                    c.append(p)
                    break
            else:
                circles.append([p])
        haunts = []
        for c in circles:
            cx, cy = sum(q[0] for q in c) / len(c), sum(q[1] for q in c) / len(c)
            reach = max(((q[0] - cx) ** 2 + ((q[1] - cy) * ASPECT) ** 2) ** 0.5 for q in c)
            haunts.append([round(cx, 1), round(cy, 1), round(max(HAUNT_MIN, reach + 1.5), 1)])
        if not haunts:
            errors.append(f"{f}: quarry {id}: no point the traces and Wowhead's Forever agree on")
        else:
            quarries[str(uimap)] = {"id": id, "name": quarry.get("name") or (npcs.get(id) or {}).get("name"), "haunts": haunts}
            if game_names("creature", id, quarries[str(uimap)]["name"]):
                quarries[str(uimap)]["names"] = game_names("creature", id, quarries[str(uimap)]["name"])
    for r in rs:
        id, out, where = r["id"], {"zone": uimap}, f"{f}: {r['id']}"
        if r.get("found") == "place" and (r.get("reading") or r.get("companions")
            or type(r.get("radius")) is not int or not 10 <= r["radius"] <= 100):
            errors.append(f"{where}: found: place needs no reading or companions and a radius of 10 to 100 yards")
            continue
        if r.get("found") == "patrol" or "position_check" in r:
            errors.append(f"{where}: patrol and position_check require the Classic world records")
            continue
        if "landmark" in r and (not r.get("name") or r.get("found") or r.get("reading")
            or type(r.get("radius")) is not int or not 10 <= r["radius"] <= 100):
            errors.append(f"{where}: landmark needs its own name, a radius of 10 to 100 yards, no found mode or reading")
            continue
        if "indoors" in r:
            errors.append(f"{where}: indoors is not a verified solution condition")
            continue
        kind = next((k for k in ("object", "creature", "trigger", "area", "landmark") if k in r), None)
        out["of"] = f"{kind}:{r[kind]}" if kind else None
        if "anchor" in r:
            out["of"] += " " + ",".join(f"{k}:{v}" for k, v in r["anchor"].items())
        if r.get("found"):
            out["of"] += f" found:{r['found']}"
        if r.get("hint_area"):
            out["hint"] = [r["hint_area"][k] for k in ("x", "y", "r")]
        ha = r.get("hint_area") or {}
        held = lambda p: ha and (p[0] - ha["x"]) ** 2 + ((p[1] - ha["y"]) * ASPECT) ** 2 <= ha["r"] ** 2
        if kind == "landmark":
            out["name"] = r["name"]
            try:
                points = [landmark_position(r["landmark"], uimap, ("forever",))]
            except ValueError as e:
                errors.append(f"{where}: {e}")
                continue
            out.update(spots=points, r=r["radius"])
        elif kind == "creature":
            out["name"] = r.get("name") or (npcs.get(r["creature"]) or {}).get("name")
            if game_names("creature", r["creature"], out["name"]):
                out["names"] = game_names("creature", r["creature"], out["name"])
            target = r.get("found") == "target"
            kept, _ = agreed(r["creature"], AGREE_HAUNT if target else AGREE)
            points = [p for p in kept if held(p)]
            if not points:
                errors.append(f"{where}: creature {r['creature']}: no point inside the hint circle that the traces and Wowhead's Forever agree on")
                continue
            if target:
                out["npc"] = r["creature"]
            else:
                # one that stands: its points within NEAR yards of each other
                spread = max(yards(p, q) for p in points for q in points)
                if spread > NEAR:
                    errors.append(f"{where}: creature {r['creature']} is met {spread:.0f} yards apart: found: target")
                    continue
                out.update(spots=points, r=r["radius"] if r.get("found") == "place" else NEAR + math.ceil(spread))
        elif kind == "area":
            out["name"] = r.get("name") or r["area"]
            ids = [i for i in mine if areas[i]["AreaName_lang"].strip() == r["area"]]
            if not ids:
                errors.append(f"{where}: no sub-area {r['area']!r} in this zone")
                continue
            out["areas"] = ids
            if game_names("area", min(ids), out["name"]):
                out["names"] = game_names("area", min(ids), out["name"])
            points = [overlays[i] for i in ids if i in overlays][:1]
            if not points:
                errors.append(f"{where}: the area has no overlay on Forever's map")
                continue
        else:
            errors.append(f"{where}: a zone of Forever's own takes a creature or an area")
            continue
        if not out["name"]:
            errors.append(f"{where}: no name: give the riddle's own (name:)")
        if not ha:
            errors.append(f"{where}: no hint_area")
        elif not [p for p in points if held(p)]:
            errors.append(f"{where}: the hint circle {ha} doesn't hold the spot {points[0]}")
        if "spots" in out:
            out["spots"] = [[round(x, 2), round(y, 2)] for x, y in out["spots"]]
        riddles[id] = out


if __name__ == "__main__":
    main()
