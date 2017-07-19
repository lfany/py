#!/usr/bin/env python

# formatter 1
aa = 'aaa %s %s' % ('^^', '$$')
print(aa)

# formatter 2

bb = 'bbb {} xx {}'.format('@@', ' ##')
print(bb)

# formatter 3

cc = f'bbb {"&&&"}, {"xxx"}'
print(cc)

# to be added...
