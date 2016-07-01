# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 22:11:53 2016

@author: alexis
"""

from interface_aport import InterfaceAport
import re

class MusicPython(object):
    
    def __init__(self):
        
        self.interface_ = InterfaceAport()
        self.tempo_=60 # 60 noirs/minutes
        self.duration_=1
        self.halfduration_=0
        
        
#    def __del__(self):
        
    @property
    def tempo(self):
        return self.tempo_
    @tempo.setter
    def bitrate(self, x):
        self.tempo_=x
        
    def playNote(self, note, sin, duration_):
        
        # Getting octave
        octave=1
        r=re.search('(.*)\'',  note)
        if r:
            note=r.group(1)
            octave=2  
        r=re.search('(.*)\,',  note)
        if r:
            note=r.group(1)
            octave=0.5
       
        if note == 'a': f=440.0*octave
        else:
            if note == 'ais' or note == 'bes': num=1
            elif note == 'b': num=2
            elif note == 'c': num=3
            elif note == 'cis' or note == 'des': num=4
            elif note == 'd': num=5
            elif note == 'dis' or note == 'ees': num=6
            elif note == 'e': num=7
            elif note == 'f': num=8
            elif note == 'fis' or note == 'ges': num=9
            elif note == 'g': num=10
            elif note == 'gis' or note == 'aes': num=11
            f= 440.0*octave*pow(2,num/12.0)
                   
        sout=[[sin[0][0]*f,sin[0][1]]]
        for i in range(len(sin)):
            sout.append([sin[i][0]*f,sin[i][1]])

        self.interface_.playTone(sout,duration_) 

    def playCScale(self,s,duration_):
        music.playNote('c',s,duration_)
        music.playNote('d',s,duration_)
        music.playNote('e',s,duration_)
        music.playNote('f',s,duration_)
        music.playNote('g',s,duration_)
        music.playNote('a\'',s,duration_)
        music.playNote('b\'',s,duration_)
        music.playNote('c\'',s,duration_)
        
    def computeduration_(self,i):
        self.halfduration_=0
        if i != '':
            r=re.search('([1-9]{0,2})(\.{0,1})',i)
            self.duration_=  60.0/self.tempo_*4/float(r.group(1))
            if r.group(2) == '.':
                self.halfduration_=1
        
    def playLySheet(self,sheet,s):
        l=re.split(' ', sheet)
        for i in range(len(l)):
            n=re.search('([a-g\'is,]+)([1-9\.]{0,2})',l[i])
            if n!= None:
                self.computeduration_(n.group(2))
                self.playNote(n.group(1),s,self.duration_*(1+self.halfduration_*0.5))
  
if __name__ == "__main__":
       
    music = MusicPython()
    
    s=[[1,1]] # first harmonic, amplitude 1
    duration_=0.5
    
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
       
    #music.playCScale(s,duration_)
    
    sheet="{ a,4 ais,8 b, c, cis, d, dis, e, f, fis, g, gis, a4 ais8 b c cis d dis e f fis g gis a'4 ais'8 b' c' cis' d' dis' e' f' fis' g' gis' }"
    sheet="{ ais8 ais a g,16 f, f, d,8. c,4 f,2  }"
    music.playLySheet(sheet,s)
    shhet="{ bes'8 bes' a' g'16 f' f' d'8. c'4 f'2 }"
    music.playLySheet(sheet,s)
        
