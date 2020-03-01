# 从前序与中序遍历序列构造二叉树。这个和之前的一样，只不过前序是找的第一个。
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if preorder==[]:
            return None
        
        node = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        
        left_tree = self.buildTree(preorder[1:index+1],inorder[:index])
        right_tree = self.buildTree(preorder[index+1:],inorder[index+1:])
        
        node.left = left_tree
        node.right = right_tree
        
        return node
