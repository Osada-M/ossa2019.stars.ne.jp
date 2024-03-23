#! /usr/local/bin/env python3
#! encode : -*- utf-8 -*-
#author : osada (http://ossa2019.stars.ne.jp/)

import tkinter as t, pyautogui as g, time

boo = True

def opn(event):
    lnk = ent0.get()
    g.hotkey('win','r')
    time.sleep(0.5)
    g.write('cmd')
    time.sleep(0.1)
    g.press('enter')
    time.sleep(1)
    g.write('explorer '+lnk)
    time.sleep(0.1)
    g.press('enter')

def bld(event):
    cdr = ent0.get()
    fil = ent1.get()
    ex = cdr
    if cdr[0] == "\"":
        ex = ex[1:-1]
    filename = ''
    inf = fil[::-1][4:]
    for i in inf:
        if i != '\\':
            filename += i
        else:
            filename = filename[::-1]
            break
    filink = ex+'\\dist\\'+filename+'\\'+filename+'.exe'
    uwa = val0.get()
    cos = val1.get()
    onf = val2.get()
    stt = val3.get()
    out0 = 'cd '+cdr
    out1 = 'pyinstaller '+fil
    out2 = ''
    if not (cos):
        out1 += ' --noconsole'
    if(onf):
        out1 += ' --onefile'
    if(stt):
        out2 = 'start '+filink

    g.hotkey('win','r')
    time.sleep(0.5)
    g.write('cmd')
    time.sleep(0.1)
    g.press('enter')
    time.sleep(1)

    g.write(out0)
    time.sleep(0.1)
    g.press('enter')
    time.sleep(0.5)

    g.write(out1)
    time.sleep(0.1)
    g.press('enter')
    time.sleep(0.5)

    if(uwa):
        time.sleep(1)
        g.write('y')
        time.sleep(0.1)
        g.press('enter')
        time.sleep(0.5)
    if(stt):
        time.sleep(2)
        g.write(out2)
        time.sleep(0.1)
        g.press('enter')
        time.sleep(0.5)

    time.sleep(1)
    g.write('exit')
    time.sleep(0.1)
    g.press('enter')
    time.sleep(0.5)

app = t.Tk()
app.title('Python build for exe')
app.geometry('723x250')
lab0 = t.Label(text='展開するフォルダ >')
lab0.place(x=10,y=20)
ent0 = t.Entry()
ent0.place(x=130,y=22,width=500)
btn0 = t.Button(text=u'開いてみる',background='#D0D0D0')
btn0.place(x=633,y=21,height=25)
btn0.bind('<Button-1>',opn)

lab1 = t.Label(text='ビルドするファイル >')
lab1.place(x=10,y=70)
ent1 = t.Entry()
ent1.place(x=130,y=72,width=500)

val0 = t.BooleanVar()
val0.set(False)
chk0 = t.Checkbutton(text=u'上書き',variable=val0)
chk0.place(x=125,y=115)
val1 = t.BooleanVar()
val1.set(False)
chk1 = t.Checkbutton(text=u'コンソールあり',variable=val1)
chk1.place(x=220,y=115)
val2 = t.BooleanVar()
val2.set(False)
chk2 = t.Checkbutton(text=u'１ファイルにまとめる',variable=val2)
chk2.place(x=350,y=115)
val3 = t.BooleanVar()
val3.set(True)
chk3 = t.Checkbutton(text=u'ビルド後に実行',variable=val3)
chk3.place(x=515,y=115)

btn1 = t.Button(text=u'ビルド開始',background='#DFEFDF')
btn1.place(x=130,y=165,width=500,height=60)
btn1.bind('<Button-1>',bld)

app.mainloop()
