import random

def get_user_choice():
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

def display_result(user_choice, computer_choice, winner):
    print(f"\nUser's choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")
    if winner == 'tie':
        print("It's a tie!")
    elif winner == 'user':
        print("Congratulations! You win!")
    else:
        print("Sorry, you lose.")

def play_again():
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    return play_again == 'yes'

def play_game():
    user_score = 0
    computer_score = 0
    
    while True:
        print("\n--- Rock-Paper-Scissors Game ---")
        
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        winner = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, winner)
        
        if winner == 'user':
            user_score += 1
        elif winner == 'computer':
            computer_score += 1
        
        print(f"\nCurrent Score - User: {user_score}, Computer: {computer_score}")
        
        if not play_again():
            break

play_game()
