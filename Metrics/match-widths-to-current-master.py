# MenuTitle: Match Width(s) to Current Master
# -*- coding: utf-8 -*-

__doc__="""
Applies width(s) of the selected glyphs of the current master to the other masters.
"""

Glyphs.clearLog() # clears macro window log

# --------------------
# Variables
# --------------------

currentFont = Glyphs.font # frontmost font
currentFontMaster = currentFont.selectedFontMaster # active master
currentFontMasterName = currentFontMaster.name
selectedLayers = currentFont.selectedLayers
listOfSelectedLayers = [ l for l in selectedLayers if hasattr(l.parent, 'name')]
 # active layers of selected glyphs

currentFont.disableUpdateInterface() # suppresses UI updates in Font View

print "Current Master: %s" % currentFontMaster.name

for thisGlyph in listOfSelectedLayers:
	thisGlyph = thisGlyph.parent

	# first determine the width of the glyph in the current master
	for layer in thisGlyph.layers:
		if layer.name == currentFontMasterName:
			sourceWidth = layer.width
	# then loop through the layers and apply that width to them
	# this will automatically adjust the right side bearing as needed
	for layer in thisGlyph.layers:
		layer.width = sourceWidth

currentFont.enableUpdateInterface() # re-enables UI updates in Font View
