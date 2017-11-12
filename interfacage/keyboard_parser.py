# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 18:28:54 2016

@author: alexis
"""

class KeyboardParser(object):
    
    def __init__(self):
        self.L = ["q","z","s","e","d","f","t","g","y","h","u","j","k"]
        self.scale = ['C','Cis','D','Dis','E','F','Fis','G','Gis','A','Ais','B','C']
        self.num = None
        
    def parseEvent(self,event):
        found = False
        for i in xrange(len(self.L)):
            if event.Key == self.L[i] : 
                self.num = i
                found = True       
        if found==False:
            self.num = - int('Inf')
            
    def getHeight(self,event):
        self.parseEvent(event)
        return 523.25*pow(2,float(self.num/12.0))
        
    def getNote(self,event):
        self.parseEvent(event)
        return self.scale[self.num]
        
    def isIn(self,event):
        found = False
        for l in self.L:
            if event.Key == l : 
                found = True
                break
        return found
                
        
if __name__ == "__main__":
    a=1