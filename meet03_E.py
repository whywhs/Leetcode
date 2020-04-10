# 数组中重复的数字。一个简单的桶排序。
class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = [0]*len(nums)
        for i in range(len(nums)):
            if result[nums[i]] == 1:
                return nums[i]
            result[nums[i]] += 1