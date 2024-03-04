import psutil
while True:
    print ("Welcome to Brenda's Buggy Byte Barn\n")
# the menu which will drive the entire programme
# numbers are being used to make the menu easier to use with multiple items
# implement error handling if letters or decimals are entered
    print("Press 1 to see cpu cores")
    print("Press 2 to see cpu times")
    print("Press 0 to exit")
    choice = int(input())
    if choice < 0:
        print("Not an option try again")
    elif choice > 2:
        print("Not an option try again")
    elif choice == 1:
        print("cpu cores")
        print(psutil.cpu_count())
    elif choice == 2:
        print("cpu times")
        print(psutil.cpu_times())
    elif choice ==0:
        break
    