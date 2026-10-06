YouTube Downloader

A simple desktop app to download YouTube videos as MP4, built with Python, CustomTkinter and yt-dlp. Videos are saved in a downloads folder created next to the script.

Requirements

Python 3.10 or newer and FFmpeg available in your PATH. FFmpeg is needed to merge video and audio into MP4.

Installation
python -m pip install customtkinter yt-dlp
Usage
python main.py

Paste a YouTube URL, select the quality and click Download.

Troubleshooting

If you get ModuleNotFoundError for customtkinter, install the packages with the same Python you use to run the script, using python -m pip. If a valid URL fails, update yt-dlp with python -m pip install -U yt-dlp.
