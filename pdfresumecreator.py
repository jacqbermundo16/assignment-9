# import pdf library and json module
import json
from fpdf import FPDF

# open and read the json file
data = open('cvdetails.json')
jsonData = data.read()
obj = json.loads(jsonData)
# check if you can access the data 
for i in obj:
    print(i)
# add a page for pdf
# set font size and style
# add image: set location and size
# test if it can print the data in the json file