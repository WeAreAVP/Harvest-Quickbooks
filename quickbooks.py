
import sys
import os
import csv
from array import *
import json

#Welcome message

val = ""
val1 = ""
ans1 = ""
newFile = ""
file_Path = ""
option = False
    



headers = [""] * 0
headersCont = {}
data = [{}] * 0 #data array of dictionaries
newData = [{}] * 0 #data array of dictionaries
labels = [""] * 0 #header array of strings
count = 0



def new(headers, headersCont, data, newData, labels, count):

    headers = headers
    headersCont = headersCont
    data = data #data array of dictionaries
    newData = newData #data array of dictionaries
    labels = labels #header array of strings
    count = count



#The iif file is read in
def readIn(count, val, newFile):
    temp = {}
    
    try:
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
                    
                            temp[labels[r]] = row[r]
                    data.append(temp)
                    temp = {}
                count += 1
            count = 0
    except:
        print("An error occurred. Please make sure there are no spaces.\n\n")
        start(val1, count, option)




        
def change(newFile, val1, val, data):

    option1 = False
    
    while option1 == False:
        if val1 == "":
            val1 = raw_input("Please enter the task/item name: ")

        else:
            for d in range(0, len(data)):
                data[d]["ITEM"] = val1
            option1 = True
            writeOut(newFile, val, data)
            
            
    
        


    
def delete(data):
    temp3 = {}
    for d in range(0, len(data)):
        if data[d] != None:
            temp3 = data[d]
            newData.append(temp3)


            
            
def calc(time1, time2):
    timeList = [] * 0
    timeList.append(time1)
    timeList.append(time2)
    totalMins = 0
    result = ""
    
    for tm in timeList:
        timeParts = [int(s) for s in tm.split(":")]
        totalMins += (timeParts[0] * 60) + timeParts[1]
        
    hr, min = divmod(totalMins, 60)
    result = "%02d:%02d" % (hr, min)
    return result
    
            
            
            
            
def writeOut(newFile, val, data):
    delete(data)
    int = 0
        
    file_Path = getFilePath(val)
    
#    iif_file = filePath + newFile + "_qb.iif"
    iif_file = file_Path + "/" + newFile + "_qb.iif"
    print(iif_file)
    
#    for d in newData:
#        print(d)
   
    
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
                    writer.writerow(newData[d]) #Writing in the rest of the data
                int += 1
    except IOError:
        print("I/O error") #Error message
        
    print("\n\nYour file has successfully been converted!\n\n")
    ans = raw_input("Would you like to convert another file? \n \nEnter 'a' for Yes\nEnter 'b' for No\n\n\n: ")
    
    del data[:]
    del newData[:]
    del labels[:]
    val1 = ""
    
    option1 = False
    while option1 == False:
        if ans == "a":
            
            start(val1, count, False)
            option1 = True
            
        elif ans == "b":
            print("\n\nGoodbye!\n\n")
            exit()
        else:
            print("Invalid input try again\n \n")
            ans = raw_input("Would you like to convert another file? \n \nEnter 'a' for Yes\nEnter 'b' for No\n\n\n: ")



def dedup(string1, string2):

    stringParts = [string1.split("; ")]
    
    if stringParts[len(stringParts)-1] == string2:
        return True
        
    else:
        return False
        
        
        
        
        
def getFileName(filePath):

    stringParts = [filePath.split("/")]
    result = ""
    result = stringParts[len(stringParts)-1]
#    print(result)
    return result


def getFilePath(filePath):

    stringParts = filePath.split("/")
#    print(stringParts)
    leng = len(stringParts)
    result = ""
    temp_1 = ""
    
    for d in range(0, leng):
        if d != leng-1 and d != 0:
            temp_1 = stringParts[d]
            result += "/" + temp_1
            temp_1 = ""
    return result
   
            

    
def taskNote():
    temp = ""
    for d in range(0, len(data)):
        temp = data[d]["ITEM"]
        data[d]["NOTE"] = data[d]["ITEM"]
        temp = ""
        
    
    
        
