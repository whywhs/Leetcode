#最小zhai,注意的一点list.insert(index,value)
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.new = []
        self.min_m = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.new.append(x)
        if not self.min_m:
            self.min_m.append(x)
        else:
            self.min_m += [min(self.min_m[-1],x)]

    def pop(self):
        """
        :rtype: None
        """
        self.new.pop()
        self.min_m.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.new[-1]

    def min(self):
        """
        :rtype: int
        """
        return self.min_m[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()