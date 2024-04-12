import csv

my_file = open('albumlist.csv', 'r')
reader = csv.DictReader(my_file)

for r in reader:
    print(r)