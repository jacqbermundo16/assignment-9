# import pdf library and json module
import json
from fpdf import FPDF
pdf = FPDF()

# add a page for pdf
pdf.add_page()

# set font size and style
pdf.set_font('Arial', size=10, ) 

# open and read the json file
data = open('cvdetails.json')
jsonData = data.read()
obj = json.loads(jsonData)
# check if you can access the data 
for i in obj:
    
# test if it can print the data in the json file

    pdf.cell(200,5, txt = i , ln=1, align='L')

# add image: set location and size

#save as pdf
pdf.output('BERMUNDO_JACQUELINE.pdf')
