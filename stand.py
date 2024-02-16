import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def stand(player_choice_list, computer_choice_list):
    total_of_player = sum(player_choice_list)
    total_of_dealer = sum(computer_choice_list)

    while total_of_dealer < 17:
        computer_choice = random.choice(cards)
        computer_choice_list.append(computer_choice)
        total_of_dealer += computer_choice

    if total_of_dealer>21:
        if (11 in computer_choice_list):
            computer_choice_list.remove(11)
            computer_choice_list.append(1)
            total_of_dealer = sum(computer_choice_list)

    if total_of_dealer>21:
        return "players",player_choice_list,computer_choice_list
    elif total_of_player>total_of_dealer:
        return "players", player_choice_list, computer_choice_list
    elif total_of_player==total_of_dealer:
        return "draw",player_choice_list, computer_choice_list
    else:
        return "dealers", player_choice_list, computer_choice_list
