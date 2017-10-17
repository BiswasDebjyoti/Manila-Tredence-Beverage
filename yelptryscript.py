import requests
from bs4 import BeautifulSoup
import xlwt
#This is for educational purposes only I dont have the permission to use their data for commercial use

count = 0
#create a spreadsheet file
wb=xlwt.Workbook()
#create a sheet
ws = wb.add_sheet("sheet 1")
url="https://www.yelp.com/search?find_desc=Grocery+Store&find_loc=Manila,+Metro+Manila,+Philippines&start="
for x in range(0,520,10):
    _url=url+str(x)
    #add request
    r = requests.get(_url)

   # print r

    #create a BS instance using the request data
    soup = BeautifulSoup(r.content,"lxml")
    
    store_name = soup.find_all("div",{"class":"search-result natural-search-result"})
    for item in store_name:
        
        name=item.contents[1].contents[1].contents[1].contents[3].contents[1].contents[1].contents[1].text
        
        rating=item.contents[1].contents[1].contents[1].contents[3].contents[3].contents[1].get("title")
        print name
        print rating
        if rating != None:
            count = count + 1
            ws.write(count-1,0,name)
            try:
                ws.write(count-1,1,float(rating.strip(' star rating')))
            except:
                pass
        wb.save("YelpData.xls")   



    
 
