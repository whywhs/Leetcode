# 和为k的子数组。这个题目使用了连续子数组和的做法。即对数组进行连续求和，每一个index之前的和均保存在dict中。
# 当sum_now-k存在于dict中时，说明以sum_now-k的index为基准到当前index可以构成一个符合条件的数组，然后count累加在这之前的
# 所有数组即可。初始的{0:1}代表的即当前值==k的情况。

# 更正下，为什么可以采用连续数组和的形式进行count的计算，原因在于：1、对于当前下标i的数组和来说，sum_all代表了nums[:i]的和
# 对于任意j，j<i的下标来说，num[:j]代表了到j的和，也即是在i之前所计算的连续和之一。那么nums[:i]-nums[:j]即代表了从j到i的子数组
# 和。如果这个=k，说明count+1. 即当sum_all-nums[:j]==k，也即是sum_all-k==nums[:j]，而每个nums[:j]即存储在dict_r中。
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dict_r = {0:1}
        count = 0
        len_n,sum_now = len(nums),0
        for i in range(len_n):
            sum_now += nums[i]
            if sum_now - k in dict_r:
                count += dict_r[sum_now-k]
            dict_r[sum_now] = dict_r.setdefault(sum_now,0)+1

        return count