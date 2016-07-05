# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 22:11:53 2016

@author: alexis
"""

from interface_aport import InterfaceAport
from timbre import Timbre
from lylipond_parser import LyParser
import numpy as np
import re

class MusicPython(object):
    
    def __init__(self):
        
        self.interface_ = InterfaceAport()
        self.parser_ = LyParser()
        self.timbre_ = Timbre()        
               
        # Harmony
        self.note_ = None
        self.spectre_=None
        self.data_=None
        
        # Rythm
        self.tempo_=60 # 60 noirs/minutes
        self.duration_=1.0
        self.numberofperiods_=0.0
        
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
        
    def computeSpectre(self, height, sin):
        if self.note_.height != None:
            self.spectre_=[[sin[0][0]*height,sin[0][1]]]
            for i in range(len(sin)):
                self.spectre_.append([sin[i][0]*height,sin[i][1]])   
        else:
            self.spectre_ = [[0,1]]
            
    def computeDuration(self, duration, f0):
        if self.note_.duration != None:
            self.duration_ = 60.0/self.tempo_*4.0/float(duration)
        else:
            self.duration_ = 0.0  
            
        numberofframes = int(self.interface_.bitrate * self.duration_)
        if f0 != 0.0:
            self.numberofperiods_ = int(self.duration_ * f0)
        else:
            self.numberofperiods_ = int(numberofframes)
        
    def normalizeSpectre(self,sin):
        
        sum=0
        for i in range(len(sin)-1):
           sum += sin[i+1][1]
           
        sout=sin
        sout[0][1]=1.0/(1.0+sum)
        
        for i in range(len(sin)-1):
           sout[i+1][1]=sout[0][1]*sin[i+1][1]
        
        return sout        
        
    def computeData(self, spectre):
        
        if spectre[0][0] != 0.0:
            periodlength = int(self.interface_.bitrate / spectre[0][0])
        else:
            periodlength = 1
        
        s=self.normalizeSpectre(spectre)        
        
        self.data_=()        
        for x in xrange(periodlength):  
            y = 0.0
            for n in range(len(s)):
                y+=s[n][1]*np.sin(2*np.pi*s[n][0]*x/self.interface_.bitrate)
            self.data_+=(y,)
                    
    def playTone(self, data, numberofperiods):      
        self.interface_.playData(data, numberofperiods)
        
    def playLySheet(self,sheet):
        l=re.split(' ', sheet)
        for i in range(len(l)):
            self.note_ = self.parser_.getNote(l[i])
            self.computeSpectre(self.note_.height,self.timbre)
            self.computeDuration(self.note_.duration, self.spectre_[0][0])
            self.computeData(self.spectre_)
            self.playTone(self.data_, self.numberofperiods_)
  
if __name__ == "__main__":
       
    #sheet="{ a,4 ais, b, c, cis, d, dis, e, f, fis, g, gis, a4 ais b c cis d dis e f fis g gis a'4 ais' b' c' cis' d' dis' e' f' fis' g' gis' }"
    #sheet="{ ais8 ais a g,16 f, f, d,8. c,4 f,2  }"
    sheet="{ r2 c,8 c, a4 g, f, g,2 e,4 f, r f, g,2 c,4 a b c g,2 e,8 e, f,4 e, d, c,2. r2. }"       
    #sheet="{ c4 c c d e2 d c4 e d d c2 c4 c c d e2 d c4 e d d c2 d4 d d d a2 a d4 c b a g,2 c4 c c d e2 d c4 e d d c2}"

    music = MusicPython()
    music.timbre='violon'
    music.tempo=100
    music.playLySheet(sheet)
        
