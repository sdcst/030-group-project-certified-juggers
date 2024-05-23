import volcalc,areacalc,intercalc,taxcalc

loop = 0

def menu():

    while loop != 1:
        try:
            x = input("                                                                              Choice: ")
                

            if x == "1":
                print("")
                print("                                            Would you like to calculate the area of a square, triangle or circle?")
                x = input("                                                                         Choice: ")
                if x == "square":
                    areacalc.square()
                    return
                if x == "triangle":
                    areacalc.triangle()
                    return
                if x == "circle":
                    areacalc.circle()
                    return
            

            if x == "2":
                print("")
                print("                                          Would you like to calculate the volume of a cube, sphere, cone or rectangualar prism?")
                x = input("                                                                         Choice: ")
                if x == "cube":
                    volcalc.volCube()
                    return
                if x == "sphere":
                    volcalc.volSphre()
                    return
                if x == "cone":
                    volcalc.volCone()
                    return
                if x == "rectangular prism":
                    volcalc.volRectPris()
                    return
                    
            if x == "4":
                print("")
                print("                                                           Would you like to calculate simple or compound")
                x = input("                                                                         Choice: ")
                if x == "simple":
                    intercalc.simple()
                    return
                if x == "compound":
                    intercalc.compound()
                    return

            
            if x == "3":
                print("")
                taxcalc.taxCalc()
                return
    
        except:
            print("")

    