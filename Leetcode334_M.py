#递增的三元子序列，要求空间复杂度O(1).做法即通过两个标记a,b.初始值分别设定为最大值。
#对nums进行索引，则当索引到一个小于a的数，就将a标记为该数。继续索引，当索引到一个大于a，且小于b的数，就将b标记为该数。则此时就完成了一个递增的二元子序列。
#在进行索引的过程中，还要对a,b进行更新。即当a和b有更小的值，就将其进行更新。
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
