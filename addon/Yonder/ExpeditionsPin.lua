-- A riddle or a quarry pinned to the screen: the kit's banner card (K.bannerCard,
-- the banners' own: its picture, where over its name, the cross), taller, that
-- stays while the reader goes looking. Under its head it shows the verse
-- (and the clue or the map, once asked for), and once solved or brought down
-- its seal; dragged anywhere (kept where it was left, per character), closed
-- by its cross; a click opens the book there. One at a time: pinning another
-- replaces it. The book's pages pin and unpin (ns.pin); the record keeps it
-- (Expeditions.lua: pinned, pinAt).
local _, ns = ...
local L = ns.kit.L
local ui = ns.ui
local T = ui.T
local WIDTH, PAD = 380, 14 -- (a banner's width: a name the room its banner gives it)
local TIERS = { near = L["Near the road"], off = L["Off the road"], hidden = L["Hidden"], town = L["In town"] }
local card

function ns.pinned()
  local e = ns.journal() and ns.expeditions()
  return e and e.pinned
end

-- What a key names: the riddle, or the quarry ("quarry:<id>"), if this
-- character may have it.
local function subject(key)
  if type(key) ~= "string" then return end
  local qid = tonumber(key:match("^quarry:(%d+)$"))
  if qid then
    local q = ns.quarryById[qid]
    return nil, q and ns.quarryOpen(q) and q or nil
  end
  local r = ns.riddleById[key]
  return r and ns.riddleOpen(r) and r or nil
end

local function save()
  local e = ns.expeditions()
  local point, _, relative, x, y = card:GetPoint(1)
  if e and point then e.pinAt = { point, relative, x, y } end
end

local function place()
  local e = ns.expeditions()
  local at = e and e.pinAt
  card:ClearAllPoints()
  if at then
    card:SetPoint(at[1], UIParent, at[2], at[3], at[4])
  else
    card:SetPoint("TOPRIGHT", UIParent, "TOPRIGHT", -240, -220)
  end
end

local function build()
  card = ns.kit.bannerCard("YonderPinnedCard", WIDTH)
  card:SetFrameStrata("MEDIUM")
  card:SetMovable(true)
  card:EnableMouse(true)
  card:RegisterForDrag("LeftButton")
  -- (the head the banner's, where over its name; the verse and what is known under it)
  card.verse = ui.label(card.body, ui.BODY_FONT, 12, T.text)
  card.verse:SetPoint("TOPLEFT", PAD, -ns.kit.BANNER_H)
  card.verse:SetWidth(WIDTH - 2 * PAD)
  card.verse:SetSpacing(3)
  card.extra = ui.label(card.body, ui.BODY_FONT, 11, T.soft)
  card.extra:SetPoint("TOPLEFT", card.verse, "BOTTOMLEFT", 0, -8)
  card.extra:SetWidth(WIDTH - 2 * PAD)
  card.extra:SetSpacing(2)
  card.close:SetScript("OnClick", function() ns.pin(nil) end)
  -- (the hover's glow, a row's, on the head alone: stretched over the verse
  -- it would smear)
  local hover = card:GetHighlightTexture()
  if hover then
    hover:ClearAllPoints()
    hover:SetPoint("TOPLEFT")
    hover:SetPoint("TOPRIGHT")
    hover:SetHeight(ns.kit.BANNER_H)
  end

  card:SetScript("OnDragStart", function(self) self:StartMoving() end)
  card:SetScript("OnDragStop", function(self)
    self:StopMovingOrSizing()
    if self.SetUserPlaced then self:SetUserPlaced(false) end
    save()
  end)
  card:SetScript("OnClick", function(self)
    if self.riddle then
      ns.openRiddle(self.riddle)
    elseif self.quarry then
      ns.openQuarry(self.quarry)
    end
  end)
  card:SetScript("OnEnter", function(self)
    GameTooltip:SetOwner(self, "ANCHOR_BOTTOM")
    GameTooltip:AddLine("Yonder", T.accent[1], T.accent[2], T.accent[3])
    GameTooltip:AddLine(
      L["Click to open it in the journal, or drag to move it."],
      T.text[1],
      T.text[2],
      T.text[3],
      true
    )
    GameTooltip:Show()
  end)
  card:SetScript("OnLeave", function() GameTooltip:Hide() end)
  card:Hide()
  place()
end

local function seal(name, color)
  return ("|cff%02x%02x%02x%s|r"):format(color[1] * 255, color[2] * 255, color[3] * 255, name)
end
local SEAL_COLORS = { gold = { 1, 0.82, 0 }, silver = { 0.78, 0.8, 0.84 }, plain = { 0.8, 0.55, 0.35 } }

-- (its seal its ring, as on the riddle's page: ExpeditionsBook's ns.sealRing)
local function ring(spec) ns.kit.ringColour(card.picture, spec and spec[1], spec and spec[2]) end

local function fill(r, q)
  card.riddle, card.quarry = r and r.id, q and q.id
  card.picture.tex:SetVertexColor(1, 1, 1)
  card.picture.tex:SetDesaturated(false)
  local extra = {}
  if r then
    local rec = ns.riddleRecord(r.id) or {}
    ns.riddlePicture(r)(card.picture)
    ring(ns.sealRing(rec.at and ns.SEALS[ns.riddleSeal(rec)], rec.at ~= nil))
    if rec.at then
      local s = ns.riddleSeal(rec)
      card.title:SetText(ns.riddleName(r))
      table.insert(extra, L["Read, with %s."]:format(seal(ns.SEALS[s][6], SEAL_COLORS[s])))
    else
      card.title:SetText(TIERS[r.tier])
      if (rec.hints or 0) >= 1 then table.insert(extra, L["The clue: %s"]:format(r.hint)) end
      if (rec.hints or 0) >= 2 then table.insert(extra, L["Its place is shaded on your world map."]) end
    end
    card.kicker:SetText(ns.zoneName(r.zone) .. (r.night and L["  -  by night"] or ""))
    card.verse:SetText(table.concat(r.verse, "\n"))
  else
    local rec = ns.huntRecord(q.id) or {}
    ns.quarryPicture(q)(card.picture)
    ring(ns.sealRing(rec.at and ns.HUNT_SEALS[ns.huntSeal(rec)], rec.at ~= nil))
    card.title:SetText(q.name)
    card.kicker:SetText(ns.zoneName(q.zone) .. L["  -  the quarry"])
    card.verse:SetText(table.concat(q.verse, "\n"))
    if rec.at then
      local s = ns.huntSeal(rec)
      table.insert(
        extra,
        s == "before" and L["Brought down before the journal kept the hunts."]
          or L["Brought down, with %s."]:format(seal(ns.HUNT_SEALS[s][6], SEAL_COLORS[s]))
      )
    else
      local target = ns.huntTarget()
      if target and target.id == q.id then table.insert(extra, L["Its haunts are shaded on your world map."]) end
    end
  end
  card.extra:SetText(table.concat(extra, "\n"))
  local h = ns.kit.BANNER_H + card.verse:GetStringHeight() + PAD
  if #extra > 0 then h = h + 8 + card.extra:GetStringHeight() end
  card:SetHeight(h)
end

-- The card as the record has it: shown with what is pinned, else hidden.
function ns.refreshPin()
  local r, q = subject(ns.pinned())
  if not (r or q) then
    if card then card:Hide() end
    return
  end
  if not card then build() end
  fill(r, q)
  card:Show()
end

-- Pinned (a riddle's id, "quarry:<id>"), or nothing (nil).
function ns.pin(key)
  local e = ns.expeditions()
  if not e then return end
  e.pinned = key
  ns.refreshPin()
  ns.onRecord()
end

-- What changes the record changes the card.
local onRecord = ns.onRecord
ns.onRecord = function(...)
  if onRecord then onRecord(...) end
  ns.refreshPin()
end
