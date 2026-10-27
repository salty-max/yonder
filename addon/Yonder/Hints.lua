-- A line on creature tooltips: "not yet in the journal" for a creature this
-- character hasn't met, else how many it has slain (and a trophy's mark).
-- Off in the settings (tooltipHints).
local _, ns = ...
local L = ns.kit.L
local D = ns.data

local function addHint(tooltip)
  if tooltip ~= GameTooltip or not ns.option("tooltipHints") then return end
  local _, unit = tooltip:GetUnit()
  if not unit or ns.secret(unit) then return end
  local isPlayer = UnitIsPlayer(unit)
  if ns.secret(isPlayer) or isPlayer then return end
  local id = ns.creatureId(UnitGUID(unit))
  if not id then return end
  local journal = ns.journal()
  local rec = journal and journal.creatures[id]
  if not rec then
    -- Only creatures the journal would keep: those the data knows or can file,
    -- while they can be fought (as recording itself).
    local canAttack = UnitCanAttack("player", unit)
    local ctype = not D.creatures[id] and UnitCreatureType(unit)
    local fileable = D.creatures[id] or (ctype and not ns.secret(ctype) and ns.knownType(ctype))
    if fileable and (ns.secret(canAttack) or canAttack) then
      ns.kit.tooltipLine(tooltip, L["Yonder: not yet recorded"], true)
    end
    return
  end
  local slain = rec.slain or 0
  local mark = rec.trophy and L[" (trophy)"] or ""
  ns.kit.tooltipLine(
    tooltip,
    L["Yonder: %s%s"]:format(slain > 0 and L["%d slain"]:format(slain) or L["met"], mark),
    false
  )
end

ns.kit.onUnitTooltip(addHint)
