#!/usr/bin/env python3
"""
你可以定义一个由自己想要功能的函数，以下是简单的规则：
函数代码块以 def 关键词开头，后接函数标识符名称和圆括号()。
任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数。
函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
函数内容以冒号起始，并且缩进。
return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。


在 python 中，类型属于对象，变量是没有类型的：
在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。
"""


def test():
    return


def func(argv1, *vartuple):
    "可以传入多个参数"
    print(argv1)
    for i in vartuple:
        print(i)
    return

sum = lambda arg1, arg2: arg1 + arg2

print(sum(1, 2))

func(1, 10, 'xxxx', [1, 2.0, 'zx'])

a = 1

def xx():
    global a
    a = 2
    return

xx()
print(a)

import time

print(dir(time))