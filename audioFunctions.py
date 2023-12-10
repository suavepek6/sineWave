from os import path
from pydub import AudioSegment
from pydub.playback import play
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import pandas as pd


def convertToWav(origFile): 
    
    dst = "clap_sample.wav"
    
    sound = AudioSegment.from_mp3(origFile)
    sound.export(dst, format="wav")
    print("MP3 audio file converted to WAV")
    return dst
    
    
    ## Do/fix metadata later ##
 
def cleanData(soundFile):
    # Changing to monochannel
    
    '''
    dst = "clap_sample.wav"
    
    sound = AudioSegment.from_file(soundFile)
    print("Number of channels (originally):" , sound.channels)
    
    sound = sound.set_channels(1)
    print("Audiofile is set to monochannel", sound.channels)
    print("Number of seconds in audio file:", len(sound)/1000.0)
    '''
    
    

def audioPlot(soundFile):
    
    samplerate, data = wavfile.read(soundFile)
    
    length = data.shape[0] / samplerate
    print("Time of audio:", length)
    
    # Multichannel to mono by deleting other channels except one 
    if data.shape[len(data.shape)-1] > 1:
        data = data[:, 0]
        print("Data has been set to index 0")
    else:
        pass
    
    
    waveGraph = plt.figure(1)
    time = np.linspace(0., length, data.shape[0])
    plt.plot(time, data)
    plt.legend()
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    maxAmp = data.max()
    
    
    
    df = pd.DataFrame(data)
    maxidx = df[0].idxmax()
    print(maxidx) # MAX INDEX

    
    # waveGraph.show()
    
    
    
    ##### SPECTROGRAM (2nd plot) #####
    
    spectrumGraph = plt.figure(2)
    spectrum, freqs, t, im = plt.specgram(data, Fs=samplerate, NFFT=1024, cmap=plt.get_cmap('autumn_r'))
    cbar = plt.colorbar(im)
    plt.xlabel('Time [s]')
    plt.ylabel('Frequency (Hz)')
    cbar.set_label('Intensity (dB)')
    
    
    # print("LOOK HERE:", freqs[maxidx])
    
    
    # spectrumGraph.show()
    
    
    
    ##### REVERB (3rd plot) #####
    '''
    The three functions below are needed for reverb graphing.
    '''
    
    global range
    
    def find_target_frequency(freqs,range):
        for x in freqs:
            if x > range:
                break
        return x    
    
    
    
    def frequency_check():
        
        global target_frequency
        
        target_frequency = find_target_frequency(freqs,range)
        index_of_frequency = np.where(freqs == target_frequency)[0][0]
        
        # find sound data for a particular frequency
        
        data_for_frequency = spectrum[index_of_frequency]
        
        # change a digital signal for a values in decibels
        
        data_in_db_fun = 10 * np.log10(data_for_frequency)
        return data_in_db_fun
    
    
        # find a nearest value
    def find_nearest_value(array, value):
        array = np.asarray(array)
        idx = (np.abs(array - value)).argmin()
        return array[idx]
    
    
    ######################## MID RANGE ########################
    reverbGraphMid = plt.figure(3)
    range = 1000
    
    
    
    data_in_db = frequency_check()
    #plt.figure() (ignore)
    plt.plot(t, data_in_db, linewidth=1, alpha=0.7, color='#00ab00')
    plt.xlabel('Time (s)')
    plt.ylabel('Power (dB)')
    
    index_of_max = np.argmax(data_in_db)
    value_of_max = data_in_db[index_of_max]
    
    plt.plot(t[index_of_max], data_in_db[index_of_max], 'go')
    
    # slice array from a max value
    
    sliced_array = data_in_db[index_of_max:]
    
    value_of_max_less_5 = value_of_max - 5
    print("MID: VALUE_OF_MAX", value_of_max)
    print("MID: VALUE_OF_MAX_LESS_5", value_of_max_less_5)
    

    
    
    value_of_max_less_5 = find_nearest_value(sliced_array, value_of_max_less_5)
    index_of_max_less_5 = np.where(data_in_db == value_of_max_less_5)
    plt.plot(t[index_of_max_less_5], data_in_db[index_of_max_less_5], 'yo')
    
    # slice array from a max-5db
    value_of_max_less_25 = value_of_max - 25
    value_of_max_less_25 = find_nearest_value(sliced_array, value_of_max_less_25)
    index_of_max_less_25 = np.where(data_in_db == value_of_max_less_25)
    plt.plot(t[index_of_max_less_25], data_in_db[index_of_max_less_25], 'ro')
    
    rt20 = (t[index_of_max_less_25] - t[index_of_max_less_5])[0]
    print("MID RT20 VALUE: ", rt20)
    rt60Mid = 3 * rt20
    
    plt.grid()
    
    ######################## LOW RANGE ########################
    reverbGraphLow = plt.figure(4)
    range = 200
    
    data_in_db = frequency_check()
    #plt.figure() (ignore)
    plt.plot(t, data_in_db, linewidth=1, alpha=0.7, color='#b21000')
    plt.xlabel('Time (s)')
    plt.ylabel('Power (dB)')
    
    index_of_max = np.argmax(data_in_db)
    value_of_max = data_in_db[index_of_max]
    
    plt.plot(t[index_of_max], data_in_db[index_of_max], 'go')
    
    # slice array from a max value
    
    sliced_array = data_in_db[index_of_max:]
    
    value_of_max_less_5 = value_of_max - 5
    
    value_of_max_less_5 = find_nearest_value(sliced_array, value_of_max_less_5)
    index_of_max_less_5 = np.where(data_in_db == value_of_max_less_5)
    plt.plot(t[index_of_max_less_5], data_in_db[index_of_max_less_5], 'yo')
    
    # slice array from a max-5db
    value_of_max_less_25 = value_of_max - 25
    value_of_max_less_25 = find_nearest_value(sliced_array, value_of_max_less_25)
    index_of_max_less_25 = np.where(data_in_db == value_of_max_less_25)
    plt.plot(t[index_of_max_less_25], data_in_db[index_of_max_less_25], 'ro')
    
    rt20 = (t[index_of_max_less_25] - t[index_of_max_less_5])[0]
    print("LOW RT20 VALUE: ", rt20)
    rt60Low = 3 * rt20
    
    plt.grid()
    
    
    ######################## HIGH RANGE ########################
    reverbGraphHigh = plt.figure(5)
    range = 5000
    
    data_in_db = frequency_check()
    #plt.figure() (ignore)
    plt.plot(t, data_in_db, linewidth=1, alpha=0.7, color='#004bc6')
    plt.xlabel('Time (s)')
    plt.ylabel('Power (dB)')
    
    index_of_max = np.argmax(data_in_db)
    value_of_max = data_in_db[index_of_max]
    
    plt.plot(t[index_of_max], data_in_db[index_of_max], 'go')
    
    # slice array from a max value
    
    sliced_array = data_in_db[index_of_max:]
    
    value_of_max_less_5 = value_of_max - 5
    
    value_of_max_less_5 = find_nearest_value(sliced_array, value_of_max_less_5)
    index_of_max_less_5 = np.where(data_in_db == value_of_max_less_5)
    plt.plot(t[index_of_max_less_5], data_in_db[index_of_max_less_5], 'yo')
    
    # slice array from a max-5db
    value_of_max_less_25 = value_of_max - 25
    value_of_max_less_25 = find_nearest_value(sliced_array, value_of_max_less_25)
    index_of_max_less_25 = np.where(data_in_db == value_of_max_less_25)
    plt.plot(t[index_of_max_less_25], data_in_db[index_of_max_less_25], 'ro')
    
    rt20 = (t[index_of_max_less_25] - t[index_of_max_less_5])[0]
    print("HIGH RT20 VALUE: ",rt20)
    rt60High = 3 * rt20
    
    plt.grid()
    
    
    ### AVERAGE RT60 VALUE ###
    
    rt60Avg = (rt60Mid + rt60Low + rt60High) / 3 
    print("AVERAGE RT60 VALUE:", rt60Avg)
    
    #### SHOWTIME ####
    waveGraph.show()
    spectrumGraph.show()
    reverbGraphMid.show()
    reverbGraphLow.show()
    reverbGraphHigh.show()
    