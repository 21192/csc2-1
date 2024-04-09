import math
def myhistory():
    for x in Equation:
      print(UserHistory)  

UserHistory = ("UH")
Equation = 0

    
History_list = []
Equations = 0


while True:
    try:
        AandP = input ("(A) Area\n(B) Perimeter\n(C) HINT\n")
        if AandP == "A" or AandP == "a":
    
            AShape = input("Shape:\n(A) Triangle\n(B) Square\n(C) Rectangle\n(D) Circle\n")
            if AShape == "A" or AShape == "a":
                THeight = float(input("Height: "))
                TBase = float(input("Base: "))
                print("The Answer is: "+str(THeight * TBase /2)) 
                break

            elif AShape == "B" or AShape == "b":
                SSize = float(input("Square Size: "))
                print("The Answer is: "+str(SSize * SSize))
                break
            elif AShape == "C" or AShape == "c":
                RLength = float(input("Length: "))
                RWidth = float(input("Width: "))
                print("The Answer is: "+str(RLength * RWidth))
                break
            elif AShape == "D" or AShape == "d":
                CRadius = float(input("Radius: "))
                print("The Answer is: "+str(CRadius^2 * math.pi ))
                break
        
        elif AandP == "B" or AandP == "b":        
            PShape = input("Shape:\n(A) Triangle\n(B) Square\n(C) Rectangle\n(D) Circle\n")
            if PShape == "A" or PShape == "a":
                T1 = float(input("Size: "))
                T2 = float(input("Size: "))
                T3 = float(input("Size: "))
                print("The Answer is: "+str(T1 + T2 + T3))
                break
            elif PShape == "B" or PShape == "b":
                SPeri = float(input("Square Size: "))
                print("The Answer is: "+str(SPeri * 4))
                break
            elif PShape == "C" or PShape == "c":
                R1 = float(input("Length: "))
                R2 = float(input("Width: "))
                print("The Answer is: "+str(R1 + R1 + R2 + R2))
                break
            elif PShape == "D" or PShape == "d":
                C1 = float(input("Radius: "))
                print("The Answer is: "+str(2 * math.pi * C1))
                break
        elif AandP == "C" or AandP == "c":
            print("HINT")
    except ValueError:
        print("Pick either (A) (B) or (C)")
        continue