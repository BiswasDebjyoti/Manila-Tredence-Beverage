#dict_pop={'':,} 
import csv
import pprint
reader = csv.DictReader(open('/home/debjyoti/Desktop/Manila-Tredence-Beverage/xls_files/populationden.csv', 'rb'))
dict_list = []
for line in reader:
    dict_list.append(line)
pprint.pprint(dict_list)