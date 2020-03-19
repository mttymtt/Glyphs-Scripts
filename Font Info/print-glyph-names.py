# MenuTitle: Print Exportable Glyph Names
# -*- coding: utf-8 -*-

__doc__="""
Prints a list of all exportable glyphs in the Macro Panel.
"""

# brings macro window to front and clears its log:
Glyphs.clearLog()
Glyphs.showMacroWindow()

# --------------------
# Variables
# --------------------

currentFont = Glyphs.font # open font
exportableGlyphs = [g for g in currentFont.glyphs if g.export]

# --------------------
# Action
# --------------------

for g in exportableGlyphs:
    print(g.name)
