from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql
root2=Tk()
root2.title("Register-Page")
root2.geometry("1920x1080+0+0")
root2.state('zoomed')

bg = ImageTk.PhotoImage(file="schol1.jpg")
bg_image = Label(root2, image=bg).place(x=0, y=0, relwidth=1, relheight=1)

# creating Frame
Frame_Home0 = Frame(root2, bg="white")
Frame_Home0.place(x=50, y=10, height=100, width=1440)

Frame_Home1 = Frame(root2, bg="white")
Frame_Home1.place(x=50, y=120, height=630, width=300)

Frame_Home3 = Frame(root2, bg="white")
Frame_Home3.place(x=360, y=120, height=630, width=1130)

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
def Past(npa1,npa2,npa3,npa4,npa5,npa6):
    if npa1 == "" or npa2 == "" or npa3== "" or npa4 == "" or npa5== "" or npa6 == "":
        messagebox.showerror("Error", "All Fields are Required")
    else:
        con = pymysql.connect(host='localhost', user='root', password='LordTesla77', database='Scholarship')
        cur = con.cursor()
        cur.execute('insert into Past_q(LPE,E_stream,School,E_board,Marks,Mark_name) values(%s,%s,%s,%s,%s,%s)',
                    (
                        npa1,
                        npa2,
                        npa3,
                        npa4,
                        npa5,
                        npa6
                    ))
        row = cur.fetchone()        
        if row != None:
            messagebox.showerror('Error', 'User already Exists')
        else:
            try:
                # cur.execute(
                #     'insert into Past_q(LPE,E_stream,School,E_board,Marks,Mark_name) values(%s,%s,%s,%s,%s,%s)',
                #     (
                #         npa1,
                #         npa2,
                #         npa3,
                #         npa4,
                #         npa5,
                #         npa6
                #     ))
                con.commit()
                con.close()
                messagebox.showinfo('Success', 'Details Filled Successfully !')
            except Exception as e:
                messagebox.showerror('Error', f'Error due to {e}')
                
def home_main2():
    def Past1():
        npa1 = Name1_input.get()
        npa2 = n11_input.get()
        npa3 = n12_input.get()
        npa4 = n13_input.get()
        npa5 = n14_input.get()
        npa6 = n16_input.get()
        Past(npa1,npa2,npa3,npa4,npa5,npa6)


    # Frame Past Qualification - 11111111
    # Detail Frame Header
    frame_head = Label(Frame_Home3, text="Past Qualification", font=("Times New Roman", 35, "bold"), fg="Black",
                       bg="white").place(x=400, y=10)
    Name1_input = StringVar()
    n11_input = StringVar()
    n12_input = StringVar()
    n13_input = StringVar()
    n14_input = StringVar()
    # n15_input=StringVar()
    n16_input = StringVar()
    # n17_input=StringVar()
    choices = {'SSC', 'HSC', 'CBSE-10th', 'CBSE-12th', 'ICSE-10th', 'ICSE-12th'}
    Name1_input.set('HSC')
    name_lab10 = Label(Frame_Home3, text="Last Exam Passed (LEP) : ", font=('Times New Roman', 20), fg="Black",
                       bg="white").place(x=80, y=150)
    name_inp10 = OptionMenu(Frame_Home3, Name1_input, *choices).place(x=370, y=150, width=220, height=40)
    name_lab11 = Label(Frame_Home3, text="Last School Name           : ", font=('Times New Roman', 20), fg="Black",
                       bg="white").place(x=80, y=230)
    name_inp11 = Entry(Frame_Home3, textvariable=n11_input, font=('Times New Roman', 20, 'normal'), bg="#FCFFE9").place(
        x=370, y=230, width=220, height=40)

    name_lab12 = Label(Frame_Home3, text="Marks Obtianed (in LEP)     : ", font=('Times New Roman', 20), fg="Black",
                       bg="white").place(x=230, y=310)
    name_inp12 = Entry(Frame_Home3, textvariable=n12_input, font=('Times New Roman', 20, 'normal'), bg="#FCFFE9").place(
        x=600, y=310, width=270, height=40)
    name_lab16 = Label(Frame_Home3, text="Name (As Per Marksheet)    : ", font=('Times New Roman', 20), fg="Black",
                       bg="white").place(x=230, y=390)
    name_inp16 = Entry(Frame_Home3, textvariable=n16_input, font=('Times New Roman', 20, 'normal'), bg="#FCFFE9").place(
        x=600, y=390, width=270, height=40)
    # Left Side lables and entry ends
    name_lab13 = Label(Frame_Home3, text="Stream of Exam : ", font=('Times New Roman', 20), fg="Black",
                       bg="white").place(x=630, y=150)
    name_inp13 = Entry(Frame_Home3, textvariable=n13_input, font=('Times New Roman', 20, 'normal'), bg="#FCFFE9").place(
        x=830, y=150, width=220, height=40)
    name_lab14 = Label(Frame_Home3, text="Board Of Exam : ", font=('Times New Roman', 20), fg="Black",
                       bg="white").place(x=630, y=230)
    name_inp14 = Entry(Frame_Home3, textvariable=n14_input, font=('Times New Roman', 20, 'normal'), bg="#FCFFE9").place(
        x=830, y=230, width=220, height=40)
    # name_lab15=Label(Frame_Home3, text="Mother Name  : ", font=('Times New Roman',20), fg="Black", bg="white"   ).place(x=570, y=310)
    # name_inp15=Entry(Frame_Home3,textvariable=n15_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"      ).place(x=760, y=310, width=220,height=40)
    # name_lab17=Label(Frame_Home3, text="Name5 : ", font=('Times New Roman',20), fg="Black", bg="white"          ).place(x=570, y=390)
    # name_inp17=Entry(Frame_Home3,textvariable=n17_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"      ).place(x=760, y=390, width=220,height=40)

    Frame3_btn11 = Button(Frame_Home3, text="Save",command=Past1 ,bd=0, bg="#d77337", fg="white", font=("times new roman", 20)).place(
        x=340, y=530, width=180, height=50)
    Frame3_btn12 = Button(Frame_Home3, text="Reset", bd=0, bg="#d77337", fg="white",
                          font=("times new roman", 20)).place(x=540, y=530, width=180, height=50)

home_main2()
root2.mainloop()