import os
import datetime

#Function to save some data into the file in the current project folder
def SaveLogFile(data):
    print('saving data into the file')

    #path = '/home/user01/projects/HardwareSurveillance'    
    #os.makedirs('/home/user01/projects/HardwareSurveillance/SavedLogs')
    
    time = datetime.datetime.now() #tracking the time of log saving
    time = time.strftime("%c")
    dataLog = "\n Logs from date: " + time + " " + data
    
    f = open("SavedLogs.txt", "a")
    f.write(dataLog)
    
    f.close()

def ReadLogFile():
    f = open("SavedLogs.txt", "r")
    print(f.read())