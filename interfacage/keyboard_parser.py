# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 18:28:54 2016

@author: alexis
"""

class KeyboardParser(object):
    
    def __init__(self):
        self.L = ["q","z","s","e","d","f","t","g","y","h","u","j","k"]
        
    def parseEvent(self,event):
        
        found = False
        for i in xrange(len(self.L)):
            if event.Key == self.L[i] : 
                num = float(i)
                found = True
                
        if found==False:
            num = - float('Inf') 
        
        height = 523.2511306011972*pow(2,num/12.0)
        return height
        
    def isIn(self,event):
        
        found = False
        for l in self.L:
            if event.Key == l : 
                found = True
                break
        return found
                
        
if __name__ == "__main__":
    a=1