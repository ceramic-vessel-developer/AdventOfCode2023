filename = "puzzle_input.txt"
result = 0


def check_if_part(main_index, indexes, matrix):
    is_part = False
    for i in indexes:
        if not (('0' <= matrix[main_index - 1][i] <= '9') or matrix[main_index - 1][i] == '.') and main_index > 0:
            is_part = True
        elif not (('0' <= matrix[main_index - 1][i - 1] <= '9') or matrix[main_index - 1][
            i - 1] == '.') and main_index > 0 and i > 0:
            is_part = True
        elif not (('0' <= matrix[main_index][i - 1] <= '9') or matrix[main_index][i - 1] == '.') and i > 0:
            is_part = True

        if i < len(matrix[0]) - 1:
            if not (('0' <= matrix[main_index - 1][i + 1] <= '9') or matrix[main_index - 1][i + 1] == '.') and main_index > 0:
                is_part = True
            elif not (('0' <= matrix[main_index][i + 1] <= '9') or matrix[main_index][i + 1] == '.'):
                is_part = True
        if main_index < len(matrix) - 1:
            if not (('0' <= matrix[main_index + 1][i] <= '9') or matrix[main_index + 1][i] == '.'):
                is_part = True
            elif not (('0' <= matrix[main_index + 1][i - 1] <= '9') or matrix[main_index + 1][i - 1] == '.') and i > 0:
                is_part = True
            if i < len(matrix[0]) - 1:
                if not (('0' <= matrix[main_index + 1][i + 1] <= '9') or matrix[main_index + 1][i + 1] == '.'):
                    is_part = True
    return is_part


with open(filename) as file:
    schema = file.readlines()
    part_number = ''
    indexes = []
    number = False
    for i in range(len(schema)):
        schema[i] = schema[i].strip()
        for j in range(len(schema[i])):
            if '0' <= schema[i][j] <= '9':
                number = True
                part_number += schema[i][j]
                indexes.append(j)
            else:
                if number:
                    if check_if_part(i, indexes, schema):
                        result += int(part_number)
                    part_number = ''
                    number = False
                    indexes = []
        if number:
            if check_if_part(i, indexes, schema):
                result += int(part_number)
            part_number = ''
            number = False
            indexes = []

print(result)
