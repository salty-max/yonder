"""The riddle gates of scripts/expeditions.py against the 20 October 2026
review's findings: the quests tied to a riddle's place, and the keepers who
attack one side by its spot.

The first tests need no database (CI has none): the rows are wow-data's, as
the resolver read them on 20 October 2026. The last one runs the resolver on
the four zones with the review's fixes undone, where wow-data's database is.
"""
import os
import pathlib
import re
import subprocess
import sys
import tempfile
import unittest

HERE = pathlib.Path(__file__).parent
sys.path.insert(0, str(HERE))
import expeditions as e  # noqa: E402


def index(asks, drops=None, gives=None):
    """quest_index()'s shape from a few rows."""
    drops = drops or {}
    sources = {}
    for owner, items in drops.items():
        for item in items:
            sources.setdefault(item, set()).add(owner)
    return {"asks": asks, "drops": drops, "sources": sources, "gives": gives or {}, "names": {}}


class QuestTies(unittest.TestCase):
    def test_pool_of_tears_artifacts_and_tablets(self):
        # 1424 asks for Atal'ai Artifacts (6175) from objects 30854-30856, 1475 for
        # Atal'ai Tablets (6288) from object 37099: on the zone's map, 63 of each
        # artifact object's 68 spawns and all 15 tablets' are in the circle
        # (the temple's 40 tablets inside the instance are on no zone's map).
        artifacts = [("object", i) for i in (30854, 30855, 30856)]
        idx = index({("item", 6175): {1424}, ("item", 6288): {1475}},
                    {**{o: {6175} for o in artifacts}, ("object", 37099): {6288}})
        inside = {**{o: 63 for o in artifacts}, ("object", 37099): 15}
        total = {**{o: 68 for o in artifacts}, ("object", 37099): 15}
        self.assertEqual(set(e.quest_ties([], inside, total, idx)), {1424, 1475})

    def test_lakkari_tar(self):
        # 4504 asks for Super Sticky Tar (11834), dropped on the quest by the four
        # tar elementals: 39 of their 58 spawns in Un'Goro are the pits'.
        tar = {("creature", 6517): (3, 14), ("creature", 6518): (16, 16),
               ("creature", 6519): (16, 16), ("creature", 6527): (4, 12)}
        idx = index({("item", 11834): {4504}}, {c: {11834} for c in tar})
        ties = e.quest_ties([], {c: n for c, (n, _) in tar.items()}, {c: n for c, (_, n) in tar.items()}, idx)
        self.assertEqual(set(ties), {4504})
        self.assertIn("39 of the zone's 58", ties[4504])

    def test_kel_theril_fragments_and_its_spirit(self):
        # 5245 asks for four relic fragments, each from one object in the ruins;
        # the Remorseful Highborne (10684), the area's anchor, gives and ends
        # 5248 and 5252. The yetis of all Winterspring are no errand of the
        # ruins: 3 of the zone's 31 Ice Thistle Yetis (7457) stand there.
        fragments = {("object", 175888): 12896, ("object", 175891): 12897, ("object", 175892): 12898, ("object", 175893): 12899}
        idx = index({**{("item", i): {5245} for i in fragments.values()}, ("item", 12366): {3783}},
                    {**{o: {i} for o, i in fragments.items()}, ("creature", 7457): {12366}},
                    {("creature", 10684): {5248, 5252}})
        inside = {**{o: 1 for o in fragments}, ("creature", 7457): 3}
        total = {**{o: 1 for o in fragments}, ("creature", 7457): 31}
        self.assertEqual(set(e.quest_ties([("creature", 10684)], inside, total, idx)), {5245, 5248, 5252})

    def test_the_subjects_own_drop(self):
        # The Emperor's Tomb (object 54) yields Kurzen's Mystery's item (2008).
        idx = index({("item", 2008): {207}}, {("object", 54): {2008}})
        self.assertEqual(set(e.quest_ties([("object", 54)], {}, {}, idx)), {207})

    def test_nothing_there_is_no_tie(self):
        idx = index({("creature", 1161): {224}})
        self.assertEqual(e.quest_ties([], {}, {("creature", 1161): 40}, idx), {})


