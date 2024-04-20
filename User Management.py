import subprocess
import os
try:
    print("Welcome to the User Management section")
    print("Enter 1 to create a user")
    print("Enter 2 to create a group")
    print("Enter 3 to modify a users password")
    print("Enter 4 to modify a users group/permissions on a file")
    print("Enter 5 to delete a user")
    menu = int(input())
    if menu == 1:
        def bash_create_user(script_path):
            try:
                output = subprocess.check_output(['bash', script_path])
                print(output.decode('utf-8'))
            except Exception as e:
                print(f"An error occurred: {e}")
        bash_create_user('Add_User.sh')
    elif menu == 2:
        def bash_create_group(script_path):
            try:
                output = subprocess.check_output(['bash', script_path])
                print(output.decode('utf-8'))
            except Exception as e:
                print(f"An error occurred: {e}")
    elif menu == 3:
        def bash_modify_password(script_path):
            try:
                output = subprocess.check_output(['bash', script_path])
                print(output.decode('utf-8'))
            except Exception as e:
                print(f"An error occurred: {e}")
    elif menu == 4:
        def bash_modify_group(script_path):
            try:
                output = subprocess.check_output(['bash', script_path])
                print(output.decode('utf-8'))
            except Exception as e:
                print(f"An error occurred: {e}")
    elif menu == 5:
        def bash_delete_user(script_path):
            try:
                output = subprocess.check_output(['bash', script_path])
                print(output.decode('utf-8'))
            except Exception as e:
                print(f"An error occurred: {e}")
    else:
        print("Not an option try again")
except ValueError:
    print("Please enter a number")
except FileNotFoundError:
    print("File not found")
except KeyboardInterrupt:
    print("Keyboard interrupt")
except TypeError:
    print("Type error")
