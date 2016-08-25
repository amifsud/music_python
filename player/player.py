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
        
    def playSheet(self, sheet, tempo=None):
         end = False
         while end != True:
             note = sheet.getLastNoteToPlay
             if  note != 'end':
                if self.timbre_ != None:
                    duration = sheet.computeDuration(note.duration, tempo)
                    data = self.timbre_.computeData(note.height, self.interface_.bitrate)
                else:
                    print 'No instrument given to the player'
                self.playTone(data, duration, self.interface_.bitrate)
             else:
                end = True        
                sheet.begin()
        
    def playLySheet(self,lySheet, tempo=None, scale=None):   
         self.sheet_ = self.parser_.getSheet(lySheet,scale)
         self.playSheet(self.sheet_, tempo)
                
    def playScale(self,scale, tempo=None):        
         self.sheet_ = scale.getScale()     
         self.playSheet(self.sheet_, tempo)