from chips import *
import tkinter
from tkinter import *

#COLORS
grey = '#BBBBBB'
purple = '#6B4694'
blue = '#4783A8'
green = '#4DAB64'
orange = '#C45652'
black = '#FFFFFF'
white = '#000000'

global blackTurn 
blackTurn = TRUE

#create the Tkinter GUI interface, set title and turn cursor off
root = tkinter.Tk()
root.wm_title('Othello, take one')
root.configure(background=grey) #, cursor="none")

#global screenW, screenH, padding, scale, size
screenW = 1500 #screen width
screenH = 900 #screen height
padding = 20 #default padding
scale = 8 #how many boxes are in a row (and, as a square, how many columns there are)
size = (screenH)/scale #size of each individual box (width and height, it's a square)
labelW = 40 #screenW - (size*6) #width available to label

#create the main game interface (where the boxes and mines are) , set its size and color and location onscreen
canvas = tkinter.Canvas(root, height=screenH, width=screenH, bd = 0, background=grey)
canvas.grid(row=0, column=1, rowspan=1, columnspan = 1)
canvas.pack

#create the label with instructions, set its location on-screen
inst = tkinter.Label(root, width = int(labelW), bd = 0, bg = grey, fg = purple, font =('arial', 14, 'bold'),text='Text here')
inst.grid(row = 0,column = 0, rowspan = 1, columnspan=1)

#set up board itself - each square is tagged with its location?
for colum in range(1,int(size+1)):
        cob = colum - 1
        for cells in range(1,scale+1):
            cev = cells + (scale*cob)
            ceb = cells - 1
            startx = cells + (size*ceb)
            starty = colum + (size*cob)
#             new_cell = canvas.create_polygon(startx, starty,  startx+size,starty,  startx+size, starty+size, startx, starty+size, 
#                                 fill = grey, outline = purple, tags = (str(cev)))
            new_cell = canvas.create_rectangle(startx, starty, startx+size, starty+size, 
                                fill = grey, outline = purple, tags = (str(cev)))

#when you click on the screen, this happens
def click(self):
    global blackTurn
    flags = canvas.gettags(canvas.find_withtag(CURRENT))
    coords = canvas.coords(canvas.find_withtag(CURRENT))
    #print(flags)
    #print(canvas.coords(canvas.find_withtag(CURRENT)))
    if (blackTurn == TRUE) :
        color = "black"
        blackTurn = FALSE
    else :
        color = "white"
        blackTurn = TRUE
    place = int(flags[0])
    newChip = Chip(place,coords, color, canvas)
    print()

canvas.bind("<Button-1>", click)

root.mainloop()
