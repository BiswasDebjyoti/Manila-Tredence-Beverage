from list_stores_dict import lister
a=lister()
add_pop_den=[0]*265
add_rating=[0]*265
count=0 
for item in a:
    add_pop_den[count]=float(item['City'])
    add_rating[count]=float(item['Rating'])
    count +=1



