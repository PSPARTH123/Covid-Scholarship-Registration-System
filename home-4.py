from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql
root4=Tk()
root4.title("Register-Page")
root4.geometry("1920x1080+0+0")
root4.state('zoomed')

bg = ImageTk.PhotoImage(file="schol1.jpg")
bg_image = Label(root4, image=bg).place(x=0, y=0, relwidth=1, relheight=1)

# creating Frame
Frame_Home0 = Frame(root4, bg="white")
Frame_Home0.place(x=50, y=10, height=100, width=1440)

Frame_Home1 = Frame(root4, bg="white")
Frame_Home1.place(x=50, y=120, height=630, width=300)

Frame_Home5 = Frame(root4, bg="white")
Frame_Home5.place(x=360, y=120, height=630, width=1130)

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

def Address(na1,na2,na3,na4,na5,na6):
    if na1 == "" or na2 == "" or na3== "" or na4 == "" or na5== "" or na6 =="":
        messagebox.showerror("Error", "All Fields are Required")
    else:
        con = pymysql.connect(host='localhost', user='root', password='LordTesla77', database='Scholarship')
        cur = con.cursor()
        cur.execute('insert into Address(Line_1,Line_2,State,Village,District,Pincode) values(%s,%s,%s,%s,%s,%s)',
                    (
                        na1,
                        na2,
                        na3,
                        na4,
                        na5,
                        na6
                    ))
        row = cur.fetchone()
        if row != None:
            messagebox.showerror('Error', 'User already Exists')
        else:
            try:
                # cur.execute(
                #     'insert into Address(Line_1,Line_2,State,Village,District,Pincode) values(%s,%s,%s,%s,%s,%s)',
                #     (
                #         na1,
                #         na2,
                #         na3,
                #         na4,
                #         na5,
                #         na6
                #     ))
                con.commit()
                con.close()
                messagebox.showinfo('Success', 'Details Filled Successfully !')
            except Exception as e:
                messagebox.showerror('Error', f'Error due to {e}')

def home_main3():
    def Address1():
        na1 = Name3_input.get()
        na2 = n31_input.get()
        na3 = n32_input.get()
        na4 = n33_input.get()
        na5 = n34_input.get()
        na6 = n35_input.get()
        Address(na1,na2,na3,na4,na5,na6)

    # Frame Address Details - 3333333
    # Detail Frame Header
    frame_head = Label(Frame_Home5, text="Address Details", font=("Times New Roman", 35, "bold"), fg="Black",
                       bg="white").place(x=400, y=10)
    Name3_input = StringVar()
    n31_input = StringVar()
    n32_input = StringVar()
    n33_input = StringVar()
    n34_input = StringVar()
    n35_input = StringVar()
    # n36_input=StringVar()
    # n37_input=StringVar()
    choices4 = {'Maharashtra', 'Delhi', 'Haryana', 'Punjab', 'Chennai'}
    n31_input.set('Select One')
    choices5 = {'Mumbai', 'Pune', 'Nashik', 'Nagpur', 'Aurangabad'}
    n34_input.set('Select One')
    name_lab30 = Label(Frame_Home5, text="Line - 1         : ", font=('Times New Roman', 20), fg="Black",
                       bg="white").place(x=100, y=150)
    name_inp30 = Entry(Frame_Home5, textvariable=Name3_input, font=('Times New Roman', 20, 'normal'),
                       bg="#FCFFE9").place(x=270, y=150, width=250, height=40)
    name_lab31 = Label(Frame_Home5, text="State             : ", font=('Times New Roman', 20), fg="Black",
                       bg="white").place(x=100, y=230)
    name_inp31 = OptionMenu(Frame_Home5, n31_input, *choices4).place(x=270, y=230, width=250, height=40)
    name_lab32 = Label(Frame_Home5, text="Village/City  : ", font=('Times New Roman', 20), fg="Black",
                       bg="white").place(x=100, y=310)
    name_inp32 = Entry(Frame_Home5, textvariable=n32_input, font=('Times New Roman', 20, 'normal'), bg="#FCFFE9").place(
        x=270, y=310, width=250, height=40)
    # name_lab36=Label(Frame_Home5, text="Name5 : ", font=('Times New Roman',20), fg="Black", bg="white"      ).place(x=180, y=390)
    # name_inp36=Entry(Frame_Home5,textvariable=n36_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"  ).place(x=290, y=390, width=220,height=40)
    # Left Side lables and entry ends
    name_lab33 = Label(Frame_Home5, text="Line - 2    : ", font=('Times New Roman', 20), fg="Black", bg="white").place(
        x=600, y=150)
    name_inp33 = Entry(Frame_Home5, textvariable=n33_input, font=('Times New Roman', 20, 'normal'), bg="#FCFFE9").place(
        x=750, y=150, width=250, height=40)
    name_lab34 = Label(Frame_Home5, text="District     : ", font=('Times New Roman', 20), fg="Black", bg="white").place(
        x=600, y=230)
    name_inp34 = OptionMenu(Frame_Home5, n34_input, *choices5).place(x=750, y=230, width=250, height=40)
    name_lab35 = Label(Frame_Home5, text="Pincode    : ", font=('Times New Roman', 20), fg="Black", bg="white").place(
        x=600, y=310)
    name_inp35 = Entry(Frame_Home5, textvariable=n35_input, font=('Times New Roman', 20, 'normal'), bg="#FCFFE9").place(
        x=750, y=310, width=250, height=40)
    # name_lab37=Label(Frame_Home5, text="Name5 : ", font=('Times New Roman',20), fg="Black", bg="white"          ).place(x=570, y=390)
    # name_inp37=Entry(Frame_Home5,textvariable=n37_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"      ).place(x=760, y=390, width=220,height=40)

    Frame3_btn31 = Button(Frame_Home5, text="Save",command=Address1,bd=0, bg="#d77337", fg="white", font=("times new roman", 20)).place(
        x=340, y=530, width=180, height=50)
    Frame3_btn32 = Button(Frame_Home5, text="Reset", bd=0, bg="#d77337", fg="white",
                          font=("times new roman", 20)).place(x=540, y=530, width=180, height=50)
home_main3()
root4.mainloop()