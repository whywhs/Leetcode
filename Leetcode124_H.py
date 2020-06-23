# 二叉树中的最大路径和。这个题目递归的思路是分两种情况，第一种情况是当前root作为结束的根节点，另外一种情况是当前root作为子节点返回。
# 对于递归到当前root，一共存在四种值。第一个就是当前root值，第二个是当前root+left的值，第三个是当前root+right的值，第四个是当前root+left+right值。
# 对于第一种情况，那么肯定就是第四种值的代表，因为一旦当前root与左右两个子叶均进行相加，那么递归也就完成了。
# 对于第二种情况，那么就是前三种值，由于递归未完成，故返回max(value1,value2,vaule3)
# 最后，就对所有的情况取最大值即可。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # if not root.left and not root.right:
        #     return root.val
        result,result_all = self.judge(root)
        max_result = max(result)
        return max(max_result,result_all)
        
        
    def judge(self,root):
        if not root:
            return [],0 

        l_fin,left = self.judge(root.left)
        r_fin,right = self.judge(root.right)
        
        result = []
        value1 = root.val
        value2 = root.val + left
        value3 = root.val + right
        value4 = root.val + left + right
        
        result += l_fin
        result += r_fin
        result += [max(value1,value2,value3,value4)]
        
        return result,max(value1,value2,value3)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def func(root):
            if not root.left and not root.right:
                return root.val,root.val
            left,right = float('-inf'),float('-inf')
            left_all,right_all = float('-inf'),float('-inf')
            if root.left:
                left,left_all = func(root.left)
            if root.right:
                right,right_all = func(root.right)
            max_return = max(left,right)
            return max(max_return+root.val,root.val),max(left+right+root.val,left_all,right_all,max_return)
        return max(func(root))