import psutil
import time

def printCpuUsage():
    i = 0
    while i < 6:
        print(psutil.cpu_percent(interval = 1, percpu = True))
        i += 1
        #time.sleep(.100)
    else:
        print("the while loop has ended!")
