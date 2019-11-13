#Adding modules for using in the function
import os
import datetime

"""
    Function to save received data 
    into the log file placed 
    in the current project folder 
"""
def SaveLogFile(data):
    #Getting local version of date and time for logs storage    
    time = datetime.datetime.now()
    #Casting received dato into string format 
    time = time.strftime("%c")
    #Preparing log string to be writen into the file
    dataLog = "\n Logs from date: " + time + " " + data
    #Openning stream of the file with append option
    f = open("SavedLogs.txt", "a")
    #Writing data into the file
    f.write(dataLog)
    #Closing work with file
    f.close()

"""
    Function to read from log file,
    stored in the current project folder
"""
def ReadLogFile():
    #Openning file with option read
    f = open("SavedLogs.txt", "r")
    #Printing data
    print(f.read())
    #Closing work with file
    f.close()