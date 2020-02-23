# 二叉搜索树中的搜索。
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return None
        
        tree = root
        while(tree):
            if val>tree.val:
                tree = tree.right
            elif val<tree.val:
                tree = tree.left
            else:
                return tree
        return None
        
