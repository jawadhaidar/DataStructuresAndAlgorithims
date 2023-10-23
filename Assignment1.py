# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



input_assignement=input("select assignment: ")

if input_assignement=="1":
    top=float(input("enter the top  "))
    bottom=float(input("enter the bottom number "))
    val=float(input("enter the number "))
    if val<=top and  val>=bottom:
        print("True")
    else:
        print("False")
elif input_assignement=="2":
    num1=float(input("enter the first number "))
    num2=float(input("enter the second number "))
    num3=float(input("enter the third number "))
    max_num=0
    min_num=0
    
    if num1>=num2 and num1>=num3:
        max_num=num1
        if num2<=num3:
            min_num=num2
        else:
            min_num=num3
    elif num2>=num1 and num2>=num3:
        max_num=num2
        if num1<=num3:
            min_num=num1
        else:
            min_num=num3
    elif num3>=num1 and num3>=num1:
        max_num=num3
        if num1<=num2:
            min_num=num1
        else:
            min_num=num2
    print(f"the min is {min_num} and max is {max_num}")
    
    
elif input_assignement=="3":
    grade=float(input("enter the grade "))
    
    if grade>89:
        print("A")
    elif grade<89 and grade>79:
        print("B")
    elif grade<=79 and grade>69:
        print("C")
    elif grade<=69 and grade>59:
        print("D")
    elif grade<=59:
        print("F")
        
    
    
    
