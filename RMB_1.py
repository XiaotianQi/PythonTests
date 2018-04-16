# _*_coding:utf-8_*_
No2CN = {0: u'零', 1: u'壹', 2: u'贰', 3: u'叁', 4: u'肆', 5: u'伍',\
            6: u'陆', 7: u'柒', 8: u'捌', 9: u'玖'}
units = [u'亿', u'仟', u'佰', u'拾', u'万', u'仟', u'佰', u'拾', u'圆']
replace_zero = [
    (u'零仟', u'零佰', u'零拾', u'零零零', u'零零', u'零万', u'零圆'),
    (u'零', u'零', u'零', u'零', u'零', u'万', u'圆')
    ]

a = -10670207
b = abs(a)
new = []
for i in str(b):
    if int(i) in No2CN.keys():
        new.append(No2CN[int(i)])
units_new = units[-len(new):]
result = ''
for i, j in zip(new, units_new):
    result += i+j
for i, j in zip(replace_zero[0], replace_zero[1]):
    result = result.replace(i, j)
if a < 0:
    print(u'负'+result)
else:
    print(result)
