# This is the Guess Number

import random

number = random.randint(1, 20)
print("Hello! What's your name?")
myName = input()
print(f"Well, {myName}, I am thinking of a number between 1 to 20.")
print("You have 6 guess.")
guessesTaken = 0
for guessesTaken in range(6):
    print("Take a guess")
    guess = int(input())
    
    if guess < number:
        print("Your guess is too low")
        
    if guess > number:
        print("Your guess is too high")
        
    if guess == number:
        break
    
if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print(f"Good job, {myName}! You guessed my number in {guessesTaken} guess!")

else:
    print(f"Nope The number I was thinking of was {str(number)}. Good luck next time!")