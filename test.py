import requests
from bs4 import BeautifulSoup
import csv
link='https://market.isagha.com/prices'

gold_details=[]
def main_code():

    page=requests.get(link)
    soup=BeautifulSoup(page.text,'html.parser')
    golds=soup.find_all('div',{'class':'col-sm-12'})
    for g in golds:
        gauage=g.find('span').text
        sell_value=g.find_all('div',{'class':'value'})[0].text
        buy_value=g.find_all('div',{'class':'value'})[1].text
        status_value=g.find_all('div',{'class':'value'})[2].text
        status=g.find_all('div',{'class':'state'})[2].text

        gold_details.append(
            {
                'العيار':gauage,
                'سعر البيع':sell_value,
                'سعر الشراء':buy_value,
                'الحالة':status,
                'السعر':status_value
            })

def printing():
    header=gold_details[0].keys()
    path='D:\Data analysis\Web Scrabing.csv'
    with open(path,'w',encoding='utf-8',newline='') as file:
        writer = csv.DictWriter(file,header)
        writer.writeheader()
        writer.writerows(gold_details)
        print('file saved')

main_code()
printing()