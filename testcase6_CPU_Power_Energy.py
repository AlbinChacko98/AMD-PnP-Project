from test_utility import run_cmd, log_output
import time

def test_power():
    print("Reading initial energy...")
    start = run_cmd("cat /sys/class/powercap/intel-rapl:0/energy_uj")
    
    print("Running CPU load...")
    run_cmd("stress-ng --cpu 0 --timeout 10")
    
    print("Reading final energy...")
    end = run_cmd("cat /sys/class/powercap/intel-rapl:0/energy_uj")
    
    print("Running turbostat...")
    turbostat = run_cmd("sudo turbostat --interval 1 --num_iterations 5")
    
    log_output("power_test", f"Start: {start}\nEnd: {end}\n" + turbostat)

if __name__ == "__main__":
    test_power()