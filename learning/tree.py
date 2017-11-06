# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 01:08:11 2016

@author: alexis
"""

from ete2 import Tree

class Node(object):
    def __init__(self,name,p=None):
        
        self.name = name
        self.continuations = []
        
        self.parent = None
        self.childs = {}
        
        if p != None: self.addParent(p)
        
    def addParent(self,p):
        if self.parent == None:
            self.parent = p
            p.addChild(self)
        
    def addChild(self,c):
        if c not in self.childs :
            self.childs[c.name] = c
            c.addParent(self)
            
    def addContinuation(self,c):
        if c not in self.continuations and c != None:
            self.continuations += [c]        
        
class Tree(object):
    def __init__(self, ):
        
        self.nodes = []
        self.heads = {}
        
        self.totalSize = 0
        self.currentContinuation = None
        
    def createNode(self,s,p=None):
        n = Node(s,p)       
        self.nodes.append(n)
        if p == None: self.heads[s] = n
        return n
               
    def parseSubSequence (self,S,p=None):
        if p != None: 
            s=S.pop(0)
            if s in p.childs:
                p = p.childs[s]
            else:
                p = self.createNode(s,p)               
        else:
            S.reverse()
            s=S.pop(0)
            if s in self.heads:
                p = self.heads[s]
            else:
                p = self.createNode(s)
            
        p.addContinuation(self.currentContinuation)        
        if len(S)>0 : self.parseSubSequence(S,p)
        
    def parseSequence (self,S):
        S1 = list(S)
        S2 = list(S)
        lS1 = len(S1)
        while len(S1) > 0:
            self.currentContinuation = self.totalSize + len(S1) + 1
            if self.currentContinuation > self.totalSize+lS1: self.currentContinuation = None
            self.parseSubSequence(S1)
            S2.pop(len(S2)-1)
            S1 = list(S2)
        self.totalSize += lS1
        
#    def display(self):
#        t = "("
#        for n in self.heads:
#            t+= self.heads[n].name + 
#        t += ";)"
        

if __name__ == "__main__":
    
    T = Tree()
    T.parseSequence(['A','B','C','D'])
    T.parseSequence(['A','B','B','C'])
    
    