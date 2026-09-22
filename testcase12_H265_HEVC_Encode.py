# tests/hevc_encode.py
from test_utility import run_cmd, log_output
import os

def run():
    if not os.path.exists("/dev/dri/renderD128"):
        log_output("hevc_encode", "VAAPI NOT AVAILABLE")
        return

    check = run_cmd("vainfo | grep HEVC")

    encode = run_cmd("""
    ffmpeg -hwaccel vaapi -hwaccel_device /dev/dri/renderD128 \
    -f lavfi -i testsrc=duration=5:size=1280x720:rate=30 \
    -c:v hevc_vaapi out_hevc.mp4
    """)

    output = f"""
=== HEVC ENCODE ===
{check}

{encode}
"""
    log_output("hevc_encode", output)

if __name__ == "__main__":
    run()