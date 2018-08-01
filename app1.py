# This Part will gather Infos and demonstrate the use of Variables.
usrName = input("What is your Name?")
usrAge = int(input("What is your Age?"))
usrGPA = float(input("What is your GPA?"))
print () #cheap way to get a new line
print ("Hello, %s" % (usrName))
print ("Did you know that in two years you will be %d years old? " % (usrAge +2))
print ("Also you need to improve your GPA by %f points to have a perfect score." % (4.0 - usrGPA))
print ()
