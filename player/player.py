# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 01:08:11 2016

@author: alexis
"""

from interfacage.interface_aport import InterfaceAport
from interfacage.lylipond_parser import LyParser

class Player(object):
    def __init__(self, timbre):
        self.interface_ = InterfaceAport()
        self.parser_ = LyParser()        
        self.timbre_ = timbre
        
        self.tempo_=60 # 60 noirs/minutes

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
        
    def playTone(self, data, duration, bitrate):
        
        if len(data) != 1:
            numberofperiods = int(duration * bitrate / float(len(data)))
        else:
            numberofperiods = int(bitrate * duration)
            
        self.interface_.playData(data, numberofperiods)
        
    def playSheet(self, sheet):
         end = False
         while end != True:
             note = sheet.lastPlayedNote
             if  note != 'end':
                duration = sheet.computeDuration(note.timeDiv)                 
                data = self.timbre_.computeData(note.height, self.interface_.bitrate)            
                self.playTone(data, duration, self.interface_.bitrate)
             else:
                end = True        
        
    def playLySheet(self,lySheet):   
         self.sheet_ = self.parser_.getSheet(lySheet)
         self.sheet_.tempo = self.tempo_
         self.playSheet(self.sheet_)
                
    def playScale(self,scale):        
         self.sheet_ = scale.getScale()
         self.sheet_.tempo = self.tempo_         
         self.playSheet(self.sheet_)