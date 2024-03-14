while True:
    print("Welcome to Brenda's Buggy Byte Barn\n")
# the menu which will drive the entire programme
# numbers are being used to make the menu easier to use with multiple items
# implement error handling if letters or decimals are entered
    try:
        print("enter 1 to see CPU usage")
        print("")
        print("")
        print("Enter 4 to see bibliography")
        print("enter 0 to exit")
        choice = int(input())
        if choice < 0:
            print("Not an option try again")
        elif choice > 4:
            print("Not an option try again")
        elif choice == 1:
            with open('CPU Usage.py') as file:
                exec(file.read())
        elif choice == 2:
            print("memory usage")
        elif choice == 3:
            print("disk usage")
        elif choice == 4:
            with open('bibliography.py') as file:
                exec(file.read())
# the with command is used to open the file so that it closes down when the code is done
# the exec command is used to execute the code within the file
        elif choice == 0:
            break
    except Exception:
        print("An error has occurred, please try again")
# the try will try and execute the code, if it fails it will print the error message in the except block