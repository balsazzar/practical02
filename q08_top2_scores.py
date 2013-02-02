a = int(input("Enter number of students: "))
b = 1
e = 0
g = 0
f = str("name")
while(b <=a):
    c = input("Enter name of student: ")
    d = int(input("Enter score of " + str(c) +":"))
    if e<d:
        g=int(e)
        j=str(f)
        e=int(d)
        f=str(c)
    if g<d<e:
        g=int(d)
        j=str(c)
    b=b+1
print(str(f) + " has the higest score of " + str(e))
print(str(j) + " has the second higest score of " + str(g))
