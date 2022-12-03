def translate(move):
    if move in ["a", "x"]:
        return "rock"
    elif move in ["b", "y"]:
        return "paper"
    elif move in ["c", "z"]:
        return "scissors"


def process_inputs(input_file_path):
    raw_input = open(input_file_path).read()
    text_list = raw_input.split("\n")
    tuple_list = []
    for text in text_list:
        tuple_list.append(text.split(" "))
    move_tuples = []
    for tuple in tuple_list:
        move_tuples.append([translate(tuple[0].lower()), translate(tuple[1].lower())])
    print(len(tuple_list))
    return move_tuples


input = process_inputs("../inputs/02_1.txt")

# a or x = rock
# b or y = paper
# c or z = scissors

moves = {"rock": 1, "paper": 2, "scissors": 3}

results = {"loss": 0, "draw": 3, "win": 6}

rules = {
    "rock": {"rock": "draw", "paper": "win", "scissors": "loss"},
    "paper": {"rock": "loss", "paper": "draw", "scissors": "win"},
    "scissors": {"rock": "win", "paper": "loss", "scissors": "draw"},
}


def score_round(opponent, you):
    opponent = opponent.lower()
    you = you.lower()
    score = 0
    result = rules[opponent][you]
    score += results[result]
    score += moves[you]
    return score


tournament = []

for round in input:
    tournament.append(score_round(round[0], round[1]))

print(sum(tournament))
