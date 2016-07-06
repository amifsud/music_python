# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 19:56:50 2016

@author: alexis
"""

from note import Note

class Sheet(object):
    
    def __init__(self,):
        
        self.notes_ = ()
        self.lastNoteIndex_ = None
        self.lastTimeDiv_ = None
        
    @property
    def lastNote(self):
        if self.lastNoteIndex_ != None:
            return self.notes_[self.lastNoteIndex_]
        else:
            return Note(None, None)

    def addNote(self, height, timeDiv):
        if self.lastNoteIndex_ !=None:
            self.lastNoteIndex_+=1
        else:
            self.lastNoteIndex_ = 0
        self.notes_ += (Note(height,timeDiv),)
        
if __name__ == "__main__":
    
    l=()
    for i in range(3):
        l+=(Sheet(),)
    
    for i in range(3):
        print l[i].a