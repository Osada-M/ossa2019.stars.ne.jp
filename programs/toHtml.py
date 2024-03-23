#! /usr/local/bin/env python3
#! encode : -*- utf-8 -*-
# author : osada (http://ossa2019.stars.ne.jp/)


import tkinter as t

def func(code:str=None):
    # 通常変換
    def rep(xs):
        xs = xs.replace('&', '&amp;')
        #xs = xs.replace('\t', '&#9')
        xs = xs.replace('\t', '&nbsp;&nbsp;&nbsp;&nbsp;')
        #xs = xs.replace('\t', '&ensp;&ensp;')
        xs = xs.replace('　', '&emsp;')
        xs = xs.replace('<', '&lt;')
        xs = xs.replace('>', '&gt;')
        xs = xs.replace('¥', '&yen;')
        xs = xs.replace('←', '&larr;')
        xs = xs.replace('↑', '&uarr;')
        xs = xs.replace('→', '&rarr;')
        xs = xs.replace('↓', '&darr;')
        xs = xs.replace('^', '&circ;')
        xs = xs.replace('~', '&tilde;')
        xs = xs.replace('―', '&mdash;')
        xs = xs.replace('"', '&quot;')
        xs = xs.replace('\n', '<br>\n')
        return xs

    frm = inp.get(0., t.END)
    boo = [ True, True ]
    new = ''
    for i in frm:
        boo[1] = True
        if(boo[0]):
            if(i == ' '):
                new += '&nbsp;'
                boo[1] = False
            else:
                boo[0] = False
        if(i == '\n'):
            boo[0] = True
        if(boo[1]):
            new += rep(i)
    
    if(code=='py'):
        new = rep_py(new)
    elif(code=='html'):
        new = rep_html(new)
        new = rep_html_1(new)
    elif(code=='js'):
        new = rep_js(new)
    elif(code=='sp'):
        new = rep_sp(new)
    
    if(new[ len(new)-5: ] == '<br>\n'):
        new = new[ :len(new)-5 ]
    out.delete(0., t.END)
    out.insert(0., new)
    if(len(new) == 0):
        first()

def func_py(event):
    func('py')
def func_html(event):
    func('html')
def func_js(event):
    func('js')
def func_sp(event):
    func('sp')

# Python
def rep_py(xs):
    # ValueError
    xs = xs.replace('ValueError', '<span class="dec4">ValueError</span>')

    # dec0
    lis0 = ['def', 'return', 'import', 'pass', 'yield', 'lambda', 'raise', 'break', 'continue', 'with', 'while', 'from', 'match', 'case']
    for l in lis0:
        xs = xs.replace(l, '<span class="dec0">'+l+'</span>')
    xs = xs.replace('class ', '<span class="dec0">class</span> ')

    # dec1
    xs = xs.replace('elif', '<span class="dec1">el</span>if')
    xs = xs.replace('if(', '<span class="dec1">if</span>(')
    lis1 = ['else', 'try', 'except']
    lis1_space = ['if', 'for', 'in', 'is', 'as']
    for l in lis1:
        xs = xs.replace(l, '<span class="dec1">'+l+'</span>')
    for l in lis1_space:
        xs = xs.replace(l+' ', '<span class="dec1">'+l+'</span> ')

    # dec2
    xs = xs.replace('kwargs', '<span class="dec2">kw</span>args')
    lis2 = ['self', '@', 'event', 'args']
    for l in lis2:
        xs = xs.replace(l, '<span class="dec2">'+l+'</span>')

    # dec3
    lis3 = ['True', 'False', 'None']
    lis3_space = ['not', 'and', 'or']
    lis3_kakko = ['not', 'and', 'or']
    for l in lis3:
        xs = xs.replace(l, '<span class="dec3">'+l+'</span>')
    for l in lis3_space:
        xs = xs.replace(l+' ', '<span class="dec3">'+l+'</span> ')
    for l in lis3_kakko:
        xs = xs.replace(l+'(', '<span class="dec3">'+l+'</span>(')

    # dec4
    lis4_underScore = ['init', 'name', 'main', 'del', 'new']
    lis4_kakko = ['print', 'range', 'type', 'super', 'replace', 'open', 'close', 'read', 'write', 'isinstance', 'len', 'chr', 'ord', 'append', 'pop', 'get',
    'int', 'float', 'str', 'byte', 'list', 'dict', 'set', 'taple', 'max', 'min', 'sum', 'abs', 'translate', 'maketrans']
    for l in lis4_underScore:
        xs = xs.replace('__'+l+'__', '<span class="dec4">__'+l+'__</span>')
    for l in lis4_kakko:
        xs = xs.replace(l+'(', '<span class="dec4">'+l+'</span>(')

    # dec5
    # なし
    
    xs = xs.replace('auth<span class="dec3">or</span>', 'author')

    return xs

