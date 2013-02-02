i = 1
k = 20
print("{0:<} {1:<} {2:<} {3:<}".format("Miles","Kilometre","Kilometre","miles"))
while ((i<=10) and (k<=65)):
    print("{0:<5} {1:<9.3f} {2:<9} {3:<.3f}".format(str(i),float(int(i)*1.609),
                                                   str(k),float(int(k)/1.609)))
    i = i + 1
    k = k + 5
