#循环队列的实现，先入先出的代表，区别于栈。这个的关键在于self.end的计算，要将self.end与self.start区分开来，且先后顺序要搞明白。对end进行更新
#是在操作之前，而不是之后。因为如果放在之后，那么指向的其实是下一个元素。
#另外一个主意的在于要记住，None和0都是非的意思。所以不能用if 数组[i]这种来进行判断。
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
