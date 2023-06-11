from tkinter import  *
import time





window  = Tk()
window.geometry("500x400")
window.resizable(width = False , height = False)


class Ball : 
    def __init__(self , canvas , color) :
       self.canvas = canvas 
       self.oval = canvas.create_oval(200,200,215,215, fill = color)
       self.x = 0 
       self.y = 0

    def draw(self): 
        self.canvas.move(self.oval ,self.x ,self.y )

canvas = Canvas(window , width=500 , height=400)
canvas.pack()
ball = Ball(canvas = canvas , color = "red")









while 1 > 0 :
    ball.draw()
    window.update








    



    
    





