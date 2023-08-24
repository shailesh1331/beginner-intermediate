import random

print("Welcome to the Hangman game urff Name guessing game!")
word_list = ["aardvark", "baboon", "camel"]
chosen_word=random.choice(word_list)
blanks=[]
for x in range(0,len(chosen_word)):
    blanks.append("_")
player_lives=3
game_on=True
while game_on:
    print(blanks)
    guess=input("Guess a letter:\n")
    if guess in chosen_word:
        for x in range(0,len(chosen_word)):
            if guess==chosen_word[x]:
                blanks[x]=guess
        if "_" not in blanks:
            print(blanks)
            print(f"You have completed the word {chosen_word}!")
            print("You have won!")
            game_on=False
    else:
        player_lives-=1
        if player_lives==0:
            print("You lost all your lives!")
            game_on=False
        else:
            print(f"You have guessed wrong! You have {player_lives}lives left!")