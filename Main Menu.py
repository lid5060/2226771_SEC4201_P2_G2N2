while True:
    print("Welcome to Brenda's Buggy Byte Barn\n")
# the menu which will drive the entire programme
# numbers are being used to make the menu easier to use with multiple items
# implement error handling if letters or decimals are entered
    try:
        print("Enter 1 to enter CPU usage")
        print("Enter 2 to enter memory usage")
        print("Enter 3 to enter disk usage")
        print("Enter 4 to enter bibliography")
        print("Enter 0 to exit")
        menu = int(input())
        if menu < 0:
            print("Not an option try again")
        elif menu > 4:
            print("Not an option try again")
        elif menu == 1:
            with open('CPU Usage.py') as file:
                exec(file.read())
        elif menu == 2:
            with open('Memory.py') as file:
                exec(file.read())
        elif menu == 3:
            with open('Disk Usage.py') as file:
                exec(file.read())
        elif menu == 4:
            with open('bibliography.py') as file:
                exec(file.read())
        elif menu == 0:
            break
# the with command is used to open the file so that it closes down when the code is done
# the exec command is used to execute the code within the file
# change all except blocks to handle specific errors rather than all errors allowing for more specific error messages
    except ValueError:
        print("Please enter a number")
    except FileNotFoundError:
        print("File not found")
    except KeyboardInterrupt:
        print("Keyboard interrupt")
# the try will try and execute the code,
# if it fails it will print the error message in the except block