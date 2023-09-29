import random

# Set the range for the random number
lower_limit = 1
upper_limit = 100
secret_number = random.randint(lower_limit, upper_limit)

attempts = 0

print(f"Welcome to the Number Guessing Game! Guess a number between {lower_limit} and {upper_limit}.")

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < lower_limit or guess > upper_limit:
            print(f"Please enter a number between {lower_limit} and {upper_limit}.")
        elif guess < secret_number:
            print("Too low! Try a higher number.")
        elif guess > secret_number:
            print("Too high! Try a lower number.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} correctly in {attempts} attempts.")
            break

    except ValueError:
        print("Invalid input. Please enter a valid number.")

print("Thank you for playing!")