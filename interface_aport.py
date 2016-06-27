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

        # Audio parameters
        self.bitrate_ = 44100

        # create an audio object
        self.p_ = pyaudio.PyAudio()
        self.stream_ = None
        self.createDefaultStream()
              
    def __del__(self):
        self.p_.terminate()
        self.stream_.close()  
        
    def getBitrate(self):
        return self.bitrate_

    def setBitrate(self, v):
        self.bitrate_  =  v
        
    def createDefaultStream(self):
        self.stream_ = self.p_.open(format = self.p_.get_format_from_width(1), 
            channels = 1, 
            rate = self.bitrate_, 
            output = True)
        
    def playTone(self,f,amp,duration):
        numberofframes = int(self.bitrate_ * duration)
        
        data = ''    
        for x in xrange(numberofframes):
            data = data+chr(int(amp*np.sin(x/((self.bitrate_/f)/3.14))*127+128))    

        self.stream_.write(data)  
              
    def playWave(self, fileName):
        
        chunk = 1024
        wf = wave.open(fileName, 'rb')    
        data = wf.readframes(chunk)
         
        # open stream based on the wave object which has been input.
        self.stream_ = self.p_.open(format =
                  self.p_.get_format_from_width(wf.getsampwidth()),
                  channels = wf.getnchannels(),
                  rate = wf.getframerate(),
                  output = True)
            
        while data != '':
            # writing to the stream is what *actually* plays the sound.
            self.stream_.write(data)
            data = wf.readframes(chunk)
            
        self.createDefaultStream()
            
    bitrate=property(getBitrate, setBitrate)
            

if __name__ == "__main__":

    interface=InterfaceAport()
    
    interface.playWave("ressources/COW_1.WAV")
    interface.playTone(440,0.5,3) # f(Hz), rate of amplitude, duration (s)

    