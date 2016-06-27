#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 12:05:09 2016

@author: alexis
"""

import pyaudio
import wave

class InterfaceAport:
    
    def __init__(self):
        # Attributs
        self._b=1
        
    def getb(self):
        print "Récupération du nombre de roues"
        return self._b

    def setb(self, v):
        print "Changement du nombre de roues"
        self._b  =  v
        
    def playWave(self, fileName):
        '''
        From the example "play" of Pyaudio
        '''
        
        # length of data to read.
        chunk = 1024

        '''
        ************************************************************************
        This is the start of the "minimum needed to read a wave"
        ************************************************************************
        '''
        # open the file for reading.
        wf = wave.open(sound, 'rb')
          
        # create an audio object
        p = pyaudio.PyAudio()
         
        # open stream based on the wave object which has been input.
        stream = p.open(format =
                  p.get_format_from_width(wf.getsampwidth()),
                  channels = wf.getnchannels(),
                  rate = wf.getframerate(),
                  output = True)
                    
        # read data (based on the chunk size)
        data = wf.readframes(chunk)
                  
        # play stream (looping from beginning of file to the end)
        while data != '':
        # writing to the stream is what *actually* plays the sound.
            stream.write(data)
            data = wf.readframes(chunk)

        # cleanup stuff.
        stream.close()    
        p.terminate()
            
    b=property(getb, setb)
            

if __name__ == "__main__":
    import sys
    
    interface=InterfaceAport()
    a=interface.b
    
    # validation. If a wave file hasn't been specified, exit.
    if len(sys.argv) < 2:
        print "Plays a wave file.\n\n" +\
                "Usage: %s filename.wav" % sys.argv[0]
        sound="ressources/COW_1.WAV" 
    else:
        sound=sound
        
    interface.playWave(sound)

    