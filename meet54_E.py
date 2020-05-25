# 二叉搜索树的第K大节点。 这个题目的关键其实在于要有两个全局的变量来不断检视长度是否达到了，顺序就是先右后左的来。
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthLargest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.nums = []
        self.out = []
        self.func(root,k)
        return self.out[0]
    
    def func(self,root,k):
        if not root or self.out:
            return
        self.func(root.right,k)
        self.nums.append(root.val)
        if len(self.nums)==k:
            self.out.append(self.nums[-1])
        self.func(root.left,k)