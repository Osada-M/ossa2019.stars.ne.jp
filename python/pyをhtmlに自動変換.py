# -*- encode : utf-8 -*-
# written by windows / 2019-12-21

print(
'''server　\\　[任意のディレクトリ]　\\　[pythonファイル]
必ず上記のファイル構成にしてください．
'''
)
head1 = '''
<!DOCTYPE html>
<html lang='ja'>
<head>
<meta charset='utf-8'>
<link rel="shortcut icon" href="..\pic\o.ico">
<link rel='apple-touch-icon-precomposed' href='..\pic\o.png'>
<link rel='stylesheet' href='..\css\code.css'>
<title>ソースコード</title>
</head>
<body class='back'>
<h1>
'''
head2 = '''
</h1>
<div class='a0'>
<a href='..\\apps.html' class='a2'>
戻る
</a>
</div>
<div class='main'>
<p>
'''
foot = '''
</p>
</div>
<script src='../count/count.php'></script>
</body>
</html>
'''
dr = input( 'directory > ' )
dr += '\\'
file = input( 'filename > ' )
with open ( dr + file, 'r', encoding = 'utf8' ) as f:
    s = f.read()
s = s.split( '\n' )
print( '< ' + file + ' read >\n' )
title = input( 'title > ' )
out = input( 'output > ' )
head = head1 + title + head2
with open ( dr + out, 'w', encoding = 'utf8' ) as f:
    f.write(head)
    for i in s:
        i = i.replace( '&', '&amp;' )
        i = i.replace( '\t', '&#9' )
        i = i.replace( ' ', '&nbsp;' )
        i = i.replace( '　', '&emsp;' )
        i = i.replace( '<', '&lt;' )
        i = i.replace( '>', '&gt;' )
        i = i.replace( '¥', '&yen;' )
        i = i.replace( '←', '&larr;' )
        i = i.replace( '↑', '&uarr;' )
        i = i.replace( '→', '&rarr;' )
        i = i.replace( '↓', '&darr;' )
        i = i.replace( '^', '&circ;' )
        i = i.replace( '~', '&tilde;' )
        i = i.replace( '―', '&mdash;' )
        i = i.replace( '"', '&quot;' )
        f.write( '<br>' + i + '\n' )
    f.write(foot)
print( '< ' + out + ' write >\n' )

finish = input( 'Press [Enter] finish.' )
