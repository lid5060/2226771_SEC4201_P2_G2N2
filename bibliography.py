while True:
    print("Bibliography")
    print("Chris, K., 2022. with open in python with statement syntax example. [Online]")
    print("Available at: https://www.freecodecamp.org/news/with-open-in-python-with-statement-syntax-example/")
    print("[Accessed 14 March 2024]")
    print("user3063850, 2014. psutil virtual memory units of measurement?.[Online]")
    print("Available at: https://stackoverflow.com/questions/21792655/psutil-virtual-memory-units-of-measurement")
    print("[Accessed 15 March 2024]")
    print("Cruz, R.S., 2018. Bash scripting cheatsheet.[Online]")
    print("Available at: https://devhints.io/bash")
    print("[Accessed 17 April 2024]")
    print("geeks, g. f., 2024. Bash Scripting – Introduction to Bash and Bash Scripting. [Online]")
    print("Available at: https://www.geeksforgeeks.org/bash-scripting-introduction-to-bash-and-bash-scripting/")
    print("[Accessed 17 April 2024]")
    print("Hira, Z., 2023. Bash Scripting Tutorial – Linux Shell Script and Command Line for Beginners. [Online]")
    print("Available at: Available at: https://www.freecodecamp.org/news/bash-scripting-tutorial-linux-shell-script-and-command-line-for-beginners/")
    print("[Accessed 17 April 2024]")
    try:
        print("Enter 0 to return to main menu")
        bibliography_menu = int(input())
        if bibliography_menu == 0:
            break
    except Exception:
        print("An error has occurred, please try again")