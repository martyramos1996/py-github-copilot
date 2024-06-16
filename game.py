import random


def get_user_choice():
    user_choice = input("Enter your choice (r - Rock, p - Paper, or s - Scissors): ")
    if user_choice == "r":
        return "rock"
    elif user_choice == "p":
        return "paper"
    elif user_choice == "s":
        return "scissors"
    else:
        print("Invalid choice! Please try again.")
    return user_choice.lower()


def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])


def compare_choices(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == "rock":
        if computer_choice == "scissors":
            return "You win!"
        else:
            return "You lose!"
    elif user_choice == "paper":
        if computer_choice == "rock":
            return "You win!"
        else:
            return "You lose!"
    elif user_choice == "scissors":
        if computer_choice == "paper":
            return "You win!"
        else:
            return "You lose!"
    else:
        return "Invalid choice!"


def play_again():
    play = input("Do you want to play again? (yes/no): ")
    return play.lower() == "yes"


def game():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"The computer chose {computer_choice}")
        result = compare_choices(user_choice, computer_choice)
        print(result)
        if not play_again():
            break
    print("Goodbye!")


game()
