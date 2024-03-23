#! /usr/local/bin/env python3
#! encode : -*- utf-8 -*-
# author : osada (http://ossa2019.stars.ne.jp/)

'''
[*] Windows Only

English:
If you put "0" in the "最初にあける数", the answer will be filled automatically.
Enter "*" (asterisk) in the unknown cell. Replace the "*" with the answer.

日本語:
"最初にあける数"に「 0 」を入れると答えがすでに埋まった状態で始まる．
分からないマスに「 * 」(アスタリスク)を入力するとそこが答えに置換される．
'''

import numpy as np, tkinter as t, random, sys

def main():
    global nums_9x9, answer
    nums_9x9 = np.zeros((9,9), dtype=int)
    squr = []
    for i in range(0, 9):
        for j in range(0, 9):
            squr.append((i, j))
    while(len(squr) > 0):
        c = 0
        squr = rand_insert(0, squr, nums_9x9)
        squr = rand_insert(3, squr, nums_9x9)
        squr = rand_insert(6, squr, nums_9x9)
        while(c < 81):
            c = c + 1
            zc_TF = zero_count(nums_9x9)
            squr_l = len(squr)
            if(zc_TF and (squr_l >= 0)):
                squr = all_num_set(squr, nums_9x9)
                squr_l = len(squr)
                if(squr_l == 0):
                    break
                r = random.randint(0, squr_l - 1)
                x, y = squr[r]
                n = ok_num(x, y)
                if(n != 0):
                    nums_9x9[squr[r]] = n
                    cl_TF = check_list(n, x, y)
                    if(cl_TF):
                        squr.pop(r)
                    else:
                        nums_9x9[squr[r]] = 0
                        pass
                else:
                    break
            else:
                break
        if(len(squr) == 0):
            break
        nums_9x9 = np.zeros((9,9), dtype=int)
        squr = []
        for i in range(0, 9):
            for j in range(0, 9):
                squr.append((i, j))
    if answer:
        print('Answer ：\n{}'.format(nums_9x9),end='\n\n') # debug

def zero_count(arraylist):
    for i in range(0, 9):
        for j in range(0, 9):
            n = nums_9x9[(i, j)]
            if(n == 0):
                return True
            else:
                pass
    return False

def row_num_list(x, y):
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(0, 9):
        n = nums_9x9[(x, i)]
        if((y != i) and (n != 0)):
            num_list.remove(n)
    return num_list

def col_num_list(x, y):
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(0, 9):
        n = nums_9x9[(i, y)]
        if((x != i) and (n != 0)):
            num_list.remove(n)
    return num_list

def box_num_list(x, y):
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    sets1 = [0, 1, 2]
    sets2 = [-1, 0, 1]
    sets3 = [-2, -1, 0]
    sets_list = [sets1, sets2, sets3]
    x_sets = sets_list[x % 3]
    y_sets = sets_list[y % 3]
    for i in range(0, 3):
        for j in range(0, 3):
            setx = x + x_sets[i]
            sety = y + y_sets[j]
            n = nums_9x9[(setx, sety)]
            if((x != setx or y != sety) and (n != 0)):
                num_list.remove(n)
    return num_list

def row_check(number, x, y):
    c = 0
    for i in range(0, 9):
        if(number == nums_9x9[(x, i)]):
            c = c + 1
        else:
            pass
    if(c == 1):
        return True
    else:
        return False

def col_check(number, x, y):
    c = 0
    for i in range(0, 9):
        if(number == nums_9x9[(i, y)]):
            c = c + 1
        else:
            pass
    if(c == 1):
        return True
    else:
        return False

def box_check(number, x, y):
    sets1 = [0, 1, 2]
    sets2 = [-1, 0, 1]
    sets3 = [-2, -1, 0]
    sets_list = [sets1, sets2, sets3]
    x_sets = sets_list[x % 3]
    y_sets = sets_list[y % 3]
    c = 0
    for i in range(0, 3):
        for j in range(0, 3):
            setx = x + x_sets[i]
            sety = y + y_sets[j]
            n = nums_9x9[(setx, sety)]
            if(number == n):
                c = c + 1
            else:
                pass
    if(c == 1):
        return True
    else:
        return False

