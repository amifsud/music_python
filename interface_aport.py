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
              
    def playWave(self, fileName):      
        # length of data to read.
        chunk = 512 #1024
        # open the file for reading.
        wf = wave.open(fileName, 'rb')    
         
        # open stream based on the wave object which has been input.
        self._stream = self._p.open(format =
                  self._p.get_format_from_width(wf.getsampwidth()),
                  channels = wf.getnchannels(),
                  rate = wf.getframerate(),
                  output = True)
            
        print 'format=' + str(self._p.get_format_from_width(wf.getsampwidth()))
        print 'channels=' + str(wf.getnchannels())
        print 'rate=' + str(wf.getframerate())
        print 'output=' + str(True)
                    
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
        
    interface.playWave(sound)

    