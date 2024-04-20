import psutil
while True:
    print("Enter 1 to see CPU cores")
    print("Enter 2 to see CPU frequency")
    print("Enter 3 to see CPU states")
    print("Enter 4 to see CPU load")
    print("Enter 0 to return to main menu")
    try:
        CPU_Usage_menu = int(input())
        if CPU_Usage_menu == 1:
            print("Your device has", psutil.cpu_count(logical=False), "CPU cores")
            print("Your device has", psutil.cpu_count(logical=True), "CPU threads")
# logical = false makes psutil only count cores instead of threads
# logical = true makes psutil count threads instead of cores
        if CPU_Usage_menu == 2:
            print("Your device's current CPU frequency is", psutil.cpu_freq().current, "MHz")
            print("Your device's minimum CPU frequency is", psutil.cpu_freq().min, "MHz")
            print("Your device's maximum CPU frequency is", psutil.cpu_freq().max, "MHz")
# the current, min and max commands are used to get the current, minimum and maximum frequencies of the CPU
        if CPU_Usage_menu == 3:
            print("Your CPU times are")
            print("User:", psutil.cpu_times().user, "seconds")
            print("System:", psutil.cpu_times().system, "seconds")
            print("Idle:", psutil.cpu_times().idle, "seconds\n")
# the user, system and idle commands are used to get the time the CPU has spent in the user,
# system and idle states of the CPU
            print("Your CPU stats are")
            print("Context switches:", psutil.cpu_stats().ctx_switches)
            print("Interrupts:", psutil.cpu_stats().interrupts)
            print("Soft interrupts:", psutil.cpu_stats().soft_interrupts)
            print("Syscalls:", psutil.cpu_stats().syscalls)
# the ctx_switches, interrupts, soft_interrupts and syscalls commands are used to get the number
# of context switches, interrupts, soft interrupts and syscalls
        if CPU_Usage_menu == 4:
            load1, load5, load15 = psutil.getloadavg()
            print("Your CPU load averages are")
            print("1 minute:", load1)
            print("5 minutes:", load5)
            print("15 minutes:", load15)
# the getloadavg command is used to get the load averages of the CPU,
# and then it is printed to the screen for the user to see
        if CPU_Usage_menu == 0:
            break
    except ValueError:
        print("Please enter a number")
    except FileNotFoundError:
        print("File not found")
    except KeyboardInterrupt:
        print("Keyboard interrupt")
# the try will try and execute the code, if it fails it will print the error message in the except block
# an error is happening when loading a file for the main menu when the user enters 0,
# changing it to a break statement seems to have fixed the issue so that it doesn't start an infinite loop
