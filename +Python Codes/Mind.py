from tkinter import *


class draw():
    def __init__(self, canvas_width, canvas_height):
        self.x = canvas_width//2
        self.y = canvas_height//2

        self.main = Tk()
        self.main.title("Drawing")

        self.papaer = Canvas(self.main, width=canvas_width, height=canvas_height)
        self.papaer.pack(expand=YES, fill=BOTH)

    def point(self, x, y):
        x1, y1 = (x - 0.5), (y - 0.5)
        x2, y2 = (x + 0.5), (y + 0.5)
        self.papaer.create_oval(x1, y1, x2, y2, fill="#000000")
        
        #self.x, self.y = x, 

    def finish(self):
        mainloop()



length = 500
drawer = draw(length, length)

def cube(x_center, y_center, side_length):
    x_from = x_center - side_length//2
    y_from = y_center - side_length//2
    for x in range(x_from, x_from+side_length+1):
        for y in range(y_from, y_from+side_length+1):
            drawer.point(x, y)

def circular(x_center, y_center, radius):
    side_length = radius * 2 
    x_from = x_center - side_length//2
    y_from = y_center - side_length//2
    for x in range(x_from, x_from+side_length+1):
        for y in range(y_from, y_from+side_length+1):
            if int((x-x_center)**2) + int((y-y_center)**2) <= radius**2:
                drawer.point(x, y)


circular(drawer.x, drawer.y, 100)


drawer.finish()