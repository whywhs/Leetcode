# 从中序与后序遍历序列构造二叉树。这个是麻烦的做法，简单的做法就是观察后序遍历的特点。即list中的最后一个数一定是一个根节点，然后进行递归，依次达到
# 解决的目的。
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder)==0:
            return None
        elif len(inorder)==1:
            node = inorder.pop(0)
            return TreeNode(node)
                
        if inorder[0]==postorder[0]:
            postorder.pop(0)
            left = TreeNode(inorder.pop(0))
            mid = TreeNode(inorder.pop(0))
            mid.left = left
        else:
            mid = TreeNode(inorder.pop(0))
            mid.left = None 
        if inorder==[]: return mid
        
        right_p,right_i = [],[]
        while(postorder[0]!=mid.val):
            right_p.append(postorder.pop(0))
            right_i.append(inorder.pop(0))
        result = self.buildTree(right_i,right_p)
        mid.right = result
        if inorder!=[]:
            left_new = mid
            postorder.pop(0)
            mid = self.buildTree(inorder,postorder)
            root = mid
            while(root.left):
                root = root.left
            root.left = left_new
            
        return mid
