# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 19:56:50 2016

@author: alexis
"""

from note import Note

class Sheet(object):
    
    def __init__(self,):
        
        self.notes_ = ()
        self.lastAddedNoteIndex_ = None
        self.lastNoteToPlayIndex_ = 0
        self.lastTimeDiv_ = None
        
        self.tempo_=60 # 60 noirs/minutes

    @property
    def tempo(self):
        return self.tempo_
    @tempo.setter
    def tempo(self, x):
        self.tempo_=x        
        
    @property
    def getLastAddedNote(self):
        if self.lastAddedNoteIndex_ != None:
            return self.notes_[self.lastAddedNoteIndex_]
        else:
            return Note(None, None, 0)
            
    @property
    def getLastNoteToPlay(self):           
        if self.lastNoteToPlayIndex_ <= self.lastNoteToPlayIndex_:
            note = self.notes_[self.lastNoteToPlayIndex_]
            self.lastNoteToPlayIndex_ += 1
        else:
            if self.lastNoteToPlayIndex_ != 0:
                print "No more note"
                note = Note(None, None, 0)
            else:
                print "Still no note"
                note = Note(None, None, 0)

        return note

    def addNote(self, height, timeDiv):
        if self.lastAddedNoteIndex_ !=None:
            self.lastAddedNoteIndex_+=1
        else:
            self.lastAddedNoteIndex_ = 0
        self.notes_ += (Note(height,timeDiv),)
        
    def addEnd(self):
        if self.lastAddedNoteIndex_ !=None:
            self.lastAddedNoteIndex_+=1
        else:
            self.lastAddedNoteIndex_ = 0
        self.notes_ += ('end',)

    def computeDuration(self, timeDiv):
        if timeDiv != None:
            duration = 60.0/self.tempo_*4.0/float(timeDiv)
        else:
            duration = 0.0  
                   
        return duration        
       
if __name__ == "__main__":
    
    l=()
    for i in range(3):
        l+=(Sheet(),)
    
    for i in range(3):
        print l[i].a