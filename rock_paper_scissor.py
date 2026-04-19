import random

ROCK = 'r'
SCISSORS = 's'
PAPER = 'p'
emojis = { ROCK: '🪨', SCISSORS: '✂️', PAPER: '📃' }
choices = tuple(emojis.keys())

def get_user_choice():
    while True:
        user_input = input("Enter your choice (r for rock, s for scissors, p for paper): ").lower()
        if user_input in choices:
            return user_input
        else:
            print("Invalid input. Please enter 'r', 's', or 'p'.")

def get_computer_choice():
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == ROCK and computer_choice == SCISSORS) or \
         (user_choice == SCISSORS and computer_choice == PAPER) or \
         (user_choice == PAPER and computer_choice == ROCK):    
        return "You win!"
    else:
        return "Computer wins!"

def main():
    print("Welcome to Rock, Paper, Scissors!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    print(f"You chose: {emojis[user_choice]} ({user_choice})")
    print(f"Computer chose: {emojis[computer_choice]} ({computer_choice})")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    main()