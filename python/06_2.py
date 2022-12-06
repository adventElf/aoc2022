def process_input(input="../inputs/06_1.txt"):
    stream = open(input, "r").read()
    span = 14
    start = 0
    end = span
    searching = True
    while searching:
        window = set(stream[start:end])
        if len(window) < span:
            start += 1
            end += 1
        elif len(window) == span:
            print(window)
            return end


process_input()
