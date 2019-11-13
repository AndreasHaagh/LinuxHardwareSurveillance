import psutil
import time

def printCpuUsage():
    print("Seconds the cpu spent on each mode")
    print(psutil.cpu_times())

    index = 0
    print("\nPercentage of usage on each cpu")
    while index < 6:
        print(psutil.cpu_percent(interval = 1, percpu = True))
        index += 1
    else:
        print("The loop has ended")

#Only works on Linux
#percentage = [x / psutil.cpu_count() * 100 for x in psutil.getloadavg()]
#print(percentage)
