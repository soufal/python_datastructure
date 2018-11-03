#!/usr/bin/env python3

from stack import Stack

def matches(open, end):
    opens = "([{"
    ends = ")]}"
    return opens.index(open) == ends.index(end)
    
    
def parCheck(symbString):
    s = Stack()
    temp = True
    for i in symbString:
        if temp == True:
            if i in "([{":
                s.push(i)
            elif s.isEmpty():
                temp = False
            else:
                top = s.pop()
                if not matches(top, i):
                    temp = False
    if s.isEmpty() and temp:
        return True
    else:
        return False

print(parCheck('((()))'))
print(parCheck('(()'))
print(parCheck('()))'))
print(parCheck('{{([][])}()}'))
print(parCheck('[{()]'))
