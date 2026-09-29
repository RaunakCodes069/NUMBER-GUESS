import random
# Pick a random number between 1 and 100
secret_number = random.randint(1, 100)
# Start the game
print("I am thinking of a number between 1 and 100.")
guessed = False
attempts = 0
# Keep asking until they guess it
while guessed == False:
    # Get the user's guess
    guess = input("Take a guess: ")
    guess = int(guess)
    attempts = attempts + 1
    
    # Check if they are right
    if guess < secret_number:
        print("Your guess is too low.")
    elif guess > secret_number:
        print("Your guess is too high.")
    else:
        print("Good job! You guessed the number in " + str(attempts) + " tries.")
        guessed = True