# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 18:28:54 2016

@author: alexis
"""

import re
from note import Note

class LyParser(object):
    
    def __init__(self):
        self.lyNote_ = None # String to parse
        self.r_ = None # ==None if self.note_ isn't a valid Lylipond note
        
        self.note_ = Note(None,None)
        self.lastDuration_ = None
        
    def computeHeight(self, lyNote, lyAccidental, lyOctave):        
        if lyNote == 'r': height=0.0
        else:
            if   lyNote == 'a': num=0.0
            elif lyNote == 'b': num=2.0
            elif lyNote == 'c': num=3.0
            elif lyNote == 'd': num=5.0
            elif lyNote == 'e': num=7.0
            elif lyNote == 'f': num=8.0
            elif lyNote == 'g': num=10.0
            else:
                print "Bad note definition"
                
            if   lyAccidental == None  : num+=0.0
            elif lyAccidental == 'es': num-=1.0
            elif lyAccidental == 'is': num+=1.0
            else:
                print "Bad accidental definition"
        
            if   lyOctave == None  : octave=1.0
            elif lyOctave == '\'': octave=2.0
            elif lyOctave == ',' : octave=0.5
            else:
                print "Bad octave definition"
                
            height = 440.0*octave*pow(2,num/12.0)
        
        return height
        
    def computeDuration(self, lyDuration, lyHalfDuration):
        if lyDuration == None:
            duration = self.lastDuration_
        elif re.search('[0-9]{1,2}',lyDuration):
            duration = float(lyDuration)
        else:
            print "Bad duration definition"

        if lyHalfDuration == None:
            self.lastDuration_=duration
        elif lyHalfDuration == '.':
            self.lastDuration_=duration
            duration=float(2/3.0*duration)
        else:
            print "Bad half duration definition"

        return duration
        
    def getNote(self, lyNote):
        
        self.lyNote_=lyNote
        self.r_=re.search('([a-gr](?!s)){1}([ei]s){,1}([\',]){,1}([1-9]){,2}(\.){,1}',self.lyNote_)
 
        if self.r_ != None:
            self.note_.height=self.computeHeight(self.r_.group(1),self.r_.group(2),self.r_.group(3))
            self.note_.duration_=self.computeDuration(self.r_.group(4),self.r_.group(5))
        else:
            self.note_.height=None
            self.note_.duration=None
            
        return self.note_
                 
        
if __name__ == "__main__":
    
    parser=LyParser()
    parser.getNote('aes\'2.')
    print parser.note_.height
    print parser.note_.duration
