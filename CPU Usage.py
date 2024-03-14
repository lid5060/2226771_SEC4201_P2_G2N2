import psutil
while True:
    print("Enter 1 to see CPU cores")
    print("Enter 2 to see CPU frequency")
    print("Enter 3 to see CPU states")
    print("Enter 4 to see CPU load")
    print("Enter 0 to return to main menu")
    try:
        menu = int(input())
        if menu == 1:
            print("Your device has", psutil.cpu_count(logical=False), "CPU cores")
            print("Your device has", psutil.cpu_count(logical=True), "CPU threads")
# logical = false makes psutil only count cores instead of threads
# logical = true makes psutil count threads instead of cores
        if menu == 2:
            print("")
        if menu == 3:
            print("")
        if menu == 4:
            print("")
        if menu == 0:
            with open('Main Menu.py') as file:
                exec(file.read())
    except Exception:
        print("An error has occurred, please try again")
# the try will try and execute the code, if it fails it will print the error message in the except block