def ok_row_num(x, y):
    coordinate_list = []
    collect_list = []
    all_list = []
    for i in range(0, 9):
        if(nums_9x9[(x, i)] == 0):
            row_list = row_num_list(x, i)
            col_list = col_num_list(x, i)
            box_list = box_num_list(x, i)
            l = set(row_list) & set(col_list) & set(box_list)
            and_list = list(l)
            coordinate_list.append((x, i))
            collect_list.append(and_list)
            all_list = all_list + and_list
    for i in range(0, len(coordinate_list)):
        for j in collect_list[i]:
            coorx, coory = coordinate_list[i]
            c = all_list.count(j)
            if((x == coorx) and (y == coory) and (c == 1)):
                return j
    return 0

def ok_col_num(x, y):
    coordinate_list = []
    collect_list = []
    all_list = []
    for i in range(0, 9):
        if(nums_9x9[(i, y)] == 0):
            row_list = row_num_list(i, y)
            col_list = col_num_list(i, y)
            box_list = box_num_list(i, y)
            l = set(row_list) & set(col_list) & set(box_list)
            and_list = list(l)
            coordinate_list.append((i, y))
            collect_list.append(and_list)
            all_list = all_list + and_list
    for i in range(0, len(coordinate_list)):
        for j in collect_list[i]:
            coorx, coory = coordinate_list[i]
            c = all_list.count(j)
            if((x == coorx) and (y == coory) and (c == 1)):
                return j
    return 0

def ok_box_num(x, y):
    sets1 = [0, 1, 2]
    sets2 = [-1, 0, 1]
    sets3 = [-2, -1, 0]
    sets_list = [sets1, sets2, sets3]
    x_sets = sets_list[x % 3]
    y_sets = sets_list[y % 3]
    coordinate_list = []
    collect_list = []
    all_list = []
    for i in range(0, 3):
        for j in range(0, 3):
            setx = x + x_sets[i]
            sety = y + y_sets[j]
            if(nums_9x9[(setx, sety)] == 0):
                row_list = row_num_list(setx, sety)
                col_list = col_num_list(setx, sety)
                box_list = box_num_list(setx, sety)
                l = set(row_list) & set(col_list) & set(box_list)
                and_list = list(l)
                coordinate_list.append((setx, sety))
                collect_list.append(and_list)
                all_list = all_list + and_list
    for i in range(0, len(coordinate_list)):
        for j in collect_list[i]:
            coorx, coory = coordinate_list[i]
            c = all_list.count(j)
            if((x == coorx) and (y == coory) and (c == 1)):
                return j
    return 0

def ok_num(x, y):
    row_list = row_num_list(x, y)
    col_list = col_num_list(x, y)
    box_list = box_num_list(x, y)
    l = set(row_list) & set(col_list) & set(box_list)
    and_list = list(l)
    if(len(and_list) == 0):
        return 0
    else:
        row_num = ok_row_num(x, y)
        col_num = ok_col_num(x, y)
        box_num = ok_box_num(x, y)
        row_num_TF = row_num in and_list
        col_num_TF = col_num in and_list
        box_num_TF = box_num in and_list
        if(row_num_TF):
            return row_num
        else:
            if(col_num_TF):
                return col_num
            else:
                if(box_num_TF):
                    return box_num
                else:
                    r = random.randrange(0, len(and_list))
                    return and_list[r]

def row_only_check(number, x, y):
    row_only_list = []
    for i in range(0, 9):
        row_list = row_num_list(x, i)
        col_list = col_num_list(x, i)
        box_list = box_num_list(x, i)
        l = set(row_list) & set(col_list) & set(box_list)
        and_list = list(l)
        row_only_list.append(and_list)
    for i in range(0, 9):
        rolist = row_only_list[i]
        if((y != i) and (len(rolist) == 1) and (rolist[0] == number)):
            return False
    return True

