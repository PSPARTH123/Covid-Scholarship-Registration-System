from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk
from fpdf import FPDF
import pymysql
from setuptools import Command

root00=Tk()
root00.title("Register-Page")
root00.geometry("1920x1080+0+0")
root00.state('zoomed')

bg = ImageTk.PhotoImage(file="schol1.jpg")
bg_image = Label(root00, image=bg).place(x=0, y=0, relwidth=1, relheight=1)

#************************************ All Data-Base Functions ************************************

#                          ***** Personal *******
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
                home_main2()
            except Exception as e:
                messagebox.showerror('Error', f'Error due to {e}')

#         ************** Past **************
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
                home_main3()
            except Exception as e:
                messagebox.showerror('Error', f'Error due to {e}')

#        ********* Current **************
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
                home_main4()
                messagebox.showinfo('Success', 'Details Filled Successfully !')
            except Exception as e:
                messagebox.showerror('Error', f'Error due to {e}')

#           *********** Address **************
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
                home_main5()
                messagebox.showinfo('Success', 'Details Filled Successfully !')
            except Exception as e:
                messagebox.showerror('Error', f'Error due to {e}')

#      *********** Fetch for Available Courses ************
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

#     *********** Gaurdian Details ***************
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
                Receipt()
            except Exception as e:
                messagebox.showerror('Error', f'Error due to {e}')


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
                login()
            except Exception as e:
                messagebox.showerror('Error', f'Error due to {e}')

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

def welcome():
    # creating Frame
    Frame_Wlecome = Frame(root00, bg="white")
    Frame_Wlecome.place(x=470,y=90,height=650,width=580)

    # Adding Lables to frame
    title = Label(Frame_Wlecome, text="Covi-Scholarship", font=("Impact", 55, "bold"), fg="Black", bg="white").place(x=30, y=30)
    desc = Label(Frame_Wlecome, text="!! welcome !!", font=("Goudy old style", 25, "bold"), fg="Black", bg="white").place(x=205, y=190)

    LogIn_btn = Button(Frame_Wlecome,command=login, text="LogIn", bd=0, bg="#d77337", fg="white",font=("times new roman", 25)).place(x=200, y=350, width=200, height=70)
    Reset_btn = Button(Frame_Wlecome,command=register, text="Register", bd=0, bg="#d77337", fg="white",font=("times new roman", 25)).place(x=200, y=450, width=200, height=70)

#Register Page Calling
def register():
     #creating Frame
    Frame_Register=Frame(root00,bg="white")
    Frame_Register.place(x=470,y=10,height=760,width=580)
    
    def Register2():
        r1 = txt_Name1.get()
        r2 = txt_Email1.get()
        r3 = txt_Phone1.get()
        r4 = txt_user1.get()
        r5 = txt_pass1.get()
        Reg(r1,r2,r3,r4,r5)
        
    txt_Name1=StringVar()
    txt_Email1=StringVar()
    txt_Phone1=StringVar()
    txt_user1=StringVar()
    txt_pass1=StringVar()

    #Adding Lables to frame
    title_reg=Label(Frame_Register,text="Registration",font=("Impact",55,"bold"),fg="Black",bg="white").place(x=90,y=30)
    desc_reg=Label(Frame_Register,text="Student Register",font=("Goudy old style",25,"bold"),fg="Black",bg="white").place(x=90,y=140)
    
    #Adding Lables and fields
    User_Lable_reg=Label(Frame_Register,text="Name : ",font=("Goudy old style",20,"bold"),fg="black",bg="white").place(x=90,y=210)
    txt_name1=Entry(Frame_Register,textvariable=txt_Name1,font=("times new roman",18),bg="#FCFFE9").place(x=90,y=250,width=380,height=35)

    Email_Lable_reg=Label(Frame_Register,text="Email : ",font=("Goudy old style",20,"bold"),fg="black",bg="white").place(x=90,y=300)
    txt_email1=Entry(Frame_Register,textvariable=txt_Email1,font=("times new roman",18),bg="#FCFFE9").place(x=90,y=340,width=380,height=35)

    Phone_Lable_reg=Label(Frame_Register,text="Phone : ",font=("Goudy old style",20,"bold"),fg="black",bg="white").place(x=90,y=390)
    txt_phone1=Entry(Frame_Register,textvariable=txt_Phone1,font=("times new roman",18),bg="#FCFFE9").place(x=90,y=430,width=370,height=35)

    User_Lable_reg=Label(Frame_Register,text="User-ID : ",font=("Goudy old style",20,"bold"),fg="black",bg="white").place(x=90,y=480)
    txt_user01=Entry(Frame_Register,textvariable=txt_user1,font=("times new roman",18),bg="#FCFFE9").place(x=90,y=520,width=380,height=35)

    Pass_Lable_reg=Label(Frame_Register,text="Password : ",font=("Goudy old style",20,"bold"),fg="black",bg="white").place(x=90,y=570)
    txt_pass01=Entry(Frame_Register,show='*',textvariable=txt_pass1,font=("times new roman",18),bg="#FCFFE9").place(x=90,y=610,width=380,height=35)
 
    LogIn_btn_reg=Button(Frame_Register,command=Register2,text="Register",bd=0,bg="#d77337",fg="white",font=("times new roman",20)).place(x=120,y=670,width=150,height=50)
    Reset_btn_reg=Button(Frame_Register,text="Reset",bd=0,bg="#d77337",fg="white",font=("times new roman",20)).place(x=300,y=670,width=150,height=50)

