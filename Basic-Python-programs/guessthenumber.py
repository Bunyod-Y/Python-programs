import random
print("Welcome to the Guess the Number game!")
print("I'm thinking of a number between 1 and 100.")
number_to_guess = random.randint(1, 100)
attempts = 0    
max_attempts = 10
while attempts < max_attempts:
    guess = int(input("Take a guess: "))
    attempts += 1
    if guess < number_to_guess:
        print("Your guess is too low.")
    elif guess > number_to_guess:
        print("Your guess is too high.")
    else:
        print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
        break
if attempts == max_attempts:
    print(f"Sorry! You've used all your attempts. The number was {number_to_guess}.")
# This is a simple number guessing game where the user has to guess a number between 1 and 100.
