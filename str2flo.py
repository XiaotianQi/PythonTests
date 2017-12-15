# _*_coding:utf-8_*_
from functools import reduce
strings = ['123.456']


def str2flo(s):
    def char2num(i):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[i]
    a = reduce(lambda x, y: x*10 + y, map(char2num, s.split('.')[0]))
    b = reduce(lambda x, y: x*10 + y, map(char2num, s.split('.')[1])) / 10**len(s.split('.')[1])
    return a + b
print('str2float(\'123.456\') =', str2flo('123.456'))
