import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    
    # Define the range for the random number
    lower_bound = int(input("Enter the lower bound of the range: "))
    upper_bound = int(input("Enter the upper bound of the range: "))
    
    # Generate a random number within the specified range
    secret_number = random.randint(lower_bound, upper_bound)
    
    attempts = 0
    guessed = False
    
    print(f"\nI have selected a number between {lower_bound} and {upper_bound}.")
    print("Try to guess it!")

    while not guessed:
        try:
            # Get user's guess
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            # Check if the guess is correct
            if guess < lower_bound or guess > upper_bound:
                print(f"Please enter a number within the range {lower_bound} to {upper_bound}.")
            elif guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                guessed = True
                print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    number_guessing_game()
