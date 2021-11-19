import openpyxl

path='D:\\'


def getInput():
    product_url=input("enter your product url :   ")
    # element_selector = input("input css selector of the price tag :   ")
    return product_url

#write a function that add the input into an excel sheet
def getProduct():
    input_arr=[]
    input_arr.append(getInput())
    # workbook=openpyxl.load_workbook('product_Input.xlsx')
    # sheet=workbook.get_sheet_by_name('Sheet1')

    wb = openpyxl.load_workbook(path+'product_Input.xlsx')
    ws = wb.active
    #sheet['A1']=product_url

    ws.append(input_arr)

    wb.save(path+'product_Input.xlsx')

getProduct()
# https://www.amazon.in/BAGHADBILLO-Unisex-Hoodies-B-W-NARUTO-BLACK-40_Black_Medium/dp/B08L5BB2XX/ref=sr_1_omk_6?keywords=hoodie&qid=1636544022&sr=8-6




