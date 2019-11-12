import psutil
import time

def printCpuUsage():
    index = 0
    while index < 6:
        print(psutil.cpu_percent(interval = 1, percpu = True))
        index += 1
    else:
        print("The loop has ended")

#percentage = [x / psutil.cpu_count() * 100 for x in psutil.getloadavg()]
#print(percentage)
