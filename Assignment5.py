# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 11:01:51 2023

@author: mcc
"""



input_user=input("excersise number: ")

if input_user=="1":
    #alphabatical order
    def compare_alpha(in1,in2):#check nif in1 less than in2
        #loop acc to min length
        in1_length=len(in1)
        in2_length=len(in2)
        #compare
        for id in range(min(in1_length,in2_length)):
            in1_status=in1[id].isupper()
            in2_status=in2[id].isupper()
            #case both are small or capital
            if in1_status==in2_status:
                if in1[id]<in2[id]:
                    return True
            #case first is capital and second small
            elif in1_status and not in2_status:
                if in1[id].lower() < in2[id]:
                    return True
    
            #case second is capital
            elif not in1_status and in2_status:
                if in1[id] <= in2[id].lower(): #= to give privilege for lower case
                    return True
                
        return False
    #order matters once you call func inside func
    def selectionSort(list1): #O(n^2)
      border=0
      while border <len(list1)-1: #O(n), n being the length of the list
        minIndex=border # contain the index of the minimum element
        for i in range(border+1, len(list1)): # to find the index of the minimum element, O(n)
          if compare_alpha(list1[i],list1[minIndex]): #O(1), is the line that specifies the order
            minIndex=i
        #swap the two elements
        temp=list1[border] #O(1)
        list1[border]=list1[minIndex]
        list1[minIndex]=temp
    
        # list1[border],list1[minIndex]=list1[minIndex],list1[border]
    
        border=border+1
        # border+=1
      print(list1)
      
    list1=["aA","B","b", "BD","Bc","D"]
    #list1=["abbbbbbbb","c","b","B"]
    selectionSort(list1)

#equal case -->move to second index 
#capital case to capital --> leave 
#capital to small --> chane to small , if equall choose small as min else choose the smaller value


else:
    #merge sort 
    
    def mergeSort(list1,start,end): #O(n log n)
      # base case
      if start==end: #I have a list of length 1
        return
      mid=(start+end)//2 #binary search
      mergeSort(list1,start,mid) # dividing the list further
      mergeSort(list1,mid+1,end)
      merge(list1,start,mid,end) # I am passing the division of the list
    
    def merge(list1,start,mid,end): # to merge the two sublists into a sorted one, O(n), n being the length of the list
      new_list=[]
      ind1=start # this points to the start of the first sub-list
      ind2=mid+1 # this points to the start of the second sub-list
    
      while ind1<=mid and ind2<=end: # I have elements in both sublists
        if list1[ind1]>list1[ind2]:
          new_list.append(list1[ind1])
          ind1+=1
        else: # the element in my second sublist is smaller
          new_list.append(list1[ind2])
          ind2+=1
      # this means that the elements of sublist 1 OR sublist 2 are complete
    
      while ind1<=mid:
        new_list.append(list1[ind1])
        ind1+=1
        
      while ind2<=end: 
        new_list.append(list1[ind2])
        ind2+=1
    
      # I finished copying all the elements
      #new_list contains the same elements as list1 but in an ordered way
      list1[start:end+1]=new_list
      
    list1=[1,5,3,7,8,5,3,9,6]
    mergeSort(list1,start=0,end=len(list1)-1)
    print(list1)
    