def col_only_check(number, x, y):
    col_only_list = []
    for i in range(0, 9):
        row_list = row_num_list(i, y)
        col_list = col_num_list(i, y)
        box_list = box_num_list(i, y)
        l = set(row_list) & set(col_list) & set(box_list)
        and_list = list(l)
        col_only_list.append(and_list)
    for i in range(0, 9):
        colist = col_only_list[i]
        if((x != i) and (len(colist) == 1) and (colist[0] == number)):
            return False
    return True

def box_only_check(number, x, y):
    box_only_list = []
    sets1 = [0, 1, 2]
    sets2 = [-1, 0, 1]
    sets3 = [-2, -1, 0]
    sets_list = [sets1, sets2, sets3]
    x_sets = sets_list[x % 3]
    y_sets = sets_list[y % 3]
    for i in range(0, 3):
        for j in range(0, 3):
            setx = x + x_sets[i]
            sety = y + y_sets[j]
            row_list = row_num_list(setx, sety)
            col_list = col_num_list(setx, sety)
            box_list = box_num_list(setx, sety)
            l = set(row_list) & set(col_list) & set(box_list)
            and_list = list(l)
            box_only_list.append(and_list)
    count = 0
    for i in range(0, 3):
        for j in range(0, 3):
            bolist = box_only_list[count]
            count = count + 1
            setx = x + x_sets[i]
            sety = y + y_sets[j]
            if((x != setx or y != sety) and (len(bolist) == 1) and (bolist[0] == number)):
                return False
    return True

def rand_insert(place, squr, nums_9x9_list):
    global erasure1,erasure2,number,st
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(num_list)
    squr_li = []
    for i in range(0, 3):
        for j in range(0, 3):
            squr_li.append((i + place, j + place))
    while(len(squr_li) > 0):
        r = random.randrange(0, len(squr_li))
        x, y = squr_li[r]
        count = 0
        while(True):
            try:
                squrx, squry = squr[count]
            except IndexError:
                st['text'] = 'エラー'
                sys.exit()
            if((x == squrx) and (y == squry)):
                nums_9x9_list[(x, y)] = num_list[r]
                erasure1 = squr.pop(count)
                erasure2 = squr_li.pop(r)
                number = num_list.pop(r)
                break
            else:
                count = count + 1
    return squr

def check_list(n, x, y):
    rc_TF = row_check(n, x, y)
    cc_TF = col_check(n, x, y)
    bc_TF = box_check(n, x, y)
    roc_TF = row_only_check(n, x, y)
    coc_TF = col_only_check(n, x, y)
    boc_TF = box_only_check(n, x, y)
    if(rc_TF and (cc_TF and (bc_TF and (roc_TF and (coc_TF and (boc_TF)))))):
        return True
    return False

def row_only_set(squr, nums_9x9):
    global erasure
    for i in range(0, 9):
        coordinate_list = []
        collect_list = []
        all_list = []
        for j in range(0, 9):
            if(nums_9x9[(i, j)] == 0):
                row_list = row_num_list(i, j)
                col_list = col_num_list(i, j)
                box_list = box_num_list(i, j)
                l = set(row_list) & set(col_list) & set(box_list)
                and_list = list(l)
                coordinate_list.append((i, j))
                collect_list.append(and_list)
                all_list = all_list + and_list
        for k in range(0, len(all_list)):
            c = all_list.count(all_list[k])
            if(c == 1):
                for coor in range(0, len(collect_list)):
                    TF = all_list[k] in collect_list[coor]
                    if(TF):
                        coorx, coory = coordinate_list[coor]
                        nums_9x9[(coorx, coory)] = all_list[k]
                        count_up = 0
                        clist = len(squr)
                        while(clist > count_up):
                            squrx, squry = squr[count_up]
                            if((coorx == squrx) and (coory == squry)):
                                erasure = squr.pop(count_up)
                                count_up = count_up - 1
                                break
                            else:
                                pass
                            count_up = count_up + 1
                            clist = len(squr)
    return squr

