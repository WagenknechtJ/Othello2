from tkinter import *
from othelloMain import *

class Chip(Main):
    
    global allChips, padding
    allChips = []
    padding = 5
    
    def __init__(self, place, coords, color, canvas):
        self.place = place
        self.coords = coords
        self.color = color
        self.canvas = canvas
        zero = float(coords[0])
        one = float(coords[1])
        two = float(coords[2])
        three = float(coords[3])
        place = canvas.create_oval(zero + padding, one + padding, two - padding, three - padding, fill = Chip.setColor(color))
        allChips.append(place)
    
    def setColor(self, color):
        if ("black" in color):
            self.color = "#FFFFFF"
        elif ("white" in color):
            self.color = "#000000" 
        print(self.color)           

    def updateColors(self):
        #check all colors around it, change their colors
        print("done")

