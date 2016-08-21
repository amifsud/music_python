# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 18:22:12 2016

@author: alexis
"""

from music.sheet import Sheet

class Scale(object):
    def __init__(self):
        self.tonality_ = 440.0
        self.mode_ = ()
        self.scale_ = Sheet()
        
    def setMajorMode(self):
        self.mode_ = (1.0, pow(2,2.0/12.0), pow(2,4.0/12.0), pow(2,5.0/12.0), pow(2,7.0/12.0), pow(2,9.0/12.0), pow(2,11.0/12.0), 2.0)
        
    def getScale(self):
        
        for note in self.mode_:
            self.scale_.addNote(self.tonality_*note, 8)
            
        self.scale_.addEnd()
            
        return self.scale_ 
        
if __name__ == "__main__":
    
    scale = Scale()
    scale.setMajorMode()
    
    print scale.tonality
    