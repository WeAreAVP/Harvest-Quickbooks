
import sys
import os
import csv
from array import *
import json

#Welcome message

val1 = ""
ans1 = ""
option = False
    





headers = [""] * 0
headersCont = {}
data = [{}] * 0 #data array of dictionaries
newData = [{}] * 0 #data array of dictionaries
labels = [""] * 0 #header array of strings
count = 0
#temp1 = {}
#length = 0


#The iif file is read in
def readIn(count):
    temp = {}
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
                for r in range(0, len(row)):
                    labels.append(row[r])
                    #print(r)
            if count > 2: #appending the rest of the contents
                for r in range(0, len(row)):
                
    #                if r == 4:
    #                    temp[labels[r]] = val1
    #                else:
                        temp[labels[r]] = row[r]
                data.append(temp)
                temp = {}
            count += 1
            
    if val1 == "":
        modifi()
    
    else:
        for d in range(0, len(data)):
            data[d]["ITEM"] = val1
        modifi()
        


    
def delete():
    temp3 = {}
    for d in range(0, len(data)):
        if data[d] != None:
            temp3 = data[d]
            newData.append(temp3)

            
            
            
            
            
            
def writeOut():
    delete()
    int = 0
    iif_file = "newData2.iif"
    try:
        with open(iif_file, 'w') as csvfile: #writing the new file
        
            writer = csv.DictWriter(csvfile, headers, delimiter='\t')
            writer.writeheader()
            writer.writerow(headersCont) #writing in the first two lines
                    
            for d in range(0, len(newData)):
                if int == 0:
                    writer = csv.DictWriter(csvfile, labels, delimiter='\t', quoting=csv.QUOTE_NONE, escapechar=' ')
                    writer.writeheader() #writing in the third line
                
                if int >= 0:
                    writer.writerow(newData[d]) #writing in the rest of the data
                int += 1
    except IOError:
        print("I/O error") #Error message

        
    
        
def modifi():
    temp2 = {}

    length = len(data)
    
    for d in range(0, length):
        if d < length:
            for e in range(d + 1, length):
            
                if bool(data[d]) and bool(data[e]):
                
                    if data[d]["JOB"] == data[e]["JOB"]:
#                        print("d is equal to: ", d)
#                        print("e is equal to: ", e)
#                        print("length is equal to: ", length)
                        
                        temp2 = data[e]
            
                        if data[d]["ITEM"] == data[e]["ITEM"] and data[d]["DATE"] == data[e]["DATE"]:
                        
                            if data[d]["EMP"] == data[e]["EMP"] and data[d]["NOTE"] == data[e]["NOTE"]:
                            
                                    
                                    data[d][labels[6]] = data[d][labels[6]] + "; " + temp2[labels[6]]
                                   
                                    #del data[e]
                                    data[e] = data[e].clear()
                                    #data[e] = data[e].fromkeys(data[e], "")
#                                    print("1st condition")
                            
                                
                            elif data[d]["EMP"] == data[e]["EMP"] and data[d]["NOTE"] != data[e]["NOTE"]:
                                    

                                    data[d][labels[6]] = data[d][labels[6]] + "; " + temp2[labels[6]]
                                    data[d][labels[8]] = data[d][labels[8]] + "; " + temp2[labels[8]]
                                    #del data[e]
                                    data[e] = data[e].clear()
                                    #data[e] = data[e].fromkeys(data[e], "")
#                                    print("2nd condition")
                                    
                            
                            
                            elif data[d]["EMP"] != data[e]["EMP"] and data[d]["NOTE"] == data[e]["NOTE"]:
                                    
                                    data[d][labels[3]] = data[d][labels[3]] + "; " + temp2[labels[3]]
                                    data[d][labels[6]] = data[d][labels[6]] + "; " + temp2[labels[6]]
                                    #del data[e]
                                    data[e] = data[e].clear()
                                    #data[e] = data[e].fromkeys(data[e], "")
#                                    print("3rd condition")
                            
                            
                            elif data[d]["EMP"] != data[e]["EMP"] and data[d]["NOTE"] != data[e]["NOTE"]:
                                    
                                    data[d][labels[3]] = data[d][labels[3]] + "; " + temp2[labels[3]]
                                    data[d][labels[6]] = data[d][labels[6]] + "; " + temp2[labels[6]]
                                    data[d][labels[8]] = data[d][labels[8]] + "; " + temp2[labels[8]]
                                    #del data[e]
                                    data[e] = data[e].clear()
                                    #data[e] = data[e].fromkeys(data[e], "")
#                                    print("4th condition")
#                                    print("\n")
#                                    print(data[d])
                        temp2 = {}
                        #else:
                    else:
                        print("One or more jobs differ. Please enter another file.")
                        exit()
                    
    writeOut()
                        
                        




print("\nWelcome to the Harvest Quickbooks Converter!!! \n \n")

#Retreiving the user input
val = raw_input("Please enter file name of the iif file with the extension: ")

print("\n \n")

ans = raw_input("Would you like to modify all the tasks to be the same? \n \nEnter 'a' for Yes\nEnter 'b' for No\nEnter 'c' for Cancel\n\n: ")


while option == False:
    if ans == "a": #Option 1 then 2
        val1 = raw_input("Please enter the task/item name: ")
        option = True
        readIn(count)
    elif ans == "b": #Option 2 then 3
        readIn(count)
        option = True
        #ans1 = raw_input("Would you like to consolidate rows where date/task match? \n \nEnter 'a' for Yes\nEnter 'b' for No\n\n
    elif ans == "c":
        print("\n\nGoodbye!\n\n")
        exit()
#    : ")
    else: #Error
        print("Invalid input try again\n \n")
        ans = raw_input("Would you like to modify all the tasks to be the same? \n \nEnter 'a' for Yes\nEnter 'b' for No\n\n: ")



        
        
        
        
        
        
        
        
        
        
        
        
        
        

