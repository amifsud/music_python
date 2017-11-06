#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 12:05:09 2016

@author: alexis
"""

from pyaudio import PyAudio
from threading import Thread
import Queue

class InterfaceAport(Thread):
    
    def __init__(self, bitrate):
        Thread.__init__(self)

        # Stream parameters
        self.bitrate_ = bitrate
        self.channels_ = 1

        # create an audio object
        self.p_ = PyAudio()
        self.stream_ = None
        self.createStream()
        
        self.q = Queue.Queue()
        self.lastq = [None,0]
        
        self.play_ = True
        self.stop_ = False
        
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
                         
    def playData(self, dataIn, repetitions=None):
        # Encodage
        data=''
        for x in xrange(int(len(dataIn))):
            data+=chr(int(dataIn[x]*127+128))
                        
        self.q.put([data,repetitions])
            
    def run(self):
        while (self.stop_ == False): # stop = True on arrete tout
            if (self.q.qsize()!=0  and self.play_ == True): # Si il a a à jouer et que cest pas pause
                self.lastq = self.q.get()               
                if self.lastq[1] == None: # Si un nombre de repetition nest pas None
                    while self.lastq[1] == None and self.q.qsize()==0:
                       self.stream_.write(self.lastq[0]) # on joue a linfini
                else :
                    for x in xrange(int(self.lastq[1])):
                        self.stream_.write(self.lastq[0])
    
    def stopLast(self,repetitions=0):
        self.lastq[1] = repetitions

    def play(self):
        self.play_ = True
        self.stop_ = False
        
    def pause(self):
        self.play_ = False
        self.stop_ = False
        
    def stop(self):
        self.play_ = False
        self.stop_ = True
              
if __name__ == "__main__":

    interface=InterfaceAport()
    
#    interface.playWave("ressources/COW_1.WAV")
    
    f=220.0    
    
    s=[[f,1]]

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

    # Violoncelle
    s=[[196, 1],
       [392, 2],
       [784, 1]]

    # Orgue
    f=220
    s=[[f, 0.5],
       [2*f, 1.0],
       [3*f, 0.2],
       [4*f, 0.3],
       [5*f, 0.1]]

#    print interface.stream_.__dict__
#    interface.bitrate=22000
#    interface.channels=2
#    print interface.stream_.__dict__
    
    #del interface
    
   