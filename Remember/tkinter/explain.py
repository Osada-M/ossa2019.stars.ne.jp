import tkinter as t

boo = True

def func( event ):
    global boo
    if( boo ):
        func_make()
        boo = False
    else:
        func_destroy()
        boo = True

def func_make():
    global lab
    lab = t.Label( text = u'ラベル', font = ('Arail',20) )
    lab.pack( pady = 10 )
    trigger[ 'text' ] = '破壊'
    trigger[ 'background' ] = '#f8d0d0'

def func_destroy():
    try:
        lab.destroy()
    except:
        pass
    trigger[ 'text' ] = '生成'
    trigger[ 'background' ] = '#d0f8d0'
    
app = t.Tk()
app.title( 'テスト' )
app.geometry( '200x100' )

trigger = t.Button( text = u'生成', font = ('Arial',15), background = '#d0f8d0' )
trigger.place( x = 20, y = 60, width = 160, height = 30 )
trigger.bind( '<Button-1>', func )

app.mainloop()
