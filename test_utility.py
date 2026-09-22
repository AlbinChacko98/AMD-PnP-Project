import subprocess
import time

def run_cmd(cmd):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        return str(e)

def log_output(test_name, output):
    with open(f"{test_name}_log.txt", "a") as f:
        f.write("\n===== OUTPUT =====\n")
        f.write(output + "\n")