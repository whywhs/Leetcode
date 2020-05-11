# 缺失的第一个正数。这个题目主要做法如下：
# 1、判断1是否在数组中。 2、将数组中小于1的以及大于len(n)的，都变为1.关键的地方就在于右边界，是大于len(n)，因为对于长len(n)的数组
# 最大的就是len(n)。 3、此时数组中一定没有了负数，那么将数组中的i，这里应该取绝对值，因为有可能被前面的数加上了负号。然后将nums[i]变成
# 负数。 4、从头检索数组，找到第一个正数，注意是从1开始检索，如果都为-，那么判断nums[0],因为nums[0]中存的是len(n)的情况。如果全部都是
# 负的，那么就返回len(n)+1.
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if 1 not in nums:
            return 1
        
        len_n = len(nums)
        for i in range(len_n):
            if nums[i]<=0 or nums[i]>=len_n+1:
                nums[i] = 1
        
        for i in range(len_n):
            a = abs(nums[i])
            if a==len_n:
                nums[0] = -abs(nums[0])
            else:
                nums[a] = -abs(nums[a])
        
        for i in range(1,len_n):
            if nums[i]>0:
                return i
                
        return len_n if nums[0]>0 else len_n+1