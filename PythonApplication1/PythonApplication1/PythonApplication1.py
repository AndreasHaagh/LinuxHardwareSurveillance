import psutil
import time

i = 0
while i < 6:
    print(psutil.cpu_percent(interval = 2, percpu = True))
    i += 1
else:
    print("the while loop has ended!")