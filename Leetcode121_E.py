# 买卖股票的最佳时间。这个题目是个简单的题目，就是一个标准的动态规划，结果等于上一时刻与本时刻所可以取得的最大值之间的最大值。
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<2:
            return 0
        result = [0]*len(prices)
        for i in range(1,len(result)):
            result[i] = max(result[i-1],prices[i]-min(prices[:i]))
        return result[-1]