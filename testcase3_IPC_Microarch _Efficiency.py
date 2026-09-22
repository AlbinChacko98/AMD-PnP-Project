from test_utility import run_cmd, log_output

def test_ipc():
    print("Running perf stat...")
    perf = run_cmd("perf stat -e instructions,cycles,cache-misses sleep 5")
    
    print("Running AMD uProf (if installed)...")
    uprof = run_cmd("AMDuProfCLI collect -m ipc -d 10")
    
    log_output("ipc_test", perf + "\n" + uprof)

if __name__ == "__main__":
    test_ipc()