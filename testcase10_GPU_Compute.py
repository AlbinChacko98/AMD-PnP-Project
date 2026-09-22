# tests/gpu_compute.py
from test_utility import run_cmd, log_output

def run():
    clinfo = run_cmd("clinfo | grep -E 'Device|Compute Units'")
    clpeak = run_cmd("clpeak")

    output = f"""
=== GPU COMPUTE ===
{clinfo}

{clpeak}
"""
    log_output("gpu_compute", output)

if __name__ == "__main__":
    run()