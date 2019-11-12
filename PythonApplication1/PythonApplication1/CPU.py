import psutil
import time

def printCpuUsage():
    percentage = [x / psutil.cpu_count() * 100 for x in psutil.getloadavg()]
    print(percentage)
