# 队列中的最大值。这个题目参考滑动窗口最大值一题。
class MaxQueue(object):
    def __init__(self):
        self.my_squ = []
        self.max_squ = []
        self.judge = []
        self.push,self.pop = 0,0

    def max_value(self):
        """
        :rtype: int
        """
        if self.max_squ==[]:
            return -1
        return self.max_squ[0]

    def push_back(self, value):
        """
        :type value: int
        :rtype: None
        """

        self.push += 1
        self.my_squ.append(value)

        if self.max_squ==[]:
            self.max_squ.append(value)
            self.judge.append(self.push)
        else:
            while(self.max_squ!=[] and value > self.max_squ[-1]):
                self.max_squ.pop()
                self.judge.pop()
            self.max_squ.append(value)
            self.judge.append(self.push)

    def pop_front(self):
        """
        :rtype: int
        """
        if self.my_squ==[]:
            return -1
        self.pop += 1
        if self.pop == self.judge[0]:
            self.max_squ.pop(0)
            self.judge.pop(0)
        return self.my_squ.pop(0)



# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()
