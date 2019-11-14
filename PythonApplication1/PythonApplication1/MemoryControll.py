#Adding modules for using in the function
import psutil
import FileControll

"""
    Function to return statistics 
    about system memory usage,
    expressed in bytes.
"""
def printMemoryUsage():
    print ('\n System Memory Statistics:')
    data = psutil.virtual_memory()    
    print(data) # printing named tuple    
    #printing received information in human readable format
    #Total physical memory in MB
    memory = data.total >> 20
    print('Total memory: ', memory, 'MB')
    #Used memory in MB
    memory = data.used >> 20
    print('Used: ', memory, 'MB')
    #Memory not being used at all that is readibally avalaible    
    memory = data.free >> 20
    print('Free: ', memory, 'MB')
    #Saving data into the log fill
    # via casting into the string format and
    #calling SaveLogFile function from FileControll
    data = str(data)
    FileControll.SaveLogFile("System Memory: " + data)
    #Swap memory statistics
    data1 = psutil.swap_memory()
    print("\n System Swap Memory Statistics: ")
    print(data1)#printing named tuple
    data1=str(data1)
    #calling SaveLogFile function from FileControll
    FileControll.SaveLogFile("Swap Memory: " + data1)