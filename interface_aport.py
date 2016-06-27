#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 12:05:09 2016

@author: alexis
"""

import pyaudio
import wave
import numpy as np

class InterfaceAport(object):
    
    def __init__(self):

        # Audio parameters
        self.bitrate_ = 44100
        self.channels_ = 1

        # create an audio object
        self.p_ = pyaudio.PyAudio()
        self.stream_ = None
        self.createStream()
        
    @property
    def bitrate(self):
        return self.bitrate_
    @bitrate.setter
    def bitrate(self, x):
        self.bitrate_=x
        self.createStream()
        
    @property
    def channels(self):
        return self.channels_
    @channels.setter
    def channels(self, x):
        self.channels_=x
        self.createStream()
            
    def __del__(self):
        self.p_.terminate()
        self.stream_.close()
        
    def createStream(self):
        if self.stream_ != None:
            self.stream_.close()
            
        self.stream_ = self.p_.open(
            format = self.p_.get_format_from_width(1), 
            channels = self.channels_, 
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
         
        self.stream_ = self.p_.open(
            format =self.p_.get_format_from_width(wf.getsampwidth()),
            channels = wf.getnchannels(),
            rate = wf.getframerate(),
            output = True)
            
        while data != '':
            self.stream_.write(data)
            data = wf.readframes(chunk)
            
        self.createStream()

if __name__ == "__main__":

    interface=InterfaceAport()
    
    #interface.playWave("ressources/COW_1.WAV")
    #interface.playTone(440,0.5,3) # f(Hz), rate of amplitude, duration (s)
    
    print interface.stream_.__dict__
    interface.bitrate=22000
    interface.channels=2
    print interface.stream_.__dict__
    
    #del interface
    

    