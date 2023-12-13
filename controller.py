# Code structure based on template provided by Dr. Navarro

from os import path
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import matplotlib.pyplot as plt


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.waveGraph = plt.figure()
        self.summGraph = plt.figure()
        self.combinedGraph = plt.figure()
        self.lowGraph = plt.figure()
        self.midGraph = plt.figure()
        self.highGraph = plt.figure()
        self.rt60Low = 0
        self.rt60Mid = 0
        self.rt60High = 0

    
    def NewAudio(self):
        self.model.SetData()
        self.model.monoChange()
        self.waveGraph = self.model.wavePlot()
        self.summGraph = self.model.summerPlot()
        self.lowGraph, self.rt60Low = self.model.reverbPlot(0)
        self.midGraph, self.rt60Mid = self.model.reverbPlot(1)
        self.highGraph, self.rt60High = self.model.reverbPlot(2)
        self.combinedGraph = self.model.combinedPlot()
        self.view.t = self.model.LengthToString()
        self.view.freq = self.model.CalcResFreq()
        self.view.rt60 = self.model.CalcRT60Diff(self.rt60Low, self.rt60Mid, self.rt60High)
        self.view.UpdateGUI()
    
    def select_file(self):
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
            gfile = self.model.convertToWav(gfile)
        else:
            self.model.sourceFile = gfile
        # tkinter.messagebox — Tkinter message prompts
        showinfo(
            title='Selected File',
            message=filename
        )
        self.NewAudio()


    def DisplayFigure(self, plotId):
        if(plotId == 0):
            self.view.ShowPlot(self.waveGraph)
        elif(plotId == 1):
            self.view.ShowPlot(self.summGraph)
        elif(plotId == 2):
            self.view.ShowPlot(self.combinedGraph)
        elif(plotId == 3):
            self.view.ShowPlot(self.lowGraph)
        elif(plotId == 4):
            self.view.ShowPlot(self.midGraph)
        elif(plotId == 5):
            self.view.ShowPlot(self.highGraph)