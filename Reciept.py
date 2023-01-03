from ast import Lambda
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk
from fpdf import FPDF
import pymysql

root0=Tk()
root0.title("Register-Page")
root0.geometry("1920x1080+0+0")
root0.state('zoomed')

bg = ImageTk.PhotoImage(file="schol1.jpg")
bg_image = Label(root0, image=bg).place(x=0, y=0, relwidth=1, relheight=1)

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

def print_slip():
    
    # inp1=Fetch01()
    # inp2=Fetch02()
    # inp3=Fetch03()
    # inp4=Fetch04()
    # inp5=Fetch05()
    # inp6=Fetch06()
    # inp7=Fetch07()

    f = filedialog.asksaveasfilename(filetypes=[('PDf file','*.pdf')],defaultextension='*pdf')
    p = FPDF('p','mm','Letter')
    p.add_page()
    p.set_font('Arial',size=24)
    p.image('schol1.jpg',300,10,12)
    p.cell(160,50,txt='-- RECEIPT --',align='C',ln=True)
    p.cell(120,20,txt='Name                 : ' ,align='C')
    p.cell(30,20,txt=Fetch01(),align='C',ln=True)

    p.cell(120,20,txt='Gaurdian Name  : '      ,align='C')
    p.cell(30,20,txt=Fetch02(),align='C',ln=True)

    p.cell(120,20,txt='Email                 : ' ,align='C')
    p.cell(30,20,txt=Fetch03(),align='C',ln=True)

    p.cell(120,20,txt='Aadhar No.       : '      ,align='C')
    p.cell(30,20,txt=Fetch04,align='C',ln=True)

    p.cell(120,20,txt='Sholarship          : '  ,align='C')
    p.cell(30,20,txt=Fetch05(),align='C',ln=True)

    p.cell(120,20,txt='Course              : '  ,align='C')
    p.cell(30,20,text=Fetch06(),align='C',ln=True)

    p.cell(120,20,txt='College             : '  ,align='C')
    p.cell(30,20,txt=Fetch07(),align='C',ln=True)
    p.output(f)

def Receipt():
    Frame_receipts=Frame(root0,bg="white")
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

Receipt()
root0.mainloop()