# Game between two players
"""
Author: Anirudhya
Date: 13-11-2021
Purpose: Just for Practise
"""
import random

print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")

try:
    print("Game Description: \n"
          "It is a Offline game based on Number choosing a Number will generate randomly but you can't see but you "
          "have to guess it who will guess it first will be the winner.")
    player_no = int(input("How many Player want to participate at once: \n"))
    player_list = []
    score_dict = {}
    for i in range(1, player_no + 1):
        player_list.append(input(f"Please Give Player{i}'s username: \n"))
except Exception as e:
    print(e)
else:
    for player in player_list:
        ran_no = random.randrange(1, 20)
        chance = 0
        print(f"Please Choose Number {player} -> ")
        while True:
            chance += 1
            try:
                response = int(input(f"{chance}. Please Choose your Number -> "))
            except Exception as e:
                print(e)
            else:
                if response == ran_no:
                    score_dict.update({chance: player})
                    break
                elif response < ran_no:
                    print("Choose Greater ....")
                elif response > ran_no:
                    print("Choose Smaller ...")
                else:
                    print("Something Went Wrong.")

    print(f"winner is {sorted(score_dict.values())[0]}")
    for key, value in sorted(score_dict.items()):
        print(f"{value} has done it in {key} no of chances")


finally:
    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
