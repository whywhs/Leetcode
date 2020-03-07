# 完全平方数。这是一个动态规划的题目。动态规划的关键在于while循环，对比当前值小的数进行完全平方，然后对比每一个完全平方数所需要的次数，取最小的。
# 这里也有一个定理，就是任何一个正整数都可以表示成四个整数的平方和。根据这个定理也可以有别的写法但是感觉不如这个简单明了。
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = [i for i in range(n+1)]
        for i in range(len(result)):
            j=1
            while(i>=j*j):
                result[i] = min(result[i],result[i-j*j]+1)
                j = j+1
        return result[-1]
