#! /usr/local/bin/env python3
#! encode : -*- utf-8 -*-
# author : osada (http://ossa2019.stars.ne.jp/)

def func( event ):
    frm = inp.get( 0., t.END )
    boo = [ True, True ]
    new = ''
    for i in frm:
        boo[1] = True
        if( boo[0] ):
            if( i == ' ' ):
                new += '&ensp;'
                boo[1] = False
            else:
                boo[0] = False
        if( i == '\n' ):
            boo[0] = True
        if( boo[1] ):
            new += rep( i )
    if( new[ len(new)-5: ] == '<br>\n' ):
        new = new[ :len(new)-5 ]
    out.delete( 0., t.END )
    out.insert( 0., new )
    if( len(new) == 0 ):
        first()
    
def rep( xs ):
    xs = xs.replace( '&', '&amp;' )
    #xs = xs.replace( '\t', '&#9' )
    xs = xs.replace( '\t', '&ensp;&ensp;&ensp;&ensp;' )
    xs = xs.replace( '　', '&emsp;' )
    xs = xs.replace( '<', '&lt;' )
    xs = xs.replace( '>', '&gt;' )
    xs = xs.replace( '¥', '&yen;' )
    xs = xs.replace( '←', '&larr;' )
    xs = xs.replace( '↑', '&uarr;' )
    xs = xs.replace( '→', '&rarr;' )
    xs = xs.replace( '↓', '&darr;' )
    xs = xs.replace( '^', '&circ;' )
    xs = xs.replace( '~', '&tilde;' )
    xs = xs.replace( '―', '&mdash;' )
    xs = xs.replace( '"', '&quot;' )
    xs = xs.replace( '\n', '<br>\n' )
    return xs

def first():
    out.insert( 0., '←左画面にHtmlに変換したい文章を入力' )

def main():
    global app, inp, out
    
    app = t.Tk()
    app.geometry( '1300x600' )
    app.title( 'PythonCode-Html変換' )
    app.resizable( width=False, height=False )
    
    inp = t.Text( app, background='#f0f0e0', font=('Arial',12) )
    inp.place( x=0, y=0, width=500, height=600 )
    out = t.Text( app, background='#d0d0f8', font=('Arial',12) )
    out.place( x=500, y=0, width=800, height=600 )
    
    but = t.Button( text=u'変換' )
    but.place( x=450, y=0, width=50 )
    but.bind( '<Button-1>', func )
    
    app.bind( '<Return>', func )
    app.bind( '<Key-v>', func )
    
    first()
    
    app.mainloop()

import tkinter as t

if __name__ == '__main__':
    main()
    