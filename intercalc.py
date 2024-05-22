def simple():
    loop=1
    while loop!=0: 
        x = input("                                                              Enter in an amount of money: ")
        y = input("                                                              Enter in a rate: ")
        z = input("                                                              Enter in a period of time (in years):")
        try:
            x = float(x)
            y = float(y)
            z = float(z)
            print(f"your area is {round((x*(y/100)*z),2)}")
            return
        except:
            print("                                                             One of your values was not a correct number")

    
def compound():
    loop=1
    while loop!=0: 
        x = input("                                                              Enter in an amount of money: ")
        y = input("                                                              Enter in a rate: ")
        z = input("                                                              Enter in a period of time (in years): ")
        w = input("                                                              Enter in how much its compounded per year: ")
        try:
            x = float(x)
            y = float(y)
            z = float(z)
            w = float(w)
            print(f"your amount is {x *((1 + (y/100)/w)**(w*z))}") 
            return
        except:
            print("                                                             One of your values was not a correct number")