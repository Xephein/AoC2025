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
