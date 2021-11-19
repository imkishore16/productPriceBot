import openpyxl
import os

os.chdir('c:\\Users\\imkar\\Documents')


def Input():
    product_url=input("enter your product url :   ")
    element_selector = input("input css selector of the price tag :   ")

#write a function that add the input into an excel sheet
def getProduct():
    Input()
    workbook=openpyxl.load_workbook('product_input.xlsx')
    sheet=workbook.get_sheet_by_name('Sheet1')

    sheet['A1']=product_url
    sheet['B1']=element_selector
    # for i in range(10):
    #     sheet["".join(['A',i])]=product_url
    #
    # for i in range(10):
    #     sheet["".join(['B', i])] =element_selector
    os.chdir('c:\\Users\\imkar\\Documents')
    workbook.save

getProduct()
# https://www.amazon.in/BAGHADBILLO-Unisex-Hoodies-B-W-NARUTO-BLACK-40_Black_Medium/dp/B08L5BB2XX/ref=sr_1_omk_6?keywords=hoodie&qid=1636544022&sr=8-6
# #priceblock_ourprice