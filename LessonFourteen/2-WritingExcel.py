# install openpyxl in setting first
import openpyxl

file = "/LessonFourteen\\data1.xlsx"

workbook = openpyxl.load_workbook(file)
sheet = workbook["Sheet1"]
# sheet = workbook.active

# writing to excel

for r in range(1, 6):
    for c in range(1, 4):
        sheet.cell(r, c).value = 'welcome'

workbook.save(file)
