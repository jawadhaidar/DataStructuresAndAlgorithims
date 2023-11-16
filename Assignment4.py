

print("i did a basic implementation as I  was overloaded in work")
#cities that this company cover
city_list=["saida","sour","chwayfat"]
NotValid=True
DriverRoute={"jawad":["saida","sour"]}
system_status=True
d_l=[]
while system_status:
    user_input=int(input("enter the number: 1. To add a city 2. To add a driver 3. To add a city to the route of a driver 4. Remove a city from a driver’s route 5. To check the deliverability of a package or 6 to exit"))

    if user_input==1:
        # To add a city
        while(NotValid):
            city=input("add a city: ")
            #valid critieria 
            if isinstance(city, str): #i can add more
                city_list.append(city)
                NotValid=False
    
    elif user_input==2:
       # 2. To add a driver
       
        driver=input("add driver name: ")
        DriverRoute[driver]=[]
        print(DriverRoute)
        while(True):
            driver_city=input(f"add a city to drivers route from this option {city_list} in order otherwise enter # ")
            if driver_city=="#":
                break
            if driver_city in city_list:
                d_l=DriverRoute[driver]
                DriverRoute[driver].append(driver_city)
                print(DriverRoute[driver])
            else:
                print("please add it first to the available city list ")
    
    
    elif user_input==3:
        #3. To add a city to the route of a driver
        driver=input("enter the name of the driver: ")
        #I can check if the driver is already there
        city=input("enter the name of the city to add: ")
        #I can check if the city is valid and if it is already in his route
        where=input(f"enter a valid location 1 first, -1 last,# to choose a relevant location: ")
        if where=="1":
            DriverRoute[driver][0]=city
        elif where=="-1":
            DriverRoute[driver][-1]=city
        elif where=="#":
            #I can check if the index is valid
            DriverRoute[driver][int(where)]=city
            
    
    elif user_input==4:
         #4. Remove a city from a driver’s route
        driver=input("enter the name of the driver: ")
        #I can check if the city is even there
        city_remove=input("enter the name of the city to remove: ")
        DriverRoute[driver].remove(city_remove)
        
    
    elif user_input==5:
        #To check the deliverability of a package
        drivers_available=[]
        where2go=input("enter the name of the city you want to go to: ")
        for drive,route in DriverRoute.items():
            if where2go in route:
                drivers_available.append(drive)
        print(drivers_available)
        
    elif user_input==6:
        system_status==False