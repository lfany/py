#!/usr/bin/env python

import socket

import os

import sys

import struct


def inet_ntoa(address):
    """
    :param address:
    :return:
    """
    if len(address) != 4:
        raise Exception('address not legal')
    if not isinstance(address, bytearray):
        address = bytearray(address)
    return ('%u.%u.%u.%u' % (address[0],
                             address[1],
                             address[2],
                             address[3]))


def inet_aton(text):
    """
    :param text:
    :return:
    """
    if not isinstance(text, bytes):
        text = text.encode()
    parts = text.split(b'.')
    if len(parts) != 4:
        raise Exception('ip is not legal')
    for part in parts:
        if not part.isdigit():
            raise Exception('ip with [%s] is not legal' % part)
        if len(part) > 1 and part[0] == 0:
            raise Exception('ip with [%s] is not legal' % part)
    try:
        results = [int(part) for part in parts]
        return struct.pack('BBBB', *results)
    except:
        raise Exception('ip: error parse')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: %s [ipaddress]' % __file__)
    else:
        print(inet_aton(sys.argv[1]))
