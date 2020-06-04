


#Date : 10/01/2018
#This program does what?
#it reads a text file and extracts uuid from the line
#containing the uuid value and then makes a command line with that value.
#It then writes the command line in a batch file. This batch file is then run
#at the DOS prompt for automatic donwloading of the Sentinel Data File associated with the
#uuids.
#The text file containg the uuid value is created from the file products.meta4 which is a collection
#of all Sentinel Data Files in the cart as a result of an executed  query.
import os,sys
#file = open("C:\\Users\\IIRS\\Downloads\\Products_Dec1.txt","r")
#file = open("C:\\Users\\IIRS\\Downloads\\Products_Jun4.txt","r")
file = open("O:\\10FEB2018.txt","r")
#file = open("C:\\Users\IIRS\\Downloads\\.txt","r")
file1 = open("C:\\Python27\\Scripts\\10FEB2018.bat","w")
ctr = 0
for line in file:
    if (line.find("$value") <> -1):
        print line
        myline = line.split("/")
        reqdline =  myline[7]
        print reqdline[6:42]
        uuid = reqdline[6:42]
        cmd = "sentinelsat -u username -p password -d --path E:\\10FEB2018 --uuid "+ uuid
        #cmd =  "sentinelsat -u username -p password -d --path E:\\16DEC2017 --uuid "+ uuid
        file1.write(cmd+"\n")
        print cmd
        ctr = ctr + 1

        
        
        
file.close()
file1.close()
print "Batch File Completed.Please Run it right now"
print "Counter = ",ctr
