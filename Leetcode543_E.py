# 二叉树的直径。这个题和之前的那个算和的题目很像，只不过结果不是求和而是求长度，思路同前。
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        a,b = self.func(root)
        b.append(a)

        return max(b)-1 


    def func(self,root):
        if not root:
            return 0,[]
        
        result = []
        left,l_r = self.func(root.left)
        right,r_r = self.func(root.right)
        result += l_r
        result += r_r
        result.append(left+right+1)

        return max(left+1,right+1),result
