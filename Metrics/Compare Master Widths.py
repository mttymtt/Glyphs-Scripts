#MenuTitle: Compare Master Widths
# -*- coding: utf-8 -*-
# __doc__="""
# Compare widths across font masters.
# """

f = Glyphs.font # open font

# brings macro window to front and clears its log:
Glyphs.clearLog()
Glyphs.showMacroWindow()

# make a list of the master names
# then determine which is the longest
masterNames = []
for i, master in enumerate(f.masters):
    masterNames.append(master.name)
fontNameLen = len(max(masterNames, key=len)) # this is the longest master name

# make a list of glyph widths
# then determine which is the longest unit
glyphWidths = []
for g in [g for g in f.glyphs if f.export]:
    for i, master in enumerate(f.masters):
        master = f.masters[i]
        masterGlyph = g.layers[master.id]
        masterGlyphWidth = str(masterGlyph.width)
        glyphWidths.append(masterGlyphWidth)
widthLen = len(max(glyphWidths, key=len)) # this is the max character length of the width values

# make a list of glyph names
# then determine which is the longest name
glyphNames = []
for g in [g for g in f.glyphs if f.export]:
    glyphName = g.name
    glyphNames.append(glyphName)
glyphNameLen = len(max(glyphNames, key=len)) # this is the longest glyph name

lenList = [fontNameLen, widthLen, glyphNameLen]

# build & label table to display inconsistent glyph widths
leftColWidth = max(lenList)
title = "Master".ljust(leftColWidth + 1)
divider = "".ljust(leftColWidth + 1, "-")
spacer = "".ljust(widthLen, "-")
print "%s | wdth" % title
print "%s | %s" % (divider, spacer)

# make a list of all of the glyphs with inconsistent widths
unevenGlyphs = []

for g in [g for g in f.glyphs if f.export]:
    glyphName = g.name

    firstMaster = f.masters[0]
    firstMasterName = firstMaster.name
    firstMasterNameFormatted = firstMasterName.ljust(leftColWidth + 1)
    firstMasterGlyph = g.layers[firstMaster.id]
    firstMasterGlyphWidth = firstMasterGlyph.width

    for i, master in enumerate(f.masters):
        master = f.masters[i]
        masterName = master.name
        masterNameFormatted = masterName.ljust(leftColWidth + 1)
        masterGlyph = g.layers[master.id]
        masterGlyphWidth = masterGlyph.width

        if firstMasterGlyphWidth != masterGlyphWidth:
            unevenGlyphs.append(firstMasterGlyph)

            glyphNameFormatted = glyphName.ljust(leftColWidth + 1)

            print "%s |" % glyphNameFormatted

            print "%s | %s" % (firstMasterNameFormatted, firstMasterGlyphWidth)
            print "%s | %s" % (masterNameFormatted, masterGlyphWidth)

            # print "%s : %s\n%s : %s" % (firstMaster.name, firstMasterGlyphWidth, masterName.name, masterGlyphWidth)
            print"%s | %s" % (divider, spacer)

# if firstMasterGlyphWidth != masterGlyphWidth:
#     newTab = f.newTab()
#     newTab.layers = unevenGlyphs
