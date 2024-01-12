Color Match 1.0.2
Find a color’s closest match in a color list (i.e. Pantone or RAL).
Color Match will find the closest match for a color you choose in any
given list with a limited number of colors.
Instructions:
- Click on the left frame (with the label “Click to pick a color”)
- Pick a color or input value for Red, Green and Blue in the color
chooser window that will pop up.
- The matching color will appear in the right frame
- Red, Green, Blue and HEX code values for the matching color will be
displayed in the text box below the right color frame
- You can copy the HEX code and the RGB values by right-clicking on
the text, for use in another program
The program works reading from a color list file in CSV format. A list of
CMYK Process Uncoated colors is included in the file colors.txt (useful
 For artworks to be printed with InkJet or color Laser printers on
Regular office paper).
You can edit this list to add or remove your custom colors or create a
 new list through the following procedure:
- Create a text file with a text editor
- Input each color in the format R,G,B [Enter], i.e.:

	120,40,23
	45,72,200
	37,94,158
	and so on

The program also understands GIMP palettes exported in text format. This
palette format can be edited or created manually through a simple text
editor and it contains a list of colors in HEX format, each on a separate
row, as in the following example:

- #24024e
- #30014a
- #130957

- Save the file with the name “colors.txt” and put it in the same
folder as the program. The palette format will be recognized
automatically.
Do not delete the file colors.txt or the program will crash.
