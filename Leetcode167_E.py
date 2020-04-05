# 两数之和 II - 输入有序数组。 这个题目做法就是先对target求平均。那么对于数组numbers来说，如果和要为target，一定一个在小于
# 平均值的左边，一个在大于平均值的右边。那么这样的话，就可以通过一个{}来储存在右半部分需要查找的值。
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        mid = target/2.0
        result1 = {}
        for i in range(len(numbers)):
            if numbers[i] == mid:
                if numbers[i+1] == mid:
                    return [i+1,i+2]
            elif numbers[i]<mid:
                result1[target-numbers[i]] = i+1
            else:
                if numbers[i] in result1:
                    return [result1[numbers[i]],i+1]
