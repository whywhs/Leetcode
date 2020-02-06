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
