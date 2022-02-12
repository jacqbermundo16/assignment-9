# import pdf library and json module
import json
from fpdf import FPDF
pdf = FPDF()

# add a page for pdf
pdf.add_page()

# set font size and style
pdf.set_font('Arial','B', size=16, ) 

# open and read the json file
data = open('cvdetails.json')
jsonData = data.read()
obj = json.loads(jsonData)
# check if you can access the data 
# test if it can print the data in the json file
# put the first set on info (personal info)
perInfo1 = [obj['PERSONAL INFO']]
for h in perInfo1:
    name_ = h[0]
    pdf.cell(200,8, txt = name_, ln=1, align='L')
    address_ = h[1]
    pdf.set_font_size(size=10)
    pdf.cell(200,5, txt = address_, ln=1, align='L')
    contact_ = h[2]
    pdf.cell(200,5, txt = contact_, ln=1, align='L')
    email_ = h[3]
    pdf.cell(200,5, txt = email_, ln=1, align='L')

# add the other infos
pdf.cell(200,5, txt = " ", ln=1, align='L')

objective = [obj['OBJECTIVE']]
for i in objective:
    title_ = i[0]
    pdf.set_font_size(size=12)
    pdf.cell(20,5, txt = title_, ln=1, align='L')
    objective1_ = i[1]
    pdf.set_font_size(size=10)
    pdf.cell(200,5, txt = objective1_, ln=1, align='L')
    objective2_ = i[2]
    pdf.cell(200,5, txt = objective2_, ln=1, align='L')
    objective3_ = i[3]
    pdf.cell(200,5, txt = objective3_, ln=1, align='L')

pdf.cell(200,5, txt = " ", ln=1, align='L')

perInfo2 = [obj['PERSONAL INFORMATION']]
for j in perInfo2:
    title_ = j[0]
    pdf.set_font_size(size=12)
    pdf.cell(200,8, txt = title_, ln=1, align='L')
    bday_ = j[1]
    pdf.set_font_size(size=10)
    pdf.cell(200,5, txt = bday_, ln=1, align='L')
    age_ = j[2]
    pdf.cell(200,5, txt = age_, ln=1, align='L')
    bplace_ = j[3]
    pdf.cell(200,5, txt = bplace_, ln=1, align='L')
    civil_ = j[4]
    pdf.cell(200,5, txt = civil_, ln=1, align='L')
    cit_ = j[5]
    pdf.cell(200,5, txt = cit_, ln=1, align='L')
    rel_ = j[6]
    pdf.cell(200,5, txt = rel_, ln=1, align='L')

pdf.cell(200,5, txt = " ", ln=1, align='L')

educBG = [obj['EDUCATIONAL BACKGROUND']]
for k in educBG:
    title_ = k[0]
    pdf.set_font_size(size=12)
    pdf.cell(200,8, txt = title_, ln=1, align='L')
    subtitle1_ = k[1]
    pdf.set_font_size(size=10)
    pdf.cell(200,8, txt = subtitle1_, ln=1, align='L')
    school1_ = k[2]
    pdf.cell(200,5, txt = school1_, ln=1, align='L')
    degree_ = k[3]
    pdf.cell(200,5, txt = degree_, ln=1, align='L')
    sy1_ = k[4]
    pdf.cell(200,5, txt = sy1_, ln=1, align='L')
    subtitle2_ = k[5]
    pdf.cell(200,8, txt = subtitle2_, ln=1, align='L')
    school2_ = k[6]
    pdf.cell(200,5, txt = school2_, ln=1, align='L')
    sy2_ = k[7]
    pdf.cell(200,5, txt = sy2_, ln=1, align='L')
    subtitle3_ = k[8]
    pdf.cell(200,8, txt = subtitle3_, ln=1, align='L')
    school3_ = k[9]
    pdf.cell(200,5, txt = school3_, ln=1, align='L')
    sy3_ = k[10]
    pdf.cell(200,5, txt = sy3_, ln=1, align='L')

pdf.cell(200,5, txt = " ", ln=1, align='L')

workEx = [obj['WORK EXPERIENCE']]
for l in workEx:
    title_ = l[0]
    pdf.set_font_size(size=12)
    pdf.cell(200,8, txt = title_, ln=1, align='L')
    job_ = l[1]
    pdf.set_font_size(size=10)
    pdf.cell(200,5, txt = job_, ln=1, align='L')
    company_ = l[2]
    pdf.cell(200,5, txt = company_, ln=1, align='L')
    employment_ = l[3]
    pdf.cell(200,5, txt = employment_, ln=1, align='L')

pdf.cell(200,5, txt = " ", ln=1, align='L')

skills = [obj['SKILLS']]
for m in skills:
    title_ = m[0]
    pdf.set_font_size(size=12)
    pdf.cell(200,8, txt = title_, ln=1, align='L')
    s1_ = m[1]
    pdf.set_font_size(size=10)
    pdf.cell(200,5, txt = s1_, ln=1, align='L')
    s2_ = m[2]
    pdf.cell(200,5, txt = s2_, ln=1, align='L')
    s3_ = m[3]
    pdf.cell(200,5, txt = s3_, ln=1, align='L')
    s4_ = m[4]
    pdf.cell(200,5, txt = s4_, ln=1, align='L')
    s5_ = m[5]
    pdf.cell(200,5, txt = s5_, ln=1, align='L')
    s6_ = m[6]
    pdf.cell(200,5, txt = s6_, ln=1, align='L')
# add image: set location and size

#save as pdf
pdf.output('BERMUNDO_JACQUELINE.pdf')
