# 填充每个节点的下一个右侧节点指针。这个题目递归思想比较巧妙，一定要想得到，不然比较难写。递归就是left的下一个是right，right的下一个是上一个next的
# left.然后依次执行操作即可。
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        root.next = None
        self.func(root)
        return root
        
    def func(self,root):
        if not root.left:
            return None
        root.left.next = root.right
        root.right.next = root.next.left if root.next else None
        self.func(root.left)
        self.func(root.right)
