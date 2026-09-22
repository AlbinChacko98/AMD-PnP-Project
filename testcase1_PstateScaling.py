from test_utility import run_cmd, log_output
import time

def test_pstate():
    print("Checking AMD P-state driver...")
    driver = run_cmd("cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_driver")
    
    print("Setting performance governor...")
    run_cmd("sudo cpupower frequency-set -g performance")
    
    print("Capturing turbostat (5 sec)...")
    turbostat = run_cmd("sudo turbostat --interval 1 --num_iterations 5")
    
    log_output("pstate_test", driver + "\n" + turbostat)

if __name__ == "__main__":
    test_pstate()