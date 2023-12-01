filename = "test1.txt"
values = []
with open(filename) as file:
    for line in file.readlines():
        first = ''
        last = ''
        for character in line:
            if character >= '0' and character <= '9':
                if first:
                    last = character
                else:
                    first = character
                    last = character

        digit = first + last
        digit = int(digit)
        values.append(digit)
    print(sum(values))

