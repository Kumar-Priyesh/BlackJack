import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def hit(player_choice_list, computer_choice_list):
    player_choice_list.append(random.choice(cards))
    total_of_player = sum(player_choice_list)
    if total_of_player>21:
        if (11 in player_choice_list):
            player_choice_list.remove(11)
            player_choice_list.append(1)
            return "player_continue", player_choice_list, computer_choice_list
        return "dealerh",player_choice_list,computer_choice_list
    else:
        return "player_continue",player_choice_list,computer_choice_list
