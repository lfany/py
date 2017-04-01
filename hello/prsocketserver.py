#!/usr/bin/env python3

import socket

s = socket.socket()

host = socket.gethostname()
port = 12345
s.bind((host, port))

s.listen(5)

while True:
    c, addr = s.accept()
    print('连接数: {}'.format(addr))
    c.send(bytes('hello\n', encoding='utf8'))
    c.close()
