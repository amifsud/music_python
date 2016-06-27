#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 12:05:09 2016

@author: alexis
"""

import pyaudio
import wave
import numpy as np

class InterfaceAport:
    
    def __init__(self):
        # Attributs
        self._b=1

        # create an audio object
        self._p = pyaudio.PyAudio()
        self._stream = None
        
    def __del__(self):
        self._p.terminate()      
        
    def getb(self):
        return self._b

    def setb(self, v):
        self._b  =  v
        
    def playTone(self):
        bitrate = 44100 #number of frames per second/frameset.      
        f = 2*440 #Hz, waves per second, 261.63=C4-note.
        duration = 1 #seconds to play sound
        amp=0.5
    
        numberofframes = int(bitrate * duration)
#        restframes = numberofframes % bitrate
        data = ''    

        for x in xrange(numberofframes):
            data = data+chr(int(amp*np.sin(x/((bitrate/f)/3.14))*127+128))    

#        #fill remainder of frameset with silence
#        for x in xrange(restframes): 
#            print 'b'                
#            data = data+chr(128)

        self._stream = self._p.open(format = self._p.get_format_from_width(1), 
            channels = 1, 
            rate = bitrate, 
            output = True)
        self._stream.write(data)  

        # cleanup stuff.
        self._stream.close() 
              
    def playWave(self, fileName):
        
        chunk = 1024
        wf = wave.open(fileName, 'rb')    
        data = wf.readframes(chunk)
         
        # open stream based on the wave object which has been input.
        self._stream = self._p.open(format =
                  self._p.get_format_from_width(wf.getsampwidth()),
                  channels = wf.getnchannels(),
                  rate = wf.getframerate(),
                  output = True)
            
        while data != '':
            # writing to the stream is what *actually* plays the sound.
            self._stream.write(data)
            data = wf.readframes(chunk)

        # cleanup stuff.
        self._stream.close()    
            
    b=property(getb, setb)
            

if __name__ == "__main__":

    sound="ressources/COW_1.WAV"     
    
    interface=InterfaceAport()
    interface.playWave(sound)
    interface.playTone()

    