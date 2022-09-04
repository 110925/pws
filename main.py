from tkinter import *
from tkinter import ttk
import pyscreenshot as ImageGrab 
from PIL import Image
import random

letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]

#define the app
app = Tk()
app.geometry("400x400")

#space to draw
x1 = 100
x2 = 300
y1 = 90
y2 = 290
#get mouse coordinates when pressed
def get_x_and_y(event):
    global lasx, lasy
    lasx, lasy = event.x, event.y

#draw lines
def draw_smth(event):
    global lasx, lasy
    canvas.create_rectangle(lasx, lasy, lasx+20, lasy+20, fill="black", outline = 'black')
    lasx, lasy = event.x, event.y

#create the canvas
canvas = Canvas(app, bg='gray')
canvas.pack(anchor='nw', fill='both', expand=1)

canvas.bind("<Button-1>", get_x_and_y)
canvas.bind("<B1-Motion>", draw_smth)
canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline = 'white')

#Saving the picture in a file
def save_picture():
  box = (canvas.winfo_rootx()+x1, canvas.winfo_rooty()+y1, canvas.winfo_rootx()+x2, canvas.winfo_rooty()+y2)
  grab = ImageGrab.grab(bbox = box)
  grab.save('random/random.png')
  image = Image.open('random/random.png')
  new_image = image.resize((20, 20))
  new_image.save('random/random.png')


#clear the canvas
def clear_canvas():
  canvas.delete('all')
  canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline = 'white')

#Add a Label widget in the Canvas
label = Label(canvas,
              text="Click the Button to check!",
              font=('Helvetica 17 bold'))
label.place(x=35, y=300)

label2 = Label(canvas,
              text="Draw the letter "+ random.choice(letter),
              font=('Helvetica 17 bold'))
label2.place(x=85, y=50)
#Create a button in the canvas 
ttk.Button(canvas, text="Check", command=save_picture).place(x=162, y=340)
ttk.Button(canvas, text="Clear", command=clear_canvas).place(x=162, y=370)

canvas.pack()

app.mainloop()
