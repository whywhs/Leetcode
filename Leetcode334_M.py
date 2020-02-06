class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)<3:
            return False
        a = max(nums)+1
        b = max(nums)+1
        for i in range(len(nums)):
            if nums[i]<a:
                a = nums[i]
            elif nums[i]>a:
                if nums[i]<b:
                    b = nums[i]
                elif nums[i]>b:
                    return True
        return False
