# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 12:48:03 2023

@author: mcc
"""


class Stack:
  def __init__(self) :
    self.items=[]

  # return True if the stack is empty
  def isEmpty(self): #O(1)
    if len(self.items)==0:
      return True
    else:
      return False

  # adds an tem to the stack
  #params: value, item to add
  def push(self,value): #O(1)
    self.items.append(value)

# returns the value deleted from the stack
  def pop(self):#O(1)
    if self.isEmpty():
      return None
    return self.items.pop()

#MIB

def MIB_stack(inp):
    s=Stack()
    #loop through the inp
    for char in inp:
        #if ch*
        if char =='*':
            ##pop
            popped=s.pop()
            print(popped)
        else:
            ##push
            s.push(char)
    while not s.isEmpty():
        popped=s.pop()
        print(popped)
        
       

inpu="dawaj*****si ***trams "

MIB_stack(inpu)     
        
    ##push to stack
    
    