import random
import tkinter as tk 
y = 0
y1 = 100
y2 = 100
y3 = 200
x = 100 
x1 = 200    
x2 = 0
x3 = 100

print("start")
win = tk.Tk()

print("stop")
canvas = tk.Canvas(win, bg = 'white', height = 800, width = 800)

for t in range(0, 4):    

     for i in range(0, 4):
        canvas.create_rectangle((x, y), (x1, y1), fill = "brown")
        canvas.create_rectangle((x2,y2), (x3, y3), fill = "brown")
        if t ==0 or t == 3:
        
            canvas.create_oval((x, y), (x1, y1), fill = "black")
            canvas.create_oval((x2, y2), (x3, y3), fill = "black")
        if  t == 2:
             canvas.create_oval((x2, y2), (x3, y3), fill = "black")
        if t == 1: 
            canvas.create_oval((x, y), (x1, y1), fill = "black")
            

        
        x+= 200
        x1 += 200
        x2 += 200
        x3 += 200
     y += 200
     y1 +=200
     y2 += 200
     y3 += 200
     x = 100 
     x1 = 200
     x2 = 0
     x3 = 100


canvas.pack()
win.mainloop()