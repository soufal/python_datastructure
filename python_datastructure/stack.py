#!/usr/bin/env python3
#create a stack class

class Stack:
    def __init__(self):
        self.items = []

#stack is empty?
    def isEmpty(self):
        return self.items == []

#push stack
    def push(self, item):
        self.items.append(item)

#pop stack
    def pop(self):
        return self.items.pop()

#return item
    def peek(self):
        return self.items[len(self.items)-1]

#return size of stack
    def size(self):
        return len(self.items)
