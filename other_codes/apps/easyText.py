#! /usr/local/bin/env python3
#! encode : -*- utf-8 -*-
# author : osada (http://ossa2019.stars.ne.jp/)

'''
======= 説 明 書 =======

＜エラーが出て実行できないとき＞
コマンドプロンプトにて「 pip install tkinter 」
と入力し[ Enter ]キーを押す。
インストール完了後ならエラーが出ないはず。

それでもエラーが出るときは
またコマンドプロンプトにて「 pip install pathlib 」
と入力し[ Enter ]キーを押す。。
インストール完了後ならエラーが出ないはず。

それでもエラーが出るとき、Pythonのバージョンが３未満であるか、.pyのエンコードをutf-8以外でやっている可能性がある。


＜チェックボックスの意味＞
改行 : 改行を文字数にカウントする。
空白 : 空白を文字数にカウントする。
句読点 : 句読点（，．、。）を文字数にカウントする。
半角数字 : 連続した半角数字(100や2019など)を全て一文字としてカウントする。
        例 :「１」->１文字、「12345」->１文字。これはMicrosoft Wordと同じ。


＜文字数カウントについて＞
何かしらのキー入力がある度にカウントを行う。
もしカウントされないときはShiftや十字キーなどを適当に押すといいかも。

<#> ~~~ </#> で囲まれた文字列はカウントに含まれない。

・メモ帳など標準的なテキストエディタ -> 空白、句読点
・Microsoft Word -> Word形式


＜保存について＞
保存ファイルは「 .txt 」拡張子で保存される。
すぐ下にある変数「 kks 」の値を「 '.c' 」にすると.cで保存されるので適宜変えてください。
また、os.chdir()がディレクトリの設定なので、適宜変えてください。

保存ファイル名を指定しないまま保存すると、「 easyText-(現在時刻).txt 」
で保存される。指定すると「 (入力したファイル名).txt 」になる。
「 Ctrl 」 + 「 s 」 でも保存できる。

=======================
'''

ver = '1.3'
kks = '.txt'

import tkinter as t
import datetime as d
import os

kuten = ['、','。','，','．',',','.'] #句読点
suuji = ['1','2','3','4','5','6','7','8','9','0'] #半角数字
#suuji2 = [x+'.' for x in suuji] #小数点付き半角数字
#半角文字
han = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '-', '#', '$', '%', '&', '!', '?', '(', ')', '{', '}', '[', ']', '<', '>', '+', '-', '*', '/', '\\', '^', '~', '@', '=', ',', '.', '_']
global size
size = 14 #デフォルトのフォントサイズ

#カレントディレクトリ
#自分の好きなところに設定
os.chdir('../../')
dr = ''

def counter(event): #文字数カウント関数
    global labC,txt,fil
    fil['background'] = '#FFFFFF'
    sss = txt.get(0.,t.END)
    count = 0
    sBoo = True
    hBoo = True
    has = ''
    for i in sss:
        if i in ['<','#','>','/']:
            has += i
        else:
            has = ''
        if has == '<#>':
            if not valH.get():
                count -= 2
            hBoo = False
            has = ''
        if has == '</#>' and not hBoo:
            count -= 1
            hBoo = True
            has = ''
        if hBoo:
            if i == '\n':
                sBoo = True
                if valN.get():
                    sBoo = True
                    count += 1
            elif i == ' ' or i == '　':
                if valS.get() and not valH.get():
                    sBoo = True
                    count += 1
                if  valH.get():
                    count += 1
            elif i in kuten:
                if valP.get() and not valH.get():
                    sBoo = True
                    count += 1
            elif (i in suuji) or (i in han) or (i == '.'):
                if sBoo:
                    count += 1
                if valH.get():
                    sBoo = False
            else:
                sBoo = True
                count += 1
    if valN.get():
        count-=1
    if count < 0:
        count = 0
    labC['text']=count

def save(event): #保存する関数    
    global fil
    fil['background'] = '#CFFFCF'
    filname = fil.get()
    if len(filname) == 0:
        filname = d.datetime.now().strftime('%m-%d_%H-%M_%S')
        filname = 'easyText-'+filname
    filname += kks
    with open(dr+filname,'w') as f:
        f.write(txt.get(0.,t.END))

def smaller(event): #フォントサイズ変更関数
    global sml,size
    size -= 1    
    if size < 1:
        size = 1  
    txt['font']=('MS Gothic',size)
    lab0['text']='size : '+str(size)    
