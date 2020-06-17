# 最佳观景组合。这个题目求的解是A[i]+A[j]+i-j，首先应该进行形式的变换，把解变成A[i]+i+A[j]-j的形式。其中A[j]-j对于一个循环来说，是
# 固定的，关键就在于找到该循环前的max(A[i]+i)。对于A[i]+i来说，就相当于记录之前遍历的最大值即可，最后叠加到A[j]-j。这是O(N)的解法。
# 对于这种结果带式子的，一定一定要记住能不能先化简一下，往往经过化简之后就比较容易解出来了。
class Solution(object):
    def maxScoreSightseeingPair(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        max_sub,res = A[0],A[0]+A[1]-1
        for i in range(2,len(A)):
            now = A[i]-i
            if A[i-1]+i-1>max_sub:
                max_sub = A[i-1]+i-1
            max_now = max_sub + now
            if max_now>res:
                res = max_now
        return res