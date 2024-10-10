age = int(input("how old are you? "))
s = input("are you a student? ")

if s == "yes" and 12 <= age <= 64:
    print ("student discount - tickets cost £8")
elif age < 12 or age > 64:
    print ("child/senior discount - tickets cost £5")
else:
    print("tickets cost £10")
