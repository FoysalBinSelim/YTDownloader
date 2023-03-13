import tkinter
import customtkinter
from pytube import YouTube

def downloadvid():
    try:
        ytLink = urlbox.get()
        ytObject = YouTube(ytLink, on_progress_callback=progress_operation)
        video = ytObject.streams.get_lowest_resolution()
        header.configure(ytObject.title)
        message.configure(text="")
        video.download()
        message.configure(text="Download Successful!", text_color="orange")
    except:
        message.configure(text="Download Failed!", text_color="red")

def downloadaud():
    try:
        ytLink = urlbox.get()
        ytObject = YouTube(ytLink,on_progress_callback=progress_operation)
        audio = ytObject.streams.get_audio_only()
        header.configure(text=ytObject.title)
        message.configure(text="")
        audio.download()
        message.configure(text="Download Successful!", text_color="orange")
    except:
        message.configure(text="Download Failed!", text_color="red")

       
def progress_operation(stream,chunk,bytes_remaining):
    file_size=stream.filesize
    downloaded_file=file_size - bytes_remaining
    percentages=str(int (downloaded_file / file_size * 100))
    progress.configure(text=percentages + '%')
    progress.update()
    progressbar.set(float(percentages)/100)
    progressbar.update()

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()
app.title("Youtube Downlaoder")
app.geometry("780x400")

header = customtkinter.CTkLabel(app, text="Paste Your Youtube URL Below", font=('azonix', 16))
header.pack(padx=10, pady=15)

text_val = tkinter.StringVar()
urlbox = customtkinter.CTkEntry(app, width= 480, height= 40, corner_radius= 26, textvariable=text_val)
urlbox.pack(padx=10, pady=5)

progress = customtkinter.CTkLabel(app, text="")
progress.pack(padx=10, pady=2)

progressbar = customtkinter.CTkProgressBar(app, width=300, height=5, corner_radius= 26, fg_color="grey", progress_color="blue")
progressbar.set(0)
progressbar.pack(padx=10, pady=2)

button = customtkinter.CTkButton(app, text="Downlaod Video", command=downloadvid)
button.pack(padx=10, pady=10)

audio_button = customtkinter.CTkButton(app, text="Downlaod Audio", command=downloadaud)
audio_button.pack(padx=10, pady=10)

message = customtkinter.CTkLabel(app,text="")
message.pack(pady=10)

app.mainloop()