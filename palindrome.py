# _*_coding:utf-8_*_


def palindrome(n):
    return str(n) == str(n)[::-1]
print(list(filter(palindrome, range(1000))))
