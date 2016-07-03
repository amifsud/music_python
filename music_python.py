# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 22:11:53 2016

@author: alexis
"""

from interface_aport import InterfaceAport
from timbre import Timbre
import re

class MusicPython(object):
    
    def __init__(self):
        
        self.interface_ = InterfaceAport()
        self.timbre_ = Timbre()
        
        # Tempo
        self.tempo_=90 # 60 noirs/minutes
        self.duration_=1
        self.halfduration_=0
        
        
#    def __del__(self):
        
    @property
    def tempo(self):
        return self.tempo_
    @tempo.setter
    def tempo(self, x):
        self.tempo_=x
        
    @property
    def timbre(self):
        return self.timbre_.spectre
        
    @timbre.setter
    def timbre(self, x):
        self.timbre_.spectre=x
        
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
       
        if note == 'r': f=0.0
        else:
            if note == 'a': num=0
            elif note == 'ais' or note == 'bes': num=1
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
        
    def playLySheet(self,sheet):
        l=re.split(' ', sheet)
        for i in range(len(l)):
            n=re.search('([a-g\'isr,]+)([1-9\.]{0,2})',l[i])
            if n!= None:
                self.computeduration_(n.group(2))
                self.playNote(n.group(1),self.timbre,self.duration_*(1+self.halfduration_*0.5))
  
if __name__ == "__main__":
       
    music = MusicPython()
    music.timbre='violoncelle'

    sheet="{ a,4 ais,8 b, c, cis, d, dis, e, f, fis, g, gis, a4 ais8 b c cis d dis e f fis g gis a'4 ais'8 b' c' cis' d' dis' e' f' fis' g' gis' }"
    sheet="{ ais8 ais a g,16 f, f, d,8. c,4 f,2  }"
    sheet="{ r2 c8 c a'4 g f g2 e4 f r f g2 c,4 a' b' c' g2 e8 e f4 e d c2. r2. }"
    music.playLySheet(sheet)
        
