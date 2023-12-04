filename = "puzzle_input.txt"

with open(filename) as file:
    scratchcards = file.readlines()
    result = [1 for _ in range(len(scratchcards))]
    for i in range(len(scratchcards)):
        for _ in range(result[i]):
            numbers = scratchcards[i].split(':')[-1]
            winning_numbers = numbers.split('|')[0].split()
            my_numbers = numbers.split('|')[1].split()
            matches = 0
            for number in winning_numbers:
                if number in my_numbers:
                    matches += 1
            if matches:
                for j in range(i+1,i+1+matches):
                    result[j] += 1

print(sum(result))
