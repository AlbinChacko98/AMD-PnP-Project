# tests/video_decode.py
from test_utility import run_cmd, log_output
import os

def run():
    if not os.path.exists("/dev/dri/renderD128"):
        log_output("video_decode", "VAAPI NOT AVAILABLE")
        return

    decode = run_cmd("""
    ffmpeg -hwaccel vaapi -hwaccel_device /dev/dri/renderD128 \
    -f lavfi -i testsrc=duration=5:size=1280x720:rate=30 \
    -f null -
    """)

    output = f"""
=== VIDEO DECODE ===
{decode}
"""
    log_output("video_decode", output)

if __name__ == "__main__":
    run()