from test_utility import run_cmd, log_output

def test_cpu_throughput():
    print("Running sysbench...")
    sysbench = run_cmd("sysbench cpu --cpu-max-prime=50000 --threads=$(nproc) run")
    
    print("Running stress-ng...")
    stress = run_cmd("stress-ng --cpu 0 --timeout 30 --metrics-brief")
    
    log_output("cpu_throughput", sysbench + "\n" + stress)

if __name__ == "__main__":
    test_cpu_throughput()