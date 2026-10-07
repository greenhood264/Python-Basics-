import random

x=random.randint(1,10)
guess=(int(input("Guess a number between 1 and 10: ")))
tries=1

while(guess!=x):
    if guess<x:
        print("Your guess is too low")
    else:
        print("Your guess is too high")
    guess=(int(input("Guess a number between 1 and 10: ")))
    tries+=1
    if guess==x:
            print("You guessed it in",tries, "tries")