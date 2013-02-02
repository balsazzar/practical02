running = True
while running:
    a = int(input("Enter length of side: "))
    b = int(input("Enter length of side: "))
    c = int(input("Enter length of side: "))    
    if a+b>c and b+c>a and c+b>a :
        perimeter = int(a + b + c)
        print("Perimeter = " + str(perimeter))
        running = False
    else:
        print("Invalid triangle! Try again")
