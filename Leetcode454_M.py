#四数相加II。这个题就是将时间复杂度O(N^4)变为O(N^2)。需要注意的是dict的setdefault用法。
#dict.setdefault(i,default=x)，如果dict中包含i，那么就是返回dict[i]的值，如果dict中不包含i,则将dict[i]设置为default，并返回default。
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        dict_AB={}
        for i in A:
            for j in B:
                dict_AB[i+j]=dict_AB.setdefault(i+j,0)+1
        
        result = 0
        for i in C:
            for j in D:
                if -i-j in dict_AB:
                    result+=dict_AB[-i-j]
        return result
