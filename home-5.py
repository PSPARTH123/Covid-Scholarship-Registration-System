from tkinter import *
from PIL import ImageTk
import pymysql

root5=Tk()
root5.title("Register-Page")
root5.geometry("1920x1080+0+0")
root5.state('zoomed')

bg = ImageTk.PhotoImage(file="schol1.jpg")
bg_image = Label(root5, image=bg).place(x=0, y=0, relwidth=1, relheight=1)

# creating Frame
Frame_Home0 = Frame(root5, bg="white")
Frame_Home0.place(x=50, y=10, height=100, width=1440)

Frame_Home1 = Frame(root5, bg="white")
Frame_Home1.place(x=50, y=120, height=630, width=300)

Frame_Home6 = Frame(root5, bg="white")
Frame_Home6.place(x=360, y=120, height=630, width=1130)

#Navbar design
nav_head=Label(Frame_Home0, text="Frame head", font=("Impact", 35, "bold"), fg="Grey", bg="white"                         ).place(x=20, y=15)
nav_head=Label(Frame_Home0, text="Marquee Text", font=("Impact", 35, "bold"), fg="Grey", bg="black"                       ).place(x=350, y=15, width=700, height=70)
nav_but1=Button(Frame_Home0, text="About Us", bd=0,font=("Goudy old style", 15, "bold"), fg="Black", bg='white'           ).place(x=1300, y=25, width=120, height=50)
nav_but2=Button(Frame_Home0, text="Scholarship Details", bd=0,font=("Goudy old style", 15, "bold"), fg="Black", bg='white').place(x=1080, y=25, width=220, height=50)

#Buttons Declaration
Frame_2_lab=Label(Frame_Home1,text="Forms List",bd=0,bg="white",fg="#d77337",font=("times new roman",30,"bold")).place(x=55,y=25)
Frame_1=Button(Frame_Home1,text="Personal Details",bd=0,bg="#d77337",fg="white",font=("times new roman",20)).place(x=35,y=110,width=230,height=50)
Frame_2=Button(Frame_Home1,text="Qualifiaction",bd=0,bg="#d77337",fg="white",font=("times new roman",20)).place(x=35,y=200,width=230,height=50)
Frame_3=Button(Frame_Home1,text="Current Course",bd=0,bg="#d77337",fg="white",font=("times new roman",20)   ).place(x=35,y=290,width=230,height=50)
Frame_4=Button(Frame_Home1,text="Address Details",bd=0,bg="#d77337",fg="white",font=("times new roman",20)  ).place(x=35,y=380,width=230,height=50)
Frame_5=Button(Frame_Home1,text="Scholarships",bd=0,bg="#d77337",fg="white",font=("times new roman",20) ).place(x=35,y=470,width=230,height=50)
Frame_6=Button(Frame_Home1,text="Gaurdian Details",bd=0,bg="#d77337",fg="white",font=("times new roman",20)    ).place(x=35,y=560,width=230,height=50)

def Fetch1():
    con = pymysql.connect(host='localhost', user='root', password='LordTesla77', database='Scholarship')
    cur = con.cursor()
    cur.execute('Select * from Current')
    give = cur.fetchall()
    for c1 in give:
            give = c1[0]
            return give
def Fetch2():
    con = pymysql.connect(host='localhost', user='root', password='LordTesla77', database='Scholarship')
    cur = con.cursor()
    cur.execute('Select * from Current')
    give = cur.fetchall()
    for c1 in give:
            give = c1[3]
            return give

#Frame Available Courses - 4444444
Frame_Home6 = Frame(root5, bg="white")
Frame_Home6.place(x=360, y=120, height=630, width=1130) 

