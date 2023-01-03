import sys
from logging import PlaceHolder
from tkinter import *
from PIL import ImageTk
def marquee_fun(widget,ww,wh,tw,th,d,s,position=0):
    if d=='right':
        if position >=tw-ww:
            position=0
        position=position+s
        widget,PlaceHolder(x=position)
    widget.after(100,lambda:marquee_fun(widget,ww,wh,tw,th,d,s,position=0))


root=Tk()
root.title("Register-Page")
root.geometry("1920x1080+0+0")
root.state('zoomed')

lab=Label(root, text="Yup it Works !!",font=('Times New Roman', 30)).place(x=20,y=20)
lab.after(100, marquee_fun(lab))

root.mainloop()