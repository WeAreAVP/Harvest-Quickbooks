
import sys
import os
import csv
from array import *
import json

print("\nWelcome to the Converter Program!!! \n \n")

val = raw_input("Please enter file name of the iif file with the extension: ")


data = [{}] * 30
labels = [""]
count = 0
temp = {}


with open(val, 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\t', quotechar='|')
    for row in spamreader:
        #print(row[0:9])
        if count == 2:
            for r in row:
                labels.append(r)
        if count > 2:
            for r in row:
                for l in labels:
                    temp[l] = r
                    data.append(r)
                   # print(temp[l])
        count += 1
        
#labels.pop(0)
#for i in labels:
#    print(i)
    
#for d in data:
#    if d != {}:
#        print(d)
    
for x in data:
    print(x)
    #for l in labels:
            #print(x[""])
        







#rows, cols = (100, 10)
#arr={}
#for i in range(rows):
#    col = []
#    for j in range(cols):
#        col.append("")
#    arr.append(col)

#data = [{}] *
#data['key'] = 'value'
#json_data = json.dumps(data)

#with open(val, 'r') as csvfile:
#    spamreader = csv.reader(csvfile, delimiter='\t', quotechar='|')
#    for row in spamreader:
        #print(', '.join(row))
        #print(row[1])
        
        
#        for r in row:
#            for i in arr:
#                for j in i:
#                    arr[i][j] = row[j]
        
        
#for i in arr:
#    for j in i:
#        print j,
#    print()


#val2 = raw_input("\n\nPlease enter file name of the iif file without the extension: ")
#
##filename = sys.argv[0]


#filename = sys.argv[1]

#os.rename('report.xlsx','report.csv')

#ext = '.csv'
#filename = val2 + ext
#os.rename(val, filename)

#print(filename)

#
#with open(val) as f_obj:
#    lines = f_obj.readlines()
#for line in lines:
#    #print(line.rstrip())
#    print(line[1:10])
#


#This scipt receives an iff file as input from Harvest and outputs an iff file for Quickbooks


#filename = 'file.txt'
#with open(filename) as f_obj:
#    lines = f_obj.readlines()
#for line in lines:
#    print(line.rstrip())
