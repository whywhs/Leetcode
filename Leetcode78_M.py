# 子集。这个题目主要的思路点在于，对每一次的数组递归除最后一位外的其他位，然后将所有结果*2，一部分加上新的最后一位，另一部分不变
# 最后，在加上空集即可。
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        import copy
        result = self.func(nums)
        return result+[[]]

    def func(self,nums):
        if len(nums)<=1:
            return [nums]
            
        now = nums[-1]
        pre = self.func(nums[:len(nums)-1])
        pre_now = copy.deepcopy(pre)
        for i in pre_now:
            i += [now]
        return pre+pre_now+[[now]]