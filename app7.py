keepGoing = "yes"
print ("Hello I will demonstrate nested loops")
while (keepGoing !="no"):
    for x in range (1, 4):
        for y in range (1, 4):
            print (x,y)
            keepGoing = input ("keep going?")
            if (keepGoing == "no" or keepGoing == "No"):
                break
