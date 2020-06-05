# 这个是最优解法。时间O(N)空间O(1)。具体的解法就是首先定义输出数组res，res[0]=1。然后对输出数组进行前向类乘，得到前向的乘积
# res[i]=res[i-1]*nums[i-1]，第一项为1的目的是我们不需要整个数组的乘积。
# 再对输出数组进行后向类乘，得到最终结果。注意后向类乘的R首先定义为1，然后res[-i-1] = res[-i-1]*R
# 之后，再对R进行更新，R=R*nums[-i-1],得到下一个R
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0]*len(nums)
        res[0]=1
        for i in range(1,len(nums)):
            res[i] = res[i-1]*nums[i-1]
        R = 1
        for i in range(len(nums)):
            res[-i-1] = res[-i-1]*R
            R *= nums[-i-1]
        return res

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

#这个做法是标准的做法。用两个list来分别存储nums中前向和后向的乘积。则结果即前向的[i-1]与后向的[i+1]的乘积。
#边界条件需要进行考虑。
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        before = []
        last = []
        be=1
        la=1
        for i in nums:
            be = be*i
            before.append(be)
        
        for j in nums[::-1]:
            la = la*j
            last.append(la)
        last = last[::-1]
        
        result=[]
        for k in range(len(nums)):
            if k-1<0:
                result.append(last[k+1])
            elif k+1==len(nums):
                result.append(before[k-1])
            else:
                result.append(last[k+1]*before[k-1])
        return result
