# 子集II。这个题目存在重复的数据，所以，在进行添加的时候要做去重。但是这里又牵扯到一个顺序的问题，所以进行了sort.
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = self.func(nums)
        return result+[[]]


    def func(self,nums):
        if len(nums)<2:
            return [nums]
        now = nums[-1]
        pre = self.func(nums[:len(nums)-1])
        len_p = len(pre)
        for i in range(len_p):
            flag = pre[i]+[now]
            flag.sort()
            if flag in pre:
                continue
            pre.append(flag)
        if [now] in pre:
            return pre
        return pre+[[now]]