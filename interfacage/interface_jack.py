# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 01:18:32 2016

@author: alexis
"""

import jack

class InterfaceJack(object):
    
    def __init__(self):
        self.client = jack.Client("jackClient")
        
if __name__ == "__main__":
    
    interface = InterfaceJack()
    
    print interface.client.get_ports()
        
    interface.client.activate()
    
    # WE need to launch a2j -e and gmidimonitor before
    interface.client.connect("a2j:XP MIDI mate [24] (capture): XP MIDI mate MIDI 1", 
                             "a2j:MIDI monitor [132] (playback): midi in")