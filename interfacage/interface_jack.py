# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 01:18:32 2016

@author: alexis
"""

import jack

class InterfaceJack(object):
    
    def __init__(self):
        self.client = jack.Client("jackClient")
        self.client.activate()
        
    def __del__(self):
        self.client.deactivate()
        self.client.close()
        
    def connectToGmidimonitor (self):
        # WE need to launch a2j -e and gmidimonitor before
        if self.client.get_all_connections("a2j:MIDI monitor [132] (playback): midi in") == []:
            self.client.connect("a2j:XP MIDI mate [24] (capture): XP MIDI mate MIDI 1", 
                                 "a2j:MIDI monitor [132] (playback): midi in")
                             
    def disconnectFromGmidimonitor(self):
        self.client.disconnect("a2j:XP MIDI mate [24] (capture): XP MIDI mate MIDI 1", 
                             "a2j:MIDI monitor [132] (playback): midi in")
        
if __name__ == "__main__":
    
    interface = InterfaceJack()
    interface.connectToGmidimonitor()
    
    interface.disconnectFromGmidimonitor()
    del interface
    #print interface.client.get_ports()
