import volcalc,areacalc,intercalc

def menu():
   
    x = input("                                                                              Choice: ")

    if x == "exit":
        exit()


    if x == "1":
        print("")
        print("                                            Would you like to calculate the area of a square, triangle or circle?")
        x = input("                                                                         Choice: ")
        if x == "square":
            areacalc.square()
        if x == "triangle":
            areacalc.triangle()
        if x == "circle":
            areacalc.circle()
            

    if x == "2":
        print("")
        print("                                          Would you like to calculate the volume of a cube, sphere, cone or rectangualar prism?")
        x = input("                                                                         Choice: ")
        if x == "cube":
            volcalc.volCube()
        if x == "sphere":
            volcalc.volSphre()
        if x == "cone":
            volcalc.volCone()
        if x == "rectangular prism":
            volcalc.volRectPris()
            
    if x == "4":
        print("")
        print("                                                           Would you like to calculate simple or compound")
        x = input("                                                                         Choice: ")
        if x == "simple":
            intercalc.simple()
        if x == "compound":
            intercalc.compound()
            
    
        

    