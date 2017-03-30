#!/usr/bin/env python

lists = [111, 22.2, 'a', 'abc', [11, 2.2, 'b', 'bb']]

## get
for i in range(len(lists)):
    # print(lists[i])
    if isinstance(lists[i], list):
        print("list =>", end=' '); print(lists[i])
        for item in lists[i]:
            print("    list[%d] =>" %i, end=' ')
            print(item)
    elif isinstance(lists[i], (int, str)):
        print("int or str =>", end=' '); print(lists[i])
    pass

## add

## delete

## update


