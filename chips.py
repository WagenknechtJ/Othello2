from tkinter import *

class Chip:
    
    global allChips, padding
    allChips = {}
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
        placedChip = canvas.create_oval(zero + padding, one + padding, two - padding, three - padding, fill = self.color, outline = "", tags = (str(place), "aChip"))
        Chip.updateColors(self, color, place, canvas)
        allChips[place] = color
    
    def updateColors(self, color, place, canvas):
        #check all colors around it, change their colors
        oppositeColor = "black"
        if color == "black":
            oppositeColor = "white"         
        toChange = []
        for check in [place+1, place+7, place+8, place+9, place-1, place-7, place-8, place-9]:
            if allChips.get(check) == oppositeColor:
                incrementedPlace = check
                for nextCheck in [incrementedPlace+1, incrementedPlace+7, incrementedPlace+8, incrementedPlace+9, incrementedPlace-1, incrementedPlace-7, incrementedPlace-8, incrementedPlace-9]:
                    if allChips.get(nextCheck) == color:
                        toChange.append(nextCheck) 
                        incrementedPlace = nextCheck
                        print("phew!")
                        print(toChange)
                    elif allChips.get(nextCheck) == oppositeColor:
                        for changing in canvas.find_withtag(toChange):
                            if canvas.find_withtag("aChip") == changing:
                                canvas.itemconfig(changing, fill = oppositeColor)
                                print("changed!")
        print("done")

