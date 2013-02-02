grade = int(input("Enter Score: "))
running = True
while running:
    if 70<=grade<=100:
        print("Your grade is A")
        running = False
    elif 59<grade<70:
        print("Your grade is B")
        running = False
    elif 54<grade<60:
        print("Your grade is C")
        running = False
    elif 49<grade<55:
        print("Your grade is D")
        running = False
    elif 44<grade<50:
        print("Your grade is E")
        running = False
    elif 34<grade<45:
        print("Your grade is S")
        running = False
    elif 0<=grade<35:
        print("Your grade is U")
        running = False
    else:
        print("Invalid score! Please enter a number between 1-100")
        grade = int(input("Enter Score: "))   
