import areacalc

#print("edited by Sebastiaan ter Keurs :)")
#for i in range (1000):
#    print("\n")


t = 0

def title():
    print("                                                                  ___   _   _    ___     _   ___ ___ ")
    print("                                                                 / __| /_\ | |  / _____ /_\ | _ | _ \ ")
    print("                                                                | (__ / _ \| |_| (_|___/ _ \|  _|  _/")
    print("                                                                 \___/_/ \_|____\___| /_/ \_|_| |_|  ")
    print("                                                                         BY MARCUS AND MATTHEW")
    print("")
    print("                                                                                 OPTIONS")
    print("")
    print("                                                         1 -  Area Calculations     2 - Volume Calculations")
    print("                                                         3 -  Tax Calculations      4 - Interest Calculations")
    print('                                                                       (type in "exit" to stop) ')
    print('                                                                      (type in "enter" to return) ')
    print("")
    print("                                                   Enter in the corresponding number of whatever you want to calculate ")
title()
x = input("                                                                                 Choice: ")


if x == "exit":
    exit()

if x == "1":
    print("")
    print("                                              Would you like to calculate the area of a square, triangle or circle?")
    x = input("                                                                             Choice: ")
    if x == "square":
        areacalc.square()
    if x == "triangle":
        areacalc.triangle()
    if x == "circle":
        areacalc.circle()

else:
    x = print("                                                that is not one of the choices, please enter in either 1, 2, 3 or 4 ")
    x = input("                                                                                 Choice: ")

    