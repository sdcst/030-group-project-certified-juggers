
#volume calculations


def volRectPris():
    l = input("enter a length > ")
    l=float(l)
    w = input("enter a width > ")
    w=float(w)
    h = input("enter a height > ")
    h=float(h)
    
    

    if l  < 0 or w < 0 or h < 0:
        print("you cant do that")

    if l > 0 and w > 0 and h > 0:
        print(f"your volume is now {l*w*h}")
        return
    else:
        print("not number")
        return

volRectPris()
