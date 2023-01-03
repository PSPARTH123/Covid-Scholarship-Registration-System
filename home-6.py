from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql
root6=Tk()
root6.title("Register-Page")
root6.geometry("1920x1080+0+0")
root6.state('zoomed')

bg = ImageTk.PhotoImage(file="schol1.jpg")
bg_image = Label(root6, image=bg).place(x=0, y=0, relwidth=1, relheight=1)

# creating Frame
Frame_Home0 = Frame(root6, bg="white")
Frame_Home0.place(x=50, y=10, height=100, width=1440)

Frame_Home1 = Frame(root6, bg="white")
Frame_Home1.place(x=50, y=120, height=630, width=300)

Frame_Home7 = Frame(root6, bg="white")
Frame_Home7.place(x=360, y=120, height=630, width=1130)

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

def Gardian(ng1,ng2,ng3,ng4,ng5):
    if ng1 == "" or ng2 == "" or ng3== "" or ng4 == "" or ng5== "":
        messagebox.showerror("Error", "All Fields are Required")
    else:
        con = pymysql.connect(host='localhost', user='root', password='LordTesla77', database='Scholarship')
        cur = con.cursor()
        cur.execute('insert into Gaurdians(G_name,G_relation,G_email,G_address,G_phone) values(%s,%s,%s,%s,%s)',
                    (
                        ng1,
                        ng2,
                        ng3,
                        ng4,
                        ng5
                    ))
        row = cur.fetchone()
        if row != None:
            messagebox.showerror('Error', 'User already Exists')
        else:
            try:
                # cur.execute(
                #     'insert into Gaurdians(G_name,G_relation,G_email,G_phone,G_address) values(%s,%s,%s,%s,%s)',
                #     (
                #         ng1,
                #         ng2,
                #         ng3,
                #         ng4,
                #         ng5
                #     ))
                con.commit()
                con.close()
                messagebox.showinfo('Success', 'Details Filled Successfully !')
            except Exception as e:
                messagebox.showerror('Error', f'Error due to {e}')

def home_main6():
    def Gardian1():
        ng1 = Name5_input.get()
        ng2 = n51_input.get()
        ng3 = n52_input.get()
        ng4 = n53_input.get()
        ng5 = n54_input.get()
        Gardian(ng1,ng2,ng3,ng4,ng5)
    # Frame Gaurdians Details - 555555
    # Detail Frame Header
    frame_head = Label(Frame_Home7, text="Gaurdians Details", font=("Times New Roman", 35, "bold"), fg="Black",
                       bg="white").place(x=400, y=10)
    Name5_input = StringVar()
    n51_input = StringVar()
    n52_input = StringVar()
    n53_input = StringVar()
    n54_input = StringVar()
    # n55_input=StringVar()
    # n56_input=StringVar()
    # n57_input=StringVar()
    name_lab50 = Label(Frame_Home7, text="Gaurdian's Name  : ", font=('Times New Roman', 20), fg="Black",
                       bg="white").place(x=80, y=150)
    name_inp50 = Entry(Frame_Home7, textvariable=Name5_input, font=('Times New Roman', 20, 'normal'),
                       bg="#FCFFE9").place(x=300, y=150, width=220, height=40)
    name_lab51 = Label(Frame_Home7, text="Gaurdian's Email  : ", font=('Times New Roman', 20), fg="Black",
                       bg="white").place(x=80, y=230)
    name_inp51 = Entry(Frame_Home7, textvariable=n51_input, font=('Times New Roman', 20, 'normal'), bg="#FCFFE9").place(
        x=300, y=230, width=220, height=40)

    name_lab52 = Label(Frame_Home7, text="Gaurdian's Address : ", font=('Times New Roman', 20), fg="Black",
                       bg="white").place(x=280, y=310)
    name_inp52 = Entry(Frame_Home7, textvariable=n52_input, font=('Times New Roman', 20, 'normal'), bg="#FCFFE9").place(
        x=520, y=310, width=270, height=40)
    # name_lab56=Label(Frame_Home7, text="Name5 : ", font=('Times New Roman',20), fg="Black", bg="white"      ).place(x=180, y=390)
    # name_inp56=Entry(Frame_Home7,textvariable=n56_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"  ).place(x=290, y=390, width=220,height=40)
    # Left Side lables and entry ends
    name_lab53 = Label(Frame_Home7, text="Gaurdian's Relation : ", font=('Times New Roman', 20), fg="Black",
                       bg="white").place(x=580, y=150)
    name_inp53 = Entry(Frame_Home7, textvariable=n53_input, font=('Times New Roman', 20, 'normal'), bg="#FCFFE9").place(
        x=830, y=150, width=220, height=40)
    name_lab54 = Label(Frame_Home7, text="Gaurdian's Phone    : ", font=('Times New Roman', 20), fg="Black",
                       bg="white").place(x=580, y=230)
    name_inp54 = Entry(Frame_Home7, textvariable=n54_input, font=('Times New Roman', 20, 'normal'), bg="#FCFFE9").place(
        x=830, y=230, width=220, height=40)
    # name_lab55=Label(Frame_Home7, text="Mother Name  : ", font=('Times New Roman',20), fg="Black", bg="white"         ).place(x=570, y=310)
    # name_inp55=Entry(Frame_Home7,textvariable=n55_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"            ).place(x=760, y=310, width=220,height=40)
    # name_lab57=Label(Frame_Home7, text="Name5 : ", font=('Times New Roman',20), fg="Black", bg="white"          ).place(x=570, y=390)
    # name_inp57=Entry(Frame_Home7,textvariable=n57_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"      ).place(x=760, y=390, width=220,height=40)

    Frame3_btn51 = Button(Frame_Home7, text="Save",command=Gardian1, bd=0, bg="#d77337", fg="white", font=("times new roman", 20)).place(
        x=340, y=530, width=180, height=50)
    Frame3_btn52 = Button(Frame_Home7, text="Reset", bd=0, bg="#d77337", fg="white",
                          font=("times new roman", 20)).place(x=540, y=530, width=180, height=50)
home_main6()
root6.mainloop()