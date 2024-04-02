def History():
    print(Area, Perimeter)



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
                print("B")
                break
            elif AShape == "C" or AShape == "c":
                print("C")
                break
            elif AShape == "D" or AShape == "d":
                print("D") 
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
                print("B")
                break
            elif PShape == "C" or PShape == "c":
                print("C")
                break
            elif PShape == "D" or PShape == "d":
                print("D")
                break
    except ValueError:
        print("**Error**")
        continue

Area = input("{}*{} =".format())
Perimeter = input({}+{})