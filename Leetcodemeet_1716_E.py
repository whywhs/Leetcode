# 这个题目就是小偷偷东西的题目。这里希望记录的是下面的这个O(1)空间复杂度的解法。通过a,b来代替result[i-1]与result[i-2]
# 可以将result数组替换为常量空间。
class Solution(object):
    def massage(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if len(nums)==0:
        #     return 0
        # if len(nums)==1:
        #     return nums[0]
        # result = [0]*len(nums)
        # result[0] = nums[0]
        # result[1] = max(nums[0],nums[1])
        # for i in range(2,len(nums)):
        #     result[i] = max(result[i-1],result[i-2]+nums[i])
        # return result[-1]


        a,b,max_new = 0,0,0
        for i in range(len(nums)):
            max_new = max(a+nums[i],b)
            b,a = max_new,b
        return max_new