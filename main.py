import customtkinter as ctk
import yt_dlp
import tkinter as tk
from tkinter import messagebox

          
def clear():
    # Clear entry
    entry.delete(0, "end")  

def download():
    # This function is responsible for sending the Label text to yt_dlp and downloading the video.
    
    while True: 
        # loop to prevent errors
        try:
            text = entry.get()
            url = text
            
            yt_dlp.YoutubeDL({
                "format": "bestvideo+bestaudio/best",
                "merge_output_format": "mp4",
                "ffmpeg_location": r"C:\Users\luizs\Documents\Vscode\Projects\YT_downloader\ffmpeg\bin",
            }).download([url])
            
            break
        except:
            # Remove the Tkinter window
            root = tk.Tk()
            root.withdraw()
            
            # Show error pop-up
            messagebox.showerror("Error", "Invalid URL")  
            
            break


# Appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Window
app = ctk.CTk()
app.title("Youtube Downloader - By L-Stefanelli")
app.geometry("400x300")

# Label
label = ctk.CTkLabel(app, text="Insert Youtube URL", font=("Helvetica", 15))
label.pack(pady=20)

# Entry
entry = ctk.CTkEntry(
    master=app,
    width=200,
    height=30,
    border_width=2,
    corner_radius=10
)
entry.pack(pady=25)

# Button 1
get_button = ctk.CTkButton(master=app,text="Download", command=download)
get_button.pack(pady=5, padx=2)

# Button 2
get_button = ctk.CTkButton(master=app,text="Clear", command=clear)
get_button.pack(pady=5, padx=4)

app.mainloop()
