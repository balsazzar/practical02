a = int(input("Enter year: "))
if a % 400 == 0:
    print("Leap")
elif a% 4 == 0:
    if a% 100 == 0:
        print("Non-leap")
    else:
        print("Leap")
