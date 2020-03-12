# Pow(x,n)。这个题目如果用常规的n-1来进行递归的话汇报错，说因为递归次数太多。
# 所以，使用二分来递归，就是每次递归它的一半，然后再平方，这样就没有错误了。
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0:
            return 1
        if n==1:
            return x
        flag = 0
        if n<0:
            n = -n
            flag = 1

        if n%2==0:
            ans = self.myPow(x,n/2)
            ans = ans*ans
        else:
            ans = self.myPow(x,n//2)
            ans = ans*ans*x

        return ans if flag==0 else 1/ans
