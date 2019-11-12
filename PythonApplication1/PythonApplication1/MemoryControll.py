import psutil

#Showing memory usage 
def printMemoryUsage():
    print ('\n Memory:')
    print(psutil.virtual_memory())
