# 不同路径II. 和之前不同的地方在于路径中有障碍物，但其实做法上不用管他。只要检测到障碍物，那么就直接continue，这时障碍物这里就成了0.
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0]==1:
            return 0
        m = len(obstacleGrid[0])
        n = len(obstacleGrid)
        result = [[0 for i in range(m)] for j in range(n)]
        for i in range(n):
            for j in range(m):
                if i==0 and j==0:
                    result[i][j] = 1
                    continue
                if obstacleGrid[i][j]==1:
                    continue
                if i-1>=0 and j-1>=0:
                    result[i][j] = result[i-1][j]+result[i][j-1]
                else:
                    result[i][j] = result[i-1][j] if i-1>=0 else result[i][j-1]
        return result[-1][-1]
