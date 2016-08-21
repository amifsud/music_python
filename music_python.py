# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 22:11:53 2016

@author: alexis
"""

from interfacage.interface_aport import InterfaceAport
from interfacage.lylipond_parser import LyParser
from instruments.timbre import Timbre

class MusicPython(object):
    
    def __init__(self):
        
        self.interface_ = InterfaceAport()
        self.parser_ = LyParser()
        self.timbre_ = Timbre()        
               
        self.tempo_=60 # 60 noirs/minutes
        
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
            duration = 60.0/self.tempo_*4.0/float(timeDiv)
        else:
            duration = 0.0  
        
        if f0 != 0.0:
            numberofperiods = int(duration * f0)
        else:
            numberofframes = int(self.interface_.bitrate * duration)
            numberofperiods = int(numberofframes)
            
        return numberofperiods
                    
    def playTone(self, data, numberofperiods):      
        self.interface_.playData(data, numberofperiods)
        
    def playLySheet(self,sheet):
        
         self.sheet_ = self.parser_.getSheet(sheet)

         end = False
         while end != True:
             note = self.sheet_.lastPlayedNote
             if  note != 'end':
                (data, f0) = self.timbre_.computeData(note.height,self.timbre, self.interface_.bitrate)            
                numberofperiods = self.computeDuration(note.timeDiv, f0)
                self.playTone(data, numberofperiods)
             else:
                end = True
                
    def playScale(self,scale):
        
         self.sheet_ = scale.getScale()

         end = False
         while end != True:
             note = self.sheet_.lastPlayedNote
             if  note != 'end':
                (data, f0) = self.timbre_.computeData(note.height,self.timbre, self.interface_.bitrate)            
                numberofperiods = self.computeDuration(note.timeDiv, f0)
                self.playTone(data, numberofperiods)
             else:
                end = True        
  
if __name__ == "__main__":
       
    #sheet="{ a,4 ais, b, c, cis, d, dis, e, f, fis, g, gis, a4 ais b c cis d dis e f fis g gis a'4 ais' b' c' cis' d' dis' e' f' fis' g' gis' }"
    #sheet="{ ais8 ais a g,16 f, f, d,8. c,4 f,2  }"
    sheet="{ r2 c,8 c, a4 g, f, g,2 e,4 f, r f, g,2 c,4 a b c g,2 e,8 e, f,4 e, d, c,2. r2. }"       
    #sheet="{ c4 c c d e2 d c4 e d d c2 c4 c c d e2 d c4 e d d c2 d4 d d d a2 a d4 c b a g,2 c4 c c d e2 d c4 e d d c2}"
        
    music = MusicPython()
    music.timbre='violon'
    music.tempo=100
    music.interface_.bitrate = 44000
    
    from music.scale import Scale
    scale = Scale()
    scale.tonality_ = 440.0
    scale.setMajorScale()
    
    music.playScale(scale)
    
    
    #music.playLySheet(sheet)
    
#==============================================================================
#     import matplotlib.pyplot as plt
#     import numpy as np
#     
#     def upsampling(bitrate, data):
#         
#         size= int(bitrate/data[1])
#         data1 = [0.0]*size
#         
#         u=0
#         for i in np.arange(0, int(size), int(size/len(data[0]))):
#             data1[i]=data[0][u]
#             u+=1
#             
#         
# 
#         return (tuple(data1),bitrate)
#     
#     n=3
#     f=440.0
#     bitratein = 4.0
#     bitrateout = 44000.0
#     
#     data=music.timbre_.computeData(f, music.timbre, bitratein*f)
#     datax = np.arange(0., n, 1/bitratein)
#     
#     plt.plot(datax, n*data[0], 'ro') 
#     
#     data1 = upsampling(bitrateout, data)
#     datax1 = np.arange(0., n, f/bitrateout)
#     
#     plt.plot(datax1, n*data1[0], 'bx')
#     plt.show()
#==============================================================================
    
    
    
       
