# 买卖股票最佳时机III. 允许的操作次数是两次，在这个里面用到了一个三维的DP数组，分别记录的是
# 天数、当前剩余操作次数、当前是否持有的状态。 那么对于这三种状态进行操作，转移方程还是比较好理解的。
# 问题在于两个地方，一个是DP数组的构建，一个是边界条件的确定。
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2: return 0
        dp = [[[0,0] for i in range(3)] for j in range(len(prices))]
        for i in range(len(prices)):
            for j in [2,1]:
                if i==0:
                    dp[i][j][0] = 0
                    dp[i][j][1] = -prices[i] 
                    continue
                dp[i][j][0] = max(dp[i-1][j][0],dp[i-1][j][1]+prices[i])
                dp[i][j][1] = max(dp[i-1][j][1],dp[i-1][j-1][0]-prices[i])
        return dp[-1][-1][0]