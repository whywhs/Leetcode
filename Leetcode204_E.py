# 计算质数。这个题目算是经典的题目了，方法主要就是在(2,sqrt(n))之间进行搜索。为什么要在sqrt(n)之内进行搜索的原因在于，如果一个数可以不拆
# 分到sqrt(n)之内的话，那么这个数最小的就是sqrt(n)*sqrt(n)=n，所以这个是与n以内是相悖的。故只需要对sqrt(n)之内的所有质数进行求倍数即
# 可。那么最后的结果就是对res求和。
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2:
            return 0
        res = [1]*n
        res[0],res[1] = 0,0
        num = int(n**0.5)
        for i in range(2,num+1):
            if res[i]==0:
                continue
            k = 2
            while(i*k<n):
                res[i*k] = 0
                k += 1
        return sum(res)