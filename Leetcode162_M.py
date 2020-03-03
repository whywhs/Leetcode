# 寻找峰值。这个题目要求以log(N)的时间复杂度进行，而很容易想到的思路肯定是遍历，这个是O(N)的，不符合要求
# 符合要求的解法是，先找序列的中值，如果中值比两边的都大，那么就返回中值的index.如果中值比左边的小，说明在0到中值的index这之间一定存在极值，原因在于-1
# 代表的是-inf，所以就算是一直在递增，那么nums[0]也一定满足要求。同理对右边的也一样。

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1 or nums[0]>nums[1]:
            return 0 
        if nums[-1]>nums[-2]:
            return len(nums)-1
        
        l,r = 0,len(nums)-1
        while(l<r):
            mid = l+(r-l)//2
            if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return mid
            if nums[mid]<nums[mid+1]:
                l = mid
            else:
                r = mid
                
        return mid

