import requests
from bs4 import BeautifulSoup
import xlwt
#This is for educational purposes only I dont have the permission to use their data for commercial use
#add request
count = 0
_count = 0
counter = 0
#create a spreadsheet file
wb=xlwt.Workbook()
#create a sheet
ws = wb.add_sheet("sheet 1")
url="https://www.yelp.com/search?find_desc=cafe&find_loc=Manila,+Metro+Manila,+Philippines&start="
for x in range(0,520,10):
    _url=url+str(x)
    r = requests.get(_url)
    #create a BS instance using the request data
    soup = BeautifulSoup(r.content,"lxml")
    
    g_data = soup.find_all("div",{"class":"search-result natural-search-result"})
    for item in g_data:
        
        name=item.contents[1].contents[1].contents[1].contents[3].contents[1].contents[1].contents[1].text
        rating=None
        try:
            rating=item.contents[1].contents[1].contents[1].contents[3].contents[3].contents[1].get("title")
        except:
            pass
        address=item.contents[1].contents[3].contents[1].text
        #print name
        #print rating
        _address=str(address.replace('\n            ','',1))

        print _address
        
        if rating != None :
            if item.contents[1].contents[3].contents[1].text!=None:
                count = count + 1
                ws.write(count-1,0,name)
                ws.write(count-1,2,_address.strip("        "))
                try:
                    ws.write(count-1,1,float(rating.strip(' star rating')))
                except:
                    pass
        wb.save("data.xls")   



    
 
