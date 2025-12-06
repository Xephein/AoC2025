from time import time

from util import util as ut

def part_1(number_range):
    x1, x2 = number_range
    x1_half = x1[:len(x1)//2] if len(x1) > 1 else x1 
    x1_half = int(x1_half)
    x2_half = x2[:len(x2)//2] if len(x2) % 2 == 0 else x2[:len(x2)//2+1]
    x2_half = int(x2_half) + 1
    to_check = [str(x) for x in range(x1_half, x2_half)]
    doubled = map(lambda x: int(x+x), to_check)
    x1 = int(x1)
    x2 = int(x2)
    doubled = list(filter(lambda x: (x1 <= x) * (x <= x2) == 1, doubled))
    return sum(doubled)

def part_2(number_range):
    found = []
    x1, x2 = number_range
    x1_int, x2_int = tuple(map(int, number_range))
    x1_size = len(x1)
    x2_size = len(x2)
    unequal_length = x2_size > x1_size
    if not unequal_length:
        for length in range(0, x1_size // 2):
            for num in range(int(x1[:length+1]), int(x2[:length+1])+1):
                times_to_repeat = x1_size // len(str(num))
                if times_to_repeat == 1:
                    continue
                to_test = int(str(num) * times_to_repeat)
                if not (x1_int <= to_test \
                and to_test <= x2_int \
                and to_test not in found):
                    continue
                found.append(to_test)
        return sum(found)
    for num in range(1,10):
        for repeat in range(x1_size, x2_size+1):
            if repeat == 1:
                continue
            to_test = int(str(num)*repeat)
            if not (x1_int <= to_test \
            and to_test <= x2_int \
            and to_test not in found):
                continue
            found.append(to_test)
    for length in range(0, x2_size // 2):
        for num in range(int(x1[:length+1]), int(x2[:length+2])+1):
            repeat = x2_size // len(str(num))
            if repeat == 1:
                continue
            to_test = int(str(num)*repeat)
            if not(x1_int <= to_test \
            and to_test <= x2_int \
            and to_test not in found):
                continue
            found.append(to_test)
    return sum(found)

def parser(content):
    content = content.split(",")
    content = list(map(
        lambda x: (x.split("-")[0], x.split("-")[1]), content))
    return content

t0 = time() 

content = ut.get_input("day2.txt")
content = parser(content)
answer = 0

for number_range in content:
    answer += part_1(number_range)

t1 = time()

ut.log_result("part 1", answer, t1-t0)

t0 = time()

content = ut.get_input("day2.txt")
content = parser(content)
answer = 0

for number_range in content:
    answer += part_2(number_range)

t1 = time()

ut.log_result("part 2", answer, t1-t0)
