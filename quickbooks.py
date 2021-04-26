
import sys
import os
import csv
from array import *
import json


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







#Initializes the field variables
def new(headers, headersCont, data, newData, labels, count):

    headers = headers #array to store third row in the file
    headersCont = headersCont #array to store first two rows in the file
    data = data #data array of dictionaries
    newData = newData #data array of dictionaries
    labels = labels #header array of strings
    count = count



#The iif file is read in
def readIn(count, val, newFile):
    temp = {}
    
    fp = trimSpaces(val)
    
    try:
        with open(fp, 'r') as csvfile:
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
        print("An error occurred.\n\n")
        start(val1, count, option)




#Modifies all values in ITEM to user input
def change(newFile, val1, val, data):

    option1 = False
    
    while option1 == False:
        if val1 == "":
            val1 = raw_input("Please enter the task/item name: ")

        else:
            for d in range(0, len(data)):
                data[d]["ITEM"] = val1
            option1 = True
            
            
    
        


#Migrates data to final array
def delete(data):
    temp3 = {}
    for d in range(0, len(data)):
        if data[d] != None:
            temp3 = data[d]
            newData.append(temp3)


            
#Computes the duration strings
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
    
            
            
            
#Creates new file for user with all selected options
def writeOut(newFile, val, data):
    delete(data)
    int = 0
        
    file_Path = getFilePath(val)
    iif_file = file_Path + "/" + newFile + "_qb.iif"
    

    
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
    ans = raw_input("Would you like to convert another file? \n \nEnter 'y' for Yes\nEnter 'n' for No\n\n\n: ")
    
    del data[:]
    del newData[:]
    del labels[:]
    val1 = ""
    
    option1 = False
    while option1 == False:
        if ans == "y":
            clear = lambda: os.system('clear')
            clear()
            start(val1, count, False)
            option1 = True
            
        elif ans == "n":
            print("\n\nGoodbye!\n\n")
            exit()
        else:
            print("Invalid input try again\n \n")
            ans = raw_input("Would you like to convert another file? \n \nEnter 'y' for Yes\nEnter 'n' for No\n\n\n: ")



#Checks for duplicate strings
def dedup(string1, string2):

    stringParts = string1.split("; ")

    if stringParts[len(stringParts)-1] == string2:
        return True
        
    else:
        return False
        
        
#Trim whitespaces in filepath
def trimSpaces(filePath):
    filePath = filePath.replace(" ", "")
    temp_ = filePath
    return temp_
        
        
#Returns the file name without the filepath
def getFileName(filePath):
    stringParts = [filePath.split("/")]
    result = ""
    result = stringParts[len(stringParts)-1]
    return result


#Returns filepath without the file name
def getFilePath(filePath):
    
    filePath = trimSpaces(filePath)
    stringParts = filePath.split("/")
    leng = len(stringParts)
    result = ""
    temp_1 = ""
    
    for d in range(0, leng):
        if d != leng-1 and d != 0:
            temp_1 = stringParts[d]
            result += "/" + temp_1
            temp_1 = ""
    return result
   
            

    
#Modifies all NOTE values to be identical to ITEM values
def taskNote():
    temp = ""
    for d in range(0, len(data)):
        if data[d] != None:
            temp = data[d]["ITEM"]
            data[d]["NOTE"] = data[d]["ITEM"]
            temp = ""
        
    
    
#Consolidates
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
                        clear = lambda: os.system('clear')
                        clear()
                        print("One or more jobs differ. Please enter another file.")
                        start(val1, count, option)
    
                        
                        



#Third option
def start3(val, val1, newFile):

        print("\n\n\n\n\n\n")
#        ans2 = raw_input("Would you like to copy ITEM values to NOTE values? \n \nEnter 'a' for Yes\nEnter 'b' for No\nEnter 'c' for Cancel\n\n")
        ans2 = raw_input("Would you like to rename all ITEM values (i.e. Tasks) tasks to a single value? \n \nEnter 'y' for Yes\nEnter 'n' for No\nEnter 'c' for Cancel\n\n: ")
        option4 = False
        
        while option4 == False:
        
            if ans2 == "y": #Option 3
                option4 = True
