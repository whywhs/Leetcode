#对于这个题目来说，最简单的方法肯定是全部连乘，然后再分别除以各自的数。
#但是题目中要求不能使用除法，故下面采用的是一个移位的做法。将nums中的数分别一位一位的向前移动，并保留移动后的数组。
#接着对数组的第一列进行连乘，即得到除自身外的连乘积。但是，该做法空间上没有办法通过测试。
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        import numpy
        
        def trans(nums):
            return nums[1:]+[nums[0]]
        
        def multi(a,list_b):
            for i in list_b:
                a = a*i
            return a 
        
        if len(nums)==2:
            return [nums[1]]+[nums[0]]
        result=[]
        for i in range(len(nums)-2):
            nums = trans(nums)
            result.append(nums)
        result = numpy.array(result)
        nums=trans(nums)
        nums=trans(nums)
        
        result_all = []
        for j in range(len(nums)):
            a = nums[j]
            list_b = list(result[:,j])
            result_all.append(multi(a,list_b))
            
        return result_all[1:]+[result_all[0]]
