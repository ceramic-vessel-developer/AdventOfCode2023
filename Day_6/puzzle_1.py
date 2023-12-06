import time
filename = "input.txt"
result = 1
t0 = time.time_ns()
with open(filename) as file:
    data = file.readlines()
    times = data[0].split(":")[1].split()
    times = [int(times[i]) for i in range(len(times))]
    distance = data[1].split(":")[1].split()
    distance = [int(distance[i]) for i in range(len(distance))]

    for i in range(len(times)):
        wins = 0
        for j in range(times[i]):
            dist = j * 1 * (times[i]-j)
            if dist > distance[i]:
                wins += 1
        result *= wins
t1 = time.time_ns()
print(result)
