import psutil

#Showing memory usage 
def printMemoryUsage():
    print ('\n Memory:')
    print(psutil.virtual_memory()) #shows in Bytes
    memory = psutil.virtual_memory().total >> 20
    print('Total memory: ', memory, 'MB')
    memory = psutil.virtual_memory().used >> 20
    print('Used: ', memory, 'MB')
    memory = psutil.virtual_memory().free >> 20
    print('Free: ', memory, 'MB')