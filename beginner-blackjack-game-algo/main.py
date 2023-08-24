import random
from art import logo


def compare(user_total, computer_total):
    if user_total > computer_total:
        return user_total
    else:
        return computer_total


def total(cards):
    total = 0
    for card in cards:
        total += card
    return total


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
print(logo)
print("Welcome to the blackjack game!")

user_input = input("Enter 'yes' to deal cards: ").lower()
user_cards = []
computer_cards = []
user_total = 0
computer_total = 0

if user_input == "yes":
    for _ in range(0, 2):
        user_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))
        user_total = total(user_cards)
        computer_total = total(computer_cards)

    print(f"User cards: {user_cards}\nComputer cards: [{computer_cards[0]}, 'X']")

    if user_total > 21 and 11 not in user_cards:
        print(f"User cards: {user_cards}\nComputer cards: [{computer_cards[0]}, 'X']")
        print("You went over. You lost!")
    elif computer_total > 21:
        print(f"User cards: {user_cards}\nComputer cards: [{computer_cards[0]}, 'X']")
        print("Computer went over! You won!")
    else:
        another_card = input("Do you want another card? ").lower()
        if another_card == "yes":
            while another_card == "yes":
                user_cards.append(random.choice(cards))
                user_total = total(user_cards)
                print(f"User cards: {user_cards}\nComputer cards: [{computer_cards[0]}, 'X']")
                if user_total > 21 and 11 not in user_cards:
                    print(f"User cards: {user_cards}\nComputer cards: [{computer_cards[0]}, 'X']")
                    print("You went over. You lost!")
                    break
                elif 11 in user_cards:
                    for x in range(0, len(user_cards)):
                        if user_cards[x] == 11:
                            user_cards[x] = 1
                    user_total = total(user_cards)
                    another_card = input("Do you want another card? ").lower()
                else:
                    another_card = input("Want another card? ").lower()
                    if another_card == "no":
                        while computer_total < 16:
                            computer_cards.append(random.choice(cards))
                            computer_total = total(computer_cards)
                        if computer_total > 21:
                            print(f"User cards: {user_cards}\nComputer cards: {computer_cards}")
                            print("Computer went over! You won!")
                        else:
                            user_total = total(user_cards)
                            computer_total = total(computer_cards)
                            winner = compare(user_total, computer_total)
                            if winner == user_total:
                                print(f"User cards: {user_cards}\nComputer cards: {computer_cards}")
                                print("You won!")
                            else:
                                print(f"User cards: {user_cards}\nComputer cards: {computer_cards}")
                                print("Computer won!")
                            break
        else:
            while computer_total < 16:
                computer_cards.append(random.choice(cards))
                computer_total = total(computer_cards)
            if computer_total > 21:
                print(f"User cards: {user_cards}\nComputer cards: {computer_cards}")
                print("Computer went over! You won!")
            else:
                user_total = total(user_cards)
                computer_total = total(computer_cards)
                winner = compare(user_total, computer_total)
                if winner == user_total:
                    print(f"User cards: {user_cards}\nComputer cards: {computer_cards}")
                    print("You won!")
                else:
                    print(f"User cards: {user_cards}\nComputer cards: {computer_cards}")
                    print("Computer won!")

