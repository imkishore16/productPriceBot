import sys

import openpyxl
import os
import requests
import bs4
path="D:\\"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def parse_url(url):
    html=requests.get(url,headers=headers)
    soup = bs4.BeautifulSoup(html.text, 'html.parser')
    elems = soup.find('div', {'class' : '_30jeq3 _16Jk6d'})
    # elems = soup.find('span', id='priceblock_ourprice')
    # elems=soup.select('_30jeq3 _16Jk6d')
    #elems = soup.find('class', id='_30jeq3 _16Jk6d')
    # elems=soup.find('class','#container > div > div._2c7YLP.UtUXW0._6t1WkM._3HqJxg > div._1YokD2._2GoDe3 > div._1YokD2._3Mn1Gg.col-8-12 > div:nth-child(2) > div > div.dyC4hf > div.CEmiEU > div > div._30jeq3._16Jk6d')
    print(elems.text)
    #print(elems[0].text.strip())




def parse_xl():
    workbook = openpyxl.load_workbook(path + 'product_Input.xlsx')
    ws = workbook.active
    for i in range(sys.maxsize**10):
        cell='A'+str(i+1)
        url=ws[cell].value
        if(url is None):
            break
        parse_url(url)

parse_xl()




