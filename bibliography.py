while True:
    print("Bibliography")
    print("Chris, K., 2022. with open in python with statement syntax example. [Online]")
    print("Available at: https://www.freecodecamp.org/news/with-open-in-python-with-statement-syntax-example/")
    print("[Accessed 14 March 2024]")
    try:
        print("Enter 0 to return to main menu")
        menu = int(input())
        if menu == 0:
            with open('Main Menu.py') as file:
                exec(file.read())
    except Exception:
        print("An error has occurred, please try again")