#模拟打印机

#类Printer
class Printer:
    def __init__(self, ppm):
        #打印速度
        self.pagerate = ppm
        #是否有打印任务
        self.currentTask = None
        #打印完成剩余时间
        self.timeRemaining = 0
    
    #将内部定时器递减直到打印机设置为空闲
    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None
    

    #打印机忙碌状态
    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self, newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60/self.pagerate