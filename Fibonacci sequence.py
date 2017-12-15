# _*_coding:utf-8_*_


def fib(n):
    i, a, b = 0, 0, 1
    while i < n:  # 根据循环判断条件，i须提前声明
        yield(b)
        a, b = b, a + b
        i = i + 1
    return 'Done'
for i in fib(6):
    print(i)
