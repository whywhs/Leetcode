# 跳跃游戏。 这个题目是可以用贪心算法来解决的。对数组进行遍历，每一个遍历到的位置，将其最大可以到的位置进行计算，不断更新这个位置
# 当这个最大位置大于数组的长度时，表明可以到达该位置。
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)==1:
            return True
        max_now,i = nums[0],0
        while(i<=max_now):
            if i+nums[i]>max_now:
                max_now = i+nums[i]
            i += 1
            if max_now>=len(nums)-1:
                return True
        return False