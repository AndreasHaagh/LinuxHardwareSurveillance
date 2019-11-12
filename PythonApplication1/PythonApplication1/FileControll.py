import os
import datetime

#Function to save some data into the file in the current project folder
def SaveLogFile():
    print('saving last data in the file')

    #path = '/home/user01/projects/HardwareSurveillance'    
    #os.makedirs('/home/user01/projects/HardwareSurveillance/SavedLogs')

    x = datetime.datetime.now() #tracking the time of log saving
    x = x.strftime("%c")
    data = "\n Logs from date: " + x
    print(data)
    f = open("SavedLogs.txt", "a")
    f.write(data)
    
    f.close()