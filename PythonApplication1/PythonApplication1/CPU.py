import psutil
import FileControll

def printCpuUsage():
    print("Seconds the cpu spent on each mode")
    cpuTimes = psutil.cpu_times()
    print(cpuTimes)
    timesData = str(cpuTimes)
    FileControll.SaveLogFile(timesData)

    index = 0
    percentData = ""
    print("\nPercentage of usage on each cpu")
    while index < 6:
        cpuPercentage = psutil.cpu_percent(interval = 1, percpu = True)
        print(cpuPercentage)
        percentData = str(cpuPercentage)
        FileControll.SaveLogFile("CPU percentage: " + percentData)
        index += 1
    else:
        print("Data saved to log file")

#percentage = [x / psutil.cpu_count() * 100 for x in psutil.getloadavg()]
#print(percentage)
