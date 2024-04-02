def History():
    print(Area, Perimeter)

History_List 




while True:
    try:
        Shape = input("Shape:\n(A) Triangle\n(B) Square\n(C) Rectangle\n(D) Circle\n")
        if Shape == "A" or Shape == "a":
            print("A")
            break
        elif Shape == "B" or Shape == "b":
            print("B")
            break
        elif Shape == "C" or Shape == "c":
            print("C")
            break
        elif Shape == "D" or Shape == "d":
            print("D") 
            break
    except ValueError:
            print("**Error**")
            continue
Area = input("{}*{} =".format())
Perimeter = input({}+{})