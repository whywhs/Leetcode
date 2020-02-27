# 二叉树的最近公共祖先。这个题笨方法就是之前的把路径都保存下来，简单的方法就还是看left和right。如果left和right一旦有一个发现了p与q中的一个值，就
# 返回当前的root。然后要看left和right的值，如果发现left和right都有，那么root就必定是该两个值的公共祖先。如果只发现有一个，那么说明另外一个一定是
# 在当前值的下面，不然一定会检索到。所以，该root就是两个的公共祖先。
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        if root==p or root==q:
            return root
        
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if left and right:
            return root
        elif left or right:
            return left or right

        
#         p_list = self.judge(root,p)[::-1]
#         q_list = self.judge(root,q)[::-1]
#         result = root
#         for i in p_list:
#             if i not in q_list:
#                 return result
#             result = i
#         return result
        
        
#     def judge(self,root,p):
#         result = []
#         if not root:
#             return []
#         if root.val==p.val:
#             return [root]
#         else:
#             left_list = self.judge(root.left,p)
#             right_list = self.judge(root.right,p)
#             result = left_list+right_list
#             if result!=[]:
#                 result = result+[root]
#             return result
