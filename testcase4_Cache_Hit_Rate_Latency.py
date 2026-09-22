from test_utility import run_cmd, log_output

def test_cache():
    print("Running perf cache metrics...")
    perf = run_cmd("perf stat -e L1-dcache-load-misses,LLC-load-misses sleep 5")
    
    print("Running cachegrind...")
    cachegrind = run_cmd("valgrind --tool=cachegrind ls")
    
    log_output("cache_test", perf + "\n" + cachegrind)

if __name__ == "__main__":
    test_cache()