
import math

def taxCalc():
    try:
        pst = 0.07
        gst = 0.05
        income = float(input("enter subtotal > "))
        print(f"your PST total is {income+income * pst}")
        print(f"your PST total is {income+income * gst}")
        print(f"your FULL total is {income+income * (pst+gst)}")
        input("                                                                              press 'enter' to exit")
        return

    except:
        print("                                                                                 not number")
        input()
        return    

taxCalc()