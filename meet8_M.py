# 硬币。这个题目是一个背包问题，可以通过一维和二维数组来解决。
# 二维数组一维是coin，另外一维是钱数。对于二维数组来说，当前res[i][j]的结果代表的是使用到coin[i]位置的钱数来组成金额j的数量。
# 那么res[i][j] = res[i-1][j]+res[i][j-coin[i]]
# 如果采用一维数组来解决问题，那么就相当于是一个循环遍历。外层是当前所采用的钱数，内层是只采用当前钱数所能够完成的数量。
# 例如外层是1，那么内层代表的就是全部采用硬币为1来完成所有的金额。如果外层是n，那么内层代表的就是全部采用n来完成所有的金额。
# 则通过外层的for循环，res将不断累加。
class Solution(object):
    def waysToChange(self, n):
        """
        :type n: int
        :rtype: int
        """
        coin = [1,5,10,25]
        res = [0]*(n+1)
        res[0] = 1
        for i in range(4):
            for j in range(coin[i],n+1):
                res[j] += res[j-coin[i]]
        return res[-1]%1000000007
        # coin = [1,5,10,25]
        # res = [[1 for i in range(4)] for j in range(n+1)]
        # for i in range(1,n+1):
        #     for j in range(1,4):
        #         if i-coin[j]>=0:
        #             res[i][j] = res[i][j-1] + res[i-coin[j]][j]
        #         else:
        #             res[i][j] = res[i][j-1]
        # return res[-1][-1]%1000000007