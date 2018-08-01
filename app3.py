usrAge = int(input("enter your age:"))
if (usrAge >= 80):
    print ("you are pretty old")
elif (usrAge > 20 and usrAge < 80):
    print ("you are an adult")
elif (usrAge > 12 and usrAge > 20):
    print ("you are a teenager")
else:
    print ("You are a child")
