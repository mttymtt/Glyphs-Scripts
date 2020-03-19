# MenuTitle: Color Nonexportable Glyphs Red
# -*- coding: utf-8 -*-

__doc__="""
Colors all nonexportable glyphs red.
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
	if g.export != True:
		print g.name
		g.color = 0
