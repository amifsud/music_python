# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 23:07:12 2016

@author: alexis
"""

import shelve

class Timbre(object):
    
    def __init__(self):
        self.spectre_=[[1,1]]
        self.timbres = None
        
    @property
    def spectre(self):
        return self.spectre_
    @spectre.setter
    def spectre(self, x):
        if isinstance(x, str):
            self.setTimbre(x)
        else:
            self.spectre_=x
        
    def saveTimbre(self, name, spectre):
        self.timbres = shelve.open('timbres')
        self.timbres[name]={'spectre': spectre}
        self.timbres.close()
        
    def setTimbre(self, name):
        self.timbres = shelve.open('timbres')
        self.spectre_=self.timbres[name]['spectre']
        self.timbres.close()
        
        
if __name__ == "__main__":
    
    timbre=Timbre()       
    
    timbre.setTimbre('orgue')
    print timbre.spectre
    
    
    
   