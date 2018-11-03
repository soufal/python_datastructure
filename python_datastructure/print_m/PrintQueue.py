#打印机实现

from queuedef import Queue
import random
from Printer import *
from Task import *

def simulation(numSeconds, pagesPerMinute):
    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):
        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)

        if(not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)
        
        labprinter.tick()

    averageWait = sum(waitingtimes)/len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining." % (averageWait, printQueue.size()))

#决定是否创建一个新的打印任务
def newPrintTask():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False

for i in range(20):
    simulation(3600, 5)