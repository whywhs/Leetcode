# 验证平衡二叉树。一开始想复杂了，其实就是一个简单的递归函数。
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        num = self.judge(root)
        return num!=-1
        
    def judge(self,root):
        if not root:
            return 0
        
        left = self.judge(root.left)
        right = self.judge(root.right)
        if left==-1 or right==-1 or abs(left-right)>1:
            return -1
        
        return max(left,right)+1
