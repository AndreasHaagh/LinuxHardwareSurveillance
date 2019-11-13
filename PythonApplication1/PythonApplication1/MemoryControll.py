#Adding modules for using in the function
import psutil
import FileControll

"""
    Function to return statistics 
    about system memory usage,
    expressed in bytes.
"""
def printMemoryUsage():
    print ('\n Memory:')
    print(psutil.virtual_memory()) # printing named tuple
    #printing received information in human readable format
    #Total physical memory in MB
    memory = psutil.virtual_memory().total >> 20
    print('Total memory: ', memory, 'MB')
    #Used memory in MB
    memory = psutil.virtual_memory().used >> 20
    print('Used: ', memory, 'MB')
    #Memory not being used at all that is readibally avalaible    
    memory = psutil.virtual_memory().free >> 20
    print('Free: ', memory, 'MB')
    #Saving data into the log fill
    # via casting into the string format and
    #calling SaveLogFile function from FileControll
    data = str(psutil.virtual_memory())
    FileControll.SaveLogFile(data)