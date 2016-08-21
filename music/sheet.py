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
        self.lastPlayedNoteIndex_ = 0
        self.lastTimeDiv_ = None
        
    @property
    def lastAddedNote(self):
        if self.lastAddedNoteIndex_ != None:
            return self.notes_[self.lastAddedNoteIndex_]
        else:
            return Note(None, None)
            
    @property
    def lastPlayedNote(self):           
        if self.lastPlayedNoteIndex_ <= self.lastAddedNoteIndex_:
            note = self.notes_[self.lastPlayedNoteIndex_]
            self.lastPlayedNoteIndex_ += 1
        else:
            if self.lastPlayedNoteIndex_ != 0:
                print "No more note"
                note = Note(None, None)
            else:
                print "Still no note"
                note = Note(None, None)

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
        
if __name__ == "__main__":
    
    l=()
    for i in range(3):
        l+=(Sheet(),)
    
    for i in range(3):
        print l[i].a