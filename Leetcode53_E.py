# 最大子序和。这个题目是一个典型的动态规划题目，但是这个动态规划求的不是最后一位是当前的最大值，而是最后求res中的最大值。
# 因为求的是连续子序列，那么对于前面和为负数的，就直接让本次的数加入。对于前面正数的就让当前与前面的加入，最后求max(res)即可。
# 除了这个方法之外，还可以采用分治思想。但这个分治和题解中的不一样，这个复杂度依然是O(n)。即对左半部分求最大，再对右半部分求最大，
# 再对中间求最大。

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # DP
        # res = [0]*len(nums)
        # res[0] = nums[0]
        # for i in range(1,len(nums)):
        #     if res[i-1]<0:
        #         res[i] = nums[i]
        #     else:
        #         res[i] = nums[i]+res[i-1]
        # return max(res)

        # 分治
        if len(nums)==1:
            return nums[0]

        mid = len(nums)//2
        left = nums[:mid]
        right = nums[mid:]
        left_sum = self.maxSubArray(left)
        right_sum = self.maxSubArray(right)
        mid_left,mid_right = self.mid(left[::-1]),self.mid(right)
        mid_sum = max(mid_left,mid_right,mid_left+mid_right)
        return max(left_sum,right_sum,mid_sum)

    def mid(self,nums):
        sum_all = nums[0]
        max_all = nums[0]
        for i in nums[1:]:
            sum_all += i
            if sum_all>max_all:
                max_all = sum_all
        return max_all