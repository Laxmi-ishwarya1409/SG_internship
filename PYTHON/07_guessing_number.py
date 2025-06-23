def guessing_game():
    secret_number = 42
    max_attempts = 3

    for attempt in range(1, max_attempts + 1):
        try:
            guess = int(input(f"Attempt {attempt}/{max_attempts}: Enter your guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue 

        if guess > secret_number:
            print("Too high")
        elif guess < secret_number:
            print("Too low")
        else:
            print("Correct, You win")
            break
    else:
        print(f"Sorry, you have used all attempts. The number was {secret_number}.")

    replay = input("Play again? (yes/no): ").strip().lower()
    if replay == 'yes':
        guessing_game()

guessing_game()
