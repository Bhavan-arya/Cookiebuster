import random

def get_computer_choice():
    choices = ['Rock', 'Paper', 'Scissors']
    return random.choice(choices)

def get_user_choice():
    user_input = input("Choose your best~ (Rock, Paper, Scissors): ")
    while user_input not in ['Rock', 'Paper', 'Scissors']:
        print("Yo! Come back to senses and Please try again.")
        user_input = input("Enter your choice CLEARLY! (Rock, Paper, Scissors): ")
    return user_input

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie! Wtf how did you read the computer mind :O"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper') or \
         (user_choice == 'Paper' and computer_choice == 'Rock'):
        return "Yey! You defeated the Computer."
    else:
        return "Oopsie..You lost so Computer wins!"

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

# Start the game and kill your boredome
play_game()
