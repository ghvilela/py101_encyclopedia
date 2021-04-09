import random
from cfonts import render

class Questions():
    pass

class Answers():
    pass    

## Questions and Answers dictionary

easy_mode = {"test1"}
hard_mode = {"test2"}

## title screen

title = "ENCYCLOPEDIA"
title_message = """
Welcome to ENCYCLOPEDIA, an interactive Q&A game to play with friends!
Here are some rules to play:
1. Each round consists in the following parts:
a) I pose players a question;
b) Each player then provide an answer in secret;
c) You get a poll containing all your answers and the correct answer (I may throw some randos in there);
d) Each player will select an answer from the poll;
2. After this, I'll show you the right answer and you'll get some points, as follows:
a) 10 points if your personal answer matches the right one;
b) 5 points if you choose right in the pool;
c) 2 points for each time another player chooses your answer from the pool;
The winner is the player with most points in the end!
Feeling Lucky?!
"""

print(render(title))
print(title_message)

##2 input the number of players and player names
def number_of_players():
    players = input("Please insert the number of players [2-8]")
    while True:
        if players in ["2", "3", "4", "5", "6", "7", "8"]:
            break
        players = input("Please insert the number of players [2-8]")
    return players

num_players = int(number_of_players())       


def define_names():
    user_names = []
    for i in range(int(num_players)):
        user_names.append(input("choose a name, Player {i}: ".format(i=i+1)))
    return user_names    

define_names()

##3 set difficulty level
def set_difficulty():
    difficulty = {}
    difficulty_input = input("""
        Choose questions dificulty:
        [R] Regular
        [B] Brainiac 
        """)
    while True:
        if difficulty_input.upper() in ("R", "B"):
            break
        else:
            print("not a valid choice...")
            difficulty_input = input("""
        Choose questions dificulty:
        [R] Regular
        [B] Brainiac 
        """)
    if difficulty_input.upper() == "R":
        difficulty = easy_mode
    else:
        difficulty = hard_mode
    return difficulty

question_list = set_difficulty()
# print(question_list)


##4 display question and players inputs

##5 display pool and players inputs

##6 display correct answer and round scores

##7 display round count

## return to 4

## display final screen with scores and winner! 

