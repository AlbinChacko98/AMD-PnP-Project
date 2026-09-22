# tests/gpu_monitor.py
from test_utility import run_cmd, log_output
import os

def run():
    if not os.path.exists("/dev/dri"):
        log_output("gpu_monitor", "GPU NOT AVAILABLE (WSL/No iGPU access)")
        return

    radeontop = run_cmd("radeontop -d /dev/dri/card0 -l 1")
    clocks = run_cmd("rocm-smi --showclocks")
    util = run_cmd("rocm-smi --showuse")

    output = f"""
=== GPU MONITOR ===
{radeontop}

{clocks}

{util}
"""
    log_output("gpu_monitor", output)

if __name__ == "__main__":
    run()