from tkinter import *

class Court :

    def __init__(self, window, width, height, img) :
        self.canvas = Canvas(window, width = width, height = height)

        self.img = PhotoImage(file = img)
        self.canvas.create_image(width/2, height/2, image = self.img)

        self.width = width
        self.height = height

        self.canvas.pack()

        my_font = ("consolas", 50)
        self.board = self.canvas.create_text(width/2,65,font = my_font,fill = "white")

    def draw_score(self, score1, score2) :
        scores = str(score1) + " : " + str(score2)

        self.canvas.itemconfigure(self.board,text = scores)
        
