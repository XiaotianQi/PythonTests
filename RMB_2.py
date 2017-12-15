M = [u'零', u'壹', u'贰', u'叁', u'肆', u'伍', u'陆', u'柒', u'捌', u'玖']
N = ['', u'圆', u'拾', u'佰', u'仟', u'万', u'拾', u'佰', u'仟', u'亿', u'零']
O = {
    u'零仟': u'零', u'零佰': u'零', u'零拾': u'零', u'零零零': u'零', u'零零': u'零',
    u'零万': u'万', u'零圆': u'圆', u'亿万': u'亿'
    }

a = -10670207
s = str(abs(a))
r = ('' if a >= 0 else '负')
for i in range(0, len(s)):
    r = r + M[int(s[i])] + N[len(s)-i]
for i in range(len(s)):
    for j in O:
        r = r.replace(j, O[j])
print(r if a != 0 else u'零圆')
