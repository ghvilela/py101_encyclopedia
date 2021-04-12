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

random_quotes = [
"""Today is the tomorrow we worried about yesterday"""
,
"""It's easier to see the mistakes on someone else's paper"""
,
"""Every man dies. Not every man really lives"""
,
"""The day is already blessed, find peace within it"""
,
"""From small beginnings come great things"""
,
"""Learning is a treasure that will follow its owner everywhere"""
,
"""Talk doesn't cook rice"""
,
"""When deeds speak, words are nothing"""
,
"""Some pursue happiness, others create it"""
,
"""It takes both sunshine and rain to make a rainbow"""
,
"""A beautiful thing is never perfect"""
,
"""If you are patient in one moment of anger, you will escape one hundred days of sorrow"""
,
"""A good rest is half the work"""
,
"""Every new day is another chance to change your life"""
]


easy_list_raw = [{
"quoteText": """Genius is one percent inspiration and ninety-nine percent perspiration.""",
"quoteAuthor": "Thomas Edison"
}, {
"quoteText": """A house divided against itself cannot stand.""",
"quoteAuthor": "Abraham Lincoln"
}, {
"quoteText": """Difficulties increase the nearer we get to the goal.""",
"quoteAuthor": "Johann Wolfgang von Goethe"
}, {
"quoteText": """Peace comes from within. Do not seek it without.""",
"quoteAuthor": "Buddha"
}, {
"quoteText": """To lead people walk behind them.""",
"quoteAuthor": "Lao Tzu"
}, {
"quoteText": """Having nothing, nothing can he lose.""",
"quoteAuthor": "William Shakespeare"
}, {
"quoteText": """Everything in life is luck.""",
"quoteAuthor": "Donald Trump"
}, {
"quoteText": """Study the past, if you would divine the future.""",
"quoteAuthor": "Confucius"
}, {
"quoteText": """God always takes the simplest way.""",
"quoteAuthor": "Albert Einstein"
}, {
"quoteText": """Be as you wish to seem.""",
"quoteAuthor": "Socrates"
}, {
"quoteText": """Who sows virtue reaps honour.""",
"quoteAuthor": "Leonardo da Vinci"
}, {
"quoteText": """Be kind whenever possible. It is always possible.""",
"quoteAuthor": "Dalai Lama"
}, {
"quoteText": """Do, or do not. There is no try.""",
"quoteAuthor": "Yoda"
}, {
"quoteText": """Courage is going from failure to failure without losing enthusiasm.""",
"quoteAuthor": "Winston Churchill"
}, {
"quoteText": """Luck is what happens when preparation meets opportunity.""",
"quoteAuthor": "Seneca"
}, {
"quoteText": """Victory belongs to the most persevering.""",
"quoteAuthor": "Napoleon Bonaparte"
}]

hard_list_raw = [{
"quoteText": """Time is the wisest counsellor of all.""",
"quoteAuthor": "Pericles"
}, {
"quoteText": """The two most powerful warriors are patience and time.""",
"quoteAuthor": "Leo Tolstoy"
}, {
"quoteText": """No man was ever wise by chance.""",
"quoteAuthor": "Seneca"
}, {
"quoteText": """Reason and free inquiry are the only effectual agents against error.""",
"quoteAuthor": "Thomas Jefferson"
}, {
"quoteText": """If you want a thing done well, do it yourself.""",
"quoteAuthor": "Napoleon Bonaparte"
}, {
"quoteText": """Wrinkles should merely indicate where smiles have been.""",
"quoteAuthor": "Mark Twain"
}, {
"quoteText": """Mediocrity knows nothing higher than itself, but talent instantly recognizes genius.""",
"quoteAuthor": "Arthur Conan Doyle"
}, {
"quoteText": """Don't leave a stone unturned. It's always something, to know you have done the most you could.""",
"quoteAuthor": "Charles Dickens"
}, {
"quoteText": """A short saying often contains much wisdom.""",
"quoteAuthor": "Sophocles"
}, {
"quoteText": """I don't believe in failure. It is not failure if you enjoyed the process.""",
"quoteAuthor": "Oprah Winfrey"
}, {
"quoteText": """Living at risk is jumping off the cliff and building your wings on the way down.""",
"quoteAuthor": "Ray Bradbury"
}, {
"quoteText": """It all depends on how we look at things, and not how they are in themselves.""",
"quoteAuthor": "Carl Jung"
}, {
"quoteText": """The greatest minds are capable of the greatest vices as well as of the greatest virtues.""",
"quoteAuthor": "Rene Descartes"
}, {
"quoteText": """And as we let our own light shine, we unconsciously give other people permission to do the same""",
"quoteAuthor": "Nelson Mandela"
}]



for item in easy_list_raw:
    for text in item.values():
        if not text in (easy_mode.values() or easy_mode.keys()):
            easy_mode[item["quoteAuthor"]] = item["quoteText"]

for item in hard_list_raw:
    for text in item.values():
        if not text in (hard_mode.values() or hard_mode.keys()):
            hard_mode[item["quoteAuthor"]] = item["quoteText"]

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
    correct_answer = question_list[str(round_question)]
    round_message = """
    Question {n}:
    Come up a nice "{q}" quote: """.format(n=round, q=round_question.upper())
    print(round_message)
    
    ##4.2 display player input options and build pool
    answer_pool = []
    answer_pool.append(correct_answer.upper())
    players_answers = {}
    for player in players_list:
        player_answer = getpass.getpass("Enter your answer, {p}: ".format(p=player))
        while player_answer == "":
            player_answer = getpass.getpass("Enter your answer, {p}: ".format(p=player))
        players_answers[player]= player_answer.upper()
        if not player_answer.upper() in answer_pool:
            answer_pool.append(player_answer.upper())
        else:
            player_scores[player] += 10
    while len(answer_pool) < 5:
        random_answer = random_quotes[random.randint(1,len(random_quotes)-1)]
        if not random_answer.upper() in answer_pool:
            answer_pool.append(random_answer.upper())
    print("Each of these from the pool did he acctualy say?")
    pool_display = {}
    option = 0
    for answer in random.sample(answer_pool, len(answer_pool)):
        option += 1
        pool_display[str(option)] = answer
        print("{opt}) {answer}".format(opt=option, answer=answer))
    ## Choose answer and score points
    correct_choice = ""
    for opt, answer in pool_display.items():
        if answer == correct_answer.upper():
            correct_choice = opt
    for player in players_list:
        player_choice = input("{player}: ".format(player=player))
        while not player_choice in pool_display.keys():
            player_choice = input("{player}: ".format(player=player))
        if player_choice == correct_choice:
            player_scores[player] += 5
        for player, answer in players_answers.items():
            if pool_display[player_choice] == answer:
                player_scores[player] += 2
    
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
