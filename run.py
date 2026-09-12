import os
import subprocess

# Output path (Saves directly to your phone's Downloads)
output_file = "/sdcard/Download/mongodb_short.mp4"

# Define your lines
line1 = "Connecting MongoDB to Python \n     PYMONGO"
line2 = "Like and Subscribe for More!"

# Build the command with two separate text layers
ffmpeg_cmd = (
    f"ffmpeg -f lavfi -i color=c=0x1E293B:s=1080x1920:d=20 "
    f"-vf \""
    f"drawtext=text='{line1}':fontcolor=white:fontsize=64:x=(w-text_w)/2:y=(h-text_h)/2-50,"
    f"drawtext=text='{line2}':fontcolor=yellow:fontsize=48:x=(w-text_w)/2:y=(h-text_h)/2+50"
    f"\" "
    f"-c:v libx264 -pix_fmt yuv420p {output_file} -y"
)

print("🎬 Generating your 20-second video with two lines of text...")

try:
    subprocess.run(ffmpeg_cmd, shell=True, check=True)
    print(f"✅ Video created successfully! Check your phone's 'Download' folder.")
except subprocess.CalledProcessError as e:
    print(f"❌ Error generating video. Make sure storage permission is granted.")
