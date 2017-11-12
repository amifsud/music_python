# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 01:08:11 2016

@author: alexis
"""

import plotly.plotly as py
import plotly.graph_objs as go
from igraph import Graph, plot

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
        
    def parseSequence (self,SIn):
        S = list(SIn)
        while len(S) > 1:
            currentContinuation = len(self.listOfNodes) + len(S)
            S.pop(len(S)-1)
            self.addContinuation(S,currentContinuation)  
        self.listOfNodes += SIn
        
    def display(self):
        layout = self.tree.layout('kk')
        p = plot(self.tree, layout = layout)
        p.show()

if __name__ == "__main__":
    
    T = Tree()
    T.parseSequence(['A','B','C','D'])
    T.parseSequence(['A','B','B','C'])
    T.display()
    
    