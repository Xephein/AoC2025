from time import time

import util.util as ut

def part_1(bank):
    largest = float("-inf")
    for i in range(len(bank)-1):
        battery = int(bank[i])
        if battery == largest:
            position_tens.append(i)
        elif battery > largest:
            position_tens = []
            largest = battery
            position_tens.append(i)
    tens = bank[position_tens[0]]
    if len(position_tens) >= 2 and largest == 9:
        return int(2*tens)
    
    largest = float("-inf")
    for battery in bank[position_tens[0] + 1:]:
        battery = int(battery)
        if battery > largest:
            largest = battery
    return int(tens+str(largest))

def part_2(bank):
    joltage = ""
    length = len(joltage)
    joltage += find_largest(bank, length, joltage)
    return int(joltage)

def find_largest(bank_section, length, joltage):
    if len(joltage) == 12:
        return ""
    if len(bank_section) == 12 - len(joltage):
        return bank_section
    length = -(11 - len(joltage)) if len(joltage) < 11 else None
    largest = float("-inf")
    position = 0
    for i in range(len(bank_section[:length])):
        battery = int(bank_section[i])
        if battery > largest:
            largest = battery
            position = i
    largest = str(largest)
    joltage += largest
    length = len(joltage)
    largest += find_largest(bank_section[position + 1:], length, joltage)
    return largest


t0 = time()

content = ut.parse_input("day3.txt")
answer = 0

for line in content:
    answer += part_1(line)

t1 = time()

ut.log_result("part 1", answer, t1-t0)

t0 = time()

content = ut.parse_input("day3.txt")
answer = 0

for line in content:
    answer += int(part_2(line))

t1 = time()

ut.log_result("part 2", answer, t1-t0)
