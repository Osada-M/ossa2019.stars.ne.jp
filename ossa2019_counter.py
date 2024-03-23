# -*- encode : utf-8 -*-
# written on mac / 2020-01-09

import urllib.request

def tab( s, n ):
    return ' ' * ( n - len(str(s)) ) 
bf, bf2 = None, None

f = 'http://ossa2019.stars.ne.jp/count/count.txt'
print( f ,end='\n\n' )
visit = urllib.request.urlopen( f ).read().decode( 'utf8' )
line = visit.split( '\n' )
mine = { '210.250.190.178' : 'LAN (home)'
        ,'126.233.218.186' : 'iPhone8 (LTE)'
        ,'66.249.' : 'GoogleBot'
        ,'126.166.135.60'  : 'v-01' }

counts = dict()
count = 0
s = [ line[i].split('\t') for i in range( len(line) ) ]
for i in range(len(s)):
    count += 1
    counts[s[i][1]] = 1 if not s[i][1] in counts.keys() else int( counts[s[i][1]] ) + 1

l = '+-----------------------+-------+-----------------------+'
#Spyder用
#l = '+-------------------+-------+-------------------+'

with open( 'counter_out.txt', 'w', encoding='utf8' ) as o:
    print( l )
    print( '|ip-address\t\t|visits\t|others\t\t\t|' )
    #Spyder用
    #print( '|ip-address\t\t\t|visits\t|others\t\t\t\t|' )
    print( l )
    o.write( str(count) + '\n' )
    o.write( 'ip-address\tvisits\tothers\n' )
    for k,v in counts.items():
        boo = True
        for i in mine.keys():
            if i in k:
                boo = False
                bf2 = '\t' + mine[i]
                bf = mine[i]
        if boo:
            bf = ''
            bf2 = ''
        m = '|{}{}|{}{}|{}{}|'.format( k,tab(k,23), v,tab(v,7), bf,tab(bf,23) )
        #Spyder用
        #m = '|{}{}|{}{}|{}{}|'.format( k,tab(k,19), v,tab(v,7), bf,tab(bf,19) )
        print( m )
        m2 = '{}\t{}{}\n'.format( k, v, bf2 )
        o.write( m2 )

print( l )
print( '\n総アクセス数 : ' + str(count) ,end='\n\n\n' )
try:
    bf = input( 'Press Enter to end > ' )
except:
    pass
