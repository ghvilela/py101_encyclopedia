import random
from cfonts import render

def create_num_list(n1,n2):
    num_list = []
    for i in range(n1,n2+1):
        num_list.append(str(i))
    return num_list

class Questions():
    pass

class Answers():
    pass    

## Questions and Answers dictionary

easy_mode = {"test1":"Bla1"}
hard_mode = {"test2":"Ble2"}

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
        if players in create_num_list(2,8):
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
        continue
    return user_names    

players_list = define_names()

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

##3.5 select game length

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

for round in range(1,rounds+1):
    unavailable_questions = []
    round_question = questions[random.randint(0,len(questions)-1)]
    while round_question in unavailable_questions:
        round_question = questions[random.randint(0,len(questions)-1)]
    unavailable_questions.append(round_question)
    round_message = """
    Question {n}:
    {q}""".format(n=round, q=round_question)
    print(round_message)
    answer_pool = []
    for player in players_list:
        player_answer = input("Enter your answer, {p}: ".format(p=player))
        while player_answer == "":
            player_answer = input("Enter your answer, {p}: ".format(p=player))
        answer_pool.append(player_answer.upper())
        


##5 display pool and players inputs

##6 display correct answer and round scores

##7 display round count

## return to 4

## display final screen with scores and winner! 

