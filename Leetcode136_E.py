# 只出现一次的数字。这个题目也算是一个标志性的题目了，就是采用异或算法来做。将数组内的所有元素异或一遍，最后的结果就是只出现一次的数字。
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = nums[0]
        for i in nums[1:]:
            a = a^i
        return a
