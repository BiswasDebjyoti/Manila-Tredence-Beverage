import csv
import pprint

reader = csv.DictReader(open('/home/debjyoti/Desktop/Manila-Tredence-Beverage/xls_files/Beveragescrapeweb.csv', 'rb'))
dict_list = []
for line in reader:
    dict_list.append(line)
pprint.pprint(dict_list[0])

def lister():
    return dict_list