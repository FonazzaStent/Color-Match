"""Color Match 1.0.1 - Find a color's closest match in a color list.
Copyright (C) 2023  Fonazza-Stent

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>."""

import tkinter as tk
from tkinter import *
from tkinter.filedialog import asksaveasfilename
from tkinter import colorchooser
import csv
from math import sqrt

csvfile=open("colors.csv",'r')
database=csv.reader(csvfile)
RGBlist=[]
for lines in database:
    RGBlist.append(lines)
csvfile.close()

#create main window
def create_main_window():
    global top
    global root
    img=b'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'
    root= tk.Tk()
    top= root
    top.geometry("620x300")
    top.title("Color Match")
    top.resizable(0,0)
    favicon=tk.PhotoImage(data=img) 
    root.wm_iconphoto(True, favicon)

#ColorDisplayFrame
def color_display_frame():
    global ColorDisplayFrame
    global ColorMatchFrame
    global ColorMatchLabel
    ColorDisplayFrame= Frame(top)
    ColorDisplayFrame.place(x=20, y=20, height=220, width=280)
    ColorDisplayFrame.configure(relief='groove')
    ColorDisplayFrame.configure(borderwidth="2")
    ColorDisplayFrame.configure(relief="groove")
    ColorDisplayFrame.bind("<Button-1>",pick_color_frame)
    
    ColorDisplayLabel=Label(top)
    ColorDisplayLabel.place(x=20,y=240,height=35,width=280)
    ColorDisplayLabel.configure(text="Click to pick a color")
    

    ColorMatchFrame= Frame(top)
    ColorMatchFrame.place(x=320, y=20, height=220, width=280)
    ColorMatchFrame.configure(relief='groove')
    ColorMatchFrame.configure(borderwidth="2")
    ColorMatchFrame.configure(relief="groove")
    
    ColorMatchLabel=Text(top)
    ColorMatchLabel.place(x=320,y=250,height=25,width=280)
    ColorMatchLabel.configure(state="disabled")

#choose color
def pick_color():
    global color
    global R
    global G
    global B
    global RGBcolor
    global pickcheck
    global oldcolor
    global colorsave
    #RGBcolor=0
    color = colorchooser.askcolor(title ="Choose color")
    if str(color[1])!="None":
        ColorDisplayFrame.configure(bg=color[1])
        R,G,B=color[0]
        closest=closest_color((R, G, B))
        #print (closest)
        Rm=int(closest[0])
        Gm=int(closest[1])
        Bm=int(closest[2])
        hexmatch=rgb_to_hex(Rm,Gm,Bm)
        ColorMatchFrame.configure(bg=hexmatch)
        colorlabel="R "+str(Rm)+" G "+str(Gm)+" B "+str(Bm)+" - Hex: "+hexmatch
        ColorMatchLabel.configure(state='normal')
        ColorMatchLabel.delete(1.0,END)
        ColorMatchLabel.insert(INSERT,colorlabel)
        ColorMatchLabel.configure(state="disabled")

def pick_color_frame(event):
    pick_color()

def closest_color(rgb):
    r, g, b = rgb
    color_diffs = []
    for color in RGBlist:
        cr, cg, cb = color
        cr=int(cr)
        cg=int(cg)
        cb=int(cb)
        color_diff = sqrt((r - cr)**2 + (g - cg)**2 + (b - cb)**2)
        color_diffs.append((color_diff, color))
    return min(color_diffs)[1]


def rgb_to_hex(r,g,b):
    #return '#%02x%02x%02x' % rgb
    return "#{:02x}{:02x}{:02x}".format(r,g,b)

#CopyContextMenu
def create_context_menu():
    global menu
    menu = tk.Menu(root, tearoff = 0)
    menu.add_command(label="Copy", command=copy_text)
    root.bind("<Button-3>", context_menu)

def context_menu(event): 
    try: 
        menu.tk_popup(event.x_root, event.y_root)
    finally: 
        menu.grab_release()
        
def copy_text():
        ColorMatchLabel.event_generate(("<<Copy>>"))

#main
def main():
    create_main_window()
    color_display_frame()
    create_context_menu()

main()
root.mainloop()
