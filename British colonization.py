import time as t
import json
import os

red = "\033[91m"
green = "\033[92m"
yellow = "\033[33m"
blue = "\033[34m"
reset = "\033[0m"
white = "\033[37m"
bright_white = "\033[97m"
bold = "\033[1m"
high_scores_file = 'high_scores.json'

# Load high scores file if it even exists
if os.path.exists(high_scores_file):
    with open(high_scores_file, 'r') as f:
        high_scores = json.load(f)
else:
    high_scores = {}

def intro():
    player_name = input(f"{reset}{bold}Enter your name: ")
    print(f"{bold}Welcome, {player_name} to the British Colonization Learning Game!")
    print(f"{bold}You will learn about the British colonization of Canada and Egypt.")
    return player_name

def choose_country():
    print(f"{bold}\nWhich country would you like to learn about?")
    print(f"{bold}1. Canada")
    print(f"{bold}2. Egypt")
    choice = input(f"{reset}{bold}Enter the number of your choice: ")
    return choice

def canada_colonization():
    score = 0
    print(f"{bold}\nYou have chosen to learn about British colonization in Canada.")
    
    questions = [
        ("In which year did Britain officially gain control of Canada?", "1", ["1763", "1867"]),
        ("What was the significance of the Hudson's Bay Company?", "1", ["It was a British trading company that controlled large parts of Canada.", "It was the first Canadian political party."]),
        ("Which event led to the British military victory over the French in Canada?", "1", ["The Battle of Quebec in 1759", "The American Revolutionary War"]),
        ("What was the main purpose of the Royal Proclamation of 1763?", "1", ["To organize new lands and manage relationships with Indigenous peoples.", "To declare independence from Britain."]),
        ("What was the significance of the Confederation of Canada in 1867?", "2", ["It granted Canada complete independence from Britain.", "It united the provinces under a federal system while remaining part of the British Empire."])
    ]

    for i, (question, correct_answer, options) in enumerate(questions):
        print(f"{reset}{bold}\nQuestion {i + 1}: {question}")
        for idx, option in enumerate(options):
            print(f"{reset}{bold}{idx + 1}. {option}")
        answer = input(f"{reset}{bold}Enter the number of your answer: ")
        if answer == correct_answer:
            print(f"{bold}{green}Correct!{reset}")
            score += 1
        else:
            print(f"{bold}{red}Incorrect. The correct answer is {correct_answer}. {options[int(correct_answer) - 1]}{reset}")

    print(f"{reset}{bold}\nYour score in Canada is: {score}")
    return score

def egypt_colonization():
    score = 0
    print(f"{reset}{bold}\nYou have chosen to learn about British colonization in Egypt.")
    
    questions = [
        ("When did Britain occupy Egypt?", "1", ["1882", "1922"]),
        ("What was Britain's primary interest in Egypt?", "2", ["The Nile River for irrigation.", "The Suez Canal for trade routes."]),
        ("How did Egypt's strategic importance increase during World War I?", "1", ["It was a major supply base and control point for the Allies.", "It remained neutral and uninvolved in the war."]),
        ("What was the result of the 1919 Egyptian Revolution against British rule?", "2", ["Egypt gained full independence immediately.", "It led to Egypt gaining nominal independence in 1922 but British control remained in key areas."]),
        ("What was the impact of the 1952 Egyptian Revolution on British presence in Egypt?", "1", ["It marked the end of British influence and led to the establishment of the Republic of Egypt.", "It resulted in closer cooperation between Britain and Egypt."])
    ]

    for i, (question, correct_answer, options) in enumerate(questions):
        print(f"{reset}{bold}\nQuestion {i + 1}: {question}")
        for idx, option in enumerate(options):
            print(f"{reset}{bold}{idx + 1}. {option}")
        answer = input(f"{reset}{bold}Enter the number of your answer: ")
        if answer == correct_answer:
            print(f"{bold}{green}Correct!{reset}")
            score += 1
        else:
            print(f"{bold}{red}Incorrect. The correct answer is {correct_answer}. {options[int(correct_answer) - 1]}{reset}")

    print(f"{reset}{bold}\nYour score in Egypt is: {score}")
    return score

def update_high_scores(player_name, score):
    if player_name not in high_scores or score > high_scores[player_name]:
        high_scores[player_name] = score
        print(f"{bold}{green}New high score for {player_name}: {score}{reset}")

    with open(high_scores_file, 'w') as f:
        json.dump(high_scores, f)

def show_high_scores():
    if high_scores:
        print(f"{bold}Current High Scores:")
        for name, score in high_scores.items():
            print(f"{reset}{bold}{name}: {score}")
    else:
        print(f"{bold}No high scores yet!")

def play_game():
    player_name = intro()
    total_score = 0

    choice = choose_country()

    # plays the second country automatically
    if choice == '1':
        total_score += canada_colonization()
        print(f"{reset}{bold}\nNow switching to Egypt.")
        total_score += egypt_colonization()
    elif choice == '2':
        total_score += egypt_colonization()
        print(f"{reset}{bold}\nNow switching to Canada.")
        total_score += canada_colonization()
    else:
        print(f"{bold}{red}Invalid choice, please restart the game.{reset}")
        return

    print(f"{reset}{bold}\nCongratulations {player_name}! Your total score is: {total_score}")
    
    update_high_scores(player_name, total_score)
    show_high_scores()

play_game()

print(f"{blue}{bold}Credits")
t.sleep(1)
print(f"{yellow}{bold}Mohamed")
t.sleep(1)
print(f"{yellow}{bold}Hatem")
t.sleep(1)
print(f"{yellow}{bold}OpenAI Company")
t.sleep(1)
print(f"{yellow}{bold}Thanks for playing")
print(f"{reset}ㅤ")
