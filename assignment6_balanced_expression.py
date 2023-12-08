# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 09:52:22 2023

@author: mcc
"""

#balanced expression 
#: (), {},  or [] 

#loop through the expresion
#if par and open push
#if par and close pop and compare 
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

def balanced_expression(inp):
    s=Stack()
    open_close={'(':')',
                '[':']',
                '{':'}'
                }
    for char in inp:
        if char in ['(','{','[']:
            #push to the stack
            s.push(char)
        elif char in [')','}',']']:
            if s.isEmpty(): #case stack is empty and still there is closing tabs
                print("not balanced")
                return False
                
            else: #case not empty stack
                o=s.pop()
                if open_close[o]!=char: #and close not as the remaining open
                    #not balanced 
                    print("not balanced")
                    return False
    if not s.isEmpty():#case removed all pairs and there is still an open
        print("not balanced")
        return False
    print("balanced")
    return True

inp='(1+2)+[{5-1}]]'
inp='1+(1+2)+[{5-1}]'

print(balanced_expression(inp))



    
                
            
            
            
            
    