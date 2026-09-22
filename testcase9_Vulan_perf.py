# tests/vulkan_test.py
from test_utility import run_cmd, log_output

def run():
    vkinfo = run_cmd("vulkaninfo | grep -E 'apiVersion|driverVersion'")
    vkmark = run_cmd("vkmark -s 1920x1080")

    output = f"""
=== VULKAN TEST ===
{vkinfo}

{vkmark}
"""
    log_output("vulkan_test", output)

if __name__ == "__main__":
    run()