#                taskNote()
                change(newFile, val1, val, data)
                writeOut(newFile, val, data)
                
            elif ans2 == "n": #No option selected
                option4 = True
                writeOut(newFile, val, data)
                print("No Option was selected.\n\nGoodbye!\n\n")
                
                
            elif ans2 == "c":
                print("\n\nGoodbye!\n\n")
                exit()
                
            else: #Error
                print("Invalid input try again\n\n")
                ans = raw_input("Would you like to rename all ITEM values (i.e. Tasks) tasks to a single value? \n \nEnter 'y' for Yes\nEnter 'n' for No\nEnter 'c' for Cancel\n\n: ")


#Second option
def start2(val, val1, newFile):
    
    print("\n\n\n\n\n\n")
    ans1 = raw_input("Would you like to consolidate rows by DATE and ITEM? \n \nEnter 'y' for Yes\nEnter 'n' for No\nEnter 'c' for Cancel\n\n")
    option2 = False
    
    while option2 == False:
    
        if ans1 == "y": #Option 2
            option2 = True
            modifi(newFile, data, val)
            start3(val, val1, newFile)
            
        elif ans1 == "n": #Option 3
            option2 = True
            start3(val, val1, newFile)
            
        elif ans1 == "c":
            print("\n\nGoodbye!\n\n")
            exit()
            
        else: #Error
            print("Invalid input try again\n \n")
            ans = raw_input("Would you like to consolidate rows by DATE and ITEM? \n \nEnter 'y' for Yes\nEnter 'n' for No\nEnter 'c' for Cancel\n\n")



#First option
def start(val1, count, option):
    
    del data[:]
    del newData[:]
    del labels[:]
    headersCont.clear()
    del headers[:]
    fileName = ""
    
    new(headers, headersCont, data, newData, labels, count)
    
    print("\n\n\n\n\n\n")
    
    #Retreiving the user input
    val = raw_input("Please enter the full path of the iif file with the (.iif) extension or drag and drop the file into the terminal\n\n\n\n\n\n: ")

    print("\n\n\n\n\n\n")

    newFile = raw_input("Enter the desired name for the new file without the (_qb) addition and (.iif) extension. For example, 'new', but 'new_qb.iif'.\n: ")

    print("\n\n\n\n\n\n")

#    ans = raw_input("Would you like to rename all ITEM values (i.e. Tasks) tasks to a single value? \n \nEnter 'a' for Yes\nEnter 'b' for No\nEnter 'c' for Cancel\n\n: ")
    ans = raw_input("Would you like to copy ITEM values to NOTE values? \n \nEnter 'y' for Yes\nEnter 'n' for No\nEnter 'c' for Cancel\n\n")
    

    readIn(count, val, newFile)

    while option == False:
        if ans == "y": #Option 1
            option = True
            taskNote()
#            change(newFile, val1, val, data)
            start2(val, val1, newFile)
            
            
        elif ans == "n": #Option 2
            option = True
            start2(val, val1, newFile)
            
        elif ans == "c":
            print("\n\nGoodbye!\n\n")
            exit()
            
        else: #Error
            print("Invalid input try again\n \n")
#            ans = raw_input("Would you like to rename all ITEM values (i.e. Tasks) tasks to a single value? \n \nEnter 'a' for Yes\nEnter 'b' for No\n\n: ")
            ans = raw_input("Would you like to copy ITEM values to NOTE values? \n \nEnter 'y' for Yes\nEnter 'n' for No\nEnter 'c' for Cancel\n\n")



#Clears terminal console
clear = lambda: os.system('clear')
clear()

#Welcome Message
print("\nWelcome to the Harvest Quickbooks Converter!!! \n\n")
start(val1, count, option)
        
        
        
        
        
        
        
        
        
        
        
        

