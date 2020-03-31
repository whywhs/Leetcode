# 下一个排列。这个题目相当于要进行判断，找到当前index比前一个index大的地方为止，然后进行排序并与前一个index交换。
# 一开始对于后面的排序我用的是快排，但由于后面的序列一定是一个降序排列的，所以只需要反转即可。
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums)<2:
            return 
        if len(nums)==2:
            nums[0],nums[1] = nums[1],nums[0]
            return 
        
        len_n,i,flag = len(nums),1,0
        while(i<len_n):
            if nums[-i]<=nums[-i-1]:
                i = i+1
                continue
            flag = 1
            break
            
        if flag==0:
            self.reverse(nums,0,len_n-1)
        else:
            start,end = len_n-i,len_n-1
            self.reverse(nums,start,end)
            j = start
            while(nums[start-1]>=nums[j]):
                j = j+1
            nums[start-1],nums[j] = nums[j],nums[start-1]
    
    def reverse(self,nums,start,end):
        sub = nums[start:end+1][::-1]
        for i in range(start,end+1):
            nums[i] = sub[i-start]