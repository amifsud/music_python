# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 22:11:53 2016

@author: alexis
"""

from interface_aport import InterfaceAport

class musicPython(object):
    
    def __init__(self):
        
        self.interface = InterfaceAport()
        
#    def __del__(self):
        
        
        
  
if __name__ == "__main__":
    
    music = musicPython()
    
    f=220.0    
    s=[[f,1]] 
    music.interface.playTone(s,3)