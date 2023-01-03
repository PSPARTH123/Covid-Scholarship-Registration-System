from importlib import import_module
from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql

root1=Tk()
root1.title("Register-Page")
root1.geometry("1920x1080+0+0")
root1.state('zoomed')

bg = ImageTk.PhotoImage(file="schol1.jpg")
bg_image = Label(root1, image=bg).place(x=0, y=0, relwidth=1, relheight=1)

# creating Frame
Frame_Home0 = Frame(root1, bg="white")
Frame_Home0.place(x=50, y=10, height=100, width=1440)

Frame_Home1 = Frame(root1, bg="white")
Frame_Home1.place(x=50, y=120, height=630, width=300)

Frame_Home2 = Frame(root1, bg="white")
Frame_Home2.place(x=360, y=120, height=630, width=1130)

#Navbar design
nav_head1=Label(Frame_Home0, text="Frame head", font=("Impact", 35, "bold"), fg="Grey", bg="white"                         ).place(x=20, y=15)
nav_head2=Label(Frame_Home0, text="Marquee Text", font=("Impact", 35, "bold"), fg="Grey", bg="black"                       ).place(x=350, y=15, width=700, height=70)
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

def Personal_details(np1,np2,np3,np4,np5,np6,np7,np8):

    if np1 == "" or np2 == "" or np3== "" or np4 == "" or np5== "" or np6 == "" or np7 == "" or np8 == "":
        messagebox.showerror("Error", "All Fields are Required")
    else:
        con = pymysql.connect(host='localhost', user='root', password='LordTesla77', database='Scholarship')
        cur = con.cursor()
        cur.execute('select * from Personal where P_email = %s ',np2)
        row = cur.fetchone()
        if row != None:
            messagebox.showerror('Error', 'User already Exists')
        else:
            try:
                cur.execute(
                    'insert into Personal(F_name,P_email,P_phone,Aadhar,M_name,B_name,Acc_name,Acc_no) values(%s,%s,%s,%s,%s,%s,%s,%s)',
                    (
                        np1,
                        np2,
                        np3,
                        np4,
                        np5,
                        np6,
                        np7,
                        np8
                    ))
                con.commit()
                con.close()
                messagebox.showinfo('Success', 'Details Filled Successfully !')
            except Exception as e:
                messagebox.showerror('Error', f'Error due to {e}')
                
def home_main1():
    def personal_detail1():
        np1 = Name0_input.get()
        np2 = n01_input.get()
        np3 = n02_input.get()
        np4 = n06_input.get()
        np5 = n03_input.get()
        np6 = n04_input.get()
        np7 = n05_input.get()
        np8 = n07_input.get()
        Personal_details(np1,np2,np3,np4,np5,np6,np7,np8)


    Frame_Home2 = Frame(root1, bg="white")
    Frame_Home2.place(x=360, y=120, height=630, width=1130)

    #Frame Personal Details - 00000000
    #Detail Frame Header
    frame_head=Label(Frame_Home2, text="Personal Details", font=("Times New Roman", 35, "bold"), fg="Black", bg="white").place(x=400, y=10)
    Name0_input=StringVar()
    n01_input=StringVar()
    n02_input=StringVar()
    n03_input=StringVar()
    n04_input=StringVar()
    n05_input=StringVar()
    n06_input=StringVar()
    n07_input=StringVar()

    name_lab00=Label(Frame_Home2, text="Full Name    : ", font=('Times New Roman',20), fg="Black", bg="white"   ).place(x=100, y=150)
    name_inp00=Entry(Frame_Home2,textvariable=Name0_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"    ).place(x=270, y=150, width=250,height=40)
    name_lab01=Label(Frame_Home2, text="Email           : ", font=('Times New Roman',20), fg="Black", bg="white").place(x=100, y=230)
    name_inp01=Entry(Frame_Home2,textvariable=n01_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"      ).place(x=270, y=230, width=250,height=40)
    name_lab02=Label(Frame_Home2, text="Phone          : ", font=('Times New Roman',20), fg="Black", bg="white" ).place(x=100, y=310)
    name_inp02=Entry(Frame_Home2,textvariable=n02_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"      ).place(x=270, y=310, width=250,height=40)
    name_lab06=Label(Frame_Home2, text="Aadhar No.  : ", font=('Times New Roman',20), fg="Black", bg="white"    ).place(x=100, y=390)
    name_inp06=Entry(Frame_Home2,textvariable=n06_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"      ).place(x=270, y=390, width=250,height=40)
    #Left Side lables and entry ends
    name_lab03=Label(Frame_Home2, text="Mother Name    : ", font=('Times New Roman',20), fg="Black", bg="white").place(x=580, y=150)
    name_inp03=Entry(Frame_Home2,textvariable=n03_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"       ).place(x=780, y=150, width=250,height=40)
    name_lab04=Label(Frame_Home2, text="Bank Name       : ", font=('Times New Roman',20), fg="Black", bg="white"     ).place(x=580, y=230)
    name_inp04=Entry(Frame_Home2,textvariable=n04_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"       ).place(x=780, y=230, width=250,height=40)
    name_lab05=Label(Frame_Home2, text="Account Name  : ", font=('Times New Roman',20), fg="Black", bg="white"   ).place(x=580, y=310)
    name_inp05=Entry(Frame_Home2,textvariable=n05_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"       ).place(x=780, y=310, width=250,height=40)
    name_lab07=Label(Frame_Home2, text="Account No.     : ", font=('Times New Roman',20), fg="Black", bg="white"     ).place(x=580, y=390)
    name_inp07=Entry(Frame_Home2,textvariable=n07_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"       ).place(x=780, y=390, width=250,height=40)

    Frame3_btn01=Button(Frame_Home2,text="Save",command=personal_detail1,bd=0,bg="#d77337",fg="white",font=("times new roman",20) ).place(x=340,y=530,width=180,height=50)
    Frame3_btn02=Button(Frame_Home2,text="Reset",bd=0,bg="#d77337",fg="white",font=("times new roman",20)).place(x=540,y=530,width=180,height=50)

home_main1()
root1.mainloop()


