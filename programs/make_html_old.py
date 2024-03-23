#! /usr/local/bin/env python3
#! encode : -*- utf-8 -*-
#! author : osada (http://ossa2019.stars.ne.jp/)
#% 新たなhtmlページの生成

import os
import pprint
import time

MASTER_PATH = '/Users/osadamasashi/Desktop/ossa2019.stars.ne.jp'
PROFILE_PATH = 'programs/html_profile.txt'
os.chdir(MASTER_PATH)


#### 愉快な関数たち

dir_path = lambda x : '' if x == '' else '../'*dir_count(x)
dir_count = lambda x : 0 if x == '' else len(x.split('/'))
slash = lambda x : '' if x == '' else '/'

def tab_where(x:str = '3') -> str:
    x = '3' if x == '' else x
    re = ['' for i in range(4)]
    re[int(x)] = ' class="tab_now"'
    return re

def tab_where_path(x:str, d_path:str) -> list:
    x = '3' if x == '' else x
    dir_depth = dir_count(d_path)
    re = ['../'*dir_depth for i in range(4)]
    re[int(x)] = '../'*(dir_depth-1)
    result = [re, re[int(x)], int(x)]
    return result

with open(PROFILE_PATH, 'r') as f: profile_input = f.read().split('\n')
profile_arrange = []
for p in range(len(profile_input)):
    if(len(profile_input[p]) == 0):
        profile_arrange.append('')
    elif not(profile_input[p][0] == '#'):
        profile_arrange.append(profile_input[p])


#### 付加する変数たち

KEY_LIST = ['directory', 'file_name', 'title', 'tab_now', 'og:title', 'og:description', 'og:site_name', 'og:type', 'page title', 'caption', 'insert preset', 'reset']
PROFILE = dict(zip(KEY_LIST, profile_arrange))
pprint.pprint(PROFILE)

SRC_PATH = dir_path(PROFILE['directory'])
FILE_NAME = 'NoneName_'+str(time.time()) if PROFILE['file_name'] == '' else PROFILE['file_name']
FILE_PATH = PROFILE['directory']+slash(PROFILE['directory'])+FILE_NAME+'.html'
OG_SITE_NAME = PROFILE['og:title'] if PROFILE['og:site_name'] == '' else PROFILE['og:site_name']
OG_TYPE = 'blog' if PROFILE['og:type'] == '' else PROFILE['og:type']
TAB_NOW = tab_where(PROFILE['tab_now'])
TAB_NOW_ = tab_where_path(PROFILE['tab_now'], PROFILE['directory'])
TAB_NOW_PATH = TAB_NOW_[0]
TAB_LIST = ['index', 'apps', 'Remember/Remember', 'blog']
TAB_NOW_CHAR = TAB_NOW_[1]+TAB_LIST[TAB_NOW_[2]]
TAB_LIST_JUMP = ['トップ', 'アプリ', '備忘録', 'にっき']
TAB_NOW_CHAR_JUMP = TAB_LIST_JUMP[TAB_NOW_[2]]


#### htmlソース

