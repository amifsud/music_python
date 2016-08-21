# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 23:07:12 2016

@author: alexis
"""

import shelve
import numpy as np

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
        self.timbres = shelve.open('data/timbres')
        self.timbres[name]={'spectre': spectre}
        self.timbres.close()
        
    def setTimbre(self, name):
        self.timbres = shelve.open('data/timbres')
        self.spectre_=self.timbres[name]['spectre']
        self.timbres.close()
        
    def computeSpectre(self, height, sin):
        if height != None:
            spectre=[[sin[0][0]*height,sin[0][1]]]
            for i in range(len(sin)):
                spectre.append([sin[i][0]*height,sin[i][1]])   
        else:
            spectre = [[0,1]]
            
        return spectre
        
    def normalizeSpectre(self,sin):      
        sum=0
        for i in range(len(sin)-1):
           sum += sin[i+1][1]
           
        sout=sin
        sout[0][1]=1.0/(1.0+sum)
        
        for i in range(len(sin)-1):
           sout[i+1][1]=sout[0][1]*sin[i+1][1]
        
        return sout        
        
    def computeData(self, height, timbre, bitrate):      
        spectre = self.computeSpectre(height, timbre)
        
        f0 = spectre[0][0]
        
        if f0 != 0.0:
            periodlength = int(bitrate / f0)
        else:
            periodlength = 1
        
        nSpectre=self.normalizeSpectre(spectre)        
        
        data=()        
        for x in xrange(periodlength):  
            y = 0.0
            for n in range(len(nSpectre)):
                y+=nSpectre[n][1]*np.sin(2*np.pi*nSpectre[n][0]*x/bitrate)
            data+=(y,)
            
        return (data, f0)
        
        
if __name__ == "__main__":
    
    timbre=Timbre()       
    
    timbre.setTimbre('orgue')
    print timbre.spectre
    
    
    
   