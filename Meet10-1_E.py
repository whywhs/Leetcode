# 斐波那契数列。这个题目就是经典题目，可以用递归，可以用动态规划。
# 这里注意一点，求余数的操作只能针对于整数，如果对小数的话有可能出错。尤其当取余的数很大时。
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        a,b = 0,1
        for i in range(n):
            a,b = b,a+b
        return a %int((+1E+9+7))


    #     dict_all = {}
    #     result = self.func(n,dict_all)
    #     return int(result)


    # def func(self,N,dict_all):
    #     if N in dict_all:
    #         return dict_all[N]

    #     if N==0:
    #         return 0
    #     if N==1:
    #         return 1
        
    #     dict_all[N-1] = self.func(N-1,dict_all)
    #     dict_all[N-2] = self.func(N-2,dict_all)

    #     return (dict_all[N-1]+dict_all[N-2])%(+1E+9+7)