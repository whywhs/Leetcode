# 验证二叉搜索树。采用的是中序遍历的方法，中序遍历即先遍历节点左侧，再遍历节点，最后遍历节点右侧。则验证二叉搜索树的关键在于中序遍历的数组是否是
# 一个单调递增的数组，否则就不是二叉搜索树。
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        result = self.my_list(root)
        print(result)
        if result==[]:
            return True
        else:
            for i in range(1,len(result)):
                if result[i]<=result[i-1]:
                    return False
            return True
        
        
    def my_list(self,root):
        if not root :
            return []
        else:
            result_left = self.my_list(root.left)
            result_right = self.my_list(root.right)
            result = result_left+[root.val]+result_right
        return result
