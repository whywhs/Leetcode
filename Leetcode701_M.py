# 二叉搜索树中的插入。
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            root = TreeNode(val)
        else:
            tree = root
            while(tree):
                if val>tree.val:
                    if not tree.right:
                        tree.right = TreeNode(val)
                        break
                    tree = tree.right
                elif val<tree.val:
                    if not tree.left:
                        tree.left = TreeNode(val)
                        break
                    tree = tree.left

        return root
