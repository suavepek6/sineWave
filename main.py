
from audioFunctions import convertToWav

def main():
 ## The main code execution happens here
    fileSample = "clap_sample.mp3"
    convertToWav(fileSample)

main()

"""A programming language survey written in Python with Tkinter"""
import tkinter as tk
from tkinter.ttk import Label
from tkinter import *
from tkinter.font import Font
# Create the root window
root = tk.Tk()
# set the title
root.title('AudioFile Analysis')
# set the root window size
#root.geometry('400x300')
root.resizable(True, False)
# Widgets
# Use a Label to show the title

t = 3.44
freq = 5000
rt60 = 600
timemsg = f'Time: ' + str(t) + f' seconds'
freqmsg= f'Frequency: ' + str(freq) + f' Hz'
rt60msg= f'RT60: ' + str(rt60) + f' Hz'

bg = PhotoImage(file="soundwave0.png")

# Show image using label
label1 = Label(root, image=bg)
label1.place(x=0, y=0)
# Add image file

label = tk.Message(root, text = "File Analysis Data: ", pady = 10, font = "300", width = 150,bg= 'white',fg='#FF3D86')
rt60message = tk.Message(root, text = rt60msg, width = 150,bg= 'white',fg='#FF3D86')
freqmessage = tk.Message(root, text = freqmsg, width = 150,bg= 'white',fg='#FF3D86')
timemessage = tk.Message(root, text = timemsg, width = 150,bg= 'white',fg='#FF3D86')
'''
label.pack()
timemessage.pack()
freqmessage.pack()
rt60message.pack()
'''

title = tk.Label(
root,
text='Audio Analysis',
font=('Arial 16 bold'),
bg='white',
fg='#C88BFF'
)

title.grid( row=1, column=2)
label.grid(row=2, column=1)



timemessage.grid(row=5, column=1)
rt60message.grid(row=3, column=1)
freqmessage.grid(row=4, column=1)


load = tk.Button(root, text='Upload Audiofile',bg= 'white',fg ='#BD74FF')
#freqmessage.grid(row=4, columnspan=2, sticky=tk.W, pady=10)
load.grid(row=6, column=2,columnspan=1, sticky=tk.W + tk.E, padx=25, pady =20)

lowfreq = tk.Button(root, text='Low Frequency',bg= 'white',fg='#6173FF')
lowfreq.grid(row=3, column=3,columnspan=1, sticky=tk.W + tk.E, padx=25, pady =1)
medfreq = tk.Button(root, text='Med Frequency',bg= 'white',fg='#6173FF')
medfreq.grid(row=4, column=3,columnspan=1, sticky=tk.W + tk.E, padx=25,pady =1)
highfreq = tk.Button(root, text='High Frequency',bg= 'white',fg='#6173FF')
highfreq.grid(row=5, column=3,columnspan=1, sticky=tk.W + tk.E, padx=25,pady =1)

root.mainloop()
