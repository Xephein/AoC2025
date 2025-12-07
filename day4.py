from time import time

import util.util as ut


def part_1(row, column, layout):
    neighbours = 0
    for i in range(-1,2):
        if row + i < 0 or row + i > len(layout) - 1:
            continue
        for j in range(-1,2):
            if column + j < 0 or column + j > len(layout[row]) - 1:
                continue
            if i == 0 and j == 0:
                continue
            neighbours += 1 * (layout[row+i][column+j] == "@")
    return 1 if neighbours < 4 else 0

def part_2(row, column, layout):
    neighbours = 0
    for i in range(-1,2):
        if row + i < 0 or row + i > len(layout) - 1:
            continue
        for j in range(-1,2):
            if column + j < 0 or column + j > len(layout[row]) - 1:
                continue
            if i == 0 and j == 0:
                continue
            neighbours += 1 * (layout[row+i][column+j] == "@")
    return 0

def move_through_warehouse(layout):
    all_removed = 0
    new_layout = layout.copy()
    for row in range(len(layout)):
        for col in range(len(layout[row])):
            if layout[row][col] != "@":
                continue
            removed = part_1(row, col, layout)
            if removed != 1:
                continue
            new_layout[row] = new_layout[row][:col] + "." + new_layout[row][col + 1:]
            all_removed += 1
    if all_removed == 0:
        return all_removed
    all_removed += move_through_warehouse(new_layout)
    return all_removed

filename = "day4.txt"

t0 = time()

contents = ut.parse_input(filename)
answer = 0

for row in range(len(contents)):
    for col in range(len(contents[row])):
        if contents[row][col] != "@":
            continue
        answer += part_1(row, col, contents)

t1 = time()

ut.log_result("part 1", answer, t1-t0)

t0 = time()

contents = ut.parse_input(filename)

answer = move_through_warehouse(contents)

t1 = time()

ut.log_result("part 2", answer, t1-t0)
