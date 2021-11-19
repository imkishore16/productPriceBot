import openpyxl,os
import product_Input

os.chdir('c:\\Users\\imkar\\Documents')

wb=openpyxl.load_workbook('product_Input.xlsx')
sheet=wb.get_sheet_by_name('Sheet1')
sheet['A1'].value
sheet['B1'].value
