#!/usr/bin/env python3

a = 100
b = 100.00
c = 'hello'

aa = bb = cc = 'xx'

aaa, bbb, ccc = 1, 1.0, 'ss'

# print(a, b, c)

'''
Python有五个标准的数据类型：
Numbers（数字）
String（字符串）
List（列表）
Tuple（元组）
Dictionary（字典）

    Python支持四种不同的数字类型：
    int（有符号整型）
    long（长整型[也可以代表八进制和十六进制]）
    float（浮点型）
    complex（复数）
    
    加号（+）是字符串连接运算符，星号（*）是重复操作。
'''

del a, b, c

a = 'abc'
b = a + a
c = a * 2
# print(b); print(len(b))
# print(c)


### List ###

del a, b, c

a = [1, 1.11, 'hello', "world", """!!!"""]
a[0] = 100
# print(a)
# print(a)
#
# for i in a:
#     print(i)

### tuple
b = (1, 1.11, 'hello', "world", """!!!""")
# b[0] = 111
# print(b)

### dictionary
c = {"a": 1, "b": 1.11, "c": 'hello', "d": "world", "e": """!!!""", "f": a, "g": b,
     "h": {1, 2.2, 'aa'}, 1: 'aaa'}
# print(c.keys())
# print(c.values())

del a, b, c


### 强制数据类型转化

'''
int(x [,base])
将x转换为一个整数
long(x [,base] )
将x转换为一个长整数
float(x)
将x转换到一个浮点数
complex(real [,imag])
创建一个复数
str(x)
将对象 x 转换为字符串
repr(x)
将对象 x 转换为表达式字符串
eval(str)
用来计算在字符串中的有效Python表达式,并返回一个对象
tuple(s)
将序列 s 转换为一个元组
list(s)
将序列 s 转换为一个列表
set(s)
转换为可变集合
dict(d)
创建一个字典。d 必须是一个序列 (key,value)元组。
frozenset(s)
转换为不可变集合
chr(x)
将一个整数转换为一个字符
unichr(x)
将一个整数转换为Unicode字符
ord(x)
将一个字符转换为它的整数值
hex(x)
将一个整数转换为一个十六进制字符串
oct(x)
将一个整数转换为一个八进制字符串
'''
