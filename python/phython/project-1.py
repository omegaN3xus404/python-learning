import random

# Generate a random number from the list [-1, 0, 1]
random_number = random.choice([-1, 0, 1])

# Print the random number (for debugging purposes)
print("Computer's choice (random number):", random_number)

# Ask for user input
enter = input("Enter your choice (gun, snake, or water): ").strip().lower()

# Mapping of choices to values
name = {"snake": -1, "gun": 0, "water": 1}

# Check if the user entered a valid choice
if enter in name:
    user_choice = name[enter]

    # Check for draw
    if user_choice == random_number:
        print("It's a draw!")

    # Check for loss conditions
    elif (user_choice == -1 and random_number == 0):  # snake loses to gun
        print("You lose!")
    elif (user_choice == 0 and random_number == 1):  # gun loses to water
        print("You lose!")
    elif (user_choice == 1 and random_number == -1):  # water loses to snake
        print("You lose!")

    # Otherwise, the user wins
    else:
        print("You win!")

else:
    print("Invalid choice, please choose 'gun', 'snake', or 'water'.")









