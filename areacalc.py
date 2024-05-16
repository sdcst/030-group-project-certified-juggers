import math

def square():
    print("")
    try:
        x = float(input("                                                                         Enter in a number: "))

    except:
        print("                                                                        you did not enter in a number")
        x = input("                                                                         Enter in a number: ")
    
            
    
    if x == round(x,2):
        print(f"                                                                            your area is {x*x}")
        return
    
    else:
        print("                                                                    enter in a valid number bruh")
        x = float(input("                                                                         Enter in a number: "))
        return

        


