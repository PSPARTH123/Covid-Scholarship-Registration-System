from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql
root3=Tk()
root3.title("Register-Page")
root3.geometry("1920x1080+0+0")
root3.state('zoomed')

bg = ImageTk.PhotoImage(file="schol1.jpg")
bg_image = Label(root3, image=bg).place(x=0, y=0, relwidth=1, relheight=1)

# creating Frame
Frame_Home0 = Frame(root3, bg="white")
Frame_Home0.place(x=50, y=10, height=100, width=1440)

Frame_Home1 = Frame(root3, bg="white")
Frame_Home1.place(x=50, y=120, height=630, width=300)

Frame_Home4 = Frame(root3, bg="white")
Frame_Home4.place(x=360, y=120, height=630, width=1130)

#Navbar design
nav_head=Label(Frame_Home0, text="Covid", font=("Impact", 35, "bold"), fg="Grey", bg="white"                         ).place(x=20, y=15)
nav_head=Label(Frame_Home0, text="Scholarship", font=("Impact", 35, "bold"), fg="Grey", bg="black"                       ).place(x=350, y=15, width=700, height=70)
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

def Current(nc1,nc2,nc3,nc4,nc5):
    if nc1 == "" or nc2 == "" or nc3== "" or nc4 == "" or nc5== "":
        messagebox.showerror("Error", "All Fields are Required")
    else:
        con = pymysql.connect(host='localhost', user='root', password='LordTesla77', database='Scholarship')
        cur = con.cursor()
        cur.execute('insert into Current(Stream,University,College_N,Course,D_course) values(%s,%s,%s,%s,%s)',
                    
                    (
                        nc1,
                        nc2,
                        nc3,
                        nc4,
                        nc5
                    ))
        row = cur.fetchone()
        if row != None:
            messagebox.showerror('Error', 'User already Exists')
        else:
            try:
                # cur.execute('insert into Current(Stream,University,College_N,Course,D_course) values(%s,%s,%s,%s,%s)',
                    
                #     (
                #         nc1,
                #         nc2,
                #         nc3,
                #         nc4,
                #         nc5
                #     ))
                con.commit()
                con.close()
                messagebox.showinfo('Success', 'Details Filled Successfully !')
            except Exception as e:
                messagebox.showerror('Error', f'Error due to {e}')

def home_main3():
    def Current1():
        nc1 = Name2_input.get()
        nc2 = n21_input.get()
        nc3 = n22_input.get()
        nc4 = n23_input.get()
        nc5 = n24_input.get()
        Current(nc1,nc2,nc3,nc4,nc5)

    # Frame Current Course - 2222222
    # Detail Frame Header
    frame_head = Label(Frame_Home4, text="Current Course", font=("Times New Roman", 35, "bold"), fg="Black",
                       bg="white").place(x=400, y=10)
    Name2_input = StringVar()
    n21_input = StringVar()
    n22_input = StringVar()
    n23_input = StringVar()
    n24_input = StringVar()
    # n25_input=StringVar()
    # n26_input=StringVar()
    # n27_input=StringVar()
    
    # def Got1():
    #     if Name2_input == 'Science':
    #         choices2 = ['B.E', 'B.Tech', 'M.E', 'M.Tech', 'B.sc', 'M.Sc']
    #         return choices2
    #     elif Name2_input =='Commerce':
    #         choices2 = ['C.A', 'B.Com', 'C.S', 'M.Com']
    #         return choices2
    #     elif Name2_input =='Arts':
    #         choices2 = ['Fine Arts', 'B.A', 'M.A', 'L.L.B', 'B.H.M']
    #         return choices2

    choices2 = ['B.E', 'B.Tech', 'M.E', 'M.Tech', 'B.sc', 'M.Sc','C.A', 'B.Com', 'C.S', 'M.Com','Fine Arts', 'B.A', 'M.A', 'L.L.B', 'B.H.M']
    choices3 = ['Science', 'Commerce', 'Arts']
    Name2_input.set('Select One')
    n22_input.set('Select One')
    name_lab20 = Label(Frame_Home4, text="Stream        : ", font=('Times New Roman', 20), fg="Black",
                       bg="white").place(x=100, y=150)
    name_inp20 = OptionMenu(Frame_Home4, Name2_input, *choices3).place(x=260, y=150, width=220, height=40)
    
    name_lab21 = Label(Frame_Home4, text="University   : ", font=('Times New Roman', 20), fg="Black", bg="white").place(
        x=100, y=230)
    name_inp21 = Entry(Frame_Home4, textvariable=n21_input, font=('Times New Roman', 20, 'normal'), bg="#FCFFE9").place(
        x=260, y=230, width=220, height=40)

    name_lab22 = Label(Frame_Home4, text="Courses  : ", font=('Times New Roman', 20), fg="Black", bg="white").place(
        x=340, y=330)
    name_inp22 = OptionMenu(Frame_Home4, n22_input, *choices2).place(x=460, y=330, width=220, height=40)
 
    name_lab23 = Label(Frame_Home4, text="College Name    : ", font=('Times New Roman', 20), fg="Black",
                       bg="white").place(x=570, y=150)
    name_inp23 = Entry(Frame_Home4, textvariable=n23_input, font=('Times New Roman', 20, 'normal'), bg="#FCFFE9").place(
        x=810, y=150, width=220, height=40)
    name_lab24 = Label(Frame_Home4, text="Duration Of Course : ", font=('Times New Roman', 20), fg="Black",
                       bg="white").place(x=570, y=230)
    name_inp24 = Entry(Frame_Home4, textvariable=n24_input, font=('Times New Roman', 20, 'normal'), bg="#FCFFE9").place(
        x=810, y=230, width=220, height=40)
 

    Frame3_btn21 = Button(Frame_Home4, text="Save",command=Current1, bd=0, bg="#d77337", fg="white", font=("times new roman", 20)).place(
        x=340, y=530, width=180, height=50)
    Frame3_btn22 = Button(Frame_Home4, text="Reset", bd=0, bg="#d77337", fg="white",
                          font=("times new roman", 20)).place(x=540, y=530, width=180, height=50)

home_main3()
root3.mainloop()