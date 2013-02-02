a = int(input("Enter number: "))
b = 2
while (a/b>=1):
    if(a%b==0):
        print(b)
        a=a/b
    else:
        b = b + 1
