# 数组中的逆序对。这个题目首先想到的肯定是暴力解法，很简单但是过不去测试样例。
# 这个题目简单的做法就是采用了归并排序的思想，思路就是对于归并出来的子序列来说，当后面的序列有小于前面序列的数，即在循环j中，那么一定有一个逆序对。
# 分别统计每一步逆序中的对，就可以得到总的数。
class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res,count = self.func(nums)
        return count

    def func(self,nums):
        if len(nums)<=1:
            return nums,0
        mid = len(nums)//2
        left,count_l = self.func(nums[:mid])
        right,count_r = self.func(nums[mid:])
        i,j = 0,0
        res = []
        while(i<len(left) and j<len(right)):
            while(i<len(left) and j<len(right) and left[i]<=right[j]):
                res.append(left[i])
                i += 1
            while(i<len(left) and j<len(right) and left[i]>right[j]):
                res.append(right[j])
                j += 1
                count_l += len(left)-i
        res += left[i:]
        res += right[j:]
        return res,count_l+count_r