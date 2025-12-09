from time import time
from functools import reduce

import util.util as ut


def part_1():

    return

def part_2():

    return 


filename = "day6.txt"

t0 = time()

answer = 0
contents = ut.parse_input(filename)

exercises = []

for line in contents:
    exercises.append(
        tuple(filter(lambda x: x!= "", line.split(" ")))
    )
for col in range(len(exercises[0])):
    if exercises[-1][col] == "+":
        answer += sum(map(
            lambda x: int(x[col]), exercises[:-1]
        ))
    else:
        answer += reduce(lambda x, y: x*y, map(
            lambda x: int(x[col]), exercises[:-1]
        ))

t1 = time()

ut.log_result("part 1", answer, t1-t0)

t0 = time()

contents = ut.parse_input(filename)
answer = 0

for line in contents:

    continue

t1 = time()

ut.log_result("part 2", answer, t1-t0)