#Login Page Calling
def login():
    Frame_login=Frame(root00,bg="white")
    Frame_login.place(x=470,y=10,height=760,width=580)

    def Login():
        l1 = txt_user.get()
        l2 = txt_pass.get()
        Log(l1,l2)
        nav_Frame()
        menu_frame()
        home_main1()

    #Adding Lables to frame
    title_log=Label(Frame_login,text="LoGIN Form",font=("Impact",55,"bold"),fg="Black",bg="white").place(x=90,y=30)
    desc_log=Label(Frame_login,text="Student Login",font=("Goudy old style",25,"bold"),fg="Black",bg="white").place(x=90,y=140)

    #Adding Lables and fields
    User_Lable_log=Label(Frame_login,text="Username : ",font=("Goudy old style",25,"bold"),fg="black",bg="white").place(x=90,y=260)
    txt_user=Entry(Frame_login,font=("times new roman",20),bg="#FCFFE9")
    txt_user.place(x=90,y=330,width=380,height=40)

    User_Lable_log=Label(Frame_login,text="Password : ",font=("Goudy old style",25,"bold"),fg="black",bg="white").place(x=90,y=390)
    txt_pass=Entry(Frame_login,show='*',font=("times new roman",20),bg="#FCFFE9")
    txt_pass.place(x=90,y=460,width=380,height=40)

    forget_btn_log=Button(Frame_login,text="Forget Password ? click here",bd=0,bg="white",fg="gray",font=("times new roman", 15)).place(x=90,y=520)
    LogIn_btn_log=Button(Frame_login,command=Login,text="Log-In",bd=0,bg="#d77337",fg="white",font=("times new roman",20)).place(x=120,y=620,width=150,height=50)
    Reset_btn_log=Button(Frame_login,text="Reset",bd=0,bg="#d77337",fg="white",font=("times new roman",20)).place(x=300,y=620,width=150,height=50)
  

def nav_Frame():
        Frame_Home0 = Frame(root00, bg="white")
        Frame_Home0.place(x=50, y=10, height=100, width=1440)

        #Navbar design
        nav_head=Label(Frame_Home0, text="Covid", font=("Impact", 35, "bold"), fg="Grey", bg="white"                         ).place(x=20, y=15)
        nav_head=Label(Frame_Home0, text="Scholarship", font=("Impact", 35, "bold"), fg="Grey", bg="black"                       ).place(x=350, y=15, width=700, height=70)
        nav_but1=Button(Frame_Home0, text="About Us", bd=0,font=("Goudy old style", 15, "bold"), fg="Black", bg='white'           ).place(x=1300, y=25, width=120, height=50)
        nav_but2=Button(Frame_Home0, text="Scholarship Details", bd=0,font=("Goudy old style", 15, "bold"), fg="Black", bg='white').place(x=1080, y=25, width=220, height=50)