def col_only_set(squr, nums_9x9):
    global erasure
    for i in range(0, 9):
        coordinate_list = []
        collect_list = []
        all_list = []
        for j in range(0, 9):
            if(nums_9x9[(j, i)] == 0):
                row_list = row_num_list(j, i)
                col_list = col_num_list(j, i)
                box_list = box_num_list(j, i)
                l = set(row_list) & set(col_list) & set(box_list)
                and_list = list(l)
                coordinate_list.append((j, i))
                collect_list.append(and_list)
                all_list = all_list + and_list
        for k in range(0, len(all_list)):
            c = all_list.count(all_list[k])
            if(c == 1):
                for coor in range(0, len(collect_list)):
                    TF = all_list[k] in collect_list[coor]
                    if(TF):
                        coorx, coory = coordinate_list[coor]
                        nums_9x9[(coorx, coory)] = all_list[k]
                        count_up = 0
                        clist = len(squr)
                        while(clist > count_up):
                            squrx, squry = squr[count_up]
                            if((coorx == squrx) and (coory == squry)):
                                erasure = squr.pop(count_up)
                                count_up = count_up - 1
                                break
                            else:
                                pass
                            count_up = count_up + 1
                            clist = len(squr)
    return squr

def box_only_set(squr, nums_9x9):
    global erasure
    sets1 = [0, 1, 2]
    sets2 = [-1, 0, 1]
    sets3 = [-2, -1, 0]
    sets_list = [sets1, sets2, sets3]
    count_all = 0
    clist = len(squr)
    while(clist > count_all):
        boxx, boxy = squr[count_all]
        x_sets = sets_list[boxx % 3]
        y_sets = sets_list[boxy % 3]
        coordinate_list = []
        collect_list = []
        all_list = []
        for i in range(0, 3):
            for j in range(0, 3):
                setx = boxx + x_sets[i]
                sety = boxy + y_sets[j]
                if(nums_9x9[(setx, sety)] == 0):
                    row_list = row_num_list(setx, sety)
                    col_list = col_num_list(setx, sety)
                    box_list = box_num_list(setx, sety)
                    l = set(row_list) & set(col_list) & set(box_list)
                    and_list = list(l)
                    coordinate_list.append((setx, sety))
                    collect_list.append(and_list)
                    all_list = all_list + and_list
        for k in range(0, len(all_list)):
            c = all_list.count(all_list[k])
            if(c == 1):
                for coor in range(0, len(collect_list)):
                    TF = all_list[k] in collect_list[coor]
                    if(TF):
                        coorx, coory = coordinate_list[coor]
                        nums_9x9[(coorx, coory)] = all_list[k]
                        count_up = 0
                        clist = len(squr)
                        while(clist > count_up):
                            squrx, squry = squr[count_up]
                            if((coorx == squrx) and (coory == squry)):
                                erasure = squr.pop(count_up)
                                count_up = count_up - 1
                                break
                            else:
                                pass
                            count_up = count_up + 1
                            clist = len(squr)
        count_all = count_all + 1
        clist = len(squr)
    return squr

def all_num_set(squr, nums_9x9):
    while True:
        row_squr = row_only_set(squr, nums_9x9)
        col_squr = col_only_set(squr, nums_9x9)
        box_squr = box_only_set(squr, nums_9x9)
        if(row_squr == col_squr == box_squr):
            break
    return squr

def boo(b):
    if b:
        b = False
    else:
        b = True
    return b

