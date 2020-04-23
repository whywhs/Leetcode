# 复制复杂链表。这个题目是做一个复杂链表的深拷贝，具体的操作方法就是维护一个dict，dict中存的应该是原始的root，因为我们在迭代的过程中，函数里
# 传递的是原始的数据，但是dict中root的值是新的生成的值。这样就相当于在函数中通过root进行传递， 并且传递的值是新生成的value，从而完成整个链表的
# 复制。

"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        dict_all = {}
        return self.func(head,dict_all)
        
    def func(self,root,dict_all):
        if not root:
            return None
        if root in dict_all:
            return dict_all[root]
        new = Node(root.val)
        dict_all[root] = new
        new.next = self.func(root.next,dict_all)
        new.random = self.func(root.random,dict_all)
        return new