from datetime import datetime as dt

import util.util as ut

def part_1(position, rotation):
    direction = 1 if rotation[0] == "R" else -1
    amount = int(rotation[1:])
    return position + direction * amount

def part_2(position, rotation):
    tracker = 0
    direction = 1 if rotation[0] == "R" else -1
    amount = int(rotation[1:])
    end = position + direction * amount
    quotient = end // 100
    end -= quotient * 100
    tracker += abs(quotient)
    if position == 0 and direction == -1:
        tracker -= 1
    if end == 0 and direction == -1:
        tracker += 1
    return {"tracker": tracker, "position": end}


t0 = dt.now()
answer = 0
contents = ut.parse_input("day1.txt")
position = 50
for line in contents:
    position = part_1(position, line)
    if position % 100 == 0:
        answer += 1
t1 = dt.now()

print(f"part: {answer}\n time: {t1-t0}")

t0 = dt.now()
contents = ut.parse_input("day1.txt")
answer = 0
position = 50
for line in contents:
    run = part_2(position, line)
    position = run["position"]
    answer += run["tracker"]
t1 = dt.now()

print(f"part 2: {answer}\n time: {t1-t0}")
