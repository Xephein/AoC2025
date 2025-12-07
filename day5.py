from time import time

import util.util as ut


def part_1():

    return

def part_2():

    return 


filename = "day5.txt"

t0 = time()

answer = 0
contents = ut.parse_input(filename)

is_ingredient = False
ing_ranges = []
ingredients = []
for line in contents:
    if line == "":
        is_ingredient = True
        continue
    if is_ingredient:
        ingredients.append(int(line))
    else:
        ing_ranges.append(tuple(map(int, line.split("-"))))

for ing in ingredients:
    for lo, hi in ing_ranges:
        if lo <= ing and ing <= hi:
            answer += 1
            break


t1 = time()

ut.log_result("part 1", answer, t1-t0)

t0 = time()

contents = ut.parse_input(filename)
answer = 0

for line in contents:

    continue

t1 = time()

ut.log_result("part 2", answer, t1-t0)
