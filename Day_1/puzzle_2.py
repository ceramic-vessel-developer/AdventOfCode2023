import re
filename = "test1.txt"
values = []
translation = {"zero":'0',"one":'1',"two":'2',"three":'3',"four":'4',"five":'5',"six":'6',"seven":'7',"eight":'8',"nine":'9'}
regex = r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))"
with open(filename) as file:
    for line in file.readlines():
        digit_list = re.findall(regex,line)
        first = digit_list[0]
        if len(first)>1:
            first = translation[first]
        last = digit_list[-1]
        if len(last)>1:
            last = translation[last]
        digit = first + last
        digit = int(digit)
        values.append(digit)
    print(sum(values))

