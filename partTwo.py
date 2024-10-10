import random

secret_number = random.randint(1, 10)

guess = int(input("what is yor guess? "))

if guess > secret_number:
    print ("Too high")
elif guess < secret_number:
    print ("Too low")
else:
    print ("Correct")