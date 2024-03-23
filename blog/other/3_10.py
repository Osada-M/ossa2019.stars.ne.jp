#! /usr/local/bin/env python3
#! encode : -*- utf-8 -*-

import sys, inspect
from typing import TypeVar, Union
print(f'バージョン：{sys.version}')

def check(func):
    def f(*args, **kwargs):
        sig = inspect.signature(func)
        for (name, param) in sig.parameters.items():
            print(f'argment_name\t: {name}\ntype\t\t: {repr(param.annotation)}')
        return func(*args, **kwargs)
    return f

@check
def func(x: int | float):
    try:
        if(isinstance(x,  int | float | str)):
            print(f'argment\t\t: {x}')
    except:
        print('error!')

a = func(1)

T1 = TypeVar('T1', int, float)
print(T1)
T2 = Union[int, float]
print(T2)

import tkinter
print(tkinter.TkVersion)

print(type(int | float))

print(int.bit_count(3))

a = {0:'a', 1:'b'}
b = a.values()
print(list(a.keys()), b.mapping, type(b.mapping))

import timeit
print(timeit.timeit(lambda:[int.bit_count(x) for x in range(100)], number=100))
