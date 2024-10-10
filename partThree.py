x = int(input("what is the score between 0-100? "))

if 100 > x > 90:
    print ("A")
elif 89 > x > 80:
    print ("B")
elif 79 > x > 70:
    print ("C")
elif 69 > x > 60:
    print ("D")
elif 59 > x > 0:
    print ("F")
else:
    print("please input a number between 0-100.")