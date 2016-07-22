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
        
    