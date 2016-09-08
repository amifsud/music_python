# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 19:56:50 2016

@author: alexis
"""

from note import Note

class Sheet(object):
    
    def __init__(self):
        
        self.notes_ = ()
        self.lastAddedNoteIndex_ = None
        self.lastNoteToPlayIndex_ = 0
        self.lastTimeDiv_ = None
        
        self.tempoDefault_= 100
        self.scale_ = None
        
    def __iter__(self):
        self.i = 0
        return self
    
    def next(self):
        if self.notes_[self.i]!='end':
            self.i=self.i+1
            return self.notes_[self.i-1]
        raise StopIteration 
    __next__=next

    @property
    def tempo(self):
        return self.tempo_
    @tempo.setter
    def tempo(self, x):
        self.tempo_=x 
        
    @property
    def scale(self):
        return self.scale_
    @scale.setter
    def scale(self, x):
        self.scale_=x    
        
    def getNote(self,i):
        if self.scale_ !=None and self.notes_[i] != 'end' and self.notes_[i].degree != None:
            self.notes_[i].height = self.scale_.getFrequency(self.notes_[i].degree, self.notes_[i].octave)

        return self.notes_[i]
        
    def begin(self):
        self.lastNoteToPlayIndex_ = 0
        
    @property
    def getLastAddedNote(self):
        if self.lastAddedNoteIndex_ != None:
            return self.getNote(self.lastAddedNoteIndex_)
        else:
            return Note(None, None, 0)
            
    @property
    def getLastNoteToPlay(self):           
        if self.lastNoteToPlayIndex_ <= self.lastNoteToPlayIndex_:
            note = self.getNote(self.lastNoteToPlayIndex_)
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
            
        note = Note(height,timeDiv)
        if self.scale_ != None:
            (note.degree, note.octave) = self.scale_.getDegree(note.height)
        
        self.notes_ += (note,)
        
    def addEnd(self):
        if self.lastAddedNoteIndex_ !=None:
            self.lastAddedNoteIndex_+=1
        else:
            self.lastAddedNoteIndex_ = 0

        self.notes_ += ('end',)

    def computeDuration(self, timeDiv, tempo=None):
        if tempo == None:
            tempo = self.tempoDefault_
            
        if timeDiv != None:
            duration = 60.0/tempo*4.0/float(timeDiv)
        else:
            duration = 0.0  
                   
        return duration        
       
if __name__ == "__main__":
    
    l=()
    for i in range(3):
        l+=(Sheet(),)
    
    for i in range(3):
        print l[i].a