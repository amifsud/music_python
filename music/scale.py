# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 18:22:12 2016

@author: alexis
"""

from music.sheet import Sheet

class Scale(object):
    def __init__(self):
        self.tonality_ = None
        self.mode_ = ()
        self.scale_ = Sheet()
        
    @property
    def tonality(self):
        return self.tonality_
    @tonality.setter
    def tonality(self, x):
        self.tonality_=x     
        
    def setMajorMode(self):
        self.mode_ = (1.0, pow(2,2.0/12.0), pow(2,4.0/12.0), pow(2,5.0/12.0), pow(2,7.0/12.0), pow(2,9.0/12.0), pow(2,11.0/12.0), 2.0)
        
    def getDegree(self,frequency):
        degree = None
        i=1
        if self.tonality_ != None:
            for m in self.mode_:
                if abs(m*self.tonality_ - frequency) < 1:
                    degree = i
                i=i+1
        else:
            print 'No tonality set'
            
        return degree
    
    def getScale(self):
        
        for note in self.mode_:
            self.scale_.addNote(self.tonality_*note, 8)
            
        self.scale_.addEnd()
            
        return self.scale_ 
        
if __name__ == "__main__":
    
    scale = Scale()
    scale.setMajorMode()
    
    print scale.tonality
    