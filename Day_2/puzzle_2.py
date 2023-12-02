import copy
rules = {
    "red": 0,
    "green": 0,
    "blue": 0
}
filename = "puzzle_input.txt"
result = 0
with open(filename) as file:
    games = file.readlines()
    for i in range(len(games)):
        turns = games[i].split(':')[-1].split(';')
        rule = copy.deepcopy(rules)
        for turn in turns:

            moves = turn.split(',')
            for move in moves:
                if rule[move.split()[1].strip()] < int(move.split()[0]):
                    rule[move.split()[1].strip()] = int(move.split()[0])
        power = 1
        for i in rule.values():
            power *= i

        result += power

print(result)
