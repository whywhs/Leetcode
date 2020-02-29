# 对称二叉树。判断对称二叉树，笨方法就是像之前的二叉树层序遍历，然后判断a==a[::-1]，需要注意的是空要叫上Null
# 简单的方法就是分情况判断，如果两个都为None，那么返回True。如果一个为None，那么返回False。如果两个都是数，就要判断两者是否相等。
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if self.func(root.left,root.right):
            return True
        return False
    
    def func(self,root1,root2):
        if not root1 and not root2:
            return True
        elif not root1 and root2:
            return False
        elif not root2 and root1:
            return False
        
        if root1.val!=root2.val:
            return False
        if not self.func(root1.left,root2.right):
            return False
        if not self.func(root1.right,root2.left):
            return False
        
        
        return True
        
        
#         result = self.func(root)
#         print(result)
#         for i in result:
#             if i!=i[::-1]:
#                 return False
#         return True
    
#     def func(self,root):
#         if not root:
#             return []
#         result = [[root.val]]
#         list_my = [root]
#         while(list_my!=[]):
#             result_sub = []
#             list_next=[]
#             for i in list_my:
#                 if not i.left and not i.right:
#                     result_sub+=["null","null"]
#                 elif i.left and i.right:
#                     result_sub+=[i.left.val,i.right.val]
#                     list_next+=[i.left,i.right]
#                 else:
#                     result_sub+=[i.left.val,"null"] if i.left else ["null",i.right.val]
#                     list_next+=[i.left or i.right]
#             if list(set(result_sub))==["null"]:
#                 break
#             if result_sub!=[]:
#                 result.append(result_sub)
#             list_my = list_next
#         return result