class Keepers(unittest.TestCase):
    # Stormwind's faction template (12), High Priest Thel'danis's (1854), as
    # Classic Era's client has it.
    STORMWIND = {"ID": "12", "Faction": "72", "Flags": "0", "FactionGroup": "2", "FriendGroup": "2", "EnemyGroup": "4",
                 **{f"Enemies_{i}": "0" for i in range(8)}, "Friend_0": "72", **{f"Friend_{i}": "0" for i in range(1, 8)}}

    def test_stormwind_attacks_the_horde_alone(self):
        self.assertTrue(e.attacks(self.STORMWIND, "horde"))
        self.assertFalse(e.attacks(self.STORMWIND, "alliance"))

    def test_thel_danis_at_uthers_plaque(self):
        near = [(1854, "High Priest Thel'danis", {s for s in e.SIDES if e.attacks(self.STORMWIND, s)})]
        both, danger = ["alliance", "horde"], "Guarded (ghouls and skeletons, to level 52)"
        self.assertEqual(e.unanswered_keepers(both, danger, near), [(1854, "High Priest Thel'danis", "horde")])
        # answered: the Alliance's riddle alone (faction:), or a danger line naming him
        self.assertEqual(e.unanswered_keepers(["alliance"], danger, near), [])
        self.assertEqual(e.unanswered_keepers(both, danger + ", and for the Horde High Priest Thel'danis", near), [])

    def test_a_danger_line_names_a_kind(self):
        both = ["alliance", "horde"]
        refugees = [(2053, "Haggard Refugee", {"horde"}), (2054, "Sickly Refugee", {"horde"})]
        self.assertEqual(e.unanswered_keepers(both, "Guarded for the Horde (the refugees, levels 18 to 20)", refugees), [])
        # a word inside another is no name: "Guarded" names no guard
        self.assertEqual(len(e.unanswered_keepers(both, "Guarded", [(68, "Stormwind City Guard", {"horde"})])), 1)
        # a creature that attacks both sides is a danger, not a keeper
        self.assertEqual(e.unanswered_keepers(both, "Quiet", [(1, "Ghoul", {"alliance", "horde"})]), [])


WOWDATA = HERE.parent.parent / "wow-data" / ".cache" / "db" / "classic.db"


@unittest.skipUnless(WOWDATA.exists() or os.environ.get("WOW_DATA_CACHE"), "wow-data's databases are not here")
class TheReviewUndone(unittest.TestCase):
    """The four zones as they stood before the review's fixes: the resolver
    names every finding again."""

    UNDO = {
        "swamp-of-sorrows.md": [r"^    quest_overlap: \[.*\b1424, 1475\b.*\]\n", r"^    quest_context: .*Atal'Hakkar.*\n"],
        "ungoro-crater.md": [r"^    quest_overlap: \[.*\b4504\b.*\]\n", r"^    quest_context: .*Super Sticky.*\n"],
        "winterspring.md": [r"^    quest_overlap: \[.*\b5245\b.*\]\n", r"^    quest_context: .*Kel'Theril.*\n"],
        "western-plaguelands.md": [r"^    faction: alliance   # High Priest Thel'danis.*\n"],
    }

    def test_the_findings_come_back(self):
        with tempfile.TemporaryDirectory() as folder:
            for name, undo in self.UNDO.items():
                text = (HERE.parent / "expeditions" / name).read_text()
                for pattern in undo:
                    text, n = re.subn(pattern, "", text, count=1, flags=re.M)
                    self.assertEqual(n, 1, f"{name}: {pattern} no longer matches: update the test")
                (pathlib.Path(folder) / name).write_text(text)
            run = subprocess.run([sys.executable, str(HERE / "expeditions.py"), "--dry", folder], capture_output=True, text=True)
        self.assertEqual(run.returncode, 1, run.stdout + run.stderr)
        for riddle, finding in [("swamp-of-sorrows-pool-of-tears", "quest 1424 "), ("swamp-of-sorrows-pool-of-tears", "quest 1475 "),
                                ("ungoro-crater-lakkari", "quest 4504 "), ("winterspring-kel-theril", "quest 5245 "),
                                ("western-plaguelands-uther", "High Priest Thel'danis (1854)")]:
            self.assertRegex(run.stdout, rf"{riddle}: {re.escape(finding)}")


if __name__ == "__main__":
    unittest.main()
