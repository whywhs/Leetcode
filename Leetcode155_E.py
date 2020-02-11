#最小zhai,注意的一点list.insert(index,value)
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.a = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.a.insert(0,x)
        

    def pop(self):
        """
        :rtype: None
        """
        self.a.pop(0)
        

    def top(self):
        """
        :rtype: int
        """
        return self.a[0]
        

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.a)
