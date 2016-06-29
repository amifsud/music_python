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
        
    def playNote(self, note, sin):

        duration=0.5
        
        if note == 'a': f=440.0
        else:
            if note == 'ais': num=1
            elif note == 'b': num=2
            elif note == 'c': num=3
            elif note == 'cis': num=4
            elif note == 'd': num=5
            elif note == 'dis': num=6
            elif note == 'e': num=7
            elif note == 'f': num=8
            elif note == 'fis': num=9
            elif note == 'g': num=10
            elif note == 'gis': num=11
            elif note == 'a\'': num=12
            elif note == 'ais\'': num=13
            elif note == 'b\'': num=14
            elif note == 'c\'': num=15
            f= 440.0*pow(2,num/12.0)
        
        sout=[[0,0]]
        for i in range(len(sin)):
            sout[i][0]=sin[i][0]*f

        self.interface.playTone(sout,duration)        
  
if __name__ == "__main__":
    
    music = musicPython()
    
    s=[[1,1]] # first harmonic, amplitude 1
    
    music.playNote('c',s)
    music.playNote('d',s)
    music.playNote('e',s)
    music.playNote('f',s)
    music.playNote('g',s)
    music.playNote('a\'',s)
    music.playNote('b\'',s)
    music.playNote('c\'',s)