def modifi(newFile, data, val): #Method to modify data in dictionary array
    temp2 = {}
    temp3 = ""
    temp4 = ""
    temp5 = ""
    temp6 = ""

    length = len(data)
    
    for d in range(0, length):
        if d < length:
            for e in range(d + 1, length):
            
                if bool(data[d]) and bool(data[e]):
                
                    if data[d]["JOB"] == data[e]["JOB"]:
                        temp2 = data[e]
                        temp3 = data[d]["EMP"]
                        temp4 = data[e]["EMP"]
                        temp5 = data[d]["NOTE"]
                        temp6 = data[e]["NOTE"]
                        
            
                        if data[d]["ITEM"] == data[e]["ITEM"] and data[d]["DATE"] == data[e]["DATE"]:
                        
                            if data[d]["EMP"] == data[e]["EMP"] and data[d]["NOTE"] == data[e]["NOTE"]:
                            
                                    
                                    data[d][labels[6]] = calc(data[d][labels[6]], temp2[labels[6]])
                                    data[e] = data[e].clear()
                            
                                
                            elif data[d]["EMP"] == data[e]["EMP"] and data[d]["NOTE"] != data[e]["NOTE"]:
                                    
                                    if dedup(temp5, temp6) == False:
                                        data[d][labels[8]] = data[d][labels[8]] + "; " + temp2[labels[8]]
                                        
                                    data[d][labels[6]] = calc(data[d][labels[6]], temp2[labels[6]])
                                    data[e] = data[e].clear()
                                    
                            
                            
                            elif data[d]["EMP"] != data[e]["EMP"] and data[d]["NOTE"] == data[e]["NOTE"]:
                                
                                
                                if dedup(temp3, temp4) == False:
                                    data[d][labels[3]] = data[d][labels[3]] + "; " + temp2[labels[3]]
                                    
                                data[d][labels[6]] = calc(data[d][labels[6]], temp2[labels[6]])
                                data[e] = data[e].clear()
                            
                            
                            elif data[d]["EMP"] != data[e]["EMP"] and data[d]["NOTE"] != data[e]["NOTE"]:
                                    
                                if dedup(temp3, temp4) == False:
                                    data[d][labels[3]] = data[d][labels[3]] + "; " + temp2[labels[3]]
                                    
                                if dedup(temp5, temp6) == False:
                                        data[d][labels[8]] = data[d][labels[8]] + "; " + temp2[labels[8]]
                                        
                                data[d][labels[6]] = calc(data[d][labels[6]], temp2[labels[6]])
                                data[e] = data[e].clear()
                        temp2 = {}
                        temp3 = ""
                        temp4 = ""
                        
                    else:
                        print("One or more jobs differ. Please enter another file.")
                        exit()
    
    writeOut(newFile, val, data)
                        
                        




def start3(val, newFile):

        ans2 = raw_input("Would you like to copy ITEM values to NOTE values? \n \nEnter 'a' for Yes\nEnter 'b' for No\nEnter 'c' for Cancel\n\n")
        option4 = False
        
        while option4 == False:
        
            if ans2 == "a": #Option 3
                option4 = True
                readIn(count, val, newFile)
                taskNote()
                writeOut(newFile, val, data)
                
            elif ans2 == "b": #No option selected
                option4 = True
                readIn(count, val, newFile)
                writeOut(newFile, val, data)
                print("No Option was selected.\n\nGoodbye!\n\n")
                exit()
                
            elif ans2 == "c":
                print("\n\nGoodbye!\n\n")
                exit()
                
            else: #Error
                print("Invalid input try again\n \n")
                ans = raw_input("Would you like to consolidate rows where date/task match? \n \nEnter 'a' for Yes\nEnter 'b' for No\nEnter 'c' for Cancel\n\n")



def start2(val, newFile):
    print("In the start2 method")
#    print(val)

    ans1 = raw_input("Would you like to consolidate rows by DATE and ITEM? \n \nEnter 'a' for Yes\nEnter 'b' for No\nEnter 'c' for Cancel\n\n")
    option2 = False
    
    while option2 == False:
    
        if ans1 == "a": #Option 2
            option2 = True
            readIn(count, val, newFile)
            modifi(newFile, data, val)
            
        elif ans1 == "b": #Option 3
            option2 = True
            start3(val, newFile)
            
        elif ans1 == "c":
            print("\n\nGoodbye!\n\n")
            exit()
            
        else: #Error
            print("Invalid input try again\n \n")
            ans = raw_input("Would you like to consolidate rows by DATE and ITEM? \n \nEnter 'a' for Yes\nEnter 'b' for No\nEnter 'c' for Cancel\n\n")




def start(val1, count, option):
    
    del data[:]
    del newData[:]
    del labels[:]
    headersCont.clear()
    del headers[:]
    fileName = ""
    
    new(headers, headersCont, data, newData, labels, count)

    
    #Retreiving the user input
    val = raw_input("Please enter the full path of the iif file (NO SPACES) with the (.iif) extension or drag and drop the file into the terminal: ")

    print("\n \n")

    newFile = raw_input("Enter the desired name for the new file without the (_qb) addition and (.iif) extension. For example, 'new', but 'new_qb.iif'.\n: ")

    print("\n \n")

    ans = raw_input("Would you like to rename all ITEM values (i.e. Tasks) tasks to a single value? \n \nEnter 'a' for Yes\nEnter 'b' for No\nEnter 'c' for Cancel\n\n: ")
    
    



    while option == False:
        if ans == "a": #Option 1
            option = True
            readIn(count, val, newFile)
            change(newFile, val1, val, data)
            
            
        elif ans == "b": #Option 2
            option = True
            start2(val, newFile)
            
        elif ans == "c":
            print("\n\nGoodbye!\n\n")
            exit()
            
        else: #Error
            print("Invalid input try again\n \n")
            ans = raw_input("Would you like to rename all ITEM values (i.e. Tasks) tasks to a single value? \n \nEnter 'a' for Yes\nEnter 'b' for No\n\n: ")



        
print("\nWelcome to the Harvest Quickbooks Converter!!! \n \n")
start(val1, count, option)
        
        
        
        
        
        
        
        
        
        
        
        

