-- The book's button on the minimap (the kit's: Kit.lua): click to open the
-- book, right-click for its settings, drag to move it around the minimap.
-- Its place (and whether it shows) is kept with this character's settings
-- (Settings.lua).
local _, ns = ...
local K = ns.kit
local L = K.L

local M

function ns.createMinimapButton()
  if M then return end
  M = K.minimapButton({
    name = "YonderMinimapButton",
    icon = "Interface\\AddOns\\Yonder\\Media\\Logo",
    crop = true,
    title = "Yonder",
    lines = function()
      local creatures, families, slain = ns.counts()
      return {
        L["%d creatures in %d families, %d slain"]:format(creatures, families, slain),
        L["%d achievements"]:format((ns.milestoneCount())),
      }
    end,
    click = function() ns.toggle() end,
    rightClick = function() ns.openSettings() end,
    get = ns.option,
    set = ns.setOption,
  })
end

function ns.updateMinimapButton()
  if M then M:update() end
end
