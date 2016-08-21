# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 19:56:50 2016

@author: alexis
"""

from abstractSheet import AbstractSheet

class Sheet(AbstractSheet):
    
    def __init__(self,):
        AbstractSheet.__init__(self)        

        
if __name__ == "__main__":
    
    l=()
    for i in range(3):
        l+=(Sheet(),)
    
    for i in range(3):
        print l[i].a