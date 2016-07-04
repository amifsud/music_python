# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 18:28:54 2016

@author: alexis
"""

import re

class LyParser(object):
    
    def __init__(self):
        self.lyNote_=None # String to parse
        self.r_=None # ==None if self.note_ isn't a valid Lylipond note
        
    def getNote(self, note):
        
        self.lyNote_=note
        self.r_=re.search('([a-g](?!s)){1}([ei]s){,1}([\',]){,1}([1-9]){,2}(\.){,1}',self.lyNote_)
 
        if parser.r_ != None:
            for i in range(6):
                print parser.r_.group(i)   
        
if __name__ == "__main__":
    
    parser=LyParser()
    parser.getNote('aes,2.')
