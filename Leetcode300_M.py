# 最长上升子序列。这个题目可以用动态规划，也可以用二分法来解决。主要的解题思路是:
# 动态规划，就是维护一个result，该result的结果均是以当前index为结束的最长子序列。所以，两个循环，外层即数组的检索，内层即对index之内的数进行统计。
# 做法与经典的动态规划一样，max(result[i],result[j]+1)
# 二分法，当当前index大于result末尾时，result直接append。当当前index小于result末尾时，用二分法来进行查找，找到插入位置，对插入位置的数进行替换，
# 最后，result即为结果。返回len即可。
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#         if nums==[]:
#             return 0
        
#         result = [1]*len(nums)
#         for i in range(1,len(result)):
#             for j in range(i):
#                 if nums[i]>nums[j]:
#                     result[i] = max(result[i],result[j]+1)
#         return max(result)

        if len(nums)<2:
            return len(nums)
        
        result = [nums[0]]
        for i in range(1,len(nums)):
            if nums[i]>result[-1]:
                result.append(nums[i])
            elif nums[i]<result[-1]:
                left,right = 0,len(result)-1
                while(left<right):
                    mid = left+(right-left)//2
                    if nums[i]>result[mid]:
                        left = mid+1
                    else:
                        right = mid
                result[left] = nums[i]
        return len(result)
