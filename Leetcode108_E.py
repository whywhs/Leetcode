# 将有序数组转换为平衡二叉搜索树。查找中点然后作为顶点，通过递归的方法来进行查询。
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums==[]:
            return nums
        root = self.func(nums)
        return root
           
    def func(self,nums):
        len_n = len(nums)
        if len_n==0:
            return None
        mid = len_n//2
        mid_node = TreeNode(nums[mid])
        nums_left,nums_right = nums[:mid],nums[mid+1:]
        mid_node.left = self.func(nums_left)
        mid_node.right = self.func(nums_right)
        return mid_node
