#循环队列,先入先出的结构，可以进行广度优先搜索，寻找最短距离。需要注意的点有几个：
#1、end的更新是要在操作之前，因为在操作之后的话，就会错位。
#2、0与None均为否，所以，不能单纯以if 数组中的元素来进行判断。
class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.queue = [None]*k
        self.start = 0
        self.end = 0
        self.len = k
        

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        
        if None in self.queue:
            self.end = self.end+1
            if self.end == self.len+1:
                self.end=self.end-self.len
            self.queue[self.end-1]=value
            #print(self.queue)
            return True
        return False

            

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.queue[self.start]!=None:
            self.queue[self.start]=None
            self.start = self.start+1
            if self.start == self.len:
                self.start = self.start-self.len
            #print(self.queue)
            return True
        return False
        
    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.queue[self.start]==None:
            return -1
        return self.queue[self.start]
        

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.queue[self.end-1]==None:
            return -1
        return self.queue[self.end-1]
        

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        for i in self.queue:
            if i!=None:
                return False
        return True
        

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        for i in self.queue:
            if i==None:
                return False
        return True
