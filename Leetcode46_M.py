# 全排列。 这个用了递归来做，比较奇怪的一点就是我调用这个函数后，他会自动的返回[result]。
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)<=1:
            return [nums]

        result = []
        for i in range(len(nums)):
            re = self.permute(nums[:i]+nums[i+1:])
            for j in re:
                sub = [nums[i]]+j
                result.append(sub)
        return result