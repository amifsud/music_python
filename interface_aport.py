#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 12:05:09 2016

@author: alexis
"""

class InterfaceAport:
    
    def __init__(self):
        # Attributs
        self._b=1
 
    def getb(self):
        print "Récupération du nombre de roues"
        return self._b

    def setb(self, v):
        print "Changement du nombre de roues"
        self._b  =  v
        
    b=property(getb, setb)


if __name__ == "__main__":
    
    interface=InterfaceAport()
    a=interface.b

    