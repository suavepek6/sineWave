# Code structure and functions based on template and code provided by Dr. Navarro
from scipy.io import wavfile
import scipy.io
import matplotlib.pyplot as plt
import numpy as np
import pydub
from pydub import AudioSegment

class Model:
    global data, length, samplerate, t, freqs, spectrum
    def __init__(self,soundFile):
        self.sourceFile = soundFile

    @property
    def sourceFile(self):
        return self.__sourceFile
    
    @sourceFile.setter
    def sourceFile(self, value):
        self.__sourceFile = value
    
    def convertToWav(self, soundFile): 
    
        dst = "clap_sample.wav"

        sound = AudioSegment.from_mp3(soundFile)
        sound.export(dst, format="wav")
        self.sourceFile = dst

    def SetData(self):
        self.samplerate, self.data = wavfile.read(self.sourceFile)
        self.length = self.data.shape[0] / self.samplerate

    def LengthToString(self):
        return "%.2f"%self.length
    
    def monoChange(self):
        # Changing to monochannel
        if self.data.shape[len(self.data.shape)-1] > 1:
            self.data = self.data[:, 0]
        else:
            pass
    
    def wavePlot(self):
        waveGraph = plt.figure()
        time = np.linspace(0., self.length, self.data.shape[0])
        plt.plot(time, self.data)
        plt.legend()
        plt.xlabel("Time [s]")
        plt.ylabel("Amplitude")

        return waveGraph
    
    def summerPlot(self):
        
        spectroGraph = plt.figure()
        self.spectrum, self.freqs, self.t, im = plt.specgram(self.data, Fs=self.samplerate, NFFT=1024, cmap=plt.get_cmap('autumn_r'))
        cbar = plt.colorbar(im)
        plt.xlabel('Time [s]')
        plt.ylabel('Frequency (Hz)')
        cbar.set_label('Intensity (dB)')
        
        return spectroGraph
    
    def reverbPlot(self,optNum):
        if(optNum == 0):
            colorval = '#ab1000'
            range = 200
        elif(optNum == 1):
            colorval ='#00ab00'
            range = 1000
        elif(optNum == 2):
            colorval = '#0012a8'
            range = 5000
        
        def find_target_frequency(freqs,range):
            
            for x in freqs:
                if x > range:
                    break
            return x    
        
        
        
        def frequency_check(self):
            
            global target_frequency
            
            target_frequency = find_target_frequency(self.freqs,range)
            index_of_frequency = np.where(self.freqs == target_frequency)[0][0]
            
            # find sound data for a particular frequency
            
            data_for_frequency = self.spectrum[index_of_frequency]
            
            # change a digital signal for a values in decibels
            
            data_in_db_fun = 10 * np.log10(data_for_frequency)
            return data_in_db_fun
        
        
            # find a nearest value
        def find_nearest_value(array, value):
            array = np.asarray(array)
            idx = (np.abs(array - value)).argmin()
            return array[idx]
        
        ### COOKING TIME! ###
        reverbGraph = plt.figure()
        #if optNum < 1:
            
        #elif optNum == 4:
            #reverbGraph = plt.figure(1)
        
        data_in_db = frequency_check(self)
        #plt.figure() (ignore)
        plt.plot(self.t, data_in_db, linewidth=1, alpha=0.7, color=colorval)
        plt.xlabel('Time (s)')
        plt.ylabel('Power (dB)')
        
        index_of_max = np.argmax(data_in_db)
        value_of_max = data_in_db[index_of_max]
        
        plt.plot(self.t[index_of_max], data_in_db[index_of_max], 'go')
        
        # slice array from a max value
        
        sliced_array = data_in_db[index_of_max:]
        
        value_of_max_less_5 = value_of_max - 5
        
        value_of_max_less_5 = find_nearest_value(sliced_array, value_of_max_less_5)
        index_of_max_less_5 = np.where(data_in_db == value_of_max_less_5)
        plt.plot(self.t[index_of_max_less_5], data_in_db[index_of_max_less_5], 'yo')
        
        # slice array from a max-5db
        value_of_max_less_25 = value_of_max - 25
        value_of_max_less_25 = find_nearest_value(sliced_array, value_of_max_less_25)
        index_of_max_less_25 = np.where(data_in_db == value_of_max_less_25)
        plt.plot(self.t[index_of_max_less_25], data_in_db[index_of_max_less_25], 'ro')
        
        rt20 = (self.t[index_of_max_less_25] - self.t[index_of_max_less_5])[0]
        
        #reverbGraph.show()
        return reverbGraph, rt20*3
    
    def combinedPlot(self):
        i = 0
        while i < 3:

            if(i == 0):
                colorval = '#ab1000'
                range = 200
                graphLabel = 'Low Frequency'
            elif(i == 1):
                colorval ='#00ab00'
                range = 1000
                graphLabel = 'Mid Frequency'
            elif(i == 2):
                colorval = '#0012a8'
                range = 5000
                graphLabel = 'High Frequency'
            
            def find_target_frequency(freqs,range):
                
                for x in freqs:
                    if x > range:
                        break
                return x    
            
            
            
            def frequency_check(self):
                
                global target_frequency
                
                target_frequency = find_target_frequency(self.freqs,range)
                index_of_frequency = np.where(self.freqs == target_frequency)[0][0]
                
                # find sound data for a particular frequency
                
                data_for_frequency = self.spectrum[index_of_frequency]
                
                # change a digital signal for a values in decibels
                
                data_in_db_fun = 10 * np.log10(data_for_frequency)
                return data_in_db_fun
            
            
                # find a nearest value
            def find_nearest_value(array, value):
                array = np.asarray(array)
                idx = (np.abs(array - value)).argmin()
                return array[idx]
            
            ### COOKING TIME! ###
            reverbGraph = plt.figure(20)
            #if optNum < 1:
                
            #elif optNum == 4:
                #reverbGraph = plt.figure(1)
            
            data_in_db = frequency_check(self)
            #plt.figure() (ignore)
            plt.plot(self.t, data_in_db, linewidth=1, alpha=0.7, color=colorval, label=graphLabel)
            plt.xlabel('Time (s)')
            plt.ylabel('Power (dB)')
            
            index_of_max = np.argmax(data_in_db)
            value_of_max = data_in_db[index_of_max]
            
            plt.plot(self.t[index_of_max], data_in_db[index_of_max], 'go')
            
            # slice array from a max value
            
            sliced_array = data_in_db[index_of_max:]
            
            value_of_max_less_5 = value_of_max - 5
            
            value_of_max_less_5 = find_nearest_value(sliced_array, value_of_max_less_5)
            index_of_max_less_5 = np.where(data_in_db == value_of_max_less_5)
            plt.plot(self.t[index_of_max_less_5], data_in_db[index_of_max_less_5], 'yo')
            
            # slice array from a max-5db
            value_of_max_less_25 = value_of_max - 25
            value_of_max_less_25 = find_nearest_value(sliced_array, value_of_max_less_25)
            index_of_max_less_25 = np.where(data_in_db == value_of_max_less_25)
            plt.plot(self.t[index_of_max_less_25], data_in_db[index_of_max_less_25], 'ro')
            
            rt20 = (self.t[index_of_max_less_25] - self.t[index_of_max_less_5])[0]
            
            i += 1
        plt.legend()
        return reverbGraph

    def CalcRT60Diff(self, rt60Low, rt60Mid, rt60High):
        rt60Avg = (rt60Low + rt60Mid + rt60High) / 3
        rt60Diff = rt60Avg - 0.5
        return "%.2f"%rt60Diff
    
    def CalcResFreq(self):
        # Fourier Transform
        N = len(self.data)
        yf = np.fft.rfft(self.data)
        xf = np.fft.rfftfreq(N, 1 / self.samplerate)

        # Get the most dominant frequency and return it
        idx = np.argmax(np.abs(yf))
        freq = xf[idx]
        return "%.2f"%freq
        