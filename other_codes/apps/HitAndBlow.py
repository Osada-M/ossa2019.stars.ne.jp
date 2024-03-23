#! /usr/local/bin/env python3
#! encode : -*- utf-8 -*-
# author : osada (http://ossa2019.stars.ne.jp/)

import random

def hit(a, s):
    re = [0, 0]
    old = []
    for i in range(len(s)):
        if(s[i] == a[i]):
            re[0] += 1
            old.append(s[i])
    for i in range(len(s)):
        if((s[i] in a) and not s[i] in old):
            re[1] += 1
    return re

def rad(n):
    global color, color_ch
    color = ['r', 'b', 'g', 'w', 'p', 'y']
    nihon = ['赤','青','緑','白','ピンク','黄']
    color_ch = dict()
    for i in range(len(color)):
        color_ch[nihon[i]] = color[i]
    print(color_ch)
    return [color.pop(random.randint(0, len(color)-1)) for i in range(n)]

ans = rad(4)

for j in range(10):
    print('\n'+str(j)+' 回目 ========\n')
    inp = [input(str(i)+' > ') for i in range(4)]
    for i in range(4):
        if inp[i] in color_ch:
            inp[i] = color_ch[inp[i]]
    re = hit(ans, inp)
    print('\n{} ヒット， {} ブロー'.format(re[0], re[1]))
    if re[0] == 4:
        print('\n正解！')
        break

print('\nend')