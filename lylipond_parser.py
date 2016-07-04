# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 18:28:54 2016

@author: alexis
"""

import re
from note import Note

class LyParser(object):
    
    def __init__(self):
        self.lyNote_=None # String to parse
        self.r_=None # ==None if self.note_ isn't a valid Lylipond note
        
        self.note_=Note(None,None)
        
    def computeHeight(self):
        return 440.0
        
    def computeDuration(self):
        return 4
        
    def getNote(self, note):
        
        self.lyNote_=note
        self.r_=re.search('([a-g](?!s)){1}([ei]s){,1}([\',]){,1}([1-9]){,2}(\.){,1}',self.lyNote_)
 
        if parser.r_ != None:
            self.note_.height=self.computeHeight()
            self.note_.duration_=self.computeDuration()
                 
        
if __name__ == "__main__":
    
    parser=LyParser()
    parser.getNote('aes,2.')
