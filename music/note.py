# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 21:25:08 2016

@author: alexis
"""

class Note(object):
    def __init__(self,height,duration):
        self.height_=height
        self.duration_=duration
        
    @property
    def height(self):
        return self.height_
    @height.setter
    def height(self, x):
        self.height_=x
        
    @property
    def timeDiv(self):
        return self.duration_
    @timeDiv.setter
    def timeDiv(self, x):
        self.duration_=x
        
if __name__ == "__main__":
    
    note=Note(440.0,4)
    print note.height
    print note.duration
    
    note.height=880.0
    note.duration=2
    print note.height
    print note.duration