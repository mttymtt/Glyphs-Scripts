# MenuTitle: Remove Metric Keys of Selected Glyphs
# -*- coding: utf-8 -*-

__doc__="""
Removes left and right metrics keys of selected glyphs in selected master. For example, "H" becomes "35".
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
	leftKey = thisGlyph.leftMetricsKey
	rightKey = thisGlyph.rightMetricsKey

	for layer in thisGlyph.layers:
		if layer.name != currentFontMasterName:
			if leftKey is not None:
			    if "=" not in leftKey:
			        leftKey = "==" + leftKey
			        layer.setLeftMetricsKey_(leftKey)
			    if leftKey.startswith("="):
			        leftKey = "=" + leftKey.replace("=", "")
			        layer.setLeftMetricsKey_(leftKey)
			if rightKey is not None:
			    if "=" not in rightKey:
			        rightKey = "==" + rightKey
			        layer.setRightMetricsKey_(rightKey)
			    if rightKey.startswith("="):
			        rightKey = "==" + rightKey.replace("=", "")
			        layer.setRightMetricsKey_(rightKey)
		if layer.name == currentFontMasterName:
			thisGlyph.setLeftMetricsKey_(None)
			thisGlyph.setRightMetricsKey_(None)

currentFont.enableUpdateInterface() # re-enables UI updates in Font View
