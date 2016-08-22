# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 01:08:11 2016

@author: alexis
"""

from interfacage.lylipond_parser import LyParser

class Player(object):
    def __init__(self, interface):
        self.interface_ = interface
        self.parser_ = LyParser()        
        self.timbre_ = None

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

    @property
    def instrument(self):
        return self.timbre_.spectre        
    @instrument.setter
    def instrument(self, x):
        self.timbre_=x
        
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
                if self.timbre_ != None:
                    data = self.timbre_.computeData(note.height, self.interface_.bitrate)
                else:
                    print 'No instrument given to the player'
                self.playTone(data, duration, self.interface_.bitrate)
             else:
                end = True        
        
    def playLySheet(self,lySheet, tempo):   
         self.sheet_ = self.parser_.getSheet(lySheet)
         self.sheet_.tempo = tempo
         self.playSheet(self.sheet_)
                
    def playScale(self,scale, tempo):        
         self.sheet_ = scale.getScale()
         self.sheet_.tempo = tempo        
         self.playSheet(self.sheet_)