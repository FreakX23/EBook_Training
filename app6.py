failsafe = 0
name = input("What is your favourite book?")
while (name!="this one"):
    print ("incorrect")
    name = input ("try again")
    failsafe += 1
    if (failsafe ==4):
        print ("still wrong, but I'll go ahead and tell you")
        break
    if (name == "this one"):
            print ("correct")
print ("this book is the best book")
