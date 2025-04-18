import random

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    print(f"\n🎲 You rolled: {die1} and {die2}")
    print(f"Total: {die1 + die2}")

while True:
    user_input = input("\nRoll the dice? (y/n): ").lower()
    if user_input == 'y':
        roll_dice()
    elif user_input == 'n':
        print("Thanks for playing! 🎲 See you next time! 🎉")
        break
    else:
        print("Please enter 'y' or 'n'.")
