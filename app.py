import handlers.config as cfg
import handlers.game_controls as gc


game_data = gc.load_game_data(cfg)

for i in range(len(game_data)):
    i += 1

    questions = gc.get_question(game_data, str(i))
    options = gc.get_option(game_data, str(i))
    answers = gc.get_answers(game_data, str(i))

    print(questions)
    print(options)

    user_ans = gc.get_user_input()

    gc.match_answer(ans_user=user_ans, ans_real=answers, c=cfg)

print("Your score is: ", cfg.score, "out of", len(game_data))
if cfg.score == len(game_data):
    print("Congratulations :)")



