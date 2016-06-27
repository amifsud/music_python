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
        print "Récupération du nombre de roues"
        return self._b

    def setb(self, v):
        print "Changement du nombre de roues"
        self._b  =  v
        
    def playTone(self):
        #See http://en.wikipedia.org/wiki/Bit_rate#Audio
        bitrate = 44100 #number of frames per second/frameset.      

        #See http://www.phy.mtu.edu/~suits/notefreqs.html
        f = 2109.89 #Hz, waves per second, 261.63=C4-note.
        duration = 1.2 #seconds to play sound
    
        numberofframes = int(bitrate * duration)
        restframes = numberofframes % bitrate
        data = ''    

        for x in xrange(numberofframes):
            data = data+chr(int(np.sin(x/((bitrate/f)/3.14))*127+128))    

        #fill remainder of frameset with silence
        for x in xrange(restframes): 
                data = data+chr(128)

        stream = self._p.open(format = self._p.get_format_from_width(1), 
            channels = 1, 
            rate = bitrate, 
            output = True)
        stream.write(data)  

        # cleanup stuff.
        self._stream.close() 
              
    def playWave(self, fileName):      
        # duration of data to read.
        chunk = 512 #1024
        # open the file for reading.
        wf = wave.open(fileName, 'rb')    
         
        # open stream based on the wave object which has been input.
        self._stream = self._p.open(format =
                  self._p.get_format_from_width(wf.getsampwidth()),
                  channels = wf.getnchannels(),
                  rate = wf.getframerate(),
                  output = True)
            
#        print 'format=' + str(self._p.get_format_from_width(wf.getsampwidth()))
#        print 'channels=' + str(wf.getnchannels())
#        print 'rate=' + str(wf.getframerate())
#        print 'output=' + str(True)
                    
        # play stream (looping from beginning of file to the end)            
                    # read data (based on the chunk size)
                    
        data = wf.readframes(chunk)
        while data != '':
            # writing to the stream is what *actually* plays the sound.
            self._stream.write(data)
            data = wf.readframes(chunk)

        # cleanup stuff.
        self._stream.close()    
            
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
        sound=sys.argv[1]
        
    #interface.playWave(sound)
    interface.playTone()

    