def bigger(event):
    global big,size
    size += 1    
    if size > 350:
        size = 350
    txt['font']=('MS Gothic',size)
    lab0['text']='size :'+str(size)

def smaller10(event):    
        global sml,size
        size -= 10                
        if size < 1:
            size = 1                    
        txt['font']=('MS Gothic',size)
        lab0['text']='size : '+str(size)
        
def bigger10(event):
        global big,size
        size += 10            
        if size > 350:
            size = 350                    
        txt['font']=('MS Gothic',size)
        lab0['text']='size : '+str(size)    
        
#文章校正の関数
def kousei0F(event): #，．
        sss = txt.get(0.,t.END)
        sss = list(sss[:len(sss)-1])
        out = ''        
        for i in range(len(sss)):
            if sss[i] == '，':
                sss[i] = '、'
            elif sss[i] == '．':
                sss[i] = '。'                    
            out += sss[i]        
        txt.delete(0.,t.END)
        txt.insert(0.,out)
def kousei1F(event): #、。
        sss = txt.get(0.,t.END)
        sss = list(sss[:len(sss)-1])
        out = ''
        for i in range(len(sss)):
            if sss[i] == '、':
                sss[i] = '，'
            elif sss[i] == '。':
                sss[i] = '．'
            out += sss[i]
        txt.delete(0.,t.END)
        txt.insert(0.,out)

# UIの配置=================================--

app = t.Tk()
app.title('オサダテキストエディタ（簡易版） '+ver)
app.geometry('780x510')
app.resizable(width=False, height=False) #画面サイズ固定

#テキスト領域
txt = t.Text(font=('MS Gothic',size))
txt.place(x=5,y=5,width=770,height=477)
txt['background']='#FFFFFA'

#改行文字を含める
valN = t.BooleanVar()
valN.set(False)
kaigyou = t.Checkbutton(text=u'改行'
                        ,variable=valN)
kaigyou.place(x=5,y=484)

#空白文字を含める
valS = t.BooleanVar()
valS.set(True)
kuuhaku = t.Checkbutton(text=u'空白'
                        ,variable=valS)
kuuhaku.place(x=60,y=484)

#句読点を含める
valP = t.BooleanVar()
valP.set(True)
kutouten = t.Checkbutton(text=u'句読点'
                        ,variable=valP)
kutouten.place(x=115,y=484)

#Word形式
valH = t.BooleanVar()
valH.set(False)
hankaku = t.Checkbutton(text=u'Word形式'
                        ,variable=valH)
hankaku.place(x=180,y=484)

#文字数
lab = t.Label(text=u'count : '
              ,font=('MS Gothic',10))
lab.place(x=265,y=486)
labC = t.Label(text=u''
              ,font=('MS Gothic',10)
              ,foreground='#FF0000')
labC.place(x=324,y=486)

#保存ファイル名
labF = t.Label(text=u'保存ファイル名 : ')
labF.place(x=365,y=484)
global fil
fil = t.Entry(width=15)
fil.place(x=450,y=485)

#保存
cnt = t.Button(text=u'保存 (Ctrl + S)'
               ,font=('MS Gothic',8)
               ,background='#D0F0D0')
cnt.place(x=545,y=484,width=100,height=23)
cnt.bind('<Button-1>',save)

#フォントサイズ
lab0 = t.Label(text=u'size : '+str(size))
lab0.place(x=645,y=484)
sml = t.Button(text=u'－'
               ,font=('MS Gothic',10) #マイナス
               ,background='#E0E0E0')
sml.place(x=716,y=484,width=20)
sml.bind('<Button-1>',smaller)
big = t.Button(text=u'＋'
               ,font=('MS Gothic',10) #プラス
               ,background='#E0E0E0'
               ,foreground='#C00000')
big.place(x=736,y=484,width=20)
big.bind('<Button-1>',bigger)
sml10 = t.Button(text=u'10'
                 ,font=('MS Gothic',10) #大マイナス
                 ,background='#E0E0E0')
sml10.place(x=696,y=484,width=20)
sml10.bind('<Button-1>',smaller10)
big10 = t.Button(text=u'10'
                 ,font=('MS Gothic',10) #大プラス
                 ,background='#E0E0E0'
                 ,foreground='#C00000')
big10.place(x=756,y=484,width=20)
big10.bind('<Button-1>',bigger10)

#キーボードでボタン操作
app.bind('<Control-Key-s>',save) #ctrl+s:save
app.bind('<Key>',counter) #キー入力でカウント

app.mainloop()
