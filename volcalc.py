
#volume calculations

import math

def volRectPris():
    l = input("enter a length > ")
    l=float(l)
    w = input("enter a width > ")
    w=float(w)
    h = input("enter a height > ")
    h=float(h)
    
    if l  < 0 or w < 0 or h < 0:
        print("you cant do that")
        return
    if l > 0 and w > 0 and h > 0:
        print(f"your volume is now {l*w*h}")
        input("press 'enter' to exit")       
        return
    else:
        print("not number")
        return

volRectPris()

def volSphre():
    try:
        r = input("enter a radiuz > ")
        r=float(r)
        print(f"the volume is {(4/3)*3.14*(r**3)}")
        input("press 'enter' to exit")
        return
    except:
        print("not number")
        input()
        return

#volSphre()   


def volCube():
    try:
        v = input("enter a length > ")
        v = float(v)
        print(f"the volume is {v*v*v}")
        input("press 'enter' to exit")
        return
    except:
        print("not number")
        input()
        return

#volCube()

def volCone():
    try:
        h = input("enter a height > ")
        h=float(h)
        v2 = input("enter a radius > ")
        v2 = float(r)
        print(f"the volume is {(1/3)*3.14*v2**2*(h)}")
        input("press 'enter' to exit")
        return
    except:
        print("not number")
        input()
        return

##volCone()








