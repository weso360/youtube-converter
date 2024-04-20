import os
import subprocess
from pytube import YouTube

# Specify the full path to the ffmpeg executable
FFMPEG_PATH = '/path/to/ffmpeg'

def download_video(url, output_path):
    yt = YouTube(url)
    yt.streams.filter(only_audio=True).first().download(output_path)
    return yt.title + ".mp4"

def convert_to_mp3(input_file, output_file):
    command = [FFMPEG_PATH, "-i", input_file, "-vn", "-ar", "44100", "-ac", "2", "-ab", "192k", output_file]
    subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def main():
    url = input("Enter the YouTube video URL: ")
    output_path = os.path.join(os.path.expanduser("~"), "Downloads")

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    video_file = download_video(url, output_path)
    mp3_file = os.path.join(output_path, os.path.splitext(video_file)[0] + ".mp3")
    convert_to_mp3(os.path.join(output_path, video_file), mp3_file)

    print(f"MP3 file saved as: {mp3_file}")

if __name__ == "__main__":
    main()
