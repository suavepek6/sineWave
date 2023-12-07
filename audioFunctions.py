from os import path
from pydub import AudioSegment
from pydub.playback import play

def convertToWav(origFile): 
    
    dst = "clap_sample.wav"
    
    sound = AudioSegment.from_mp3(origFile)
    sound.export(dst, format="wav")
    print("MP3 audio file converted to WAV")
 
def cleanData(soundFile):
    # Changing to monochannel
    sound = AudioSegment.from_file(soundFile)
    print("Number of channels (originally):" , sound.channels)
    sound = sound.set_channels(1)
    print("Audiofile is set to monochannel", sound.channels)
    print("Number of seconds in audio file:", len(sound)/1000.0)
    
    # Show number of seconds of audio file