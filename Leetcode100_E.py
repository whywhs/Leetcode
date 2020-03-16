# 相同的树。就是一个简单的递归求解问题。
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if p==None or q==None:
            return False

        if p.val == q.val:
            left = self.isSameTree(p.left,q.left)
            right = self.isSameTree(p.right,q.right)
            if left and right:
                return True
        return False