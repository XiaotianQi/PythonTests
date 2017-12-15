# _*_coding:utf-8_*_
for i in range(1, 10):
    s = ''
    for j in range(1, i+1):
        a = '%d x %d = %d' % (j, i, i*j)
        s += a + '   '
    print(s)
