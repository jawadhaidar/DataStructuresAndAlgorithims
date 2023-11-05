# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 09:55:29 2023

@author: mcc
"""

items_available={ #name price
    "batata": 70000,
    "basal": 50000,
    "toom": 30000
    }
items_ordered={} #name quantity
bill_total=0
discount=0 #in percent
input_user1=1
flag=0
while flag==0:
    input_user=input(f'start a new order press 1 | close press 2')

    if input_user=="1":
        while input_user1!="4":
            input_user1=input(f'1. To add a new item 2. To check the total of the bill 3. To add a coupon 4. To checkout : ')
    
            if input_user1=="1":
                input_user2=input("enter the name of the item: ")
                #items_ordered[input_user2]=items_available[input_user2] #adds the name and price 
                try:
                    items_ordered[input_user2]= items_ordered[input_user2] + 1
                except:
                    items_ordered[input_user2]=1
                    
                print(items_ordered)
            elif input_user1=="2":
                #check the total #mandatory setp before "4
                for item in items_ordered.keys():
                    bill_total=bill_total + items_available[item]* items_ordered[item] #price*quantity
                print(bill_total)  
                 
            elif input_user1=="3":
                #add coupon
                input_user3=input("enter the discount rate : ")
    
            elif input_user1=="4":
                #checkout
                print(f"items bought and their quantity {items_ordered}")
                print(f'total before discount {bill_total}')
                print(f'ra7 no5somlak {{bill_total*(discount)}} ')
                print(f'total after discount {bill_total*(1-discount)}')
                
            
    elif input_user=="2":
        print("byee byeeeeee, zorona koli sa3a maraaa 7aram tinsona bil mara: ")
        flag=1
        
#close the program 