# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 01:08:11 2016

@author: alexis
"""

import plotly.plotly as py
import plotly.graph_objs as go
from igraph import Graph, plot
import random

class Node(object):
    def __init__(self,name,index,p=None):
        
        self.name = name
        self.index = index
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
        
        self.tree = Graph()
        
        self.nodes = []
        self.heads = {}
        
        self.listOfNodes = []
        self.historySize = 10
        
    def addVertex(self, obj, p=None):
        self.tree.add_vertex()
        self.tree.vs[len(self.tree.vs)-1]['obj']=obj
        self.tree.vs[len(self.tree.vs)-1]['name']=obj.name
        if p!=None : self.tree.add_edge(p.index,obj.index)
        
    def createNode(self,s,p=None):
        n = Node(s,len(self.nodes),p)       
        self.nodes.append(n)
        if p == None: self.heads[s] = n
        self.addVertex(n,p)
        return n
               
    def addContinuation(self,SIn,c,p=None):
        if len(SIn) > 0:
            S = list(SIn)
            if p == None:
                S.reverse()
                s=S.pop(0)
                if s in self.heads:
                    p = self.heads[s]
                else:
                    p = self.createNode(s)
            else: 
                s=S.pop(0)
                if s in p.childs:
                    p = p.childs[s]
                else:
                    p = self.createNode(s,p)
            p.addContinuation(c)        
            if len(S)>0 : self.addContinuation(S,c,p)
        
    def parseNotesSequence (self,SIn):
        S = list(SIn)
        while len(S) > 1:
            currentContinuation = len(self.listOfNodes) + len(S)
            S.pop(len(S)-1)
            self.addContinuation(S,currentContinuation)  
        self.listOfNodes += SIn
        
    def parseNote(self,note):
        self.listOfNodes += [note]
        size = len(self.listOfNodes)
        subList = self.listOfNodes[max(0,size-self.historySize-1):max(0,size-1)]
        self.addContinuation(subList, size)
        
    def display(self):
        layout = self.tree.layout('kk')
        p = plot(self.tree, layout = layout)
        p.show()
        
    def getContinuations(self,SIn,p=None):
        if len(SIn) > 0:
            if p == None:
                S=list(SIn)
                S.reverse()
                s=S.pop(0)
                if s in self.heads:
                    if len(SIn)==1: return self.heads[s].continuations
                    else: return self.getContinuations(S,self.heads[s])
                else:
                    return None
            else:
                s=SIn.pop(0)
                if s in p.childs:
                    if len(SIn)==0: return p.childs[s].continuations
                    else: return self.getContinuations(SIn,p.childs[s])
                else:
                    return None
                    
    def playRandomly(self,p=None):
        if p==None:
            L=[random.choice(self.heads.keys())]
            print L
            c=self.getContinuations(L)
            print c
            if c!=None:
                L+=[self.listOfNodes[random.choice(c)-1]]
                print L
                self.playRandomly(L)
                return L
        else:
            print p
            c=self.getContinuations(p)
            print c
            if c!=None:
                p+=[self.listOfNodes[random.choice(c)-1]]
                print p
                self.playRandomly(p)
        
        

if __name__ == "__main__":
    
    T = Tree()
    T.parseNotesSequence(['A','B','C','D','E'])
    T.parseNotesSequence(['A','B','B','C','D','E'])
    #T.display()
    
    T1 = Tree()
    l=['A','B','C','D']
    for n in l:
        T1.parseNote(n)
    #T1.display()
        
    T2 = Tree()
    T2.parseNotesSequence(['C','C','C','D','E','D','C','E','D','D','C'])
    T2.parseNotesSequence(['C','C','C','D','E','D','C','E','D','D','C'])
    T2.parseNotesSequence(['D','D','D','A','A','D','C','B','A','G'])
    T2.parseNotesSequence(['C','C','C','D','E','D','C','E','D','D','C'])
    T2.playRandomly()
    