import re, copy

filename = "test.txt"
regex = r"(.+:(\d|\s)+)"


class Map:
    def __init__(self, ranges: list):
        sranges = ranges.split("\n")
        sranges = [sranges[i].split() for i in range(len(sranges)) if sranges[i]]
        sranges = [[int(sranges[i][j]) for j in range(len(sranges[i]))] for i in range(len(sranges))]
        sranges = [[[sranges[i][0], sranges[i][0] + sranges[i][2]], [sranges[i][1], sranges[i][1] + sranges[i][2]]] for i in
                range(len(sranges))]
        self.ranges = sranges

    def translate(self, numbers):
        temp_numbers = copy.copy(numbers)

        for i in range(len(temp_numbers)):
            temp_slice = [temp[numbers[i]]]
            for r in self.ranges:
                counter = 0
                while(counter < len(temp_slice)):
                    if self.is_intersecting(r[1],):
                        dif = temp_numbers[i] - r[1][0]
                        temp_numbers[i] = r[0][0] + dif
                        break
 #       print(numbers)
        return temp_numbers
    def is_intersecting(self, range1:list,range2:range):
        pass


    def fix_list(self,list):
        pass



with open(filename) as file:
    almanac = file.read()
    maps = re.findall(regex,almanac)
    maps = [maps[i][0] for i in range(len(maps))]
    numbers = maps[0].split(':')[-1].split()
    numbers = [int(numbers[i]) for i in range(len(numbers))]
    numbers = [range(numbers[i],numbers[i]+numbers[i+1]+1) for i in range(0,len(numbers),1)]
    maps.pop(0)

    for mapp in maps:
        rule = mapp.split(":")[1]
        translator = Map(rule)
        numbers = translator.translate(numbers)


