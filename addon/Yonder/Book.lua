-- The journal as a book: the standard game window (portrait, title bar), its
-- tabs (the Expeditions, the Bestiary, Finds, the Atlas, the
-- Milestones: each a file of its own, *Book.lua, registered with ns.addTab),
-- the links in chat that open it, and what every tab is made of (ns.ui): the
-- kit's look in the journal's theme, its list on the left and page on the
-- right. Light text and gold titles on dark panels:
-- Forever's Professions cards; on Classic, the game's insets, the quest log's
-- dark book behind the list. /yonder opens it.
local _, ns = ...
local L = ns.kit.L

-- ── look ─────────────────────────────────────────────────────────────────────
-- The kit's (Kit.lua), in the Yonder's theme: a sage accent, the panels
-- a faint moss, like a naturalist's notes.
local K = ns.kit
K.theme({
  accent = { 0.70, 0.80, 0.55 },
  ring = { 0.52, 0.62, 0.36 },
  bar = { 0.55, 0.72, 0.30 },
  tint = { 0.90, 1.00, 0.88 },
  shade = { 0.02, 0.03, 0.02, 0.55 },
  highlight = { 0.80, 1.00, 0.75 },
})
local T = K.T
T.mark, T.rare, T.link = "|cffff9a40", "|cffc7ccd6", K.hex(T.accent)
local BODY_FONT, TITLE_FONT = K.BODY_FONT, K.TITLE_FONT
local SOFT = K.hex(T.soft)
local label, rule, panel, scrollArea = K.label, K.rule, K.panel, K.scrollArea
-- A round portrait in the theme's ring, a dark disc behind it (p.tex: what it shows).
local function roundPortrait(parent, size) return K.roundIcon(parent, size, true) end

local function day(stamp) return K.day(stamp and stamp.at) end

-- The search box's words, as the kit compares them ("": no search).
local function query(book) return K.query(book.search) end

-- The list on the left and the page on the right: the kit's (Kit.lua), as
-- every book of the family.
local WIDTH, HEADER_H = K.PAGE_WIDTH, K.PAGE_HEADER_H
local function newPage(parent, name, labelWidth, pairs)
  return K.page(parent, name, { labelWidth = labelWidth, pairs = pairs })
end

-- ── the window ───────────────────────────────────────────────────────────────
-- The kit's book (K.book): the window, its two panels, the search and under
-- it a tab's own select (a sort, a continent), the tabs; each tab a file of
-- its own, registered with ns.addTab: { build(book), show(selected tab),
-- refresh(), chosen() (its tab clicked), whole (over both panels), filter =
-- { default, options() } (its choice, ns.filterOf(n)) }.
-- (the Expeditions first: what the book is opened for; the Bestiary fills itself)
local TAB = { expeditions = 1, bestiary = 2, finds = 3, atlas = 4, milestones = 5 }
ns.TAB = TAB
local B = K.book({
  name = "YonderFrame",
  title = "Yonder",
  art = "Interface\\AddOns\\Yonder\\Media\\Logo",
  titles = { L["Expeditions"], L["Bestiary"], L["Finds"], L["Atlas"], L["Achievements"] },
  first = TAB.expeditions,
  search = "YonderSearch",
  filter = true,
  settle = 0.5,
})
ns.kitBook = B -- (for the tests)
function ns.addTab(n, tab) B:add(n, tab) end
function ns.filterOf(n) return B:filterOf(n) end
function ns.setFilter(n, value) B:setFilter(n, value) end
function ns.refresh() B:refresh() end
function ns.showTab(n) B:show(n) end
function ns.toggle() B:toggle() end
-- The book open at a tab (the page it shows chosen by the caller).
function ns.openTab(n) B:open(n) end

-- ── links in chat ────────────────────────────────────────────────────────────
-- |Hyonder:<what>|h: c<creature id>, m<milestone id>, z<uiMap>,
-- f<fish>, h<herb>, x<riddle id>, q<quarry's creature id>, else a family (its id, "murlocs", first: an id may begin
-- with one of those letters; an older link's index; or "?type/family").
local function followLink(key)
  if ns.familyById[key] then return ns.openFamily(key) end
  local category = key:match("^finds/(%a+)$")
  if category then return ns.openFindCategory(category) end
  local kind, rest = key:sub(1, 1), key:sub(2)
  local id = tonumber(rest)
  if kind == "m" then
    ns.openMilestones(rest)
  elseif kind == "z" and id then
    ns.openZone(id)
  elseif kind == "x" and ns.riddleById[rest] then
    ns.openRiddle(rest)
  elseif kind == "q" and id then
    ns.openQuarry(id)
  elseif kind == "f" and id then
    ns.openFish(id)
  elseif kind == "h" and id then
    ns.openPlant(id)
  elseif kind == "i" and id then
    ns.openFind(id)
  elseif kind == "c" and id then
    ns.openCreature(id)
  else
    ns.openFamily(tonumber(key) or key)
  end
end
-- (the kit's: the client's link registry, else SetItemRef)
K.links("yonder", followLink)

-- What's recorded while the book is open shows up at once (throttled: meeting
-- creatures happens constantly).
ns.onRecord = function() B:changed() end
ns.onMilestone = ns.onRecord
ns.onAtlas = ns.onRecord
ns.onFlora = ns.onRecord

-- The kit, for the tabs.
ns.ui = {
  T = T,
  TITLE_FONT = TITLE_FONT,
  BODY_FONT = BODY_FONT,
  WIDTH = WIDTH,
  HEADER_H = HEADER_H,
  SOFT = SOFT,
  QUESTION = K.QUESTION,
  label = label,
  rule = rule,
  panel = panel,
  scrollArea = scrollArea,
  roundPortrait = roundPortrait,
  icon = K.icon,
  progressBar = K.bar,
  fold = K.fold,
  day = day,
  query = query,
  itemName = K.itemName,
  itemIcon = K.itemIcon,
  newList = K.list,
  newPage = newPage,
  window = function() return B:window() end,
}
