#!/usr/bin/env python3
from stack import Stack

def baseConvert(Number, base):
    digits = "0123456789ABCDEF"
    result = Stack()

    while Number > 0:
        yu = Number % base
        result.push(yu)
        Number = Number // base

    reString = ""
    while not result.isEmpty():
        reString = reString + digits[result.pop()]

    return reString

print(baseConvert(42, 2))
print(baseConvert(100,2))
print(baseConvert(42, 8))
print(baseConvert(25, 16))
