#!/usr/bin/env python3
from stack import Stack

def divideBy2(Number):
    result = Stack()

    while Number > 0:
        yu = Number % 2
        result.push(yu)
        Number = Number // 2

    reString = ""
    while not result.isEmpty():
        reString = reString + str(result.pop())

    return reString

print(divideBy2(42))
print(divideBy2(1))
