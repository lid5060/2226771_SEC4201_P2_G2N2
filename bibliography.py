while True:
    f = open("bibliography.txt", "r")
    print(f.read())
    f.close()
    try:
        print("Enter 0 to return to main menu")
        bibliography_menu = int(input())
        if bibliography_menu == 0:
            break
    except Exception:
        print("An error has occurred, please try again")