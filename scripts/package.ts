/**
 * The addon's package: the family's (scripts/package-lib.ts, the kit's copy):
 * addon/Yonder as it is, one zip for every game, each game loading its own
 * TOC; its TOCs checked.
 *
 *   bun scripts/package.ts           dist/Yonder, dist/FieldJournal and dist/Yonder-<version>.zip
 *   bun scripts/package.ts --no-zip  the folder only (to copy into a game)
 *   bun scripts/package.ts --check   the TOCs only
 */
import { existsSync, readFileSync, readdirSync } from "node:fs";
import { join } from "node:path";
import { GAMES, run, versionOf, type Also } from "./package-lib";

// The handover (addon/FieldJournal): the addon's old name, Explorer's Field
// Journal, so that the game loads its saved files once more for Yonder to
// take (Core.lua, adopt). Classic Era only: on Forever another addon,
// Field Journal: Forever, owns a FieldJournal folder (its FieldJournal.toc).
// Its one TOC and its one file, nothing else, the old saved variables,
// Yonder's version.
const HANDOVER = "FieldJournal";
const HANDOVER_TOCS = [
  { toc: `${HANDOVER}_Vanilla.toc`, interface: GAMES.classic.interface },
];
const HANDOVER_FILES = [...HANDOVER_TOCS.map((t) => t.toc), "YonderHandover.lua"];
const also: Also = {
  folder: HANDOVER,
  files: HANDOVER_FILES,
  check: ({ src, version, fail }) => {
    const handover = existsSync(src) ? readdirSync(src).sort() : [];
    if (handover.join() !== [...HANDOVER_FILES].sort().join())
      fail(`addon/${HANDOVER}: ${handover.join(", ")}, not ${HANDOVER_FILES.join(", ")}`);
    for (const h of HANDOVER_TOCS) {
      const toc = readFileSync(join(src, h.toc), "utf8");
      if (!toc.startsWith(`## Interface: ${h.interface}\n`)) fail(`${HANDOVER}/${h.toc}: not "## Interface: ${h.interface}" first`);
      if (versionOf(toc) !== version) fail(`${HANDOVER}/${h.toc}: version ${versionOf(toc)}, Yonder's is ${version}`);
      for (const need of ["## SavedVariablesPerCharacter: FieldJournalChar", "## SavedVariables: FieldJournalSettings"])
        if (!toc.includes(`${need}\n`)) fail(`${HANDOVER}/${h.toc}: no "${need}"`);
      const files = toc.split("\n").filter((l) => l.trim() && !l.startsWith("#"));
      if (files.join() !== "YonderHandover.lua") fail(`${HANDOVER}/${h.toc} loads ${files.join(", ")}, not YonderHandover.lua alone`);
    }
  },
};

// (each game's own files: the game's data: each game's own)
run({ root: join(import.meta.dir, ".."), name: "Yonder", games: { classic: ["Data_Classic.lua"], forever: ["Data_Forever.lua"] }, also });
