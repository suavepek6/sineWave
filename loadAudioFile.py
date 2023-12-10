import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from audioFunctions import *

gfile = ''
# create the root window
root = tk.Tk()
root.title('Acoustics Sampling GUI (TESTING)')
root.resizable(False, False)
root.geometry('300x150')

'''
tkinter.filedialog.askopenfilenames(**options)
Create an Open dialog and 
return the selected filename(s) that correspond to 
existing file(s).
'''
def select_file():
    filetypes = (
        ('WAV files', '*.wav'),
        ('MP3 files', '*.mp3*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    gfile = filename
    
    if gfile.endswith('.mp3'):
        gfile = convertToWav(gfile)

    # tkinter.messagebox — Tkinter message prompts
    showinfo(
        title='Selected File',
        message=filename
    )
    
    cleanData(gfile)
    
    audioPlot(gfile)

    gfile_label = ttk.Label(root, text=gfile)
    gfile_label.pack(side="bottom")


# open button
open_button = ttk.Button(
    root,
    text='Open a File',
    command=select_file
)


open_button.pack(expand=True)


# run the application
root.mainloop()
