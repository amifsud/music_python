# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 22:11:53 2016

@author: alexis
"""

from interface_aport import InterfaceAport
import re

class musicPython(object):
    
    def __init__(self):
        
        self.interface = InterfaceAport()
        
#    def __del__(self):
        
    def playNote(self, note, sin, duration):
       
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
                   
        sout=[[sin[0][0]*f,sin[0][1]]]
        for i in range(len(sin)):
            sout.append([sin[i][0]*f,sin[i][1]])

        self.interface.playTone(sout,duration) 

    def playCScale(self,s,duration):
        music.playNote('c',s,duration)
        music.playNote('d',s,duration)
        music.playNote('e',s,duration)
        music.playNote('f',s,duration)
        music.playNote('g',s,duration)
        music.playNote('a\'',s,duration)
        music.playNote('b\'',s,duration)
        music.playNote('c\'',s,duration)
        
    def playLySheet(self,sheet,s,d):
        l=re.split(' ', sheet)
        for i in range(len(l)):
            n=l[i]
            if n != '{' and n!= '}':
                self.playNote(n,s,d)
  
if __name__ == "__main__":
       
    music = musicPython()
    
    s=[[1,1]] # first harmonic, amplitude 1
    duration=0.5
    
    # Orgue
    s=[[1, 0.5],
       [2, 1.0],
       [3, 0.2],
       [4, 0.3],
       [5, 0.1]]
       
    # Violon
    s=[[1, 140.0],
       [2, 80.0],
       [3, 15.0],
       [4, 45.0],
       [5, 75.0],
       [6, 1.0],
       [7, 12.0],
       [8, 30.0],
       [9, 2.0],
       [10, 2.0],
       [11, 5.0],
       [12, 2.0],
       [13, 5.0]]
       
    # Violoncelle
    s=[[1, 1],
       [2, 2],
       [4, 1]]
       
    #music.playCScale(s,duration)
    
    sheet="{ c e e g }"
    music.playLySheet(sheet,s,duration)
        
