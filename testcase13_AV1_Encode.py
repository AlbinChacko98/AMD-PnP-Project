# tests/av1_encode.py
from test_utility import run_cmd, log_output
import os

def run():
    if not os.path.exists("/dev/dri/renderD128"):
        log_output("av1_encode", "AV1 NOT AVAILABLE")
        return

    check = run_cmd("vainfo | grep AV1")

    encode = run_cmd("""
    ffmpeg -hwaccel vaapi -hwaccel_device /dev/dri/renderD128 \
    -f lavfi -i testsrc=duration=5:size=1280x720:rate=30 \
    -c:v av1_vaapi out_av1.mp4
    """)

    output = f"""
=== AV1 ENCODE ===
{check}

{encode}
"""
    log_output("av1_encode", output)

if __name__ == "__main__":
    run()