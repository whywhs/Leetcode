class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        if len_nums > 1:
            i=0
            j=0
            while(i<len_nums):
                if nums[i]==0:
                    j = i
                    while(j<len_nums and nums[j]==0):
                        j = j+1
                    if j==len_nums:
                        break
                    nums[i]=nums[j]
                    nums[j]=0
                    i=i+1
                else:
                    i=i+1
