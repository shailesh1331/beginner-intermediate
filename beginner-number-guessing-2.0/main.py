import random

NUMBER = random.randint(1, 100)
print("Welcome to the number guessing game!")
print("I am thinking of a number between 1 and 100!")
difficulty = input("Enter difficulty: type easy or hard:\n")
if difficulty == "easy":
    lives = 10
elif difficulty == "hard":
    lives = 5
else:
    lives = 0
print(f"You have {lives} lives!")
game_on = True
while game_on:
    guess = int(input("Guess the number\n"))
    if guess == NUMBER:
        print("Yes you guessed it right! You won!")
        game_on = False
    elif guess < NUMBER:
        print("Too low!")
        lives -= 1
        print(f"You have {lives} lives left!")
        if lives == 0:
            print("You ran out of lives!")
            game_on = False
    else:
        print("Too high")
        lives -= 1
        print(f"You have {lives} lives left!")
        if lives == 0:
            print("You ran out of lives!")
            game_on = False
