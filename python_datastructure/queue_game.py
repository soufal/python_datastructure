#!/usr/bin/env python3

from queuedef import Queue

def hotPotato(namelist, num):
    simqueue = Queue()
    for i in namelist:
        simqueue.enqueue(i)

    while simqueue.size() > 1:
        for i in range(0, num):
            simqueue.enqueue(simqueue.dequeue())
        simqueue.dequeue()

    return simqueue.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))
