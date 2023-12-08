# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 19:42:07 2023

@author: mcc
"""
# a linked list is a list of nodes
class LinkedList:
  def __init__(self):
    self.head=None
    self.tail=None
    self.size=0 # the number of nodes in the LL
    
  def addAtHead(self,value): #O(1)
    n=Node(value,None)
    if self.size==0: # LL is empty
      self.head=n
      self.tail=n
      self.size=1
    else: # LL is not empty
      n.next=self.head
      self.head=n
      self.size+=1
      
  def addAtTail(self,value):#O(1)
    n=Node(value,None)
    if self.size==0: # LL is empty
      self.head=n
      self.tail=n
      self.size=1
    else:
      self.tail.next=n
      self.tail=n
      self.size+=1

  def search(self,info): #O(n), n being the length of the list
    if self.size==0:
      return False # LL is empty

    current=self.head # current keeps track of the node I am at

    while current != None: #O(n)
      if current.value == info:
        return True
      else:
        current=current.next
    return False

  def deleteHead(self): #O(1)
    if self.size==0:#O(1)
      return None#O(1)
    elif self.size==1:#O(1)
      temp=self.head.value #O(1)
      self.head=None#O(1)
      self.tail=None#O(1)
      self.size=0#O(1)
      return temp#O(1)
    # we have more than one node
    else:
      temp=self.head.value #O(1)
      self.head=self.head.next#O(1)
      self.size-=1
      return temp#O(1)

  
  def deleteTail(self): #O(n), n being the size of the LL
    if self.size <=1: # size == 0 or size ==1 
      return self.deleteHead()

    # size>=2
    current=self.head
    temp=self.tail.value
    # while current.next!=self.tail: #O(n)
    while current.next.next!=None:
      current=current.next

    current.next=None
    self.tail=current
    self.size-=1
    return temp

  def printLL(self):
    if self.size==0:
      print("my LL is empty")
    current=self.head
    while current!= None:
      print(current.value,"->",end=" ")
      current=current.next
    print()
    
class AdjacencyList:
  def __init__(self,V):
    self.list_LL=[]
    for i in range(V):
      self.list_LL.append(LinkedList())

  def addEdge(self,vs,ve): #O(V)
    if not self.list_LL[vs].search(ve): #O(V), v being the number of vertices
      self.list_LL[vs].addAtHead(ve)

  def deleteEdge(self,vs,ve): #O(V)
    if self.list_LL[vs].search(ve):
      self.list_LL[vs].deleteValue(ve)

  def showGraph(self):
    for i in range(len(self.list_LL)):
      print("(",i,")",end="")
      self.list_LL[i].printLL()

  def getVerticesInCommon(self,v1,v2): #O(V^2)
    V=len(self.list_LL)
    for i in range(V): #O(V)
      if self.list_LL[v1].search(i) == True and self.list_LL[v2].search(i): #O(V)
        print(i,end=" ")
    print()
    
def citiesIncommon(graph,c1,c2):
    graph.getVerticesInCommon(c1,c2)

def directReach(graph,c):
    #Write another function that takes as input one city 
    #and prints all the other cities directly reachable from it
    for city in self.list_LL[c]:
        print(city)


'''        
def cycle(graph):
    num_v=len(graph.list_LL)
    #for each vertix 
    for v in range(num_v):
        ##get all the v1s connected to it
        if v in graph.list_LL[v]:
            return true
        else:
        #if vertix in v1s return true
        #else
        ##for each of the v1s get their v2s that they are connected to 
        #if vertix in v2ss return true
    
    def cycle1(v,graph)
'''

if __name__=='__main__':
    

    
    
    








