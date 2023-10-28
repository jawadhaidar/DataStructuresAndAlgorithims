
assignment_num=int(input("choose the assignment number: "))
print(12/5)
if assignment_num==1:
    number=int(input("enter the number: "))
    count=1
    while(number>=10):
        number=number/10
        count+=1
    print(f'number of digits: {count}')
    
elif assignment_num==2:
    number=int(input("enter the number of stars: "))
    for i in range(number):
        print("*"*(i+1))
        
elif assignment_num==3:
    list1=[54,76,2,4,98,100]
    list_inrange=[]
    number1=int(input("enter the upper bound: "))
    number2=int(input("enter the lower bound: "))
    for num in list1:
        if num<=number1 and num>=number2:
            list_inrange.append(num)
            
    print(list_inrange)
            
elif assignment_num==4: 
    Names=["Maria","Hala","Ghady","Ehsan","Joe","Zoe"]
    chosen_names=[]
    while(True):
        input_letter=input("enter a letter: ")
        for name in Names:
            if input_letter in name or input_letter.upper() in name:
                chosen_names.append(name)
        print(chosen_names)
                
           
    