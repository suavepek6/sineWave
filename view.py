# Code structure based on template provided by Dr. Navarro

import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Label
from tkinter import filedialog as fd
from tkinter import *
from tkinter.font import Font
from tkinter.messagebox import showinfo
import matplotlib.pyplot as plt
from controller import Controller
from model import Model

class View(ttk.Frame):
    global t, freq, rt60
    def __init__(self, parent):
        super().__init__(parent)
        # create widgets
        # label

        # Create the root window
        self = tk.Tk()

        # set the title
        self.title('AudioFile Analysis')

        #root.geometry('400x300')
        self.resizable(True, False)

        self.t = 3.44
        self.freq = 5000
        self.rt60 = 600
        self.controller = None
        self.controllerSet = FALSE
        self.timemsg = f'Time: ' + str(self.t) + f' seconds'
        self.freqmsg= f'Resonant Frequency: ' + str(self.freq) + f' Hz'
        self.rt60msg= f'RT60 difference from 0.5: ' + str(self.rt60) + f' seconds'

    def UpdateGUI(self):
            self.timemsg = f'Time: ' + str(self.t) + f' seconds'
            self.freqmsg= f'Resonant Frequency: ' + str(self.freq) + f' Hz'
            self.rt60msg= f'RT60 difference from 0.5: ' + str(self.rt60) + f' seconds'
            

            

            self.bg = PhotoImage(file="soundwave.png")
            self.bgLabel = tk.Label(self, image=self.bg)
            self.bgLabel.place(x=0,y=0)

            # Show image using label
            # self.label1 = Label(self, image=self.bg)
            # self.label1.place(x=0, y=0)
            # Add image file

            self.datalabel = tk.Message(self, text = "File Analysis Data: ", font=('Calibri 15'), width = 200,bg= 'white',fg='#FF35BD')
            self.plotlabel = tk.Message(self, text = "File Analysis Plots: ", font=('Calibri 15'), width = 200,bg= 'white',fg='#2E61FF')

            self.freqmessage = tk.Message(self, text = self.freqmsg, width = 200,font=('Calibri 9'),bg= 'white',fg='#FF35BD')
            self.timemessage = tk.Message(self, text = self.timemsg, width = 200,font=('Calibri 9'),bg= 'white',fg='#FF35BD')
            self.rt60message = tk.Message(self, text = self.rt60msg, width = 220,font=('Calibri 9'),bg= 'white',fg='#FF35BD')

            self.wavplt = tk.Button(self, text='Waveform',font=('Calibri 9'), bg= 'white',fg ='#BD74FF',command=self.dispWave)
            self.spctplt = tk.Button(self, text='Spectrogram',font=('Calibri 9'), bg= 'white',fg ='#BD74FF',command=self.dispSumm)
            self.rt60plt = tk.Button(self, text='Combined RT60',font=('Calibri 9'), bg= 'white',fg ='#BD74FF',command=self.dispComb)

            self.lowfreq = tk.Button(self, text='Low Frequency',font=('Calibri 9'),padx=15,bg= 'white',fg='#2EACFF',command=self.dispLow)
            self.medfreq = tk.Button(self, text='Med Frequency',font=('Calibri 9'),padx=15,bg= 'white',fg='#2EACFF',command=self.dispMid)
            self.highfreq = tk.Button(self, text='High Frequency',font=('Calibri 9'),padx=15,bg= 'white',fg='#2EACFF',command=self.dispHigh)

            self.upload = tk.Button(self, text='Upload Audiofile',font=('Calibri 10'),pady=5, bg= 'white',fg ='#BD74FF',command=self.selFile)
            '''
            label.pack()
            timemessage.pack()
            freqmessage.pack()
            rt60message.pack()
            '''
            
            self.title = tk.Label(
            self,
            text='Audio Analysis',
            font=('Calibri 20'),
            bg='white',
            fg='#C88BFF'
            )

            self.title.grid( row=1, column=2, pady = 20)
            self.datalabel.grid(row=2, column=1,padx=20,pady=30)
            self.plotlabel.grid(row=2, column=2, columnspan=2,padx=20,pady=20)

            #waveform spectragram combined RT60

            self.timemessage.grid(row=3, column=1)
            self.rt60message.grid(row=5, column=1,padx=10)
            self.freqmessage.grid(row=4, column=1)


            self.wavplt.grid(row=3, column=2,columnspan=1, sticky=tk.W + tk.E, padx=10, pady =1)
            self.spctplt.grid(row=4, column=2,columnspan=1, sticky=tk.W + tk.E, padx=10, pady =1)
            self.rt60plt.grid(row=5, column=2,columnspan=1, sticky=tk.W + tk.E, padx=10, pady =1)



            #freqmessage.grid(row=4, columnspan=2, sticky=tk.W, pady=10)
            self.upload.grid(row=6, column=2,columnspan=1, sticky=tk.W + tk.E, padx=30, pady =30)


            self.lowfreq.grid(row=3, column=3,columnspan=1, sticky=tk.W + tk.E, padx=50, pady =1)
            self.medfreq.grid(row=4, column=3,columnspan=1, sticky=tk.W + tk.E, padx=50,pady =1)
            self.highfreq.grid(row=5, column=3,columnspan=1, sticky=tk.W + tk.E, padx=50,pady =1)
            
    
    def set_controller(self, controller):
        self.controller = controller
        self.controllerSet = TRUE
        self.UpdateGUI()
        
    
    def ShowPlot(self, newFig):
         newFig.show()
    
    def dispWave(self):
        if self.controllerSet:
            self.controller.DisplayFigure(0)

    def dispSumm(self):
        if self.controllerSet:
            self.controller.DisplayFigure(1)

    def dispComb(self):
        if self.controllerSet:
            self.controller.DisplayFigure(2)

    def dispLow(self):
        if self.controllerSet:
            self.controller.DisplayFigure(3)

    def dispMid(self):
        if self.controllerSet:
            self.controller.DisplayFigure(4)

    def dispHigh(self):
        if self.controllerSet:
            self.controller.DisplayFigure(5)

    def selFile(self):
        if self.controllerSet:
            self.controller.select_file()
            
