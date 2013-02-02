month = [ "January", "February", "March", "April", "May", "June", "July", "August",
          "September", "October", "November", "December"]
a = int(input("Enter Month: "))
b = int(input("Enter Year: "))
if a==1 or a==3 or a==5 or a==7 or a==8 or a==10 or a==12:
    print( month[a-1] +" " + str(b) + " has 31 days.")
elif a ==4 or a==6 or a==9 or a==11:
    print(month[a-1] +" " + str(b) + " has 30 days.")
else:
    if b%400==0 or (b%4==0 and b%100!=0):
        print(month[a-1] + " " + str(b) + " has 29 days.")
    else:
        print(month[a-1] + " " + str(b) + " has 28 days.")
