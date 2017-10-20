import csv
import pprint

reader = csv.DictReader(open('/home/debjyoti/Desktop/Manila-Tredence-Beverage/xls_files/cafedata.csv', 'rb'))
dict_list = []
for line in reader:
    dict_list.append(line)


def lister():
    return dict_list