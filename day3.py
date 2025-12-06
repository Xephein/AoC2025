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

t0 = time()

content = ut.parse_input("day3.txt")
answer = 0

for line in content:
    answer += part_1(line)

t1 = time()

ut.log_result("part 1", answer, t1-t0)
