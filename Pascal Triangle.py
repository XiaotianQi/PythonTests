# _*_coding:utf-8_*_


def triangles3():
    L = [1]
    while True:
        yield L
        L = [sum(i) for i in zip([0] + L, L + [0])]  # 利用错位相加


def triangles():
    L = [1]
    while True:
        yield L
        L.append(0)  # 利用错位相加
        print(len(L))
        L = [L[i - 1] + L[i] for i in range(len(L))]
        print(L)


def triangles1():
    ret = [1]
    while True:
        yield ret
        for i in range(1, len(ret)):
            ret[i] = pre[i] + pre[i - 1]
        ret.append(1)
        pre = ret[:]
n = 0
for i in triangles3():
    print(i)
    n = n + 1
    if n == 10:
        break
