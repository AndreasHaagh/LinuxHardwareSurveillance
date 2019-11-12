import CPU

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
    if (menuItem == "2"):
    