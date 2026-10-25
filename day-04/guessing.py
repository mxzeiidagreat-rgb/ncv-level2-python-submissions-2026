secret_number = 12
attempts = 0
guessed_correctly = False

while attempts < 5 and not guessed_correctly:
    guess = input("Enter your guess (1-20): ")

    if not guess.isdigit():
        print("Please enter a numeric value.")
    else:
        guess = int(guess)

        if guess < 1 or guess > 20:
            print("Please enter a number between 1 and 20.")
        else:
            attempts += 1

            if guess == secret_number:
                print("Correct!")
                guessed_correctly = True
            elif guess < secret_number:
                print("Too low")
            else:
                print("Too high")

if not guessed_correctly:
    print(f"You did not guess correctly. The secret number was {secret_number}.")