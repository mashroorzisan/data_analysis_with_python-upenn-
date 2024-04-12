import csv
with open('albumlist.csv', 'r')as csvfile:
    reader = csv.DictReader(csvfile)
    print(reader.fieldnames)


with open('albumlist.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)