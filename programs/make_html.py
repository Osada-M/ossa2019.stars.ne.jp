#! /usr/local/bin/env python3
#! encode : -*- utf-8 -*-
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
    re[int(x)] = ' id="now"'
    return re

def tab_where_path(x:str, d_path:str) -> list:
    x = '1' if x == '' else x
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
NOTE_BUF = "blog/" if PROFILE['tab_now'] in list("02") else ""
# TAB_LIST = ['index', 'blog', 'apps', 'Remember/Remember']
# TAB_NOW_CHAR = TAB_NOW_[1]+TAB_LIST[TAB_NOW_[2]]
# TAB_LIST_JUMP = ['トップ', 'アプリ', '備忘録', 'にっき']
# TAB_NOW_CHAR_JUMP = TAB_LIST_JUMP[TAB_NOW_[2]]


#### htmlソース

head = """\
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon" href="%spic/o.ico">
    <link rel="shortcut icon" href="%spic/o.ico">
    <link rel="apple-touch-icon-precomposed" href="%spic/o.png">
    <!-- pc版css -->
    <link rel="stylesheet" href="%scss/mainContent.css" media="screen and (min-width:600px)">
    <link rel="stylesheet" href="%scss/sidebar.css" media="screen and (min-width:600px)">
    <link rel="stylesheet" href="%scss/pointerEffect.css" media="screen and (min-width:600px)">
    <!-- モバイル版css -->
    <link rel="stylesheet" href="%scss/sidebar_mobile.css" media="screen and (max-width:599px)">
    <link rel="stylesheet" href="%scss/mainContent_mobile.css" media="screen and (max-width:599px)">
    <link rel="stylesheet" href="%scss/pointerEffect_mobile.css" media="screen and (max-width:599px)">
    <link href='https://unpkg.com/boxicons@2.0.9/css/boxicons.min.css' rel='stylesheet'>
    <meta property="og:title" content="%s">
    <meta property="og:description" content="%s">
    <meta property="og:site_name" content="%s">
    <meta property="og:type" content="%s">
    <meta property="og:url" content="https://ossa2019.stars.ne.jp/%s">
    <title>%s</title>
</head>
<body>
    <div class="sidebar">
        <div class="logo_content">
            <div class="logo">
                <!-- <i class='bx bxl-python'></i> -->
                <img src="%spic/o_alpha.PNG">
                <div class="name" id="jp_font">
                    おさだのホームページ
                </div>
            </div>
            <i class='bx bx-menu' id="open_btn"></i>
            <i class='bx bx-x' id="close_btn"></i>
        </div>
        <ul class="page_list">
            <!-- search -->
            <li>
                <i class='bx bx-search'></i>
                <input type="text" placeholder="サイト内検索..." id="search-key">
                <i class='bx bx-right-arrow-circle' id="search_btn" onclick="jump()"></i>
            </li>
            <!-- home -->
            <li%s>
                <a href="%sindex.html">
                    <i class='bx bx-home'></i>
                    <span class="link_name">home</span>
                </a>
                <span class="popup_text">home</span>
            </li>
            <!-- note -->
            <li%s>
                <a href="%s%sblog.html">
                    <i class='bx bx-book'></i>
                    <span class="link_name">note</span>
                </a>
                <span class="popup_text">note</span>
            </li>
            <!-- programs -->
            <li%s>
                <a href="%sapps.html">
                    <i class='bx bx-code-alt'></i>
                    <span class="link_name">programs</span>
                </a>
                <span class="popup_text">programs</span>
            </li>
            <!-- remember -->
            <li%s>
                <a href="%sRemember/Remember.html">
                    <i class='bx bx-paperclip'></i>
                    <span class="link_name">remember</span>
                </a>
                <span class="popup_text">remember</span>
            </li>
            <li>
                <!-- space -->
            </li>
            <!-- Sorting Sumilator -->
            <li>
                <a href="%ssorting/sorting.html">
                    <i class='bx bx-bar-chart'></i>
                    <span class="link_name" id="jp_font">Sorting Simulator</span>
                </a>
                <span class="popup_text" id="jp_font">Sorting Simulator</span>
            </li>
            <!-- tkinterの解説ページ -->
            <li>
                <a href="%sRemember/tkinter/tkinter.html">
                    <i class='bx bxl-python'></i>
                    <span class="link_name" id="jp_font">tkinterの解説ページ</span>
                </a>
                <span class="popup_text" id="jp_font">tkinterの解説ページ</span>
            </li>
            <!-- 基本情報技術者試験 -->
            <li>
                <a href="%sjouhou.html">
                    <i class='bx bx-radio-circle'></i>
                    <span class="link_name" id="jp_font">基本情報技術者試験の解答</span>
                </a>
                <span class="popup_text" id="jp_font">基本情報技術者試験の解答</span>
            </li>
            <!-- 文字数カウンター -->
            <li>
                <a href="%stext.html">
                    <i class='bx bx-pencil'></i>
                    <span class="link_name" id="jp_font">文字数カウンター</span>
                </a>
                <span class="popup_text" id="jp_font">文字数カウンター</span>
            </li>
            <li></li>
            <!-- secret page -->
            <li id="secret">
                <a href="%smyPage/home.html" target="_blank" rel="noopener noreferrer" id="secret_page">
                    <i class='bx bx-key'></i>
                    <span class="link_name">test page</span>
                </a>
                <span class="popup_text_secret">test page</span>
            </li>
        </ul>
        <div class="profile_content">
            <div class="profile">
                <div class="profile_details">
                    <div class="subscript">Writer</div>
                    <div class="name">
                        Osada Masashi
                        <br>
                        <a href="https://twitter.com/ossa2019_osada" target="_blank" rel="noopener noreferrer">
                            > twitter
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="main_content">
        <div class="tmTopBtn" id="topScroll" onclick="tmTopScroll()">
            <i class='bx bx-upvote'></i>
            <br>
            <span class="topScroll_ception">
                top
            </span>
        </div>
        <div class="text_content">
            <div class="top_title_text" id="jp_font">おさだのホームページ</div>
            <br>
            <div class="page_title" id="fade_0">
                <div class="title_text">
                    %s
                </div>
                <div class="caption_text" id="jp_font">
                    %s
                </div>
            </div>
"""%(SRC_PATH, SRC_PATH, SRC_PATH,
     SRC_PATH, SRC_PATH, SRC_PATH,
     SRC_PATH, SRC_PATH, SRC_PATH,
     PROFILE['og:title'],
     PROFILE['og:description'],
     OG_SITE_NAME,
     OG_TYPE,
     FILE_PATH,
     PROFILE['title'],
     SRC_PATH,
     TAB_NOW[0],
     TAB_NOW_PATH[0],
     TAB_NOW[1],
     TAB_NOW_PATH[1],
     NOTE_BUF,
     TAB_NOW[2],
     TAB_NOW_PATH[2],
     TAB_NOW[3],
     TAB_NOW_PATH[3],
     SRC_PATH,
     SRC_PATH,
     SRC_PATH,
     SRC_PATH,
     SRC_PATH,
     PROFILE['page title'],
     PROFILE['caption'])

