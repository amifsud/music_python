#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 12:05:09 2016

@author: alexis
"""

from pyaudio import PyAudio
import wave
import numpy as np
import scipy.fftpack as fftp
import matplotlib.pyplot as plt

class InterfaceAport(object):
    
    def __init__(self):

        # Stream parameters
        self.bitrate_ = 44100
        self.channels_ = 1

        # create an audio object
        self.p_ = PyAudio()
        self.stream_ = None
        self.createStream()
        
    def __del__(self):
        self.p_.terminate()
        self.stream_.close()
        
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
                  
    def createStream(self):
        if self.stream_ != None:
            self.stream_.close()
            
        self.stream_ = self.p_.open(
            format = self.p_.get_format_from_width(1), 
            channels = self.channels_, 
            rate = self.bitrate_, 
            output = True)
            
    def normalizeSpectre(self,sin):
        
        sum=0
        for i in range(len(sin)-1):
           sum += sin[i+1][1]
           
        sout=sin
        sout[0][1]=1.0/(1.0+sum)
        
        for i in range(len(sin)-1):
           sout[i+1][1]=sout[0][1]*sin[i+1][1]
        
        return sout
       
    def playTone(self,sin,duration):

        numberofframes = int(self.bitrate_ * duration)
        
        if sin[0][0] != 0.0:
            numberofperiods = duration * sin[0][0]
            periodlength = int(numberofframes / numberofperiods)
        else:
            numberofperiods = 1
            periodlength = int(numberofframes)
        
        s=self.normalizeSpectre(sin)
        data=()        
        for x in xrange(periodlength):  
            y = 0.0
            for n in range(len(s)):
                y+=s[n][1]*np.sin(2*np.pi*s[n][0]*x/self.bitrate_)
            data+=(y,)

        self.playData(data,numberofperiods)
                  
    def playData(self, dataIn, repetitions):
        # Encodage
        data=''
        for x in xrange(int(len(dataIn))):
            data+=chr(int(dataIn[x]*127+128))
                        
        # Playing data
        for x in xrange(int(repetitions)):
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
        

    def fourier_series(self, x, y, wn=0, n=None):
        # get FFT
        myfft = fftp.fft(y, n)
        # kill higher freqs above wavenumber wn
        #myfft[wn:-wn] = 0
        # make new series
        y2 = fftp.ifft(myfft).real
        
        print myfft        
        
        plt.figure(num=None)
        plt.plot(x, y, x, y2)
        plt.show()

if __name__ == "__main__":

    interface=InterfaceAport()
    
#    interface.playWave("ressources/COW_1.WAV")
    
    f=220.0    
    
    s=[[f,1]]
    interface.playTone(s,3) # f(Hz), rate of amplitude, duration (s) 
    
    # Violon
    s=[[f, 140.0],
       [2*f, 80.0],
       [3*f, 15.0],
       [4*f, 45.0],
       [5*f, 75.0],
       [6*f, 1.0],
       [7*f, 12.0],
       [8*f, 30.0],
       [9*f, 2.0],
       [10*f, 2.0],
       [11*f, 5.0],
       [12*f, 2.0],
       [13*f, 5.0]]
    interface.playTone(s,3) # f(Hz), rate of amplitude, duration (s)
    
    # Violoncelle
    s=[[196, 1],
       [392, 2],
       [784, 1]]
    interface.playTone(s,3) # f(Hz), rate of amplitude, duration (s) 
    
    # Orgue
    f=220
    s=[[f, 0.5],
       [2*f, 1.0],
       [3*f, 0.2],
       [4*f, 0.3],
       [5*f, 0.1]]
    interface.playTone(s,3) # f(Hz), rate of amplitude, duration (s)    
    
#    print interface.stream_.__dict__
#    interface.bitrate=22000
#    interface.channels=2
#    print interface.stream_.__dict__
    
    #del interface
    
   