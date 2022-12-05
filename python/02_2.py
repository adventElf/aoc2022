def translate_move(move):
    if move in ["a", "x"]:
        return "rock"
    elif move in ["b", "y"]:
        return "paper"
    elif move in ["c", "z"]:
        return "scissors"


def translate_strategy(strategy):
    if strategy == "x":
        return "loss"
    elif strategy == "y":
        return "draw"
    elif strategy == "z":
        return "win"


def process_inputs(input_file_path):
    raw_input = open(input_file_path).read()
    text_list = raw_input.split("\n")
    tuple_list = []
    for text in text_list:
        tuple_list.append(text.split(" "))
    move_tuples = []
    for tuple in tuple_list:
        move_tuples.append(
            [translate_move(tuple[0].lower()), translate_strategy(tuple[1].lower())]
        )
    print(len(tuple_list))
    return move_tuples


input = process_inputs("../inputs/02_1.txt")


# a or x = rock
# b or y = paper
# c or z = scissors

moves = {"rock": 1, "paper": 2, "scissors": 3}

results = {"loss": 0, "draw": 3, "win": 6}

rules = {
    "rock": {"draw": "rock", "loss": "scissors", "win": "paper"},
    "paper": {"draw": "paper", "loss": "rock", "win": "scissors"},
    "scissors": {"draw": "scissors", "loss": "paper", "win": "rock"},
}


def score_round(opponent, strategy):
    score = 0
    score += results[strategy]
    score += moves[rules[opponent][strategy]]
    return score


tournament = []

for round in input:
    tournament.append(score_round(round[0], round[1]))

print(sum(tournament))
