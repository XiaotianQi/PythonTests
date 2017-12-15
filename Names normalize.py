# _*_coding:utf-8_*_
# 人名首字符大写


def normalize1(name):
    return name[0].upper() + name[1:].lower()


def normalize(name):
    # print(name, type(name))
    for i in [name]:
        # print(i)
        return i[0].upper() + i[1:].lower()
names = [
    'Lily', 'lisa', 'adAm', 'BOB'
]
print(list(map(normalize, names)))
# print(list(map(normalize, 'lisa')))
