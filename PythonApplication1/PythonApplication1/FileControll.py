import os
import datetime

#Function to save some data into the file in the current project folder
def SaveLogFile():
    print('saving last data in the file')

    #path = '/home/user01/projects/HardwareSurveillance'    
    #os.makedirs('/home/user01/projects/HardwareSurveillance/SavedLogs')
    global data
    time = datetime.datetime.now() #tracking the time of log saving
    time = time.strftime("%c")
    dataLog = "\n Logs from date: " + time + data
    print(dataLog)
    f = open("SavedLogs.txt", "a")
    f.write(dataLog)
    
    f.close()