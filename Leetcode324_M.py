# 摆动排序II。这个题就是要注意放入数的顺序，小的和大的应该先从最大的开始放。而且，这种写法也应该学会。
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if nums!=[] and len(nums)!=1:
            nums.sort(reverse=True)
            len_m = len(nums)//2
            nums[::2],nums[1::2] = nums[len_m:],nums[:len_m]
            
#             for i in range(len(nums)):
#                 if i%2==0:
#                     nums[i] = list_small.pop(0)
#                 else:
#                     nums[i] = list_big.pop(0)
                                    
        

        
