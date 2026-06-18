import random

number = random.randint(1,100)

print("Guess the number (1-100)")
guess = 0
# Running game until user guesses the correct number 
while guess != number:
    # Taking guess from user
    guess = int(input("Enter your guess:"))
    # Checking user's guess
    if guess < number:
        print("Too Low")

    elif guess > number:
        print("Too High")

    else:
        print("You Win!")