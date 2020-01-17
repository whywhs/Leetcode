#使用了三次反转法，即先将整个序列进行反转，再对前一部分（k%len(nums)，因为k旋转的次数多了，可能会反复旋转多次，即旋转3次和旋转1次是一样
#的效果，对于长度为2的list来说）进行反转，最后对后一部分进行反转
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def reverse(nums,start,end):
            len_nums = end-start
            len_range = int(len_nums/2)
            for i in range(start,start+len_range):
                tmp = nums[i]
                nums[i] = nums[len_nums-i-1+2*start]
                nums[len_nums-i-1+2*start] = tmp
        
        if nums!=[] and len(nums)!=1:
            k = k%len(nums)
            reverse(nums,0,len(nums))
            reverse(nums,0,k)
            reverse(nums,k,len(nums))
