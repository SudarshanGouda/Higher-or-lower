## Higher or lower

import random
from game_data import data
from art import *
from replit import clear


def check_ans(first, second):
    first_count = first['follower_count']
    second_count = second['follower_count']
    if first_count > second_count:
        winner = "a"
    else:
        winner = 'b'
    return winner


# name': 'Instagram',
#         'follower_count': 346,
#         'description': 'Social media platform',
#         'country': 'United States'
print(logo)

score = 0
end_game = False

while not end_game:
    player_1 = random.choice(data)
    player_2 = random.choice(data)

    print(
        f"Player_A is {player_1['name']} and is a {player_1['description']} from {player_1['country']}"
    )
    print('\n')
    print(vs)
    print('\n')
    print(
        f"Player_B is {player_2['name']} and is a {player_2['description']} from {player_2['country']}"
    )

    pick = input('Pick a player A or B').lower()

    Winner = check_ans(player_1, player_2)
    clear()
    print(logo)
    if pick == Winner:
        score += 1
        print(f'you are right! ,Your Score s {score}')
    else:
        end_game = True
        print('You are wrong')

print(f'final score {score}')
