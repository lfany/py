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

lists.append('new item')
lists.append("zxc")
print(lists)

## delete
lists.remove(22.2)
del lists[0]
print(lists)

## update

lists[0] = 2
lists[1] = 2.2
lists[2] = {1, 0.1, 'zxc'}
lists[3] = (1, 2.1, 'xx')
lists[4] = 'xxxxxx'

print(lists)


