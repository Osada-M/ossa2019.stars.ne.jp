#! /usr/local/bin/env python3
#! encode : -*- utf-8 -*-
# author : osada (http://ossa2019.stars.ne.jp/)

import random, tkinter as t

now = 0
lim = 9
col = 4
color = ['r', 'g', 'b', 'w', 'p', 'y']
iro = ['#f87070', '#a0f8a0', '#a0a0f8', '#f8f8f8', '#f870f8', '#f8f8a0']
iro_D = dict()
for i in range( len(color) ):
    iro_D[color[i]] = iro[i]

miss0 = ['0', '1', '2', '3', '4', '5']
miss1 = ['あか', 'あお', 'みどり', 'しろ', 'ぴんく', 'き']
iro_m0 = dict()
for i in range( len(color) ):
    iro_m0[miss0[i]] = color[i]
iro_m1 = dict()
for i in range( len(color) ):
    iro_m1[miss1[i]] = color[i]
    
bf = 0 #UI配置などに使うとりあえずの変数
boo = True

#正誤判定
def hit( a, s ):
    re = [0, 0]
    old = []
    for i in range( len(s) ):
        if( s[i] == a[i] ):
            re[0] += 1
            old.append( s[i] )
    for i in range(len(s)):
        if( ( s[i] in a ) and not s[i] in old ):
            re[1] += 1
            old.append( s[i] )
    return re

#ランダムな数字の配列の生成
def rad( n ):
    global color
    color = ['r', 'b', 'g', 'w', 'p', 'y']
    return [ color.pop( random.randint( 0, len(color)-1 ) ) for i in range( n ) ]

#colの値の桁分の答えの生成
def func():
    global col
    return rad( col )

#正誤結果の処理，リスタート
def check( event ):
    global boo, now
    if boo:
        global inp, col, ans, finalAns
        ent = [ inp[now][i].get() for i in range( col ) ]
        a = hit( ans, ent )
        hitlist[now]['text'] = str( a[0] )
        blowlist[now]['text'] = str( a[1] )
        if( now != lim ):
            hitlist[now+1]['background'] = '#ffd0d0'
            blowlist[now+1]['background'] = '#ffffff'
            for i in range( col ):
                inp[now+1][i]['background'] = '#ffffff'
            labCount['text'] = '現在{}回'.format(now+1)
        if( ( now == lim ) or ( a[0] == col ) ):
            print('\a')
            for i in range( col ):
                finalAns[i].insert( 0, ans[i] )
                if( a[0] != col ):
                    inp[now][i]['background'] = '#ffd0d0'
                else:
                    inp[now][i]['background'] = '#d0ffff'
            submit['background'] = '#ffd0d0'
            submit['text'] = 'リスタート'
            boo = False
        now += 1
    else:
        appUI()
        now = 0
        labCount['text'] = '現在{}回'.format(now+1)
        boo = True

#入力から背景色を変更
def color_ch( event ):
    global col, inp, color, iro, bf, iro_D, miss0, miss1, iro_m0, iro_m1
    color = ['r', 'b', 'g', 'w', 'p', 'y']
    for i in range( col ):
        s = inp[now][i].get()
        if s in miss0:
            s = iro_m0[s]
            inp[now][i].delete( 0, t.END )
            inp[now][i].insert( 0, s )
        if s in miss1:
            s = iro_m1[s]
            inp[now][i].delete( 0, t.END )
            inp[now][i].insert( 0, s )
        if s in color:
            inp[now][i]['background'] = iro_D[s]

app = t.Tk()
app.geometry( '500x300' )
app.title( 'ヒットアンドブロー' )
app.resizable( 0, 0 )

labs = []
for i in range( len(color) ):
    labs.append( t.Label(font=('Arial', 20), relief='ridge' ) )
    labs[i]['text'] = color[i]
    labs[i]['background'] = iro[i]
    labs[i].place( x=10+35*i, y=10, width=30, height=35 )

labCount = t.Label( text=u'現在{}回'.format(now), font=('Arial', 20) )
labCount.place( x=220, y=10 )
labTab = t.Label( text=u'[tab]で移動可', font=('Arial', 12) )
labTab.place( x=328, y=15 )

labHit = t.Label( text=u'ヒット', background='#ffd0d0', font=('Arial',15) )
labHit.place( x=10, y=55, width=65, height=30 )
labBlow = t.Label( text=u'ブロー', background='#ffffff', font=('Arial',15) )
labBlow.place( x=10, y=90, width=65, height=30 )

hitlist = [ t.Label( text=u' ', background='#c0c0c0', font=('Arial', 20) ) for i in range( lim+1 ) ]
blowlist = [ t.Label( text=u' ', background='#c0c0c0', font=('Arial', 20) ) for i in range( lim+1 ) ]
bf = [ hitlist[i].place( x=80+35*i, y=55, width=30, height=30 ) for i in range( lim+1 ) ]
bf = [ blowlist[i].place( x=80+35*i, y=90, width=30, height=30 ) for i in range( lim+1 ) ]

inp = []

labAns = t.Label( text=u'答え', font=('Arial', 12) )
labAns.place( x=447, y=100 )
finalAns = [ t.Entry( font=('Arial', 20), justify=t.CENTER, background='#ffffff' ) for i in range( col ) ]
bf = [ finalAns[i].place( x=450, y=128+30*i, width=30, height=30 ) for i in range( col ) ]

for j in range( lim+1 ):
    inp.append( [ t.Entry( font=('Arial', 20), justify=t.CENTER ) for i in range( col ) ] )
    bf = [ inp[j][i].place( x=80+35*j, y=128+30*i, width=30, height=30 ) for i in range( col ) ]

#ゲームの初期化
def appUI():
    global hitlist, blowlist, inp, finalAns, bf, submit, ans
    ans = func()
    for j in range( lim+1 ):
        hitlist[j]['background'] = '#c0c0c0'
        blowlist[j]['background'] = '#c0c0c0'
        hitlist[j]['text'] = ''
        blowlist[j]['text'] = ''
        for i in range( col ):
            inp[j][i]['background'] = '#c0c0c0'
            inp[j][i].delete( 0, t.END )
    for i in range( col ):
        finalAns[i].delete( 0, t.END )
    hitlist[0]['background'] = '#ffd0d0'
    blowlist[0]['background'] = '#ffffff'
    for i in range( col ):
        inp[0][i]['background'] = '#ffffff'
    submit = t.Button( text=u'提出', background='#d0d0ff', font=('Arial', 15) )
    submit.place( x=80, y=255, width=346, height=35 )
    submit.bind( '<Button-1>', check )
    
    #print(ans) #デバッグ用，答えの出力

appUI()

app.bind( '<Key>', color_ch )
app.bind( '<Return>', check )

app.mainloop()
