import psutil
from psutil._common import bytes2human
# bytes2human allows for easy conversion of bytes to a more human-readable format
while True:
    print("Enter 1 to go to total, available and memory percentage menu")
    print("Enter 2 to go to swap memory menu")
    print("Enter 3 to go to general memory info")
    print("Enter 0 to return to main menu")
    try:
        memory_menu = int(input())
        if memory_menu < 0:
            print("Not an option try again")
        elif memory_menu > 3:
            print("Not an option try again")
        elif memory_menu == 1:
            print("Enter 1 to see total system memory")
            print("Enter 2 to see total available memory")
            print("Enter 3 to see total used memory percentage")
            print("Enter 0 to return to main menu")
            memory_menu = int(input())
            if memory_menu == 1:
                print("Total system memory")
                total_system_memory = psutil.virtual_memory().total
                print(bytes2human(total_system_memory))
# the psutil.virtual_memory().total command is used to get the total amount of memory in the system
            elif memory_menu == 2:
                print("Total available memory")
                total_available_memory = psutil.virtual_memory().available
                print(bytes2human(total_available_memory))
# the psutil.virtual_memory().available command is used to get the total amount of available memory in the system
            elif memory_menu == 3:
                print("Total used memory percentage")
                total_used_memory_percentage = psutil.virtual_memory().percent
                print(total_used_memory_percentage, "%")
# the psutil.virtual_memory().percent command is used to get the total amount of used memory in the system
            elif memory_menu == 0:
                break
        elif memory_menu == 2:
            print("Enter 1 to see total swap memory")
            print("Enter 2 to see total available swap memory")
            print("Enter 3 to see total used swap memory percentage")
            memory_menu = int(input())
            if memory_menu == 1:
                print("Total swap memory")
                total_swap_memory = psutil.swap_memory().total
                print(bytes2human(total_swap_memory))
            elif memory_menu == 2:
                print("Total available swap memory")
                total_available_swap_memory = psutil.swap_memory().free
                print(bytes2human(total_available_swap_memory))
            elif memory_menu == 3:
                print("Total used swap memory percentage")
                total_used_swap_memory_percentage = psutil.swap_memory().percent
                print(total_used_swap_memory_percentage, "%")
# the psutil.swap_memory() command is used to get the total amount of swap memory in the system
        elif memory_menu == 3:
            active_memory = psutil.virtual_memory().active
            print("Active memory:", bytes2human(active_memory))
            inactive_memory = psutil.virtual_memory().inactive
            print("Inactive memory:", bytes2human(inactive_memory))
            buffers_memory = psutil.virtual_memory().buffers
            print("Buffers memory:", bytes2human(buffers_memory))
            cached_memory = psutil.virtual_memory().cached
            print("Cached memory:", bytes2human(cached_memory))
            shared_memory = psutil.virtual_memory().shared
            print("Shared memory:", bytes2human(shared_memory))
            print("Enter 0 to return to main menu")
            memory_menu = int(input())
            if memory_menu == 0:
                break
        elif memory_menu == 0:
            break
        else:
            print("Not an option try again")
    except ValueError:
        print("Please enter a number")
    except FileNotFoundError:
        print("File not found")
    except KeyboardInterrupt:
        print("Keyboard interrupt")
