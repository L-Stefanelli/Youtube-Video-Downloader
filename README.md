YouTube Downloader

A desktop app for downloading YouTube videos as MP4 files, with a dark interface built on CustomTkinter. Paste a link, click Download, and the video is saved in the best video and audio quality available.

How it works

The app uses yt-dlp to fetch the best video and audio streams separately and FFmpeg to merge them into a single MP4 file. The window has a text field for the URL, a Download button, and a Clear button that empties the field. If a download fails, an error popup is shown.

Requirements
Python 3.9 or newer
FFmpeg (needed to merge video and audio)
The customtkinter and yt-dlp packages

Tkinter ships with most Python installations. On Linux you may need to install the python3-tk package.

Installation

Clone the repository and install the dependencies:

bash
git clone https://github.com/YOUR_USERNAME/YT_downloader.git
cd YT_downloader
pip install customtkinter yt-dlp

Download FFmpeg from https://ffmpeg.org/download.html and extract it inside the project folder, for example ffmpeg/, so that ffmpeg/bin/ffmpeg.exe exists.

FFmpeg configuration

The FFmpeg path is hardcoded in the yt-dlp call, in the ffmpeg_location option. Replace the value with the path to the bin folder of your own FFmpeg install:

python
"ffmpeg_location": r"C:\path\to\ffmpeg\bin",

If FFmpeg is already on your system PATH, you can remove that line.

Usage
bash
python main.py
Paste the video URL into the text field.
Click Download.
Wait for the process to finish. Progress is printed in the terminal where the app was started.

The video is saved in the folder the app was launched from.

Disclaimer

Only download content you have permission to copy. Downloading videos may violate YouTube's Terms of Service and the creator's copyright.

Author

L-Stefanelli
