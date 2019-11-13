import psutil
import FileControll

def printCpuUsage():
    print("Seconds the cpu spent on each mode")
    print(psutil.cpu_times())
    timesData = str(psutil.cpu_times())
    FileControll.SaveLogFile(timesData)

    index = 0
    percentData = ""
    print("\nPercentage of usage on each cpu")
    while index < 6:
        print(psutil.cpu_percent(interval = 1, percpu = True))
        percentData = str(psutil.cpu_percent(interval = 1, percpu = True))
        FileControll.SaveLogFile("CPU percentage: " + percentData)
        index += 1
    else:
        print("Data saved to log file")

#percentage = [x / psutil.cpu_count() * 100 for x in psutil.getloadavg()]
#print(percentage)
