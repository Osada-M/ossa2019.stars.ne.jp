#! /usr/local/bin/env python3
#! encode : -*- utf-8 -*-
# author : osada (http://ossa2019.stars.ne.jp/)

import tkinter as t

app = t.Tk()
app.geometry('170x205')
app.title('ColorCode')

lab = t.Label(text=u'RGB ->', font=('MS Gothic', 20))
lab.place(x=3, y=5)
ent = t.Entry(font=('MS Gothic', 20))
ent.place(x=73, y=5, width=90)

alp = {'a':'A','b':'B','c':'C','d':'D','e':'E','f':'F'}
def func(event):
    try:
        s = ent.get()
        if len(s) == 3:
            ss = [s[0],s[0],s[1],s[1],s[2],s[2]]
        elif len(s) == 6:
            ss = list(s)
        elif len(s) > 6:
            ss = list(s[:6])
        else:
            return False
        re = ''
        ss = [alp[ss[i]] if ss[i] in alp.keys() else ss[i] for i in range(len(ss))]
        for s in ss:
            re += s
        #cvs['background'] = '#'+re
        app['background'] = '#'+re
        lab['background'] = '#'+re
    except:
        print('\aerror')

##ボタンで色を変えたい時はコメントアウトを外してください。
#cvs = t.Button(text=u'[Enter] or クリック\nで色が変わるよ')
#cvs.place(x=5, y=40, width=160, height=160)
#cvs.bind('<Button-1>', func)

app.bind('<Key>', func)

app.mainloop()
