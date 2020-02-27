# 二叉搜索树的最近公共祖先。二叉搜索树因为可以进行值的判断来去找特定的点，所以当p和q的值在一个节点值的两端时，该节点即为p和q的祖先节点。
# 笨方法就是对路径进行迭代，把找到该点之前的路径均打印出来。
Definition for a binary tree node.
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
        root_val = root.val
        p_val = p.val
        q_val = q.val
        
        if p_val>root_val and q_val>root_val:
            result = self.lowestCommonAncestor(root.right,p,q)
        elif p_val<root_val and q_val<root_val:
            result = self.lowestCommonAncestor(root.left,p,q)
        else:
            return root
    
        return result
        
#         dict_list_p = self.judge(root,p)
#         dict_list_q = self.judge(root,q)
#         # print(dict_list_p)
#         # print(dict_list_q)

#         for i in dict_list_p:
#             if i not in dict_list_q:
#                 break
#             result = i
#         return result
        
        
#     def judge(self,root,p):
#         dict_list=[]
#         if root.val>p.val:
#             dict_list.append(root)
#             root = root.left
#         elif root.val<p.val:
#             dict_list.append(root)
#             root = root.right
#         else:
#             dict_list.append(root)
#             return dict_list
#         list_sub = self.judge(root,p)
#         dict_list = dict_list+list_sub
        
#         return dict_list
