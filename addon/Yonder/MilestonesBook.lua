-- The Milestones' tab in the book, over both panels: the kit's board (the
-- figures on top: all earned, and those of the creatures, the land and the
-- expeditions; then one row per milestone under its group's heading and how
-- many of it are earned: its group's picture, a medal on it once earned, the
-- title, what it asks, when it was earned or how far along it is).
-- Milestones: Achievements.lua.
local _, ns = ...
local L = ns.kit.L

-- (each group: its id, its heading, its picture, the figure it counts in)
local GROUPS = {
  { "tally", L["Tallies"], "Interface\\Icons\\INV_Misc_Book_09", "creatures" },
  { "type", L["Every Family"], "Interface\\Icons\\Ability_Hunter_BeastTaming", "creatures" },
  { "feat", L["Feats"], "Interface\\Icons\\INV_Misc_Head_Dragon_01", "creatures" },
  { "zone", L["Rares by Zone"], "Interface\\Icons\\INV_Misc_Map_01", "creatures" },
  { "fishing", L["Fishing"], "Interface\\Icons\\Trade_Fishing", "land" },
  { "herbs", L["Herbs"], "Interface\\Icons\\INV_Misc_Herb_07", "land" },
  { "mining", L["Ores & Gems"], "Interface\\Icons\\INV_Ore_Copper_01", "land" },
  { "cloth", L["Cloth"], "Interface\\Icons\\INV_Fabric_Linen_01", "land" },
  { "leather", L["Leather & Hides"], "Interface\\Icons\\INV_Misc_LeatherScrap_03", "land" },
  { "travel", L["Travels"], "Interface\\Icons\\Ability_Mount_RidingHorse", "land" },
  { "explore", L["Exploration"], "Interface\\Icons\\INV_Misc_Map02", "land" },
  { "expeditions", L["Expeditions"], "Interface\\Icons\\INV_Misc_Note_02", "expeditions" },
}
local FIGURES = {
  { "all", L["earned"] },
  { "creatures", L["of the creatures"] },
  { "land", L["of the land"] },
  { "expeditions", L["of the expeditions"] },
}
ns.milestoneRows = {} -- for the tests

-- (the kit's tab, K.deedsTab: its board over both panels and the count; none
-- of a type or zone not met yet, no spoilers)
local tab = ns.kit.deedsTab(ns.deeds, {
  name = "YonderMilestones",
  groups = GROUPS,
  figures = FIGURES,
  rows = ns.milestoneRows,
  n = ns.TAB.milestones,
})
ns.addTab(ns.TAB.milestones, tab.tab)

-- Open the book at the milestones, one of them picked out.
function ns.openMilestones(id)
  tab:pick(id)
  ns.openTab(ns.TAB.milestones)
end
