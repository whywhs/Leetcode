# 排序数组。这个就是一个快排，需要记录快排算法。
class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.quicksort(0,len(nums)-1,nums)
        return nums

    def quicksort(self,start,end,nums):
        if start<end:
            m,n = start,end
            now = nums[m]
            while(m<n):
                while(m<n and nums[n]>=now):
                    n -= 1
                nums[m] = nums[n]
                while(m<n and nums[m]<=now):
                    m += 1
                nums[n] = nums[m]
            nums[n] = now
            self.quicksort(start,n-1,nums)
            self.quicksort(n+1,end,nums)