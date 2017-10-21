from list_stores_dict import lister
import matplotlib.pyplot as plt
a=lister()
add_pop_den=[0]*265
add_rating=[0]*265
count=0 
for item in a:
    add_pop_den[count]=float(item['City'])
    add_rating[count]=float(item['Rating'])
    count +=1
plt.scatter(add_pop_den,add_rating, label='Stores', color='r', s=25, marker="o")
plt.xlabel('Population Density')
plt.ylabel('Rating')
plt.title('Scatter Plot\nRatings vs Population Density')
plt.legend()
plt.show()



