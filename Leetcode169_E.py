class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_n = len(nums)
        long_n = int(len_n/2)+1
        list_nums = {}
        for i in nums:
            if i in list_nums:
                count_i = list_nums[i]
            else:
                count_i =  nums.count(i)
                list_nums[i]=count_i
            if count_i>=long_n:
                return i
