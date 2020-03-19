# MenuTitle: Remove All Glyph Colors
# -*- coding: utf-8 -*-

__doc__="""
Removes all glyph colors.
"""

# brings macro window to front and clears its log:
Glyphs.clearLog()
Glyphs.showMacroWindow()

# --------------------
# Variables
# --------------------

currentFont = Glyphs.font # open font

# --------------------
# Action
# --------------------

glyphOrder = []

for g in currentFont.glyphs:
	g.colorObject = None
