while True:
    print("Bibliography")
    print("Chris, K., 2022. with open in python with statement syntax example. [Online]")
    print("Available at: https://www.freecodecamp.org/news/with-open-in-python-with-statement-syntax-example/")
    print("[Accessed 14 March 2024]")
    print("user3063850, 2014. psutil virtual memory units of measurement?.[Online]")
    print("Available at: https://stackoverflow.com/questions/21792655/psutil-virtual-memory-units-of-measurement")
    print("[Accessed 15 March 2024]")
    try:
        print("Enter 0 to return to main menu")
        bibliography_menu = int(input())
        if bibliography_menu == 0:
            break
    except Exception:
        print("An error has occurred, please try again")