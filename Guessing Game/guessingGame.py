import random

number = random.randint(1, 10)
tries = 1


username = input("Hello, What is your name? ")

print("Hello", username + ".", )

question = input("Would you like to play a game? [Y/N] ")
if question == "n":
    print("oh..okay")
    print("That's Fine Good No Problem")

if question == "y":
    print("I'm thinking of a number between 1 & 10")
guess = int(input("Have a guess: "))
if guess > number:
    print("Guess a Lower Number...")
if guess < number:
    print("Guess a Higher Number..")
while guess != number:
    tries += 1
    guess = int(input("Try again: "))
    if guess < number:
        print("Guess a Higher Number...")
    if guess > number:
        print("Guess a Lower Number...")
if guess == number:
    print("You're right " + username + "!! you win! The number was {0} and it only took you {1} tries".format(number, tries))