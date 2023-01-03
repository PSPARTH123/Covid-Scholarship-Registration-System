from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql

root00=Tk()
root00.title("LogIN-Page")
root00.geometry("1920x1080+0+0")
root00.state('zoomed')

bg=ImageTk.PhotoImage(file="schol1.jpg")
bg_image=Label(root00,image=bg).place(x=0,y=0,relwidth=1,relheight=1)

#creating Frame
Frame_login=Frame(root00,bg="white")
Frame_login.place(x=470,y=10,height=760,width=580)

def Log(l1,l2):
    if l1 == "" or l2 == "":
        messagebox.showerror("Error", "All Fields are Required")
    else:
        con = pymysql.connect(host='localhost', user='root', password='LordTesla77', database='Scholarship')
        cur = con.cursor()
        cur.execute('select * from Reg where User =%s and Password =%s',
                    (l1,l2))
        row = cur.fetchone()
        if row == None:
            messagebox.showinfo('Error', 'Invalid username and password')
        else:
            messagebox.showinfo('Success', 'Login Successfully')
            con.commit()
            con.close()
def Login():
        l1 = txt_user.get()
        l2 = txt_pass.get()
        Log(l1,l2)

#Adding Lables to frame
title_log=Label(Frame_login,text="LoGIN Form",font=("Impact",55,"bold"),fg="Black",bg="white").place(x=90,y=30)
desc_log=Label(Frame_login,text="Student Login",font=("Goudy old style",25,"bold"),fg="Black",bg="white").place(x=90,y=140)

#Adding Lables and fields
User_Lable_log=Label(Frame_login,text="Username : ",font=("Goudy old style",25,"bold"),fg="black",bg="white").place(x=90,y=260)
txt_user=Entry(Frame_login,font=("times new roman",20),bg="#FCFFE9")
txt_user.place(x=90,y=330,width=380,height=40)

User_Lable_log=Label(Frame_login,text="Password : ",font=("Goudy old style",25,"bold"),fg="black",bg="white").place(x=90,y=390)
txt_pass=Entry(Frame_login,font=("times new roman",20),bg="#FCFFE9")
txt_pass.place(x=90,y=460,width=380,height=40)

forget_btn_log=Button(Frame_login,text="Forget Password ? click here",bd=0,bg="white",fg="gray",font=("times new roman", 15)).place(x=90,y=520)
LogIn_btn_log=Button(Frame_login,command=Login,text="Log-In",bd=0,bg="#d77337",fg="white",font=("times new roman",20)).place(x=120,y=620,width=150,height=50)
Reset_btn_log=Button(Frame_login,text="Reset",bd=0,bg="#d77337",fg="white",font=("times new roman",20)).place(x=300,y=620,width=150,height=50)


root00.mainloop()