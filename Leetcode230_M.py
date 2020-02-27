# 二叉搜索树中第K小的元素。笨方法就是进行中序遍历，然后找第K个数。简单的方法就是如下，先将所有的left存在一个stack里面，然后对stack进行pop。
# pop的过程中，k减1，当k为0则输出value。当stack进行pop后，还要将root.right加入。
# 然后，pop()的默认值是pop(-1)。
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        while(root or stack):
            while(root):
                stack.append(root)
                root = root.left
            root = stack.pop()
            k = k-1
            if k==0:
                return root.val
            root = root.right
        
#         list_root = self.mid_judge(root)
#         return list_root[k-1]
    
#     def mid_judge(self,root):
#         if not root:
#             return []
#         else:
#             list_left = self.mid_judge(root.left)
#             list_right = self.mid_judge(root.right)
#             return list_left+[root.val]+list_right
