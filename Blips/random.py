from random import randint

#Simple number guessing game.

number = randint(0,100)

while True:
    guess = int(input("Guess a number between 0 and 100:"))
    if (guess > number):
        print ("Too high")
    elif (guess < number):
        print ("Too low")
    else:
        print ("Correct! Thanks for playing.")
        break

