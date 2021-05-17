import moviepy.editor
import os
import Tkinter as tk

root = tk.Tk()
root.title("Enter directory path")

input_label = tk.Label(root, text="Enter directry path", font=("Arial", 12),
                          pady=10,
                          fg='black')
input_label.grid(row=0, column=0)
input_entry = tk.Entry(root, width=20, font=("Arial", 12))
input_entry.grid(row=0, column=1)

def get_duration():
    path = str(input_entry.get().replace('\\', '/'))
    
    file_list = os.listdir(path)

    def convert(seconds):
        mins = seconds // 60
        seconds %= 60

        return mins, seconds

    total_hours = 0
    total_minutes = 0
    total_seconds = 0

    for file_name in file_list:
        if file_name.count("mp4")>0 or file_name.count("mkv")>0 or file_name.count("MP4")>0 or file_name.count("MKV")>0:
            video = moviepy.editor.VideoFileClip(path + "\{}".format(file_name))
            video_duration = int(video.duration)
            mins, secs = convert(video_duration)
            total_minutes+=mins
            total_seconds+=secs

    new_seconds = total_seconds
    new_seconds/=60
    total_minutes+=new_seconds
    total_seconds%=60

    if total_minutes > 60:
        total_hours = total_minutes/60
        total_minutes%=60

    output_label = tk.Label(root, text="You have videos of Total duration: {} Hours, {} Minutes, {} seconds to watch".format(total_hours, total_minutes, total_seconds), font=("Arial", 12),
                          pady=10,
                          fg='black')
    output_label.grid(row=2, column=0, columnspan=2)

submit = tk.Button(root, text="Delete a flight record", command=get_duration,
                        font=("Arial", 10),
                        relief='raised',
                        bd=3,
                        bg='white')
submit.grid(row=1, column=0, pady=20, padx=20, ipadx=8, ipady=5, columnspan=2)

root.mainloop()