import CPU
import MemoryControll
import FileControll
import sys

isRunning = False

def DisplayMenu():
    print("""
1: CPU
2: RAM
3: Save into file
4: Exit
    """)
    menuItem = input("Choose menu item: ")
    if (menuItem == "1"):
        print("")
        CPU.printCpuUsage()
       
    elif (menuItem == "2"):
        MemoryControll.printMemoryUsage()
    elif (menuItem == "3"):        
        FileControll.SaveLogFile()
    elif (menuItem == "4"):
        isRunning = False
        print("Closing system!")
        sys.exit(0)
    else:
        print("\nError: invaild input")