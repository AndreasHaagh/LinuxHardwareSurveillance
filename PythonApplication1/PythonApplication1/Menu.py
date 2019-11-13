import CPU
import MemoryControll
import FileControll

isRunning = True
data = 'data log'
"""
    Function to show user interactive menu
    performing monitoring of the system
"""
def DisplayMenu():
    print("""
1: CPU
2: RAM
3: Read Log file
4: Exit
    """)
    
    menuItem = input("Choose menu item: ")
    #providing information efter user input
    if (menuItem == "1"):
        print("")
        CPU.printCpuUsage()
       
    elif (menuItem == "2"):
        MemoryControll.printMemoryUsage()

    elif (menuItem == "3"):        
        FileControll.ReadLogFile()

    elif (menuItem == "4"):
        global isRunning
        isRunning = False
        print("Closing system!")
    else:
        print("\nError: invaild input")
