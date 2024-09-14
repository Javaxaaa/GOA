import random

user_number = int(input("Please enter a number between 1 and 100: "))

attempts = 0
guessed = False

print("The program will try to guess your number!")

while not guessed:
    attempts += 1
    
    computer_guess = random.randint(1, 100)
    print(f"Guess: {computer_guess}")
    
    if computer_guess == user_number:
        print(f"The program guessed your number {user_number} in {attempts} attempts!")
        guessed = True
    else:
        print("Incorrect, trying again...")










