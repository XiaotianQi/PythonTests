# _*_coding:utf-8_*_
import random
import math
n = 10000000
i = 0
count = 0.0


def in_circle(x, y):
    distance = math.sqrt((x-0.5)**2 + (y-0.5)**2)
    return distance <= 0.5
while i <= n:
    i += 1
    x = random.random()
    y = random.random()
    if in_circle(x, y):
        count += 1
print(count*4 / n)
