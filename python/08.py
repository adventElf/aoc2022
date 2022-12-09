input = open("../inputs/08.txt").read()

forest = [[int(tree) for tree in row] for row in input.splitlines()]

perimeter = len(forest[0]) * 2 + (len(forest) - 2) * 2
rows = len(forest)
cols = len(forest[0])
area = rows * cols
first_col = 0
last_col = len(forest[0]) - 1
first_row = forest.index(forest[0])
last_row = forest.index(forest[-1])
sweep_start = first_col + 1
sweep_end = last_col
print(first_col, last_col, first_row, last_row)
print(perimeter, area)


def get_column(col_num, forest=forest):
    column = []
    for r in forest:
        column.append(r[col_num])
    return column


def check_visability_east(r, c):
    height = forest[r][c]
    if c == 0:
        return True
    for tree in forest[r][:c]:
        if tree >= height:
            return False
        else:
            pass
    return True


def check_visability_west(r, c):
    visible = True
    height = forest[r][c]
    if c == sweep_end:
        return True
    for tree in forest[r][c + 1 :]:
        if tree >= height:
            visible = False
    return visible


def check_visibility_north(r, c):
    visible = True
    height = forest[r][c]
    if r == 0:
        return True
    for tree in get_column(c)[:r]:
        if tree >= height:
            visible = False
    return visible


def check_visibility_south(r, c):
    visible = True
    height = forest[r][c]
    if r == sweep_end:
        return True
    for tree in get_column(c)[r + 1 :]:
        if tree >= height:
            visible = False
    return visible


def check_overall_visibility(r, c, forest=forest, show_me=False):
    visible = False
    east = check_visability_east(r, c)
    west = check_visability_west(
        r,
        c,
    )
    north = check_visibility_north(r, c)
    south = check_visibility_south(r, c)
    if north or east or south or west:
        visible = True
    if show_me:
        print(
            f"Tree visibility for ({r}, {c}) with height {forest[r][c]}:\n\tNorth: {north}\n\tEast: {east}\n\tSouth: {south}\n\tWest: {west}"
        )
    return visible


def generate_visibility_map():
    visibility_map = []
    for r in range(0, rows):
        row_visibility = []
        for c in range(0, cols):
            row_visibility.append(check_overall_visibility(r, c))
        visibility_map.append(row_visibility)
    return visibility_map


visibility_map = generate_visibility_map()


def visualize(forest=forest, visibility_map=visibility_map):
    end = ""
    red = "\033[91m"
    green = "\033[92m"
    for row in range(0, rows):
        for col in range(0, cols):
            visible = visibility_map[row][col]
            value = str(forest[row][col])
            if visible:
                print(green + value, end=end)
            else:
                print(red + value, end=end)
        print("\n")


def count_by_visibility(visibility_map=visibility_map):
    visible = 0
    invisible = 0
    total = 0
    for row in visibility_map:
        for tree in row:
            if tree:
                visible += 1
                total += 1
            else:
                invisible += 1
                total += 1
    print(f"Of {total} trees, {visible} are visible and {invisible} are obscured.")


visualize()

count_by_visibility()


def score_north(r, c):
    blocked = False
    score = 0
    previous = r - 1
    if previous < 0:
        return 0
    while blocked == False and previous >= 0:
        if forest[previous][c] >= forest[r][c]:
            score += 1
            blocked = True
        else:
            score += 1
            previous -= 1
    return score


def score_south(r, c):
    blocked = False
    score = 0
    next = r + 1
    if next >= len(forest):
        return 0
    while blocked == False and next < len(forest):
        if forest[next][c] >= forest[r][c]:
            score += 1
            blocked = True
        else:
            score += 1
            next += 1
    return score


def score_east(r, c):
    blocked = False
    score = 0
    previous = c - 1
    if previous < 0:
        return 0
    while blocked == False and previous >= 0:
        if forest[r][previous] >= forest[r][c]:
            score += 1
            blocked = True
        else:
            score += 1
            previous -= 1
    return score


def score_west(r, c):
    blocked = False
    score = 0
    next = c + 1
    if c >= len(forest[r]) - 1:
        return 0
    while blocked == False and next < len(forest[r]):
        if forest[r][next] >= forest[r][c]:
            score += 1
            blocked = True
        else:
            score += 1
            next += 1
    return score


def generate_scenic_score(r, c):
    return score_north(r, c) * score_south(r, c) * score_east(r, c) * score_west(r, c)


def determine_max_score():
    all_scores = []
    for r in range(0, len(forest)):
        for c in range(0, len(forest[0])):
            all_scores.append(generate_scenic_score(r, c))
    all_scores = list(set(all_scores))
    max = sorted(all_scores)[-1]
    min = sorted(all_scores)[0]
    print(f"Max: {max} / Min: {min}")
    return max


determine_max_score()
