# MenuTitle: Compare Master Widths
# -*- coding: utf-8 -*-

__doc__="""
Compare widths across font masters of the open font. Outputs a report in Macro Window, and opens Glyphs with mismatched widths in a new tab.
"""

# brings macro window to front and clears its log:
Glyphs.clearLog()
Glyphs.showMacroWindow()

# --------------------
# Variables
# --------------------

f = Glyphs.font # open font
exportableGlyphs = [g for g in f.glyphs if f.export]

# --------------------
# Table
# --------------------

# make a list of the master names
# then determine which is the longest
masterNames = []
for i, master in enumerate(f.masters):
    masterNames.append(master.name)
masterNameLen = len(max(masterNames, key=len)) # this is the longest master name

# make a list of glyph widths
# then determine which is the longest unit
glyphWidths = []
for g in exportableGlyphs:
    for i, master in enumerate(f.masters):
        master = f.masters[i]
        masterGlyph = g.layers[master.id]
        masterGlyphWidth = str(masterGlyph.width)
        glyphWidths.append(masterGlyphWidth)
widthLen = len(max(glyphWidths, key=len)) # this is the max character length of the width values

# make a list of glyph names
# then determine which is the longest name
glyphNames = []
for g in exportableGlyphs:
    glyphName = g.name
    glyphNames.append(glyphName)
glyphNameLen = len(max(glyphNames, key=len)) # this is the longest glyph name

# labels for table
col1Name = f.familyName # current font name
col1NameLen = len(col1Name)

col2Name = "Width"
col2NameLen = len(col2Name)

# make a list of the longest font name, glyph name, and col1 label
# then determine which is the longest
lenList = [masterNameLen, glyphNameLen, col1NameLen]
col1Width = max(lenList)

# make a list of the longest width len, and col2 label
# then determine which is the longest
lenList = [widthLen, col2NameLen]
col2Width = max(lenList)

# create labels and dividers for the table based on the lengths determined above
col1 = col1Name.ljust(col1Width + 1)
col2 = col2Name.ljust(col1Width + 1)
col1Divider = "".ljust(col1Width + 1, "-")
col1Spacer = "".ljust(col1Width + 1)
col2Divider = "".ljust(col2Width, "-")


# --------------------
# Make a list of all of the glyphs with inconsistent widths
# --------------------

unevenGlyphs = []

for g in exportableGlyphs:
    glyphName = g.name
    glyphWidthList = []

    for i, master in enumerate(f.masters):
        masterGlyph = g.layers[master.id]
        masterGlyphWidth = masterGlyph.width

        glyphWidthList.append(masterGlyphWidth)
    checkWidths = all(x==glyphWidthList[0] for x in glyphWidthList)
    if checkWidths == False:
        unevenGlyphs.append(g)

# --------------------
# Make a table of glyphs with uneven widths across masters
# --------------------

print "%s | %s\n%s | %s\n%s | %s" % (col1Divider, col2Divider, col1, col2, col1Divider, col2Divider)

newTabGlyphs = []

for g in unevenGlyphs:
    glyphName = g.name
    glyphNameFormatted = glyphName.ljust(col1Width + 1)

    # reformat the list of uneven glyphs to reopen later in a new tab
    firstMaster = f.masters[0]
    firstMasterGlyph = g.layers[firstMaster.id]
    newTabGlyphs.append(firstMasterGlyph)

    # start building the table
    print "%s |\n%s |\n%s |" % (col1Spacer, glyphNameFormatted, col1Spacer)

    for i, master in enumerate(f.masters):
        master = f.masters[i]
        masterName = master.name
        masterGlyph = g.layers[master.id]
        masterGlyphWidth = masterGlyph.width

        masterNameFormatted = masterName.ljust(col1Width + 1)

        print "%s | %s" % (masterNameFormatted, masterGlyphWidth)
    print "%s |\n%s | %s" % (col1Spacer, col1Divider, col2Divider)

print unevenGlyphs
print "---"
print newTabGlyphs

# --------------------
# Open uneven glyphs in new tab
# --------------------

newTab = f.newTab()
newTab.layers = newTabGlyphs
