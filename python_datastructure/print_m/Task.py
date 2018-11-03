#Task类
#表示单个打印任务
#创建任务时， 随机生成器提供1到20页的长度。使用randrange函数

import random

class Task:
    def __init__(self, time):
        #时间戳:放置到队列中的时间
        self.timestamp = time
        #随机生成页数
        self.pages = random.randrange(1, 21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    #用于检索在打印开始之前队列中花费的时间
    def waitTime(self, currenttime):
        return currenttime - self.timestamp