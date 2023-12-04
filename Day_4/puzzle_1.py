filename = "test.txt"
result = 0

with open(filename) as file:
    scratchcards = file.readlines()
    for scratchcard in scratchcards:
        numbers = scratchcard.split(':')[-1]
        winning_numbers = numbers.split('|')[0].split()
        my_numbers = numbers.split('|')[1].split()
        matches = 0

        for number in winning_numbers:
            if number in my_numbers:
                matches +=1
        if matches:
            result += 2**(matches-1)

print(result)
