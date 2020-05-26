# 二叉搜索树与双向链表。这个题目是一个双向链表的问题。关键就在于递归的想法，对于当前root来说，对左子树进行递归，得到左子树排好
# 链表的头结点和尾结点Lh,Lt。然后对右子树进行递归，得到右子树排好链表的头结点和尾结点Rh,Rt。那么root.left = Lt, root.right = Rh
# 但是这里需要注意边界条件，如果左子树为空，那么就让root变为Lh, 如果右子树为空，那么就让root变为Rt。 如果同时变成了空，就返回None,
# None 即可。
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return
        Lh,Rt = self.func(root)
        Lh.left = Rt
        Rt.right = Lh
        return Lh

    def func(self,root):
        if not root:
            return None,None
        Lh,Lt = self.func(root.left)
        Rh,Rt = self.func(root.right)
        root.left = Lt
        if Lt:
            Lt.right = root
        else:
            Lh = root
        root.right = Rh
        if Rh: 
            Rh.left = root
        else:
            Rt = root
        return Lh,Rt