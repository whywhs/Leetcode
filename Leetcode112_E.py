# 路径总和。对于路径总和，要记得看清他要求的是到叶子节点的路径，如果还没有到叶子节点就已经结束，是错误。
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        
        if self.func(root,sum):
            return True
        return False
    
    def func(self,root,x):     
        x_now = x - root.val
        if not root.left and not root.right:
            return True if x_now==0 else False
        elif root.left==None or root.right==None:
            return self.func(root.left or root.right,x_now)
        else:
            if self.func(root.left,x_now):
                return True 
            return True if self.func(root.right,x_now) else False
