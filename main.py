# Import necessary modules
import random
from art import logo, vs_symbol  # Import the logo and vs symbol from art.py
from game_data import data  # Import the list of accounts from game_data.py

# Function to get a random account from the data

def get_random_account():
    return random.choice(data)

# Function to format the account for display
def format_account(account):
    """Format account into printable format: Name, description and country."""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description} from {country}"

# Function to check if the player's guess is correct
def check_guess(guess, a_followers, b_followers):
    """Check followers against user's guess and return if they got it right."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

# Main game logic
def play_game():
    print(logo)
    score = 0
    game_should_continue = True
    account_a = get_random_account()
    account_b = get_random_account()

    while game_should_continue:
        account_a = account_b
        account_b = get_random_account()

        print(f"Compare A: {format_account(account_a)}")
        print(vs_symbol)
        print(f"Against B: {format_account(account_b)}")

        # Ask user for their guess
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        # Get follower counts
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]

        # Check if user is correct
        is_correct = check_guess(guess, a_follower_count, b_follower_count)

        # Give feedback and update score
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}.")

play_game()
