filename = "puzzle_input.txt"
result = 0

def find_ratios(main_index,i, matrix):
    # TOP ROW
    top = []
    if main_index > 0:
        if i > 0 and '0' <= matrix[main_index-1][i-1] <= '9':
            top.append((main_index-1,i-1))
        if '0' <= matrix[main_index-1][i] <= '9':
            if top:
                top.append(top[0])
            else:
                top.append((main_index-1,i))
        if i < len(matrix[0])-1 and '0' <= matrix[main_index-1][i+1] <= '9':
            if top and (len(top) == 2 or top[0] == (main_index-1,i)):
                top.append(top[0])
            else:
                top.append((main_index-1,i+1))
    top = list(dict.fromkeys(top))
    # MIDDLE ROW
    middle = []
    if i > 0 and '0' <= matrix[main_index][i-1] <= '9':
        middle.append((main_index,i-1))
    if i < len(matrix[0])-1 and '0' <= matrix[main_index][i+1] <= '9':
        middle.append((main_index,i+1))

    # BOTTOM ROW
    bottom = []
    if main_index < len(matrix)-1:
        if i > 0 and '0' <= matrix[main_index + 1][i - 1] <= '9':
            bottom.append((main_index+1,i-1))
        if '0' <= matrix[main_index + 1][i] <= '9':
            if bottom:
                bottom.append(bottom[0])
            else:
                bottom.append((main_index+1,i))
        if i < len(matrix[0])-1 and '0' <= matrix[main_index + 1][i + 1] <= '9':
            if bottom and (len(bottom) == 2 or bottom[0]==(main_index+1,i)):
                bottom.append(bottom[0])
            else:
                bottom.append((main_index+1,i+1))
    bottom = list(dict.fromkeys(bottom))

    result_list = []
    result_list.extend(top)
    result_list.extend(middle)
    result_list.extend(bottom)

    return result_list


def find_number(main_index,i, matrix):
    number = matrix[main_index][i]

    temp_i = i + 1
    while temp_i < len(matrix[0]) and '0' <= matrix[main_index][temp_i] <='9':
        number += matrix[main_index][temp_i]
        temp_i += 1
    temp_i = i - 1
    while temp_i >= 0 and '0' <= matrix[main_index][temp_i] <='9':
        number = matrix[main_index][temp_i] + number
        temp_i -= 1
    return int(number)



with open(filename) as file:
    schema = file.readlines()
    for i in range(len(schema)):
        schema[i] = schema[i].strip()
    for i in range(len(schema)):
        for j in range(len(schema[i])):
            if schema[i][j] == '*':
                ratios = find_ratios(i,j,schema)
                if len(ratios) == 2:
                    result += find_number(ratios[0][0],ratios[0][1],schema) * find_number(ratios[1][0],ratios[1][1],schema)
                else:
                    print(ratios)

print(result)

# 56368685