# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 21:25:08 2016

@author: alexis
"""

class Note(object):
    def __init__(self,height,duration):
        self.height_=height
        self.degree_=None
        self.octave_ = None
        self.duration_=duration
        
    @property
    def height(self):
        return self.height_
    @height.setter
    def height(self, x):
        self.height_=x
        
    @property
    def degree(self):
        return self.degree_
    @degree.setter
    def degree(self, x):
        self.degree_=x

    @property
    def octave(self):
        return self.octave_
    @octave.setter
    def octave(self, x):
        self.octave_=x          
        
    @property
    def duration(self):
        return self.duration_
    @duration.setter
    def duration(self, x):
        self.duration_=x
        
if __name__ == "__main__":
    
    note=Note(440.0,4)
    print note.height
    print note.duration
    
    note.height=880.0
    note.duration=2
    print note.height

    from pythonlangutil.overload import Overload, signature
    
    @Overload
    @signature("int","int")
    def stackoverflow(self,a,b):
        print 'intVersion'
        return a+b
        
    @stackoverflow.overload
    @signature("float","float")
    def stackoverflow(self,a,b):
        print 'floatVersion'
        return a+b
        
    print stackoverflow(2,3)
    
    