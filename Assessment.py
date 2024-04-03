def History():
    print(Area, Perimeter)


π = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679

    
History_list = []
Equations = 0


while True:
    try:
        AandP = input ("(A) Area\n(B) Perimeter\n")
        if AandP == "A" or AandP == "a":
    
            AShape = input("Shape:\n(A) Triangle\n(B) Square\n(C) Rectangle\n(D) Circle\n")
            if AShape == "A" or AShape == "a":
                THeight = int(input("Height: "))
                TBase = int(input("Base: "))
                print(THeight * TBase /2) 
                break

            elif AShape == "B" or AShape == "b":
                SSize = int(input("Square Size: "))
                print(SSize * SSize)
                break
            elif AShape == "C" or AShape == "c":
                RLength = int(input("Length: "))
                RWidth = int(input("Width: "))
                print(RLength * RWidth)
                break
            elif AShape == "D" or AShape == "d":
                CRadius = int(input("Radius: "))
                print(CRadius^2 * π )
                break
        
        elif AandP == "B" or AandP == "b":        
            PShape = input("Shape:\n(A) Triangle\n(B) Square\n(C) Rectangle\n(D) Circle\n")
            if PShape == "A" or PShape == "a":
                T1 = int(input("Size: "))
                T2 = int(input("Size: "))
                T3 = int(input("Size: "))
                print(T1 + T2 + T3)
                break
            elif PShape == "B" or PShape == "b":
                SPeri = int(input("Square Size: "))
                print(SPeri * 4)
                break
            elif PShape == "C" or PShape == "c":
                R1 = int(input("Length: "))
                R2 = int(input("Width: "))
                print(R1 + R1 + R2 + R2)
                break
            elif PShape == "D" or PShape == "d":
                C1 = int(input("Radius: "))
                print(2 * π * C1)
                break
    except ValueError:
        print("**Error**")
        continue

Area = input("{}*{} =".format())
Perimeter = input({}+{})