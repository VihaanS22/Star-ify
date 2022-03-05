import csv
import pandas as pd

brights = 'brights.csv'
dwarfs = 'dwarfs.csv'

df1 = []
df2 = []

with open(brights) as f:
    csv_reader =csv.reader(f)
    
    for i in csv_reader:
        df1.append(i)
        
with open(dwarfs) as f:
    csv_reader = csv.reader(f)
    
    for i in csv_reader:
        df2.append(i)

brights_headers = df1[0]
brights_data = df1[1:]

dwarfs_headers = df2[0]
dwarfs_data = df2[1:]

final_headers = brights_headers

final_data = brights_data + dwarfs_data

#for index, data_row in enumerate(brights_data):
#    final_data.append(brights_data[index] + dwarfs_data[index])

with open("final_stars.csv",'w') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(final_headers)   
    csvwriter.writerows(final_data)

