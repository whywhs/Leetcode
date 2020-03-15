# 不同的二叉搜索树II.这个用的是深度优先搜索，需要注意的就是sub进行append的时候要加deepcopy，因为浅拷贝会被改变。
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import copy
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n==0:
            return []
        return self.func([i for i in range(1,n+1)])

    def func(self,list_my):
        if list_my==[]:
            return [None]
        len_l = len(list_my)
        #if len_l == 1:
        #    return [TreeNode(list_my[0])]
        
        result = []
        for i in range(len_l):
            root = TreeNode(list_my[i])
            left = self.func(list_my[:i])
            right = self.func(list_my[i+1:])
            sub = []
            for m in left:
                for n in right:
                    root.left = m
                    root.right = n
                    sub.append(copy.deepcopy(root))
            result += sub
        return result
