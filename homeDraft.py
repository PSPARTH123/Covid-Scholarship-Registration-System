# creating Frame
Frame_Home0 = Frame(root, bg="white")
Frame_Home0.place(x=50, y=10, height=100, width=1440)

Frame_Home1 = Frame(root, bg="white")
Frame_Home1.place(x=50, y=120, height=630, width=300)

Frame_Home5 = Frame(root, bg="white")
Frame_Home5.place(x=360, y=120, height=630, width=1130)

Frame_Home6 = Frame(root, bg="white")
Frame_Home6.place(x=360, y=120, height=630, width=1130)

Frame_Home4 = Frame(root, bg="white")
Frame_Home4.place(x=360, y=120, height=630, width=1130)



Frame_Home3 = Frame(root, bg="white")
Frame_Home3.place(x=360, y=120, height=630, width=1130)

Frame_Home7 = Frame(root, bg="white")
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





#Frame Past Qualification - 11111111
#Detail Frame Header 
frame_head=Label(Frame_Home3, text="Past Qualification", font=("Times New Roman", 35, "bold"), fg="Black", bg="white").place(x=400, y=10)
Name1_input=StringVar()
n11_input=StringVar()
n12_input=StringVar()
n13_input=StringVar()
n14_input=StringVar()
# n15_input=StringVar()
n16_input=StringVar()
# n17_input=StringVar()
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
#Left Side lables and entry ends
name_lab13=Label(Frame_Home3, text="Stream of Exam : ", font=('Times New Roman',20), fg="Black", bg="white" ).place(x=630, y=150)
name_inp13=Entry(Frame_Home3,textvariable=n13_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"      ).place(x=830, y=150, width=220,height=40)
name_lab14=Label(Frame_Home3, text="Board Of Exam : ", font=('Times New Roman',20), fg="Black", bg="white"  ).place(x=630, y=230)
name_inp14=Entry(Frame_Home3,textvariable=n14_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"      ).place(x=830, y=230, width=220,height=40)
# name_lab15=Label(Frame_Home3, text="Mother Name  : ", font=('Times New Roman',20), fg="Black", bg="white"   ).place(x=570, y=310)
# name_inp15=Entry(Frame_Home3,textvariable=n15_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"      ).place(x=760, y=310, width=220,height=40)
# name_lab17=Label(Frame_Home3, text="Name5 : ", font=('Times New Roman',20), fg="Black", bg="white"          ).place(x=570, y=390)
# name_inp17=Entry(Frame_Home3,textvariable=n17_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"      ).place(x=760, y=390, width=220,height=40)

Frame3_btn11=Button(Frame_Home3,text="Save",bd=0,bg="#d77337",fg="white",font=("times new roman",20) ).place(x=340,y=530,width=180,height=50)
Frame3_btn12=Button(Frame_Home3,text="Reset",bd=0,bg="#d77337",fg="white",font=("times new roman",20)).place(x=540,y=530,width=180,height=50)

#Frame Current Course - 2222222
#Detail Frame Header 
frame_head=Label(Frame_Home4, text="Current Course", font=("Times New Roman", 35, "bold"), fg="Black", bg="white").place(x=400, y=10)
Name2_input=StringVar()
n21_input=StringVar()
n22_input=StringVar()
n23_input=StringVar()
n24_input=StringVar()
# n25_input=StringVar()
# n26_input=StringVar()
# n27_input=StringVar()
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
# name_lab26=Label(Frame_Home4, text="Name5      : ", font=('Times New Roman',20), fg="Black", bg="white"       ).place(x=100, y=390)
# name_inp26=Entry(Frame_Home4,textvariable=n26_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"   ).place(x=260, y=390, width=220,height=40)
#Left Side lables and entry ends
name_lab23=Label(Frame_Home4, text="College Name    : ", font=('Times New Roman',20), fg="Black", bg="white"   ).place(x=570, y=150)
name_inp23=Entry(Frame_Home4,textvariable=n23_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"         ).place(x=810, y=150, width=220,height=40)
name_lab24=Label(Frame_Home4, text="Duration Of Course : ", font=('Times New Roman',20), fg="Black", bg="white").place(x=570, y=230)
name_inp24=Entry(Frame_Home4,textvariable=n24_input,font=('Times New Roman',20,'normal'),bg="#FCFFE9"     ).place(x=810, y=230, width=220,height=40)
# name_lab25=Label(Frame_Home4, text="Mother Name  : ", font=('Times New Roman',20), fg="Black", bg="white"      ).place(x=570, y=310)
# name_inp25=Entry(Frame_Home4,textvariable=n25_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"         ).place(x=810, y=310, width=220,height=40)
# name_lab27=Label(Frame_Home4, text="Name5 : ", font=('Times New Roman',20), fg="Black", bg="white"             ).place(x=570, y=390)
# name_inp27=Entry(Frame_Home4,textvariable=n27_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"         ).place(x=760, y=390, width=220,height=40)

Frame3_btn21=Button(Frame_Home4,text="Save",bd=0,bg="#d77337",fg="white",font=("times new roman",20) ).place(x=340,y=530,width=180,height=50)
Frame3_btn22=Button(Frame_Home4,text="Reset",bd=0,bg="#d77337",fg="white",font=("times new roman",20)).place(x=540,y=530,width=180,height=50)

#Frame Address Details - 3333333
#Detail Frame Header 
frame_head=Label(Frame_Home5, text="Address Details", font=("Times New Roman", 35, "bold"), fg="Black", bg="white").place(x=400, y=10)
Name3_input=StringVar()
n31_input=StringVar()
n32_input=StringVar()
n33_input=StringVar()
n34_input=StringVar()
n35_input=StringVar()
# n36_input=StringVar()
# n37_input=StringVar()
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
# name_lab36=Label(Frame_Home5, text="Name5 : ", font=('Times New Roman',20), fg="Black", bg="white"      ).place(x=180, y=390)
# name_inp36=Entry(Frame_Home5,textvariable=n36_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"  ).place(x=290, y=390, width=220,height=40)
#Left Side lables and entry ends
name_lab33=Label(Frame_Home5, text="Line - 2    : ", font=('Times New Roman',20), fg="Black", bg="white" ).place(x=600, y=150)
name_inp33=Entry(Frame_Home5,textvariable=n33_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"   ).place(x=750, y=150, width=250,height=40)
name_lab34=Label(Frame_Home5, text="District     : ", font=('Times New Roman',20), fg="Black", bg="white").place(x=600, y=230)
name_inp34=OptionMenu(Frame_Home5,n34_input ,*choices5                                                   ).place(x=750, y=230, width=250,height=40)
name_lab35=Label(Frame_Home5, text="Pincode    : ", font=('Times New Roman',20), fg="Black", bg="white"  ).place(x=600, y=310)
name_inp35=Entry(Frame_Home5,textvariable=n35_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"   ).place(x=750, y=310, width=250,height=40)
# name_lab37=Label(Frame_Home5, text="Name5 : ", font=('Times New Roman',20), fg="Black", bg="white"          ).place(x=570, y=390)
# name_inp37=Entry(Frame_Home5,textvariable=n37_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"      ).place(x=760, y=390, width=220,height=40)

Frame3_btn31=Button(Frame_Home5,text="Save",bd=0,bg="#d77337",fg="white",font=("times new roman",20) ).place(x=340,y=530,width=180,height=50)
Frame3_btn32=Button(Frame_Home5,text="Reset",bd=0,bg="#d77337",fg="white",font=("times new roman",20)).place(x=540,y=530,width=180,height=50)

#Frame Available Courses - 4444444
#Detail Frame Header 
frame_head=Label(Frame_Home6, text="Available Courses", font=("Times New Roman", 35, "bold"), fg="Black", bg="white").place(x=400, y=10)
Name4_input=StringVar()
n41_input=StringVar()
n42_input=StringVar()
n43_input=StringVar()
n44_input=StringVar()
n45_input=StringVar()
n46_input=StringVar()
n47_input=StringVar()
name_lab40=Label(Frame_Home6, text="Name   : ", font=('Times New Roman',20), fg="Black", bg="white"     ).place(x=180, y=150)
name_inp40=Entry(Frame_Home6,textvariable=Name4_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9").place(x=290, y=150, width=220,height=40)
name_lab41=Label(Frame_Home6, text="Email   : ", font=('Times New Roman',20), fg="Black", bg="white"    ).place(x=180, y=230)
name_inp41=Entry(Frame_Home6,textvariable=n41_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"  ).place(x=290, y=230, width=220,height=40)
name_lab42=Label(Frame_Home6, text="Phone  : ", font=('Times New Roman',20), fg="Black", bg="white"     ).place(x=180, y=310)
name_inp42=Entry(Frame_Home6,textvariable=n42_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"  ).place(x=290, y=310, width=220,height=40)
name_lab46=Label(Frame_Home6, text="Name5 : ", font=('Times New Roman',20), fg="Black", bg="white"      ).place(x=180, y=390)
name_inp46=Entry(Frame_Home6,textvariable=n46_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"  ).place(x=290, y=390, width=220,height=40)
#Left Side lables and entry ends
name_lab43=Label(Frame_Home6, text="Last Name      : ", font=('Times New Roman',20), fg="Black", bg="white" ).place(x=570, y=150)
name_inp43=Entry(Frame_Home6,textvariable=n43_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"      ).place(x=760, y=150, width=220,height=40)
name_lab44=Label(Frame_Home6, text="Father Name   : ", font=('Times New Roman',20), fg="Black", bg="white"  ).place(x=570, y=230)
name_inp44=Entry(Frame_Home6,textvariable=n44_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"      ).place(x=760, y=230, width=220,height=40)
name_lab45=Label(Frame_Home6, text="Mother Name  : ", font=('Times New Roman',20), fg="Black", bg="white"   ).place(x=570, y=310)
name_inp45=Entry(Frame_Home6,textvariable=n45_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"      ).place(x=760, y=310, width=220,height=40)
name_lab47=Label(Frame_Home6, text="Name5 : ", font=('Times New Roman',20), fg="Black", bg="white"          ).place(x=570, y=390)
name_inp47=Entry(Frame_Home6,textvariable=n47_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"      ).place(x=760, y=390, width=220,height=40)

Frame3_btn41=Button(Frame_Home6,text="Save",bd=0,bg="#d77337",fg="white",font=("times new roman",20) ).place(x=340,y=530,width=180,height=50)
Frame3_btn42=Button(Frame_Home6,text="Reset",bd=0,bg="#d77337",fg="white",font=("times new roman",20)).place(x=540,y=530,width=180,height=50)

#Frame Gaurdians Details - 555555
#Detail Frame Header 
frame_head=Label(Frame_Home7, text="Gaurdians Details", font=("Times New Roman", 35, "bold"), fg="Black", bg="white").place(x=400, y=10)
Name5_input=StringVar()
n51_input=StringVar()
n52_input=StringVar()
n53_input=StringVar()
n54_input=StringVar()
# n55_input=StringVar()
# n56_input=StringVar() 
# n57_input=StringVar()
name_lab50=Label(Frame_Home7, text="Gaurdian's Name  : ", font=('Times New Roman',20), fg="Black", bg="white" ).place(x=80, y=150)
name_inp50=Entry(Frame_Home7,textvariable=Name5_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"      ).place(x=300, y=150, width=220,height=40)
name_lab51=Label(Frame_Home7, text="Gaurdian's Email  : ", font=('Times New Roman',20), fg="Black", bg="white").place(x=80, y=230)
name_inp51=Entry(Frame_Home7,textvariable=n51_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"        ).place(x=300, y=230, width=220,height=40)

name_lab52=Label(Frame_Home7, text="Gaurdian's Address : ", font=('Times New Roman',20), fg="Black", bg="white").place(x=280, y=310)
name_inp52=Entry(Frame_Home7,textvariable=n52_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"  ).place(x=520, y=310, width=270,height=40)
# name_lab56=Label(Frame_Home7, text="Name5 : ", font=('Times New Roman',20), fg="Black", bg="white"      ).place(x=180, y=390)
# name_inp56=Entry(Frame_Home7,textvariable=n56_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"  ).place(x=290, y=390, width=220,height=40)
#Left Side lables and entry ends
name_lab53=Label(Frame_Home7, text="Gaurdian's Relation : ", font=('Times New Roman',20), fg="Black", bg="white"   ).place(x=580, y=150)
name_inp53=Entry(Frame_Home7,textvariable=n53_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"            ).place(x=830, y=150, width=220,height=40)
name_lab54=Label(Frame_Home7, text="Gaurdian's Phone    : ", font=('Times New Roman',20), fg="Black", bg="white").place(x=580, y=230)
name_inp54=Entry(Frame_Home7,textvariable=n54_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"            ).place(x=830, y=230, width=220,height=40)
# name_lab55=Label(Frame_Home7, text="Mother Name  : ", font=('Times New Roman',20), fg="Black", bg="white"         ).place(x=570, y=310)
# name_inp55=Entry(Frame_Home7,textvariable=n55_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"            ).place(x=760, y=310, width=220,height=40)
# name_lab57=Label(Frame_Home7, text="Name5 : ", font=('Times New Roman',20), fg="Black", bg="white"          ).place(x=570, y=390)
# name_inp57=Entry(Frame_Home7,textvariable=n57_input ,font=('Times New Roman',20,'normal'),bg="#FCFFE9"      ).place(x=760, y=390, width=220,height=40)

Frame3_btn51=Button(Frame_Home7,text="Save",bd=0,bg="#d77337",fg="white",font=("times new roman",20) ).place(x=340,y=530,width=180,height=50)
Frame3_btn52=Button(Frame_Home7,text="Reset",bd=0,bg="#d77337",fg="white",font=("times new roman",20)).place(x=540,y=530,width=180,height=50)