#*************************************** Personal Details ************************************
def home_main1():
        Frame_Home2 = Frame(root00, bg="white")
        Frame_Home2.place(x=360, y=120, height=630, width=1130)
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
        def reset1():
            Name0_input.set("")
            n01_input.set("")
            n02_input.set("")
            n03_input.set("")
            n04_input.set("")
            n05_input.set("")
            n06_input.set("")

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

        name_lab03=Label(Frame_Home2, text="Mother Name    : ", font=('Times New Roman',20), fg="Black", bg="white").place(x=580, y=150)
        name_inp03=Entry(Frame_Home2,textvariable=n03_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"       ).place(x=780, y=150, width=250,height=40)
        name_lab04=Label(Frame_Home2, text="Bank Name       : ", font=('Times New Roman',20), fg="Black", bg="white"     ).place(x=580, y=230)
        name_inp04=Entry(Frame_Home2,textvariable=n04_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"       ).place(x=780, y=230, width=250,height=40)
        name_lab05=Label(Frame_Home2, text="Account Name  : ", font=('Times New Roman',20), fg="Black", bg="white"   ).place(x=580, y=310)
        name_inp05=Entry(Frame_Home2,textvariable=n05_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"       ).place(x=780, y=310, width=250,height=40)
        name_lab07=Label(Frame_Home2, text="Account No.     : ", font=('Times New Roman',20), fg="Black", bg="white"     ).place(x=580, y=390)
        name_inp07=Entry(Frame_Home2,textvariable=n07_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"       ).place(x=780, y=390, width=250,height=40)

        Frame3_btn01=Button(Frame_Home2,command=personal_detail1,text="Save",bd=0,bg="#d77337",fg="white",font=("times new roman",20) ).place(x=340,y=530,width=180,height=50)
        Frame3_btn02=Button(Frame_Home2,command=reset1,text="Reset",bd=0,bg="#d77337",fg="white",font=("times new roman",20)).place(x=540,y=530,width=180,height=50)

#********************************** Past Qualifiaction ************************************
def home_main2():
        Frame_Home3 = Frame(root00, bg="white")
        Frame_Home3.place(x=360, y=120, height=630, width=1130)
        def Past1():
            npa1 = Name1_input.get()
            npa2 = n11_input.get()
            npa3 = n12_input.get()
            npa4 = n13_input.get()
            npa5 = n14_input.get()
            npa6 = n16_input.get()
            Past(npa1,npa2,npa3,npa4,npa5,npa6)
        def reset2():
            Name1_input.set("")
            n11_input.set("-- Select --")
            n12_input.set("")
            n16_input.set("")
            n14_input.set("")
            n13_input.set("")

        frame_head=Label(Frame_Home3, text="Past Qualification", font=("Times New Roman", 35, "bold"), fg="Black", bg="white").place(x=400, y=10)
        Name1_input=StringVar()
        n11_input=StringVar()
        n12_input=StringVar()
        n13_input=StringVar()
        n14_input=StringVar()
        n16_input=StringVar()
        
        choices={'SSC','HSC','CBSE-10th','CBSE-12th','ICSE-10th','ICSE-12th'}
        Name1_input.set('HSC')
        name_lab10=Label(Frame_Home3, text="Last Exam Passed (LEP) : ", font=('Times New Roman',20), fg="Black", bg="white"     ).place(x=80, y=150)
        name_inp10=OptionMenu(Frame_Home3,Name1_input,*choices).place(x=370, y=150, width=220,height=40)
        name_lab11=Label(Frame_Home3, text="Last School Name           : ", font=('Times New Roman',20), fg="Black", bg="white" ).place(x=80, y=230)
        name_inp11=Entry(Frame_Home3,textvariable=n11_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"                  ).place(x=370, y=230, width=220,height=40)

        name_lab12=Label(Frame_Home3, text="Marks Obtianed (in LEP)     : ", font=('Times New Roman',20), fg="Black", bg="white").place(x=230, y=310)
        name_inp12=Entry(Frame_Home3,textvariable=n12_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"                  ).place(x=600, y=310, width=270,height=40)
        name_lab16=Label(Frame_Home3, text="Name (As Per Marksheet)    : ", font=('Times New Roman',20), fg="Black", bg="white" ).place(x=230, y=390)
        name_inp16=Entry(Frame_Home3,textvariable=n16_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"                  ).place(x=600, y=390, width=270,height=40)

        name_lab13=Label(Frame_Home3, text="Stream of Exam : ", font=('Times New Roman',20), fg="Black", bg="white" ).place(x=630, y=150)
        name_inp13=Entry(Frame_Home3,textvariable=n13_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"      ).place(x=830, y=150, width=220,height=40)
        name_lab14=Label(Frame_Home3, text="Board Of Exam : ", font=('Times New Roman',20), fg="Black", bg="white"  ).place(x=630, y=230)
        name_inp14=Entry(Frame_Home3,textvariable=n14_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"      ).place(x=830, y=230, width=220,height=40)

        Frame3_btn11=Button(Frame_Home3,command=Past1,text="Save",bd=0,bg="#d77337",fg="white",font=("times new roman",20) ).place(x=340,y=530,width=180,height=50)
        Frame3_btn12=Button(Frame_Home3,command=reset2,text="Reset",bd=0,bg="#d77337",fg="white",font=("times new roman",20)).place(x=540,y=530,width=180,height=50)

#************************************* Current Courses ***********************************
def home_main3():
        Frame_Home4 = Frame(root00, bg="white")
        Frame_Home4.place(x=360, y=120, height=630, width=1130)
        def Current1():
            nc1 = Name2_input.get()
            nc2 = n21_input.get()
            nc3 = n22_input.get()
            nc4 = n23_input.get()
            nc5 = n24_input.get()
            Current(nc1,nc2,nc3,nc4,nc5)
        def reset3():
            n21_input.set("")
            Name2_input.set("-- Select --")
            n22_input.set("-- Select --")
            name_inp23.set("")
            name_inp24.set("")

        frame_head=Label(Frame_Home4, text="Current Course", font=("Times New Roman", 35, "bold"), fg="Black", bg="white").place(x=400, y=10)
        Name2_input=StringVar()
        n21_input=StringVar()
        n22_input=StringVar()
        n23_input=StringVar()
        n24_input=StringVar()
        choices2={'B.E','B.Tech','M.E','M.Tech','B.sc','M.Sc'}
        choices3={'Science','Commerce','Arts'}
        Name2_input.set('Select One')
        n22_input.set('Select One')
        name_lab20=Label(Frame_Home4, text="Stream        : ", font=('Times New Roman',20), fg="Black", bg="white").place(x=100, y=150)
        name_inp20=OptionMenu(Frame_Home4,Name2_input, *choices3  ).place(x=260, y=150, width=220,height=40)
        name_lab21=Label(Frame_Home4, text="University   : ", font=('Times New Roman',20), fg="Black", bg="white" ).place(x=100, y=230)
        name_inp21=Entry(Frame_Home4,textvariable=n21_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"    ).place(x=260, y=230, width=220,height=40)

        name_lab22=Label(Frame_Home4, text="Courses  : ", font=('Times New Roman',20), fg="Black", bg="white").place(x=340, y=330)
        name_inp22=OptionMenu(Frame_Home4,n22_input,*choices2    ).place(x=460, y=330, width=220,height=40)
        name_lab23=Label(Frame_Home4, text="College Name    : ", font=('Times New Roman',20), fg="Black", bg="white"   ).place(x=570, y=150)
        name_inp23=Entry(Frame_Home4,textvariable=n23_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"         ).place(x=810, y=150, width=220,height=40)
        name_lab24=Label(Frame_Home4, text="Duration Of Course : ", font=('Times New Roman',20), fg="Black", bg="white").place(x=570, y=230)
        name_inp24=Entry(Frame_Home4,textvariable=n24_input,font=('Times New Roman',20,'normal'),bg="#FCFFE9"     ).place(x=810, y=230, width=220,height=40)
        Frame3_btn21=Button(Frame_Home4,command=Current1,text="Save",bd=0,bg="#d77337",fg="white",font=("times new roman",20) ).place(x=340,y=530,width=180,height=50)
        Frame3_btn22=Button(Frame_Home4,command=reset3,text="Reset",bd=0,bg="#d77337",fg="white",font=("times new roman",20)).place(x=540,y=530,width=180,height=50)

#************************************** Address Details **********************************
def home_main4():
        Frame_Home5 = Frame(root00, bg="white")
        Frame_Home5.place(x=360, y=120, height=630, width=1130) 
        def Address1():
            na1 = Name3_input.get()
            na2 = n31_input.get()
            na3 = n32_input.get()
            na4 = n33_input.get()
            na5 = n34_input.get()
            na6 = n35_input.get()
            Address(na1,na2,na3,na4,na5,na6)
        def reset4():
            Name3_input.set("")
            n31_input.set("-- Select --")
            n32_input.set("")
            n33_input.set("")
            n34_input.set("")
            n35_input.set("")

        frame_head=Label(Frame_Home5, text="Address Details", font=("Times New Roman", 35, "bold"), fg="Black", bg="white").place(x=400, y=10)
        Name3_input=StringVar()
        n31_input=StringVar()
        n32_input=StringVar()
        n33_input=StringVar()
        n34_input=StringVar()
        n35_input=StringVar()
        choices4={'Maharashtra','Delhi','Haryana','Punjab','Chennai'}
        n31_input.set('Select One')
        choices5={'Mumbai','Pune','Nashik','Nagpur','Aurangabad'}
        n34_input.set('Select One')
        name_lab30=Label(Frame_Home5, text="Line - 1         : ", font=('Times New Roman',20), fg="Black", bg="white" ).place(x=100, y=150)
        name_inp30=Entry(Frame_Home5,textvariable=Name3_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"      ).place(x=270, y=150, width=250,height=40)
        name_lab31=Label(Frame_Home5, text="State             : ", font=('Times New Roman',20), fg="Black", bg="white").place(x=100, y=230)
        name_inp31=OptionMenu(Frame_Home5,n31_input,*choices4                                                         ).place(x=270, y=230, width=250,height=40)
        name_lab32=Label(Frame_Home5, text="Village/City  : ", font=('Times New Roman',20), fg="Black", bg="white"    ).place(x=100, y=310)
        name_inp32=Entry(Frame_Home5,textvariable=n32_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"        ).place(x=270, y=310, width=250,height=40)

        name_lab33=Label(Frame_Home5, text="Line - 2    : ", font=('Times New Roman',20), fg="Black", bg="white" ).place(x=600, y=150)
        name_inp33=Entry(Frame_Home5,textvariable=n33_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"   ).place(x=750, y=150, width=250,height=40)
        name_lab34=Label(Frame_Home5, text="District     : ", font=('Times New Roman',20), fg="Black", bg="white").place(x=600, y=230)
        name_inp34=OptionMenu(Frame_Home5,n34_input ,*choices5                                                   ).place(x=750, y=230, width=250,height=40)
        name_lab35=Label(Frame_Home5, text="Pincode    : ", font=('Times New Roman',20), fg="Black", bg="white"  ).place(x=600, y=310)
        name_inp35=Entry(Frame_Home5,textvariable=n35_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"   ).place(x=750, y=310, width=250,height=40)

        Frame3_btn31=Button(Frame_Home5,command=Address1,text="Save",bd=0,bg="#d77337",fg="white",font=("times new roman",20) ).place(x=340,y=530,width=180,height=50)
        Frame3_btn32=Button(Frame_Home5,command=reset4,text="Reset",bd=0,bg="#d77337",fg="white",font=("times new roman",20)).place(x=540,y=530,width=180,height=50)

#************************************* Available Courses ***********************************
def home_main5():       
        Frame_Home6 = Frame(root00, bg="white")
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
        choices6={'TATA`s Covi-Special','Reliance`s Covi-Special','Goverment Scholarship'}
        n44_input.set('-- Select --')
        
        name_lab40=Label(Frame_Home6, text="Stram Selected  : ", font=('Times New Roman',20), fg="Black", bg="white"  ).place(x=330, y=150)
        name_inp40=Label(Frame_Home6,text=Fetch1(), font=('Times New Roman',20,'normal'),bg="#FCFFE9").place(x=550, y=150, width=220,height=40)

        name_lab41=Label(Frame_Home6, text="Courses   : ", font=('Times New Roman',20), fg="Black", bg="white"    ).place(x=150, y=230)
        name_inp41=Label(Frame_Home6,text=Fetch2(), font=('Times New Roman',20,'normal'),bg="#FCFFE9"  ).place(x=290, y=230, width=220,height=40)

        name_lab44=Label(Frame_Home6, text="Scholarships   : ", font=('Times New Roman',20), fg="Black", bg="white").place(x=570, y=230)
        name_inp44=OptionMenu(Frame_Home6, n44_input,*choices6                                                     ).place(x=760, y=230, width=220,height=40)

        Frame3_btn41=Button(Frame_Home6,command=home_main6,text="Save",bd=0,bg="#d77337",fg="white",font=("times new roman",20) ).place(x=340,y=530,width=180,height=50)
        Frame3_btn42=Button(Frame_Home6,text="Reset",bd=0,bg="#d77337",fg="white",font=("times new roman",20)).place(x=540,y=530,width=180,height=50)

#**************************** Gaurdian Details **************************************
def home_main6():
        Frame_Home7 = Frame(root00, bg="white")
        Frame_Home7.place(x=360, y=120, height=630, width=1130)
        def Gardian1():
            ng1 = Name5_input.get()
            ng2 = n51_input.get()
            ng3 = n52_input.get()
            ng4 = n53_input.get()
            ng5 = n54_input.get()
            Gardian(ng1,ng2,ng3,ng4,ng5) 
        def reset6():
            Name5_input.set("")
            n51_input.set("")
            n52_input.set("")
            n53_input.set("")
            n54_input.set("")
        
        frame_head=Label(Frame_Home7, text="Gaurdians Details", font=("Times New Roman", 35, "bold"), fg="Black", bg="white").place(x=400, y=10)
        Name5_input=StringVar()
        n51_input=StringVar()
        n52_input=StringVar()
        n53_input=StringVar()
        n54_input=StringVar()

        name_lab50=Label(Frame_Home7, text="Gaurdian's Name  : ", font=('Times New Roman',20), fg="Black", bg="white" ).place(x=80, y=150)
        name_inp50=Entry(Frame_Home7,textvariable=Name5_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"      ).place(x=300, y=150, width=220,height=40)
        name_lab51=Label(Frame_Home7, text="Gaurdian's Email  : ", font=('Times New Roman',20), fg="Black", bg="white").place(x=80, y=230)
        name_inp51=Entry(Frame_Home7,textvariable=n51_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"        ).place(x=300, y=230, width=220,height=40)

        name_lab52=Label(Frame_Home7, text="Gaurdian's Address : ", font=('Times New Roman',20), fg="Black", bg="white").place(x=280, y=310)
        name_inp52=Entry(Frame_Home7,textvariable=n52_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"  ).place(x=520, y=310, width=270,height=40)

        name_lab53=Label(Frame_Home7, text="Gaurdian's Relation : ", font=('Times New Roman',20), fg="Black", bg="white"   ).place(x=580, y=150)
        name_inp53=Entry(Frame_Home7,textvariable=n53_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"            ).place(x=830, y=150, width=220,height=40)
        name_lab54=Label(Frame_Home7, text="Gaurdian's Phone    : ", font=('Times New Roman',20), fg="Black", bg="white").place(x=580, y=230)
        name_inp54=Entry(Frame_Home7,textvariable=n54_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"            ).place(x=830, y=230, width=220,height=40)

        Frame3_btn51=Button(Frame_Home7,command=Gardian1,text="Save",bd=0,bg="#d77337",fg="white",font=("times new roman",20) ).place(x=340,y=530,width=180,height=50)
        Frame3_btn52=Button(Frame_Home7,command=reset6,text="Reset",bd=0,bg="#d77337",fg="white",font=("times new roman",20)).place(x=540,y=530,width=180,height=50)

#**************************** RECEIPT Sheet Code **********************************8

def print_slip():
    f = filedialog.asksaveasfilename(filetypes=[('PDf file','*.pdf')],defaultextension='*pdf')
    p = FPDF('p','mm','Letter')
    p.add_page()
    p.set_font('Arial',size=24)
    p.image('schol1.jpg',300,10,12)
    p.cell(160,50,txt='-- RECEIPT --',align='C',ln=True)

    p.cell(120,20,txt='Name                 : ' ,align='C')
    p.cell(30,20,txt='Viraj' ,align='C',ln=True)

    p.cell(120,20,txt='Gaurdian Name  : '      ,align='C')
    p.cell(30,20,txt='Giridhar'      ,align='C',ln=True)

    p.cell(120,20,txt='Email                 : ' ,align='C')
    p.cell(30,20,txt='viraj25@gmail.com' ,align='C',ln=True)

    p.cell(120,20,txt='Aadhar No.       : '      ,align='C')
    p.cell(30,20,txt='123456'      ,align='C',ln=True)

    p.cell(120,20,txt='Sholarship          : '  ,align='C')
    p.cell(30,20,txt='TATA`s Covi-Special'  ,align='C',ln=True)

    p.cell(120,20,txt='Course              : '  ,align='C')
    p.cell(30,20,txt='B.E'  ,align='C',ln=True)

    p.cell(120,20,txt='College             : '  ,align='C')
    p.cell(30,20,txt='SFIT'  ,align='C',ln=True)

    p.output(f)
    login()

def Fetch01():
    con = pymysql.connect(host='localhost', user='root', password='LordTesla77', database='Scholarship')
    cur = con.cursor()
    cur.execute('Select * from Personal')
    give = cur.fetchall()
    for c1 in give:
            give = c1[0]
            return give
    

def Fetch02():
    con = pymysql.connect(host='localhost', user='root', password='LordTesla77', database='Scholarship')
    cur = con.cursor()
    cur.execute('Select * from Gaurdians')
    give = cur.fetchall()
    for c1 in give:
            give = c1[0]
            return give

def Fetch03():
    con = pymysql.connect(host='localhost', user='root', password='LordTesla77', database='Scholarship')
    cur = con.cursor()
    cur.execute('Select * from Personal')
    give = cur.fetchall()
    for c1 in give:
            give = c1[1]
            return give

def Fetch04():
    con = pymysql.connect(host='localhost', user='root', password='LordTesla77', database='Scholarship')
    cur = con.cursor()
    cur.execute('Select * from Personal')
    give = cur.fetchall()
    for c1 in give:
            give = c1[3]
            return give  

def Fetch05():
    con = pymysql.connect(host='localhost', user='root', password='LordTesla77', database='Scholarship')
    cur = con.cursor()
    cur.execute('Select * from Current')
    give = cur.fetchall()
    for c1 in give:
            give = c1[0]
            return give  


def Fetch06():
    con = pymysql.connect(host='localhost', user='root', password='LordTesla77', database='Scholarship')
    cur = con.cursor()
    cur.execute('Select * from Current')
    give = cur.fetchall()
    for c1 in give:
            give = c1[3]
            return give  

def Fetch07():
    con = pymysql.connect(host='localhost', user='root', password='LordTesla77', database='Scholarship')
    cur = con.cursor()
    cur.execute('Select * from Current')
    give = cur.fetchall()
    for c1 in give:
            give = c1[2]
            return give

def Receipt():
    Frame_receipts=Frame(root00,bg="white")
    Frame_receipts.place(x=360, y=120, height=630, width=1130)

    rec_head=Label(Frame_receipts, text="-- Receipts --", font=("Impact", 35, "bold"), fg="Black", bg="white"    ).place(x=450, y=15)

    rev_lable1=Label(Frame_receipts, text="Name                      : ", font=("Times new roman", 20, "bold"), fg="Black", bg="white" ).place(x=280, y=130)
    rev_lable2=Label(Frame_receipts, text="Gaurdian Name     : ", font=("Times new roman", 20, "bold"), fg="Black", bg="white"         ).place(x=280, y=190)
    rev_lable3=Label(Frame_receipts, text="Email                      : ", font=("Times new roman", 20, "bold"), fg="Black", bg="white").place(x=280, y=250)
    rev_lable4=Label(Frame_receipts, text="Aadhar                   : ", font=("Times new roman", 20, "bold"), fg="Black", bg="white"  ).place(x=280, y=310)
    rev_lable6=Label(Frame_receipts, text="Scholarship Name : ", font=("Times new roman", 20, "bold"), fg="Black", bg="white"          ).place(x=280, y=370)
    rev_lable7=Label(Frame_receipts, text="Course                    : ", font=("Times new roman", 20, "bold"), fg="Black", bg="white" ).place(x=280, y=430)
    rev_lable8=Label(Frame_receipts, text="College                   : ", font=("Times new roman", 20, "bold"), fg="Black", bg="white" ).place(x=280, y=490)

    name_rec1=Label(Frame_receipts,text=Fetch01(),font=('Times New Roman',18,'normal'),bg="#FCFFE9"    ).place(x=600, y=130, width=250,height=30)
    name_rec2=Label(Frame_receipts,text=Fetch02(),font=('Times New Roman',18,'normal'),bg="#FCFFE9"    ).place(x=600, y=190, width=250,height=30)
    name_rec2=Label(Frame_receipts,text=Fetch03(),font=('Times New Roman',18,'normal'),bg="#FCFFE9"    ).place(x=600, y=250, width=250,height=30)
    name_rec3=Label(Frame_receipts,text=Fetch04(),font=('Times New Roman',18,'normal'),bg="#FCFFE9"    ).place(x=600, y=310, width=250,height=30)
    name_rec4=Label(Frame_receipts,text=Fetch05(),font=('Times New Roman',18,'normal'),bg="#FCFFE9"    ).place(x=600, y=370, width=250,height=30)
    name_rec5=Label(Frame_receipts,text=Fetch06(),font=('Times New Roman',18,'normal'),bg="#FCFFE9"    ).place(x=600, y=430, width=250,height=30)
    name_re6c=Label(Frame_receipts,text=Fetch07(),font=('Times New Roman',18,'normal'),bg="#FCFFE9"    ).place(x=600, y=490, width=250,height=30)

    print_btn=Button(Frame_receipts,command=print_slip,text="Print",bd=0,bg="#d77337",fg="white",font=("times new roman",20)).place(x=480,y=550,width=180,height=50)

def menu_frame():
        Frame_Home1 = Frame(root00, bg="white")
        Frame_Home1.place(x=50, y=120, height=630, width=300)
        #************************* Menu Buttons Declaration ********************************
        #Buttons Declaration
        Frame_2_lab=Label(Frame_Home1,text="Forms List",bd=0,bg="white",fg="#d77337",font=("times new roman",30,"bold")).place(x=55,y=25)
        Frame_1=Button(Frame_Home1,command=home_main1,text="Personal Details",bd=0,bg="#d77337",fg="white",font=("times new roman",20)).place(x=35,y=110,width=230,height=50)
        Frame_2=Button(Frame_Home1,command=home_main2 ,text="Qualifiaction",bd=0,bg="#d77337",fg="white",font=("times new roman",20)).place(x=35,y=200,width=230,height=50)
        Frame_3=Button(Frame_Home1,command=home_main3,text="Current Course",bd=0,bg="#d77337",fg="white",font=("times new roman",20)   ).place(x=35,y=290,width=230,height=50)
        Frame_4=Button(Frame_Home1,command=home_main4,text="Address Details",bd=0,bg="#d77337",fg="white",font=("times new roman",20)  ).place(x=35,y=380,width=230,height=50)
        Frame_5=Button(Frame_Home1,command=home_main5,text="Scholarships",bd=0,bg="#d77337",fg="white",font=("times new roman",20) ).place(x=35,y=470,width=230,height=50)
        Frame_6=Button(Frame_Home1,command=home_main6,text="Gaurdian Details",bd=0,bg="#d77337",fg="white",font=("times new roman",20)    ).place(x=35,y=560,width=230,height=50)


welcome()
root00.mainloop()