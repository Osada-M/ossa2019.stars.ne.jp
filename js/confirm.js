"use strict";

function dl(f){
    if(window.confirm('zipファイルをダウンロードします．よろしいですか？')){
        location.href = f
    }
}

function jump(f){
    let fs = 'リンク先 : ' + f + 'に飛ぼうとしています．よろしいですか？'
    if(window.confirm(fs)){
        location.href = f
    }
}

function back(f){
    if(window.confirm('戻ります．よろしいですか？')){
        location.href = f
    }
}