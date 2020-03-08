# 零钱兑换。动态规划经典题目。和之前那个完全平方数是基本上一样的题目。都是通过一个for循环或者while循环来对所有可能出现的情况进行判断。
# 然后通过比较min(dp[i],dp[i]...)等操作来找到最优解。
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount<=0:
            return 0
        result = [-1]*(amount+1)
        result[0] = 0
        for i in range(1,amount+1):
            for j in coins:
                if i>=j and result[i-j]!=-1:
                    if result[i]==-1:
                        result[i] = result[i-j]+1
                    else:
                        result[i] = min(result[i],result[i-j]+1)
        return result[-1]
