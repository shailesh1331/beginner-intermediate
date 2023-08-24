from art import logo, vs
from game_data import data

print(logo)

def compare(one, two):
    return "higher" if two > one else "lower"

print("Welcome to the higher lower game!")
score = 0
total_rounds = len(data) - 1

for i in range(total_rounds):
    current_data = data[i]
    next_data = data[i + 1]

    print(f"name: {current_data['name']}, description: {current_data['description']}, country: {current_data['country']}")
    print(vs)
    print(f"name: {next_data['name']}, description: {next_data['description']}, country: {next_data['country']}")

    answer = compare(current_data['follower_count'], next_data['follower_count'])
    guess = input(f"{next_data['name']} has higher or lower followers? ").lower()

    if guess == answer:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    print(f"Your score is {score} out of {i+1}")
    print()

print("Game Over!")
