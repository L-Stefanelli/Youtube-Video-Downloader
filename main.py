import os
import customtkinter as ctk
import yt_dlp
from tkinter import messagebox

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOWNLOADS_DIR = os.path.join(BASE_DIR, "downloads")

FORMATS = {
    "Best quality": "bestvideo+bestaudio/best",
    "1080p": "bv*[height<=1080]+ba/b",
    "720p": "bv*[height<=720]+ba/b",
    "480p": "bv*[height<=480]+ba/b",
    "Poor quality": "worstvideo+worstaudio/worst",
}

def download():
    url = url_entry.get().strip()
    if not url:
        messagebox.showwarning("Warning", "Insert a URL")
        return

    os.makedirs(DOWNLOADS_DIR, exist_ok=True)

    ydl_opts = {
        "format": FORMATS[quality_var.get()],
        "merge_output_format": "mp4",
        "outtmpl": os.path.join(DOWNLOADS_DIR, "%(title)s.%(ext)s"),
    }

    try:
        status_label.configure(text="Downloading... please wait", text_color="blue")
        app.update()

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        status_label.configure(text="Download finished!", text_color="green")
        messagebox.showinfo("Success", "Download finished!")

    except Exception as e:
        status_label.configure(text="Error", text_color="red")
        messagebox.showerror("Error", f"Error: {e}")

app = ctk.CTk()
app.title("YouTube Downloader")
app.geometry("400x300")

url_label = ctk.CTkLabel(app, text="Insert YouTube URL", font=("Helvetica", 15))
url_label.pack(pady=20)

url_entry = ctk.CTkEntry(
    master=app,
    width=200,
    height=30,
    border_width=2,
    corner_radius=10
)
url_entry.pack(pady=25)

quality_label = ctk.CTkLabel(app, text="Select quality", font=("Helvetica", 15))
quality_label.pack(pady=20)

quality_var = ctk.StringVar(value="Best quality")
quality_menu = ctk.CTkOptionMenu(app, variable=quality_var, values=list(FORMATS))
quality_menu.pack(pady=5)

download_button = ctk.CTkButton(master=app, text="Download", command=download)
download_button.pack(pady=15)

status_label = ctk.CTkLabel(app, text="")
status_label.pack(pady=15)

app.mainloop()