# HTMl
def rep_html(xs):
    # space
    xs = xs.replace('&ensp;&ensp;&ensp;&ensp;', '&ensp;&ensp;')

    # class, span
    xs = xs.replace(' class', ' <span class="dec1">class</span>')
    xs = xs.replace('&lt;/span', '&lt;/<span class="dec0">span</span>')
    xs = xs.replace('&lt;span', '&lt;<span class="dec0">span</span>')
    
    # dec0
    lis0 = ['html', 'body', 'head', 'meta', '!DOCTYPE html', 'link', 'title', 'div', 'p1', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p', 'p0', 'a', 'section', 'br', 'hr', 'script',
    'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8', 'h9', 'h10', 'details', 'summary', 'form', 'table', 'tr', 'td', 'input', 'textarea', 'img', 'select', 'label', 'area', 'button', 'frameset', 'main']
    for l in lis0:
        xs = xs.replace('&lt;'+l, '&lt;<span class="dec0">'+l+'</span>')
        xs = xs.replace('&lt;/'+l, '&lt;/<span class="dec0">'+l+'</span>')
    # dec1
    lis1 = ['lang', 'charset', 'name', 'content', 'rel', 'href', 'media', 'property', 'id', 'style', 'src', 'action', 'type', 'value', 'size', 'checked', 'target', 'width', 'height',
    'onclick', 'ondbclick', 'onmousedown', 'onmouseup', 'onmouseover', 'onmouseout', 'onkeypress', 'onkeyup', 'onkeydown', 'onload', 'onunload', 'onfocus', 'onblur', 'onsubmit', 'onreset', 'onselect', 'onchange', 'align', 'border']
    for l in lis1:
        xs = xs.replace(' '+l, ' <span class="dec1">'+l+'</span>')
    # dec2
    # なし

    # dec3
    # rep_html_1()
    
    # dec4
    # なし

    # dec5
    lis5 = ['altername', 'canonial', 'author', 'bookmark', 'icon', 'shortcut icon', 'stylesheet', 'og:title', 'og:description', 'og:site_name', 'og:type', 'og:url', 'apple-touch-icon-precomposed', 'UTF-8', 'SHIFT-JIS', 'viewport', 'ja', 'en']
    for l in lis5:
        xs = xs.replace('\''+l+'\'', '\'<span class="dec5">'+l+'</span>\'')
        xs = xs.replace('&quot;'+l+'&quot;', '&quot;<span class="dec5">'+l+'</span>&quot;')

    return xs

# HTML 特殊文字
def rep_html_1(xs):
    # dec3
    lis3 = ['ensp', 'lt', 'gt', 'emsp', 'amp', '#9', 'yen', 'larr', 'uarr', 'rarr', 'darr', 'circ', 'tilde', 'mdash', 'quot']
    for l in lis3:
        xs = xs.replace('&amp;'+l+';', '<span class="dec3">&amp;'+l+';</span>')
    
    return xs

