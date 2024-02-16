import random
from stand import stand
from hit import hit
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

print("Welcome to Blackjack")
print(logo)

new_game = input("want to play Blackjack game. Y-Yes , N-No\n ")
if new_game.upper() == 'YES' or new_game.upper() == 'Y':
    start = True
else:
    start = False
    print("Good Bye")

while start:
    computer_choice_list = [random.choice(cards), "_"]
    player_choice_list = [random.choice(cards), random.choice(cards)]
    print(f"Dealer cards {computer_choice_list}")
    print(f"Your cards {player_choice_list}")
    computer_choice_list[1] = random.choice(cards)

    should_continue = True
    while should_continue:
        hit_or_stand = input("You want to hit or stand- H / S\n")
        if hit_or_stand.upper() == 'H':
            result, player_choice_list, computer_choice_list = hit(player_choice_list, computer_choice_list)
        elif hit_or_stand.upper() == "S":
            result, player_choice_list, computer_choice_list = \
                stand(player_choice_list, computer_choice_list)
        else:

            print("Enter valid button.")

        if result == "player_continue":
            print(f"Your cards {player_choice_list}")

        else:
            print(f"dealer cards {computer_choice_list} ")
            print(f"Your cards {player_choice_list}")
            if result == "players":
                print("You win")
            elif result == "draw":
                print("It's a draw")
            else:
                print("Dealer win")
            should_continue = False
            new_game = input("want to play another game. Y-Yes , N-No\n")
            if new_game.upper() == 'NO' or new_game.upper() == 'N':
                start = False
                print("Good Bye")