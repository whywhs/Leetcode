# 不同路径。一个典型的二维动态规划题目，就维护一个二维数组，然后i,j等于i-2,j和i,j-1的和。如果超过边界就进行讨论。
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        result = [[0 for i in range(m)] for j in range(n)]
        for i in range(n):
            for j in range(m):
                if i==0 and j==0:
                    result[i][j] = 1
                    continue
                if i-1>=0 and j-1>=0:
                    result[i][j] = result[i-1][j]+result[i][j-1]
                else:
                    result[i][j] = result[i-1][j] if i-1>=0 else result[i][j-1]
        return result[-1][-1]
