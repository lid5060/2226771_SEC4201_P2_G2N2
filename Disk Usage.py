import subprocess

def run_bash_script(script_path):
    try:
        output = subprocess.check_output(['bash', script_path])
        print(output.decode('utf-8'))
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'script.sh' with your bash script path
run_bash_script('Disk_Usage.sh')