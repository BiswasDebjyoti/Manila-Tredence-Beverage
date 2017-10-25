import requests
from bs4 import BeautifulSoup
import xlwt
#This is for educational purposes only I dont have the permission to use their data for commercial use
count = 0

#create a spreadsheet file
wb=xlwt.Workbook()
#create a sheet


ws = wb.add_sheet(i+' City')
url="https://en.yelp.com.ph/search?find_desc=Grocery&find_loc=Makati,+Metro+Manila&start="
for x in range(0,600,10):
    _url=url+str(x)
    r = requests.get(_url)
        #create a BS instance using the request data
    soup = BeautifulSoup(r.content,"lxml")
        
    g_data = soup.find_all("div",{"class":"search-result natural-search-result"})
    for item in g_data:
        name=item.contents[1].contents[1].contents[1].contents[3].contents[1].contents[1].contents[1].text
        addr =None
            
        try:
            phn=str(item.contents[1].contents[3].contents[7].text)
            phn=str(phn.replace('\n            ','',1))
            phn=phn.strip("\n    ")
        except:
            continue
        try:
            addr=item.contents[1].contents[3].contents[3].text
            addr=str(addr.replace('\n            ','',1))
            addr=addr.strip("\n    ")
        except:
            continue
        try:
            city=str(item.contents[1].contents[3].contents[1].text)
            city=str(city.replace('\n        ','',1))
            city=city.strip("        ")
        except:
            continue
            #print addr
            
        if city == 'Makati City':
            #print i
            print name
            if addr=='Makati City':
                
                count = count + 1
                #ws=wb.get_sheet(i+' City')
                ws.write(count-1,0,name)
                ws.write(count-1,1,city)
                ws.write(count-1,2,addr)
                ws.write(count-1,3,phn)
        
        wb.save("/home/debjyoti/Desktop/Manila-Tredence-Beverage/xls_files/BeveragesYelpData.xls")   



    
 