# JavaScript
def rep_js(xs):
    # dec0
    lis0 = ['function', 'let', 'const', 'var']
    for l in lis0:
        xs = xs.replace(l, '<span class="dec0">'+l+'</span>')
    # dec1
    lis1 = ['for', 'else', 'try', 'catch', 'return', 'break', 'continue']
    for l in lis1:
        xs = xs.replace(l, '<span class="dec1">'+l+'</span>')
    xs = xs.replace('elif', '<span class="dec1">el</span>if')
    xs = xs.replace('if(', '<span class="dec1">if</span>(')
    xs = xs.replace('if (', '<span class="dec1">if</span> (')
    # dec2
    xs = xs.replace('\'use strict\';', '<span class="dec2">\'use strict\';</span>')
    xs = xs.replace('&quot;use strict&quot;;', '<span class="dec2">&quot;use strict&quot;;</span>')
    # dec3
    lis3 = ['true', 'false', 'none', 'String', 'Boolean', 'int', 'float', 'any', 'Number']
    for l in lis3:
        xs = xs.replace(l, '<span class="dec3">'+l+'</span>')
    # dec4
    lis4 = ['window', 'console', 'log', 'confirm', 'alert', 'document', 'body', 'documentElement', 'scrollLeft', 'scrollRight', 'scrollTop', 'scrollBottom', 'location', 'href', 'Math', 'round'
    ,'getElementById', 'getElementsByName', 'getElementsByClassName', 'event', 'innerHTML', 'value', 'onsubmit', 'onclick', 'onkeyup', 'onkeydown', 'replace', 'length', 'textContent', 'checked',
    'fromCharCode', 'charCodeAt', 'keyup', 'click', 'submit', 'keydown', 'execCommand', 'addEventListener', 'select', 'innerText']
    for l in lis4:
        xs = xs.replace(l, '<span class="dec4">'+l+'</span>')
    xs = xs.replace('pr<span class="dec4">event</span>Default', '<span class="dec4">preventDefault</span>')
    # dec5

    return xs

#特殊変換
def rep_sp(xs):
    #dec2
    lis2 = ['*']
    for l in lis2:
        xs = xs.replace(l, '<span class="dec2">'+l+'</span>')
    #dec6
    lis6 = ['&gt;&gt;', '$', '%']
    for l in lis6:
        xs = xs.replace(l, '<span class="dec6">'+l+'</span>')
    return xs

def first():
    out.insert(0., '←左画面にHtmlに変換したい文章を入力')

def main():
    global app, inp, out
    
    app = t.Tk()
    app.geometry('1300x625')
    app.title('Text to Html 変換アプリ')
    app.resizable(width=False, height=False)
    
    inp = t.Text(app, background='#f0f0e0', font=('Arial',12))
    inp.place(x=0, y=0, width=500, height=600)
    out = t.Text(app, background='#d0d0f8', font=('Arial',12))
    out.place(x=500, y=0, width=800, height=600)

    but = t.Button(text=u'通常変換', background='#ffaaaa')
    but.place(x=5, y=600, width=70, height=20)
    but.bind('<Button-1>', func)
    but_py = t.Button(text=u'Python', background='#ffffff')
    but_py.place(x=75, y=600, width=70, height=20)
    but_py.bind('<Button-1>', func_py)
    but_html = t.Button(text=u'HTML', background='#ffffff')
    but_html.place(x=145, y=600, width=70, height=20)
    but_html.bind('<Button-1>', func_html)
    but_js = t.Button(text=u'JavaScript', background='#ffffff')
    but_js.place(x=215, y=600, width=70, height=20)
    but_js.bind('<Button-1>', func_js)
    but_sp = t.Button(text=u'特殊変換', background='#ffffff')
    but_sp.place(x=285, y=600, width=70, height=20)
    but_sp.bind('<Button-1>', func_sp)
    but['background'] = '#ffffff'
    but_py['background'] = '#ffffff'
    but_html['background'] = '#ffffff'
    but_js['background'] = '#ffffff'
    but_sp['background'] = '#ffffff'
    app.bind('<Key-v>', func)
    
    first()
    
    app.mainloop()

if(__name__ == '__main__'):
    main()
    