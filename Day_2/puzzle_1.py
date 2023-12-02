import copy
rules = {
    "red": 12,
    "green": 13,
    "blue": 14
}
filename = "puzzle_input.txt"
result = 0
with open(filename) as file:
    games = file.readlines()
    for i in range(len(games)):
        possible = True
        turns = games[i].split(':')[-1].split(';')

        for turn in turns:
            rule = copy.deepcopy(rules)
            moves = turn.split(',')
            for move in moves:
                rule[move.split()[1].strip()] -= int(move.split()[0])
            if not (rule['red'] >= 0 and rule['green'] >= 0 and rule['blue'] >= 0):
                possible = False
        if possible:
            result += i+1

print(result)
