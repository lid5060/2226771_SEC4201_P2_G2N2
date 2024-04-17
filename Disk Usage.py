import subprocess

def run_bash_script(script_path):
    try:
        output = subprocess.check_output(['bash', script_path])
        print(output.decode('utf-8'))
    except Exception as e:
        print(f"An error occurred: {e}")

print("Your disk usage is:")
run_bash_script('Disk_Usage.sh')
input("Press enter to continue")