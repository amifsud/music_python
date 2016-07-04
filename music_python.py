# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 22:11:53 2016

@author: alexis
"""

from interface_aport import InterfaceAport
from timbre import Timbre
from lylipond_parser import LyParser
import re

class MusicPython(object):
    
    def __init__(self):
        
        self.interface_ = InterfaceAport()
        
        # Harmony
        self.timbre_ = Timbre()
        self.spectre_=None        
        
        # Rythm
        self.tempo_=90 # 60 noirs/minutes
        self.duration_=1
        self.halfduration_=0
        self.r = None
        
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
        
    def saveTimbre(self, name, spectre):
        self.timbre_.saveTimbre(name,spectre)
        
    def computeSpectre(self, note, sin):
        
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
                   
        self.spectre_=[[sin[0][0]*f,sin[0][1]]]
        for i in range(len(sin)):
            self.spectre_.append([sin[i][0]*f,sin[i][1]])
       
    def computeDuration_(self,i):
        self.halfduration_=0
        if i != '':
            self.r=re.search('([1-9]{0,2})(\.{0,1})',i)
            self.duration_=  60.0/self.tempo_*4/float(self.r.group(1))
            if self.r.group(2) == '.':
                self.halfduration_=1
                
    def playTone(self, spectre, duration):
        self.interface_.playTone(spectre,duration)
        
    def playLySheet(self,sheet):
        l=re.split(' ', sheet)
        for i in range(len(l)):
            n=re.search('([a-g\'isr,]+)([1-9\.]{0,2})',l[i])
            if n!= None:
                self.computeDuration_(n.group(2))
                self.computeSpectre(n.group(1),self.timbre)
                self.playTone(self.spectre_,self.duration_*(1+self.halfduration_*0.5)) 
  
if __name__ == "__main__":
       
    sheet="{ a,4 ais,8 b, c, cis, d, dis, e, f, fis, g, gis, a4 ais8 b c cis d dis e f fis g gis a'4 ais'8 b' c' cis' d' dis' e' f' fis' g' gis' }"
    sheet="{ ais8 ais a g,16 f, f, d,8. c,4 f,2  }"
    sheet="{ r2 c,8 c, a4 g, f, g,2 e,4 f, r f, g,2 c,4 a b c g,2 e,8 e, f,4 e, d, c,2. r2. }"       
    #sheet="{ c4 c c d e2 d c4 e d d c2 c4 c c d e2 d c4 e d d c2 d4 d d d a2 a d4 c b a g,2 c4 c c d e2 d c4 e d d c2}"
    music = MusicPython()
    music.timbre='orgue'
    music.playLySheet(sheet)
        
