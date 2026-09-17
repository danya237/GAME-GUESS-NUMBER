import random
num = random.randint(1, 100)
print("Welcome to the Number Guessing Game!")
turns = 0
while True:
    guess = int(input("Guess a number between 1 and 100: "))
    turns += 1
    if guess < num:
        print("Too low! Try again.")
    elif guess > num:   
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {num} in {turns} turns.")
        break