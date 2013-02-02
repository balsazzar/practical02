running = True
while running:
    a = int(input("Enter number: "))
    if a%2 == 0:
        print(str(a) + " is even")
    else:
        print(str(a) + " is odd")
