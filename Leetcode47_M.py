# 全排列II。用dict来记录算过的全排列，可以节省时间。同时，在append的时候，也可以再维护一个dict，来记录当前dict是否有重复。
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        dict_all ={}
        return self.func(nums,dict_all)

    def func(self,nums,dict_all):
        dict_sub = {}
        len_n = len(nums)
        if len_n <= 1:
            return [nums]
        result = []
        for i in range(len_n):
            sub = nums[:i]+nums[i+1:]
            if tuple(sub) not in dict_all:
                dict_all[tuple(sub)] = self.func(sub,dict_all)
            for j in dict_all[tuple(sub)]:
                now = [nums[i]]+j
                if tuple(now) in dict_sub:
                    continue
                result.append(now)
                dict_sub[tuple(now)] = 1
        dict_all[tuple(nums)] = result
        return result       