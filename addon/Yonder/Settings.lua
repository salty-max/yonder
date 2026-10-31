-- The addon's settings, each character's own (its profile, "Name - Realm",
-- the kit's: Kit.lua), all kept in YonderSettings so that one character
-- can take another's: chosen among this game's characters, or brought by a
-- code (/yonder export, /yonder import CODE). Their page in the game's
-- Options (AddOns tab): /yonder settings, or a right-click on the minimap
-- button; the welcome page (Welcome.lua) offers them too.
--
--   YonderSettings.profiles["Name - Realm"] = { banner, bannerSeconds, sound,
--     achievementSound, minimapHidden, minimapAngle, tooltipHints, milestoneToast, worldMapPins,
--     welcomed }
--   (banner: a riddle's and a quarry's; milestoneToast: a milestone's, the
--   game's achievement alert. The chat lines have no setting any more,
--   always shown: a profile's old chat value is left unread)
--   (the account-wide values of 0.6.0 and before, at the top of the table:
--   the first profile of a character who kept a journal before takes them)
local _, ns = ...
local L = ns.kit.L
local K = ns.kit

-- (minimapAngle: the button's place around the minimap, in degrees; 225 is
-- lower left, clear of the game's buttons; welcomed: never copied)
local DEFAULTS = {
  banner = true,
  bannerSeconds = K.BANNER_SECONDS,
  sound = 3175,
  minimapHidden = false,
  minimapAngle = K.MINIMAP_ANGLES.Yonder,
  tooltipHints = true,
  milestoneToast = true,
  achievementSound = K.ACHIEVEMENT_SOUND,
  worldMapPins = true,
  welcomed = false,
}
local SHARED = {
  "banner",
  "bannerSeconds",
  "sound",
  "milestoneToast",
  "achievementSound",
  "worldMapPins",
  "tooltipHints",
  "minimapHidden",
  "minimapAngle",
}

-- Sounds for a trophy: the kit's (all from the original game's interface; -1
-- the sting heard on discovering a new zone, which differs by race), named
-- in the reader's language.
ns.SOUNDS = {}
for i, s in ipairs(K.SOUNDS) do
  ns.SOUNDS[i] = { s[1], L[s[2]] }
end

-- The profiles: a code "YD1:b1:n10:s3175:m1:f12891:w1:t1:h0:a225" (the banners, how
-- long they stay, the trophy's sound, milestone alerts, their sound, the world map's marks, tooltip hints, the minimap
-- button hidden, its angle; an older code's c, the chat lines, is left out).
local P = K.profiles({
  saved = function()
    if type(YonderSettings) ~= "table" then YonderSettings = {} end
    return YonderSettings
  end,
  defaults = DEFAULTS,
  shared = SHARED,
  letters = {
    banner = "b",
    bannerSeconds = "n",
    sound = "s",
    milestoneToast = "m",
    achievementSound = "f",
    worldMapPins = "w",
    tooltipHints = "t",
    minimapHidden = "h",
    minimapAngle = "a",
  },
  tag = "YD1",
  changed = function(key)
    if key == "minimapHidden" or key == "minimapAngle" then ns.updateMinimapButton() end
    if key == "worldMapPins" and ns.refreshWorldMapPins then ns.refreshWorldMapPins() end
  end,
})
-- (a code made before the rename, Explorer's Field Journal's FJ1, still taken)
local import = P.import
function P:import(code)
  if type(code) == "string" then code = code:gsub("^%s*FJ1:", "YD1:") end
  return import(self, code)
end
ns.profiles = P

-- This character's profile at its login: its own, else a new one (the
-- account's old values for a character who kept a journal before, the
-- defaults for a new one).
function ns.loadProfile(before)
  P:load(function(profile, saved)
    if not before then return end
    for _, k in ipairs(SHARED) do
      profile[k] = saved[k]
    end
  end)
end
function ns.option(key) return P:get(key) end
function ns.setOption(key, value) P:set(key, value) end

-- A sound of the list, the reader's choice by default (the kit's: -1 the
-- race's own discovery sting).
function ns.playSound(id) K.playSound(id or ns.option("sound")) end

-- The opt-in that shares what the game tells of the world with the addons'
-- database (the kit's, K.collect): account-wide, in YonderCollect, which
-- Ravenpost sends; off until the player says yes.
ns.collect = K.collect({
  saved = function()
    if type(YonderCollect) ~= "table" then YonderCollect = {} end
    return YonderCollect
  end,
  prefix = ns.PREFIX,
})

-- The page in the game's Options (the kit's: K.options).
local O

function ns.createSettingsPanel()
  if O then return end
  O = K.options({
    title = "Yonder",
    key = "YONDER",
    get = ns.option,
    set = ns.setOption,
    defaults = DEFAULTS,
    profiles = P,
    slash = "/yonder",
    prefix = ns.PREFIX,
  })
  O:check(
    "banner",
    L["Banners for riddles, quarries and collections"],
    L["A banner among the game's alerts when you solve a riddle, bring down a quarry or unlock a collection (the sounds and chat lines stay)."]
  )
  O:bannerSeconds("bannerSeconds")
  O:choice("sound", L["Sound for a trophy"], L["Played when you slay a rare or a boss for the first time."], function()
    local out = {}
    for _, s in ipairs(ns.SOUNDS) do
      table.insert(out, { s[1], s[2] })
    end
    return out
  end, function(value) ns.playSound(value) end)
  O:check(
    "milestoneToast",
    L["Alert for achievements"],
    L["The game's achievement alert when you earn an achievement (the achievement sound and the chat line stay)."]
  )
  O:achievementSound("achievementSound")
  O:check(
    "worldMapPins",
    L["Deaths on the world map"],
    L["Mark on the game's world map where you died and came close, from the Atlas."]
  )
  O:check(
    "tooltipHints",
    L["Hints on tooltips"],
    L["A line on creature tooltips: not yet in the journal, or how many you have slain."]
  )
  O:check(
    "minimapHidden",
    L["Minimap button"],
    L["The book by the minimap: click to open the journal, drag to move it."],
    true
  )
  O:collect(ns.collect)
  O:copy()
  O:done()
end

function ns.openSettings() return O ~= nil and O:open() end
