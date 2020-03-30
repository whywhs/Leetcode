# 连续的子数组和. 这个题目按照之前的做法，即维护一个sum，来代表到当前index所有数的和。
# 这里面需要注意的一个点就是，0的存在需要单独进行考虑。
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums)<2:
            return False
        if k==0:
            for i in range(len(nums)):
                if nums[i]==0:
                    if i+1!=len(nums) and nums[i+1]==0:
                        return True
            return False
        len_n = len(nums)
        sum_k = [0]*len_n
        sum_k[0] = nums[0]
        for i in range(1,len_n):
            sum_k[i] = sum_k[i-1]+nums[i]
            if sum_k[i]%k==0:
                return True
            for j in range(i-1):    
                if (sum_k[i]-sum_k[j])%k==0:
                    return True
        return False