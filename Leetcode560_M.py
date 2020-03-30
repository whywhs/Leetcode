# 和为k的子数组。这个题目使用了连续子数组和的做法。即对数组进行连续求和，每一个index之前的和均保存在dict中。
# 当sum_now-k存在于dict中时，说明以sum_now-k的index为基准到当前index可以构成一个符合条件的数组，然后count累加在这之前的
# 所有数组即可。初始的{0:1}代表的即当前值==k的情况。
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