def func(event):
    global ans,now,st,level
    now = boo(now)
    num = level.get()
    try:
        num = int(num)
        if((num < 0) or (num > 100)):
            st['text'] = '最初にあける数字が異常'
        else:
            if now:
                color()
                main()
                ans['text'] = '正解確認'
                ans['background'] = '#DFFFDF'
                global op
                op = []
                if(num > 0):
                    for i in range(num):
                        op.append([random.randint(0,8),random.randint(0,8)])
                    for i in range(9):
                        for k in range(9):
                            ents[i][k].delete(0, t.END)
                            if([i,k] in op):
                                ents[i][k]['foreground'] = '#0000FF'
                                ents[i][k].insert(0, nums_9x9[i][k])
                            else:
                                ents[i][k]['foreground'] = '#000000'
                                ents[i][k].delete(0, t.END)
                else:
                    for i in range(9):
                        for k in range(9):
                            ents[i][k].delete(0, t.END)
                            ents[i][k]['foreground'] = '#0000FF'
                            ents[i][k].insert(0, nums_9x9[i][k])
                st['text'] = '「 * 」を入力\n→ 答え'
            else:
                Fault = True
                ans['text'] = 'スタート'
                ans['background'] = '#FFDFDF'
                for i in range(9):
                    for k in range(9):
                        if(not [i,k] in op):
                            inp = ents[i][k].get()
                            try:
                                inp = int(inp)
                            except:
                                st['text'] = 'あてはめた数字が異常'
                            out = nums_9x9[i][k]
                            if(inp == out):
                                ents[i][k].delete(0, t.END)
                                ents[i][k]['foreground'] = '#00A000'
                                ents[i][k].insert(0, out)
                            else:
                                Fault = False
                                ents[i][k].delete(0, t.END)
                                ents[i][k]['foreground'] = '#FF0000'
                                ents[i][k].insert(0, out)
                if(Fault):
                    for i in range(9):
                        for k in range(9):
                            ents[i][k]['background'] = '#DFFFDF'
                    st['text'] = '！！全問正解！！\nおめでとう！'
                else:
                    st['text'] = '計算に時間がかかるかも\nそんなときもある'
    except:
        st['text'] = '最初にあける数字が異常'

def color():
    global ents
    booI = False
    for i in range(9):
        if(i % 3 == 0):
            booI = boo(booI)        
        booK = False
        for k in range(9):
            if(k % 3 == 0):
                booK = boo(booK)
            if(booK == booI):
                ents[i][k]['background'] = '#D0D0D0'
            else:
                ents[i][k]['background'] = '#FFFFFF'

def hint(event):
    global ents, st
    st['text'] = '知りたい場所に「*」を入力'
    for i in range(9):
        for k in range(9):
            inp = ents[i][k].get()
            if inp == '*':
                ents[i][k].delete(0, t.END)
                ents[i][k].insert(0, nums_9x9[i][k])
                ents[i][k]['foreground'] = '#00A000'

now = False
app = t.Tk()
app.title('Sudoku - 数独')
app.geometry('460x490')
app.resizable(width=False, height=False)
ents = []
bf = []
for i in range(9):
    bf = [t.Entry() for i in range(9)]
    for k in range(9):
        bf[k].place(x=5+50*k, y=5+50*i, width=50, height=50)
        bf[k]['justify'] = t.CENTER
        bf[k]['font'] = ('MS Gothic',30)
    ents.append(bf)
color()
lab = t.Label(text=u'最初にあける数：')
lab.place(x=5, y=462)
level = t.Entry(justify=t.CENTER)
level.place(x=95,y=460, width=40)
level.insert(0, '40')
ans = t.Button(text=u'スタート', background='#FFDFDF')
ans.place(x=135, y=455, width=190, height=35)
ans.bind('<Button-1>', func)
st = t.Label(text=u'計算に時間がかかるかも\nそんなときもある')
st.place(x=325, y=455)
app.bind('<Key>',hint)

#answer = True : Output the answer to the console.
#(Japanese : answer = Trueでコンソールに答えを出力します．)
answer = False

app.mainloop()
