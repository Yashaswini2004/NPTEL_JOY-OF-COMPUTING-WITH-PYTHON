import csv
with open('route.csv','r') as f:
    reader=csv.reader(f)
    for row in reader:
        lan=float(row[0])
        long=float(row[1])
        print(lan)
        print(long)
        print(lan+long)