frame_head=Label(Frame_Home6, text="Available Courses", font=("Times New Roman", 35, "bold"), fg="Black", bg="white").place(x=400, y=10)
Name4_input=StringVar()
n41_input=StringVar()
n42_input=StringVar()
n43_input=StringVar()
n44_input=StringVar()
n45_input=StringVar()
n46_input=StringVar()
n47_input=StringVar()
def Got():
    if Fetch1() =='Science' or Fetch2() == 'B.E':
        choices6={'TATA`s Covi-Special','Reliance`s Covi-Special','Goverment Scholarship'}
    elif Fetch1() =='Science' or Fetch2() == 'B.sc':
        choices6={'TATA`s Covi-Special','Reliance`s Covi-Special','Goverment Scholarship'}
    elif Fetch1() =='Science' or Fetch2() == 'B.Tech':
        choices6={'TATA`s Covi-Special','Reliance`s Covi-Special','Goverment Scholarship'}
    elif Fetch1() =='Science' or Fetch2() == 'M.E':
        choices6={'TATA`s Covi-Special','Reliance`s Covi-Special','Goverment Scholarship'}
    elif Fetch1() =='Science' or Fetch2() == 'M.Sc':
        choices6={'TATA`s Covi-Special','Reliance`s Covi-Special','Goverment Scholarship'}
    elif Fetch1() =='Science' or Fetch2() == 'M.Tech':
        choices6={'TATA`s Covi-Special','Reliance`s Covi-Special','Goverment Scholarship'}

    elif Fetch1() =='Commerce' or Fetch2() == 'C.A':
        choices6={'TATA`s Covi-Special','Reliance`s Covi-Special','Goverment Scholarship'}
    elif Fetch1() =='Commerce' or Fetch2() == 'B.Com':
        choices6={'TATA`s Covi-Special','Reliance`s Covi-Special','Goverment Scholarship'}
    elif Fetch1() =='Commerce' or Fetch2() == 'C.S':
        choices6={'TATA`s Covi-Special','Reliance`s Covi-Special','Goverment Scholarship'}
    elif Fetch1() =='Commerce' or Fetch2() == 'M.Com':
        choices6={'TATA`s Covi-Special','Reliance`s Covi-Special','Goverment Scholarship'}

    elif Fetch1() =='Arts' or Fetch2() == 'Fine Arts':
        choices6={'TATA`s Covi-Special','Reliance`s Covi-Special','Goverment Scholarship'}
    elif Fetch1() =='Arts' or Fetch2() == 'B.A':
        choices6={'TATA`s Covi-Special','Reliance`s Covi-Special','Goverment Scholarship'}
    elif Fetch1() =='Arts' or Fetch2() == 'M.A':
        choices6={'TATA`s Covi-Special','Reliance`s Covi-Special','Goverment Scholarship'}
    elif Fetch1() =='Arts' or Fetch2() == 'L.L.B':
        choices6={'TATA`s Covi-Special','Reliance`s Covi-Special','Goverment Scholarship'}
    elif Fetch1() =='Arts' or Fetch2() == 'B.H.M':
        choices6={'TATA`s Covi-Special','Goverment Scholarship'}



        
    

n44_input.set('Select One')

name_lab40=Label(Frame_Home6, text="Stram Selected  : ", font=('Times New Roman',20), fg="Black", bg="white"  ).place(x=330, y=150)
name_inp40=Label(Frame_Home6,text=Fetch1(), font=('Times New Roman',20,'normal'),bg="#FCFFE9").place(x=550, y=150, width=220,height=40)

name_lab41=Label(Frame_Home6, text="Courses   : ", font=('Times New Roman',20), fg="Black", bg="white"    ).place(x=150, y=230)
name_inp41=Label(Frame_Home6,text=Fetch2(), font=('Times New Roman',20,'normal'),bg="#FCFFE9"  ).place(x=290, y=230, width=220,height=40)

name_lab44=Label(Frame_Home6, text="Scholarships   : ", font=('Times New Roman',20), fg="Black", bg="white").place(x=570, y=230)
name_inp44=OptionMenu(Frame_Home6, n44_input,value=Got()                                                    ).place(x=760, y=230, width=220,height=40)

Frame3_btn41=Button(Frame_Home6,text="Save",bd=0,bg="#d77337",fg="white",font=("times new roman",20) ).place(x=340,y=530,width=180,height=50)
Frame3_btn42=Button(Frame_Home6,text="Reset",bd=0,bg="#d77337",fg="white",font=("times new roman",20)).place(x=540,y=530,width=180,height=50)                                                          
root5.mainloop()