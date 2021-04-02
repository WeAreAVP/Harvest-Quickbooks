
import sys
import os
import csv
from array import *
import json

#Welcome message
print("\nWelcome to the Converter Program!!! \n \n")

#Retreiving the user input
val = raw_input("Please enter file name of the iif file with the extension: ")

headers = [""] * 0
headersCont = {}
data = [{}] * 0 #data array of dictionaries
labels = [""] * 0 #header array of strings
count = 0
temp = {}
length = 0


#The iif file is read in
with open(val, 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\t', quotechar='|')

    for row in spamreader:
        length = len(row)
        if count == 0:
            for r in row:
                headers.append(r)
            
        if count == 1:
            for r in range(0, len(row)):
                headersCont[headers[r]] = row[r]
                
                
        if count == 2: #appending header names to label array
            for r in row:
                labels.append(r)
                #print(r)
        if count > 2: #appending the rest of the contents
            for r in range(0, len(row)):
                    temp[labels[r]] = row[r]
            data.append(temp)
            temp = {}
        count += 1
        
        
        
#for d in range(0, len(data)):
#    print(data[d])
       
#print(headersCont)

#print(labels)
#
#print("\n \n")
#
#print(data)
#
#

int = 0
iif_file = "newData.iif"
try:
    with open(iif_file, 'w') as csvfile: #writing the new file
    
        writer = csv.DictWriter(csvfile, headers, delimiter='\t')
        writer.writeheader()
        writer.writerow(headersCont) #writing in the first two lines
                
        for d in range(0, len(data)):
            if int == 0:
                writer = csv.DictWriter(csvfile, labels, delimiter='\t')
                writer.writeheader() #writing in the third line
            
            if int >= 0:
                writer.writerow(data[d]) #writing in the rest of the data
            int += 1
except IOError:
    print("I/O error") #Error message

        
        
        
        
        
        
        
        
        
        
        
        
        
        
#labels.pop(0)
#for i in labels:
#    print(i)
    
#for d in data:
#    if d != {}:
#        print(d)
    
#for x in data:
#    print(x)
    
#print(data)
#    for l in labels:
#            print(l)
        







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
