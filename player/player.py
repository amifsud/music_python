# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 01:08:11 2016

@author: alexis
"""

from interfacage.lylipond_parser import LyParser
from interfacage.keyboard_parser import KeyboardParser
#from interfacage.midi_parser import MidiParser
from interfacage.interface_aport import InterfaceAport
#from interfacage.interface_jack import InterfaceJack
from interfacage.interface_keyboard import InterfaceKeyboard
from music.sheet import Sheet

class Player(object):
    def __init__(self, ):
        self.interface_ = InterfaceAport(44000) # Defining an interface with a bitrate
        self.parser_ = None    
#        self.jack_ = None
        self.timbre_ = None
        
        self.lastHeight = "vide"

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
        if duration != None :
            if len(data) != 1:
                numberofperiods = int(duration * bitrate / float(len(data)))
            else:
                numberofperiods = int(bitrate * duration)
        else:
            numberofperiods = 2
            
        print numberofperiods
            
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
         self.parser_ = LyParser()
         self.sheet_ = self.parser_.getSheet(lySheet,scale)
         self.playSheet(self.sheet_, tempo)
         return self.sheet_

    def playRealTime(self):
        self.parser_ = KeyboardParser()
        self.keyboard = InterfaceKeyboard(self)
        self.interface_.start()
        return self.keyboard
        
    def playEvent(self,event):
         if self.parser_.isIn(event):
             height = self.parser_.parseEvent(event)
             data = self.timbre_.computeData(height, self.interface_.bitrate)
             if self.lastHeight != height:
                 self.interface_.playData(data)
             self.lastHeight = height
         
    def stopEvent(self,event):
         if self.parser_.isIn(event):
             self.interface_.stopLast()
             self.lastHeight = "vide"
         
#    def playMidi(self, scale=None):
#         self.jack_ = InterfaceJack(self)
#         self.parser_ = MidiParser()
#         sheet = self.parser_.sheet_
#         end = False
#         while end != True:
#             note = sheet.getLastNoteToPlay
#             if  note != 'end':
#                if self.timbre_ != None:
#                    data = self.timbre_.computeData(note.height, self.interface_.bitrate)
#                else:
#                    print 'No instrument given to the player'
#                self.interface_.playData(data, 100)
#             else:
#                end = True
#                sheet.begin()
        
    def feedMidiSheet(self, command):
        self.parser_.parseCommand(command)
        
    def stopMidi(self, scale=None):
        del self.parser_
#        del self.jack_
        self.parser_ = None
#        self.jack_ = None
        
    def playScale(self,scale, tempo=None):        
         self.sheet_ = scale.getScale()     
         self.playSheet(self.sheet_, tempo)
         
    def playTuple(self,Tuple,tempo=None):
        self.sheet_ = Sheet()
        for note in Tuple:
            self.sheet_.addNote(note, 8) 
        self.sheet_.addEnd()
        self.playSheet(self.sheet_, tempo)