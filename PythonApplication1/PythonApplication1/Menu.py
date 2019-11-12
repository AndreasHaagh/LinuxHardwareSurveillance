import CPU
import MemoryControll

def DisplayMenu():
    print("""
1: CPU
2: RAM
3: Exit
    """)
    menuItem = input("Choose menu item: ")
    if(menuItem == "1"):
        print("")
        CPU.printCpuUsage()
       
    elif (menuItem == "2"):
        MemoryControll.printMemoryUsage()
    else:
        print("Closing program")