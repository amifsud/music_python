# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 22:11:53 2016

@author: alexis
"""

from interfacage.interface_aport import InterfaceAport
from instruments.timbre import Timbre
from music.scale import Scale
from player.player import Player

interface = InterfaceAport(44000) # Defining an interface with a bitrate
player = Player(interface) # Defining a player and giving it an interface

instrument = Timbre('violon') # Defining an instrument
player.instrument = instrument # giving an instrument to the player

tempo = 200

# Defining a scale
scale = Scale()
scale.tonality = 440.0
scale.setMajorMode()
player.playScale(scale, tempo) # Asking the player to play the scale to a specific tempo

# Defining a sheet
#sheet="{ a,4 ais, b, c, cis, d, dis, e, f, fis, g, gis, a4 ais b c cis d dis e f fis g gis a'4 ais' b' c' cis' d' dis' e' f' fis' g' gis' }"
#sheet="{ ais8 ais a g,16 f, f, d,8. c,4 f,2 }"
sheet="{ r2 c,8 c, a4 g, f, g,2 e,4 f, r f, g,2 c,4 a b c g,2 e,8 e, f,4 e, d, c,2. r2. }"       
#sheet="{ c4 c c d e2 d c4 e d d c2 c4 c c d e2 d c4 e d d c2 d4 d d d a2 a d4 c b a g,2 c4 c c d e2 d c4 e d d c2 }"    
player.playLySheet(sheet, tempo) # Asking the player to play the sheet to a specific tempo
    
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
    
    
    
       
