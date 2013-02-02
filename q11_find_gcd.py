a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a<b:
    c=int(a)
    d=int(b)
else:
    c=int(b)
    d=int(a)
if d%c==0:
    print("Greatest Common Divisor is: " +str(c))
else:
    c = c - 1
    while(d%c!=0) and (b%c!=0):
        print(c)
        c = c - 1
    while(d%c==0) and (b%c!=0):
        print("wer")
        c= c - 1
print("Greatest Common Divisor is: " +str(c))
        
    