head = """\
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="shortcut icon" href="%spic/o.ico">
    <link rel="apple-touch-icon-precomposed" href="%spic/o.png">
    <link rel="stylesheet" href="%scss/main2.css">
    <link rel="stylesheet" href="%scss/main2_half.css" media="screen and (max-width:1360px)">
    <link rel="stylesheet" href="%scss/main2_quarter.css" media="screen and (max-width:850px)">
    <link rel="stylesheet" href="%scss/main2_mobile.css" media="screen and (max-width:550px)">
    <meta property="og:title" content="%s">
    <meta property="og:description" content="%s">
    <meta property="og:site_name" content="%s">
    <meta property="og:type" content="%s">
    <meta property="og:url" content="http://ossa2019.stars.ne.jp/%s">
    <title>%s</title>
</head>
<body>
    <main>
        <div id="topScroll" class="tmTopBtn" onclick="tmTopScroll()">▲<br>top</div>
        <div class="tab">
            <p>おさだのホームページ</p>
            <a href="%sindex.html" id="home"%s>
                ホーム
            </a>
            <a href="%sapps.html" id="home"%s>
                倉　庫
            </a>
            <a href="%sRemember/Remember.html" id="home"%s>
                備忘録
            </a>
            <a href="%sblog.html" id="home"%s>
                にっき
            </a>
        </div>
        <div class="page">
            <div class="caption">
                %s
            </div>
            <div class="article">
                <p>%s</p><br>
                    <section>
"""%(SRC_PATH, SRC_PATH, SRC_PATH, SRC_PATH, SRC_PATH, SRC_PATH, PROFILE['og:title'],
PROFILE['og:description'], OG_SITE_NAME, OG_TYPE, FILE_PATH, PROFILE['title'],
TAB_NOW_PATH[0], TAB_NOW[0], TAB_NOW_PATH[1], TAB_NOW[1], TAB_NOW_PATH[2], TAB_NOW[2], TAB_NOW_PATH[3], TAB_NOW[3],
PROFILE['caption'], PROFILE['page title'])


foot = """\

                        <br><br><br><br><br>
                        <a href="%s.html" class="link">
                            %sのページに戻る
                        </a><br>
                    </section>
                <br></br>
            </div>
        </div>
    </main>
    <script src="%sjs/main.js"></script>
    <script src='//ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js'></script>
    <script src="%sjs/fade.js"></script>
    <script src="%scount/count.php"></script>
</body>
</html>
"""%(TAB_NOW_CHAR, TAB_NOW_CHAR_JUMP, SRC_PATH, SRC_PATH, SRC_PATH)


middle = """\
                        <div class="hajimeni">
                            はじめに<br>
                        </div><br><br>
                        <div class='a_list'>
                            <a href=#1>1. </a><br>
                            <a href=#2>2. </a><br>
                            <a href=#3>3. </a><br>
                        </div><br><br>
                        <br>
                        <div class="index_title", id="1">
                            1. 
                        </div><hr/><br>
                        <div class="det">
                            a
                        </div>
                        <br><br><br>
                        <div class="index_title", id="2">
                            2. 
                        </div><hr/><br>
                        <div class="code">
                            c
                        </div><br>
                        <br><br><br><br>
                        <section style="text-align:center;">(0,1)</section><br>
                        <section style="text-align:left; padding-left:10%; font-size: 80%;"></section>
                        <div class="pic"><img src="a.png" width="60%" alt="a"></div><br><br>
                        <br><br><br>
                        <div class="hajimeni">
                            さいごに<br>
                        </div>"""


#### html書き込み

with open(MASTER_PATH+'/'+FILE_PATH, 'w') as f:
    f.write(head+middle+foot if PROFILE['insert preset'] == 't' else head+foot)


#### html_profile.txtをリセットする関数

def reset():
    with open('programs/html_profile.txt', 'w') as f:
        f.write("""\
## directory ( /Users/osadamasashi/Desktop/ossa2019.stars.ne.jp/ ~~ )

## file name ( ~~ .html )

## title

## tab_now ( 0:index, 1:apps, 2:remenber, 3:blog )
3
## og:title ( shortcut name )

## og:description ( site's introduction )

## og:site_name ( 2nd shortcut name )

## og:type
blog
## page title

## caption

## insert preset ( 't' or 'f' )
t
## reset ( 't' or 'f' )
t
#% end""")


#### 最後の出力

none_value = ''
for k in PROFILE.keys():
    if(PROFILE[k] == ''):
        none_value += f'{k}, '
if not(len(none_value) == 0):
    none_value = '\n空白の要素　：　'+none_value[:len(none_value)-3]
    print(none_value)
else:
    print('\n空白の要素なし')
print(f'\n{FILE_PATH} を作成しました！\n')


#### html_profile.txtのリセット

if(__name__ == '__main__') and (PROFILE['reset'] == 't'):
    reset()
