def load_game_data(c):
    game_date = c.configurations
    return game_date


def get_question(game_data, key):
    return game_data[key]["que"]


def get_option(game_data, key):
    return game_data[key]["options"]


def get_answers(game_data, key):
    return game_data[key]["answer"]
           

def get_user_input():
    ans = input("Enter your answers: ").upper()
    return ans


def match_answer(ans_user, ans_real,c):
    if ans_user == ans_real:
        print("Correct")
        c.score += 1
    else:
        print("Incorrect")