foot = """\
        </div>
    </div>
    <script src="%sjs/copy.js"></script>
    <script src="%sjs/scroll.js"></script>
    <script src="%sjs/sidebar.js"></script>
    <script src="%sjs/details.js"></script>
    <script src="%sjs/i_btn.js"></script>
    <script src="%sjs/pointerEffect.js"></script>
    <script src="//ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    <script src="%sjs/fade.js"></script>
    <script>
        let topBtn = document.querySelector(".tmTopBtn");
        $(window).on('load scroll', function(){
            if ($(window).scrollTop() > 200) {
                topBtn.classList.add("active");
            } else {
                topBtn.classList.remove("active");
            }
        });
    </script>
    <script src="%scount/count.php"></script>
</body>
</html>
"""%(SRC_PATH, SRC_PATH, SRC_PATH,
     SRC_PATH, SRC_PATH, SRC_PATH,
     SRC_PATH, SRC_PATH)


middle = """\
            <div class="article">
                <br>
                <div class="index_content" id="fade_1">
                    <div class="index_link">
                        <span id="jp_font">
                            <a href=#code>完成したプログラムまで読み飛ばす　＞＞</a><br>
                            <a href=#1>1. RSA暗号とは</a><br>
                        </span>
                    </div>
                </div>
                <div class="fade", id="fade_2">
                    <div class="title" id="1">text</div>
                    <div class="text">
                        <span id="jp_font">
                            text
                        </span>
                    </div>
                </div>
            </div>
"""


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

## tab_now ( 0:index, 1:note, 2:programs, 3:remember )
0
## og:title ( shortcut name )

## og:description ( site's introduction )

## og:site_name ( 2nd shortcut name )

## og:type
website
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
