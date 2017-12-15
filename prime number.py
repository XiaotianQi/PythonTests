# _*_coding:utf-8_*_


def odd_number():  # 无限序列
    n = 1
    while True:
        n += 2
        yield n  # 不能使用n+2


def not_divisible(n):
    return lambda x: x % n > 0


def prime_numbers():  # 无限序列，所以调用时需要设置一个退出循环的条件
    yield 2
    it = odd_number()
    while True:
        n = next(it)
        yield n
        it = filter(not_divisible(n), it)

for n in prime_numbers():
    if n < 100:
        print(n)
    else:
        break
