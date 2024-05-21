import math

def square():
    print("")
    loop=1
    while loop!=0: 
        try:
            x = float(input("                                                                         Enter in a number: "))
            print(f"                                                                                    your area is {round((x*x),2)}")
            return
            
        except:
            print("                                                                        you did not enter in a correct side length")
            
    
        
def triangle():
    print("")
    
    loop=1
    while loop!=0: 
        x = input("                                                                         Enter in a height: ")
        y = input("                                                                         Enter in a base: ")
        try:
            x = float(x)
            y = float(y)
            print(f"your area is {round((x*y/2),2)}")
            return
        except:
            print("                                                             you did not enter in a correct height and/or base")
            
    
def circle():
    print("")
    loop=1
    while loop!=0: 
        try:
            x = float(input("                                                                         Enter in a radius: "))
            print(f"                                                                                    your area is {round((x**2),2)}")
            return
            
        except:
            print("                                                                        you did not enter in a correct radius")
            
    
