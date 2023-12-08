filename = "input.txt"
result = 0
rules = {"T": 10, "J": 1, "Q": 12, "K": 13, "A": 14}


class Hand:
    def __init__(self, line: str):
        cards = line.split()[0]
        self.bid = int(line.split()[1])
        self.weights = self.calculate_weights(cards)

    @staticmethod
    def calculate_weights(cards: str):
        og = cards
        weights = []
        jokers = cards.count('J')
        cards = cards.replace('J', '')
        occurences = dict.fromkeys(cards)
        for card in occurences.keys():
            occurences[card] = cards.count(card)
        if occurences.values():
            main_weight = max(occurences.values())
        else:
            main_weight = 0
        main_weight += jokers
        if main_weight >= 4:
            main_weight += 2
        elif main_weight == 3:
            if (2 in occurences.values() and not jokers) or (list(occurences.values()).count(2) == 2 and jokers == 1):
                main_weight += 2
            else:
                main_weight += 1
        elif main_weight == 2 and list(occurences.values()).count(2) == 2:
            main_weight += 1

        weights.append(main_weight)

        for card in og:
            if '0' < card <= '9':
                weights.append(int(card))
            else:
                weights.append(rules[card])

        return weights

    def __lt__(self, other):
        for i in range(len(self.weights)-1):
            if self.weights[i] != other.weights[i]:
                return self.weights[i] < other.weights[i]

        return self.weights[-1] < other.weights[-1]


with open(filename) as file:
    games = []
    hands = file.readlines()
    for hand in hands:
        games.append(Hand(hand))
    games.sort()

    for i in range(len(games)):
        result += games[i].bid * (i+1)

print(result)
