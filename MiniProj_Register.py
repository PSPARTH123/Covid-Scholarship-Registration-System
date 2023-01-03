from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql

root00=Tk()
root00.title("Register-Page")
root00.geometry("1920x1080+0+0")
root00.state('zoomed')

bg=ImageTk.PhotoImage(file="schol1.jpg")
bg_image=Label(root00,image=bg).place(x=0,y=0,relwidth=1,relheight=1)

def Reg(r1,r2,r3,r4,r5):
    if r1 == "" or r2 == "" or r3 == "" or r4 == "" or r5 == "":
        messagebox.showerror("Error", "All Fields are Required")
    else:
        con = pymysql.connect(host='localhost', user='root', password='LordTesla77', database='Scholarship')
        cur = con.cursor()
        cur.execute('select * from Reg where Email = %s ', r2)
        row = cur.fetchone()
        if row != None:
            messagebox.showerror('Error', 'User already Exists')
        else:
            try:
                cur.execute('insert into Reg(Name,Email,Phone,User,Password) values(%s,%s,%s,%s,%s)', (
                    r1,
                    r2,
                    r3,
                    r4,
                    r5
                ))
                con.commit()
                con.close()
                messagebox.showinfo('Success', 'Registration is Successfull')
            except Exception as e:
                messagebox.showerror('Error', f'Error due to {e}')

def Register():
        r1 = txt_name1.get()
        r2 = txt_Email1.get()
        r3 = txt_Phone1.get()
        r4 = txt_user1.get()
        r5 = txt_pass1.get()
        Reg(r1, r2, r3, r4,r5)
    
txt_Name1=StringVar()
txt_Email1=StringVar()
txt_Phone1=StringVar()
txt_user1=StringVar()
txt_pass1=StringVar()

#creating Frame
Frame_Register=Frame(root00,bg="white")
Frame_Register.place(x=470,y=10,height=760,width=580)

#Adding Lables to frame
title_reg=Label(Frame_Register,text="Registration",font=("Impact",55,"bold"),fg="Black",bg="white").place(x=90,y=30)
desc_reg=Label(Frame_Register,text="Student Register",font=("Goudy old style",25,"bold"),fg="Black",bg="white").place(x=90,y=140)

#Adding Lables and fields
User_Lable_reg=Label(Frame_Register,text="Name : ",font=("Goudy old style",20,"bold"),fg="black",bg="white").place(x=90,y=210)
txt_name1=Entry(Frame_Register,font=("times new roman",18),bg="#FCFFE9").place(x=90,y=250,width=380,height=35)

Email_Lable_reg=Label(Frame_Register,text="Email : ",font=("Goudy old style",20,"bold"),fg="black",bg="white").place(x=90,y=300)
txt_email1=Entry(Frame_Register,font=("times new roman",18),bg="#FCFFE9").place(x=90,y=340,width=380,height=35)

Phone_Lable_reg=Label(Frame_Register,text="Phone : ",font=("Goudy old style",20,"bold"),fg="black",bg="white").place(x=90,y=390)
txt_phone1=Entry(Frame_Register,font=("times new roman",18),bg="#FCFFE9").place(x=90,y=430,width=370,height=35)

User_Lable_reg=Label(Frame_Register,text="User-ID : ",font=("Goudy old style",20,"bold"),fg="black",bg="white").place(x=90,y=480)
txt_user01=Entry(Frame_Register,font=("times new roman",18),bg="#FCFFE9").place(x=90,y=520,width=380,height=35)

Pass_Lable_reg=Label(Frame_Register,text="Password : ",font=("Goudy old style",20,"bold"),fg="black",bg="white").place(x=90,y=570)
txt_pass01=Entry(Frame_Register,font=("times new roman",18),bg="#FCFFE9").place(x=90,y=610,width=380,height=35)


LogIn_btn_reg=Button(Frame_Register,command=Register,text="Register",bd=0,bg="#d77337",fg="white",font=("times new roman",20)).place(x=120,y=670,width=150,height=50)
Reset_btn_reg=Button(Frame_Register,text="Reset",bd=0,bg="#d77337",fg="white",font=("times new roman",20)).place(x=300,y=670,width=150,height=50)

root00.mainloop()