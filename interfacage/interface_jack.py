# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 01:18:32 2016

@author: alexis
"""

import jack
import binascii

client = jack.Client("jackClient")   
port = client.midi_inports.register("input")

@client.set_process_callback
def process(frames):
    for offset, data in port.incoming_midi_events():
        client.player_.feedMidiSheet("{0}:0x{1}:{2}".format(client.last_frame_time,
                                           binascii.hexlify(data).decode(), 
                                           offset))

class InterfaceJack(object):
    
    def __init__(self,player):
        self.client_ = client
        self.client_.player_ = player
        self.client_.activate()        
        self.port = port
        
    def __del__(self):
        self.client_.deactivate()
        self.client_.close()
        
    def connectToGmidimonitor (self):
        # WE need to launch a2j -e and gmidimonitor before
        if self.client.get_all_connections("a2j:MIDI monitor [128] (playback): midi in") == []:
            self.client.connect("a2j:XP MIDI mate [24] (capture): XP MIDI mate MIDI 1", 
                                 "a2j:MIDI monitor [128] (playback): midi in")
                             
    def disconnectFromGmidimonitor(self):
        self.client.disconnect("a2j:XP MIDI mate [24] (capture): XP MIDI mate MIDI 1", 
                             "a2j:MIDI monitor [128] (playback): midi in")
                             
    def makeClient(self):
        self.client.connect("a2j:XP MIDI mate [24] (capture): XP MIDI mate MIDI 1",
                            self.port)
        
if __name__ == "__main__":
    
    interface = InterfaceJack()
    #interface.connectToGmidimonitor()
    #interface.makeClient()
    
    #interface.disconnectFromGmidimonitor()
    #del interface
    #print interface.client.get_ports()
    
    #client.input()
    
    #with client:
       # print("#" * 80)
       # print("press Return to quit")
       # print("#" * 80)
       # input()
        
       # http://sametmax.com/comprendre-les-decorateur-python-pas-a-pas-partie-2/


