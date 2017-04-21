#!/usr/bin/env python3

import redis

client = redis.StrictRedis(host='192.168.71.236', port=6379, db=3, password='00')

print(client.ping())

print(client.set('test_key', 'test_value'))

