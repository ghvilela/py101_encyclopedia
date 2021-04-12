import random
from cfonts import render
import getpass

def create_num_list(n1,n2):
    num_list = []
    for i in range(n1,n2+1):
        num_list.append(str(i))
    return num_list

## Questions and Answers dictionary

easy_mode = {}
hard_mode = {}
random_quotes = []

## title screen

title = "QUOTE!"
title_message = """
Welcome to QUOTE!, an interactive game to play with friends!
Here are some rules to play:
In each round, I will assign you a famous person, then:
    a) Each player will cite a QUOTE from this person or create a fake one;
    b) The you'll get a poll containing all your answers and a real quote from this person (I may throw some randos in there);
    c) Each player will try to guess the right one from the poll;
I'll show you the right answer and assign some points, as follows:
    - 10 points if your personal answer matches the right one;
    - 5 points if you choose right in the pool;
    - 5 points for each time another player chooses your answer from the pool;
The winner is the player with most points in the end!
Feeling Lucky?!
"""

print(render(title))
print(title_message)

##2 input the number of players and player names
def number_of_players():
    players = input("Please insert the number of players [2-8]")
    while True:
        if players in create_num_list(2,8):
            break
        elif players == "":
            players = "2"
            break
        players = input("Please insert the number of players [2-8]")
    return players

num_players = int(number_of_players())       


def define_names():
    user_names = []
    i = 1
    while len(user_names) < num_players:
        player = input("choose a name, Player {i}: ".format(i=i))
        if not player == "":
            user_names.append(player)
            i += 1
        else:
            player = "Player {n}".format(n=i)
            user_names.append(player)
            i += 1
    return user_names    

players_list = define_names()
player_scores = {key:0 for key in players_list}

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
        elif difficulty_input == "":
            difficulty_input = "R"
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
questions = list(question_list.keys())
answers = list(question_list.values())

##3.1 select game length

def game_length():
    num_rounds = input("How many rounds do you want to play? [2-10]")
    while True:
        if num_rounds in create_num_list(2,10):
            break
        elif num_rounds == "":
            num_rounds = "5"
            break
        num_rounds = input("How many rounds do you want to play? [2-10]")
    return num_rounds

rounds = int(game_length())

##4 display question and players inputs
start_message = "TIME TO PLAY!"
print(render(start_message))

## Game Round Iteration
for round in range(1,rounds+1):
    ##4.1 Question asking
    round_question = questions.pop(random.randint(0,len(questions)-1))
    correct_answer = question_list[round_question][0]
    round_message = """
    Round {n}:
    It's like {q} said:""".format(n=round, q=round_question)
    print(round_message)
    
    ##4.2 display player input options and build pool
    answer_pool = []
    answer_pool.append(correct_answer.upper())
    players_answers = {}
    for player in players_list:
        player_answer = getpass.getpass("Quote ahead, {p}: ".format(p=player))
        while player_answer == "":
            player_answer = getpass.getpass("Quote ahead, {p}: ".format(p=player))
        players_answers[player]= player_answer.upper()
        if not player_answer.upper() in answer_pool:
            answer_pool.append(player_answer.upper())
        else:
            player_scores[player] += 10
    while len(answer_pool) < 5:
        random_answer = random_quotes[random.randint(0,len(random_quotes))]
        if not random_answer in answer_pool:
            answer_pool.append(random_answer.upper())
    print("Now choose a quote from the pool:")
    pool_display = {}
    option = 0
    for answer in random.sample(answer_pool, len(answer_pool)):
        option += 1
        pool_display[str(option)] = answer
        print("{opt}) {answer}".format(opt=option, answer=answer))
    ## Choose answer and score points
    correct_choice = ""
    for opt, answer in pool_display.items():
        if answer == correct_answer:
            correct_choice = opt
    for player in players_list:
        player_choice = input("{player}: ".format(player=player))
        while not player_choice in pool_display.keys():
            player_choice = input("{player}: ".format(player=player))
        if player_choice == correct_choice:
            player_scores[player] += 5
        for player, answer in players_answers.items():
            if pool_display[player_choice] == answer:
                player_scores[player] += 5
    
    ## Print current scoreboard
    for key in player_scores:
        scoreboard = "{player}, your current score is: {points} points!".format(player=key, points=player_scores[key])
        print(scoreboard)


## Winner

winner = ""
max_score = 0
for player, score in player_scores.items():
    if score > max_score:
        max_score = score
        winner = player
    elif score == max_score:
        winner = winner + " and " + player

## Final Board
print("and the winner is.........")
print(render(winner))
print(render("Score: " + str(max_score)))
print("Final Score:")
for key in player_scores:
    scoreboard = "{player}, your final score is:{points} points!".format(player=key, points=player_scores[key])
    print(scoreboard)