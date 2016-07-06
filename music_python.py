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
        self.parser_ = LyParser()
        self.timbre_ = Timbre()        
               
        # Harmony
        self.note_ = None
        
        # Rythm
        self.tempo_=60 # 60 noirs/minutes
        self.duration_=1.0
        
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

    def computeDuration(self, timeDiv, f0):
        if timeDiv != None:
            self.duration_ = 60.0/self.tempo_*4.0/float(timeDiv)
        else:
            self.duration_ = 0.0  
            
        numberofframes = int(self.interface_.bitrate * self.duration_)
        
        if f0 != 0.0:
            numberofperiods = int(self.duration_ * f0)
        else:
            numberofperiods = int(numberofframes)
            
        return numberofperiods
                    
    def playTone(self, data, numberofperiods):      
        self.interface_.playData(data, numberofperiods)
        
    def playLySheet(self,sheet):
         self.sheet_ = self.parser_.getSheet(sheet)
         for i in range(len(self.sheet_.notes_)):
            (data, f0) = self.timbre_.computeData(self.sheet_.notes_[i].height,self.timbre, self.interface_.bitrate)            
            numberofperiods = self.computeDuration(self.sheet_.notes_[i].timeDiv, f0)
            self.playTone(data, numberofperiods)
  
if __name__ == "__main__":
       
    #sheet="{ a,4 ais, b, c, cis, d, dis, e, f, fis, g, gis, a4 ais b c cis d dis e f fis g gis a'4 ais' b' c' cis' d' dis' e' f' fis' g' gis' }"
    #sheet="{ ais8 ais a g,16 f, f, d,8. c,4 f,2  }"
    sheet="{ r2 c,8 c, a4 g, f, g,2 e,4 f, r f, g,2 c,4 a b c g,2 e,8 e, f,4 e, d, c,2. r2. }"       
    #sheet="{ c4 c c d e2 d c4 e d d c2 c4 c c d e2 d c4 e d d c2 d4 d d d a2 a d4 c b a g,2 c4 c c d e2 d c4 e d d c2}"
        
    music = MusicPython()
    music.timbre='violon'
    music.tempo=100
    music.playLySheet(sheet)
        
