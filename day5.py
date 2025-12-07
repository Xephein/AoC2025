from time import time

import util.util as ut


def part_1():

    return

def part_2(ing_ranges):
    i = 0
    while i < len(ing_ranges):
        if i + 1 == len(ing_ranges):
            break
        lo, hi = ing_ranges[i]
        next_lo, next_hi = ing_ranges[i+1]
        if next_lo > hi:
            i += 1
            continue
        if hi <= next_hi:
            ing_ranges[i][1] = next_hi
            ing_ranges.pop(i+1)
            i -= 1
        elif hi > next_hi:
            ing_ranges.pop(i+1)
            i -= 1
        i += 1
    return ing_ranges


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

ing_ranges = []
for line in contents:
    if line == "":
        break
    ing_ranges.append(list(map(int, line.split("-"))))
ing_ranges.sort(key=lambda x: x[0])
ing_ranges = part_2(ing_ranges)
for lo, hi in ing_ranges:
    answer += hi + 1 - lo

t1 = time()

ut.log_result("part 2", answer, t1-t0)
