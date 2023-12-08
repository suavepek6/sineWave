from os import path
from pydub import AudioSegment
from pydub.playback import play

def convertToWav(origFile): 
    
    dst = "clap_sample_NEW.wav"
    
    sound = AudioSegment.from_mp3(origFile)
    return sound.export(dst, format="wav")
    print("MP3 audio file converted to WAV")
 
def channelInfo(soundFile):
    # Changing to monochannel
    sound = AudioSegment.from_file(soundFile)
    print("Number of channels (originally):" , sound.channels)
    sound = sound.set_channels(1)
    print("Audiofile is set to monochannel", sound.channels)
    
    # Show number of seconds of audio file
    print("Number of seconds in audio file:", len(sound)/1000.0)
    
    # Show (and remove) metadata
   
def removeMeta(soundFile):
    sound = AudioSegment.from_file(soundFile, format="wav")
    sound.export(soundFile, tags={'artist':None})