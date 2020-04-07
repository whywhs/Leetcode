# 用两个栈实现队列。 维护两个数组，第一个数组只用append即可，第二个数组用来pop()
# 做法就是，如果第二个数组不是空，那么直接pop()第二个数组，如果第二个数组空了，那么就将另外一个数组重新pop进第二个数组。
class CQueue(object):

    def __init__(self):
        self.list_a = []
        self.list_b = []

    def appendTail(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.list_a.append(value)

    def deleteHead(self):
        """
        :rtype: int
        """
        if self.list_b == []:
            if self.list_a == []:
                return -1
            else:
                while(self.list_a):
                    self.list_b.append(self.list_a.pop())
        return self.list_b.pop()


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()