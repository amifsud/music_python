# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 18:22:12 2016

@author: alexis
"""

from music.sheet import Sheet

class Scale(object):
    def __init__(self, mode, tonality=None):
        self.tonality_ = tonality
        self.mode_ = ()
        self.scale_ = Sheet()
        
        if mode=='diatonic':
            self.setDiatonicMode()
        elif mode=='major':
            self.setMajorMode()
        else:
            print "No mode set"
        
    @property
    def tonality(self):
        return self.tonality_
    @tonality.setter
    def tonality(self, x):
        self.tonality_=x     
        
    def setMajorMode(self):
        self.mode_ = (1.0, pow(2,2.0/12.0), pow(2,4.0/12.0), pow(2,5.0/12.0), pow(2,7.0/12.0), pow(2,9.0/12.0), pow(2,11.0/12.0), 2.0)
       
       
    def setDiatonicMode(self):
        self.mode_ = (1.0, pow(2,1.0/12.0), pow(2,2.0/12.0), pow(2,3.0/12.0), pow(2,4.0/12.0), pow(2,5.0/12.0), pow(2,6.0/12.0), pow(2,7.0/12.0), pow(2,8.0/12.0), pow(2,9.0/12.0), pow(2,10.0/12.0), pow(2,11.0/12.0), 2.0)
       
    
    def getDegree(self, frequency):
        degree = None
        i=1
        if self.tonality_ != None:
            octave=1
            while frequency>=self.tonality_*2:
                frequency=frequency/2.0
                octave=octave+1
            for m in self.mode_:
                if abs(m*self.tonality_ - frequency) <= 8.25:
                    degree = i
                i=i+1
        else:
            print 'No tonality set'
            
        return (degree, octave)
        
    def getFrequency(self, degree, octave):
        frequency = self.tonality_*self.mode_[degree-1]*octave
        return frequency
        
    
    def getScale(self):
        for note in self.mode_:
            self.scale_.addNote(self.tonality_*note, 8)
            
        self.scale_.addEnd()
            
        return self.scale_ 
        
if __name__ == "__main__":
    
    scale = Scale()
    scale.setMajorMode()
    
    print scale.tonality
    