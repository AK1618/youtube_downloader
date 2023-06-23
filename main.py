import tkinter as tk
from pytube import YouTube

def download_video():
    link = entry.get()
    try:
        yt = YouTube(link)
        title = yt.title
        views = yt.views
        status_label.config(text=f"Downloading: {title} (Views: {views})")
        yd = yt.streams.get_highest_resolution()
        yd.download("C:/Users/Downloads/youtube videos")
        status_label.config(text="Download completed!")
    except Exception as e:
        status_label.config(text="Error: " + str(e))

# Create the main window
window = tk.Tk()
window.title("YouTube Downloader")

# Create the input label and entry
label = tk.Label(window, text="Enter YouTube video link:")
label.pack()

entry = tk.Entry(window, width=50)
entry.pack()

# Create the download button
button = tk.Button(window, text="Download", command=download_video)
button.pack()

# Create the status label
status_label = tk.Label(window, text="")
status_label.pack()

# Start the main loop
window.mainloop()
