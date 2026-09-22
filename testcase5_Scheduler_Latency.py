from test_utility import run_cmd, log_output

def test_scheduler():
    print("Running cyclictest...")
    cyclic = run_cmd("cyclictest -p 99 -t 1 -n -i 1000 -D 10")
    
    print("Checking context switches...")
    vmstat = run_cmd("vmstat 1 5")
    
    log_output("scheduler_test", cyclic + "\n" + vmstat)

if __name__ == "__main__":
    test_scheduler()