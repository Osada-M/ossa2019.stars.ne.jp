#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as t

pad = [ 3, 3 ]
res_p = 21
xs, ys = [ pad[0] + x * 25 for x in range( res_p + 1 ) ], [ pad[1] + y * 25 for y in range( res_p + 1 ) ]
lim = 4

def alert():
    print( '\a', end='' )

def left( event ):
    global x0, y0, x1, y1
    if( x0 > 0 ) and not ( ( xs[x0-1] in zs[0] ) and ( ys[y0] in zs[1] ) ):
        canvas.delete( 'rec' )
        x0 -= 1
        x1 -= 1
        canvas.create_rectangle( xs[x0], ys[y0], xs[x1], ys[y1], tag = 'rec', fill = '#ff5050', outline = '#000000' )
    else:
        alert()

def right( event ):
    global x0, y0, x1, y1
    if( x1 < 21 ) and not ( ( xs[x0+1] in zs[0] ) and ( ys[y0] in zs[1] ) ):
        canvas.delete( 'rec' )
        x0 += 1
        x1 += 1
        canvas.create_rectangle( xs[x0], ys[y0], xs[x1], ys[y1], tag = 'rec', fill = '#ff5050', outline = '#000000' )
    else:
        alert()

def up( event ):
    global x0, y0, x1, y1
    if( y0 > 0 ) and not ( ( xs[x0] in zs[0] ) and ( ys[y0-1] in zs[1] ) ):
        canvas.delete( 'rec' )
        y0 -= 1
        y1 -= 1
        canvas.create_rectangle( xs[x0], ys[y0], xs[x1], ys[y1], tag = 'rec', fill = '#ff5050', outline = '#000000' )
    else:
        alert()

def down( event ):
    global x0, y0, x1, y1
    if( y1 < 21 ) and not ( ( xs[x0] in zs[0] ) and ( ys[y0+1] in zs[1] ) ):
        canvas.delete( 'rec' )
        y0 += 1
        y1 += 1
        canvas.create_rectangle( xs[x0], ys[y0], xs[x1], ys[y1], tag = 'rec', fill = '#ff5050', outline = '#000000' )
    else:
        alert()

app = t.Tk()
app.title( '迷路' )
app.geometry( '530x530' )
app.resizable( False, False )

canvas = t.Canvas( app, width = 525, height = 525 )
canvas.place( x = 0, y = 0 )

x0, y0, x1, y1 = 0, 0, 1, 1
canvas.create_rectangle( xs[x0], ys[y0], xs[x1], ys[y1], tag = 'rec', fill = '#ff5050', outline = '#000000' )
canvas.create_rectangle( xs[20], ys[20], xs[21], ys[21], tag = 'goal', fill = '#50ff50', outline = '#000000' )

xs_z = [ xs[i] for i in range( len(xs) ) if i % 2 != 0 ]
ys_z = [ ys[i] for i in range( len(xs) ) if i % 2 != 0 ]
zs = xs_z, ys_z

for x in xs_z:
    for y in ys_z:
        canvas.create_rectangle( x, y, x+25, y+25, tag = 'default', fill = '#000000', outline = '#000000' )

app.bind( '<Key-Left>', left )
app.bind( '<Key-Right>', right )
app.bind( '<Key-Up>', up )
app.bind( '<Key-Down>', down )

app.mainloop()
