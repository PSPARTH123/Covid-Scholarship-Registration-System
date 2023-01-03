from fpdf import FPDF
from tkinter import filedialog
from tkinter import *

f = filedialog.asksaveasfilename(filetypes=[('PDf file','*.pdf')],defaultextension='*pdf')
p = FPDF('p','mm','Letter')
p.add_page()
p.set_font('Arial',size=24)
p.image('schol1.jpg',300,10,12)
p.cell(160,50,txt='-- RECEIPT --',align='C',ln=True)

p.cell(120,20,txt='Name                 : ' ,align='C')
p.cell(30,20,txt='Name               : ' ,align='C',ln=True)

p.cell(120,20,txt='Gaurdian Name  : '      ,align='C')
p.cell(30,20,txt='Gaurdian Name : '      ,align='C',ln=True)

p.cell(120,20,txt='Email                 : ' ,align='C')
p.cell(30,20,txt='Email              : ' ,align='C',ln=True)

p.cell(120,20,txt='Aadhar No.       : '      ,align='C')
p.cell(30,20,txt='Aadhar No.    : '      ,align='C',ln=True)

p.cell(120,20,txt='Sholarship          : '  ,align='C')
p.cell(30,20,txt='Sholarship        : '  ,align='C',ln=True)

p.cell(120,20,txt='Course              : '  ,align='C')
p.cell(30,20,txt='Course            : '  ,align='C',ln=True)

p.cell(120,20,txt='College             : '  ,align='C')
p.cell(30,20,txt='College           : '  ,align='C',ln=True)

p.output(f)
