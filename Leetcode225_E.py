# 用队列实现栈。这个题目的关键在于只可以使用队列来进行操作，队列的操作手段包括pop(0)，append(x)，len()等。利用队列是先进先出的特性，需要维护两个队列
# 分别为que1和que2. 即将que1中pop出的推入que2中，直到que1只剩下1个数，那这个就是栈的栈顶元素。
class MyStack(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.que1 = []
        self.que2 = []
        self.topval = 0

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.que1.append(x)
        self.topval = x

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        len_que1 = len(self.que1)
        for i in range(len_que1-1):
            self.topval = self.que1.pop(0)
            self.que2.append(self.topval)
        val = self.que1.pop(0)
        self.que1 = self.que2
        self.que2 = []
        return val

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.topval

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if self.que1==[]:
            return True
        return False




# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
