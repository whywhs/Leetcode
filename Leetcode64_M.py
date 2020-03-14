# 最小路径和。与之前的是同样的题目，只是需要判断下上方和左方哪一个比较小即可。
lass Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid[0])
        n = len(grid)
        result = [[0 for i in range(m)] for j in range(n)]
        for i in range(n):
            for j in range(m):
                if i==0 and j==0:
                    result[i][j] = grid[0][0]
                    continue
                if i-1>=0 and j-1>=0:
                    result[i][j] = min(result[i-1][j],result[i][j-1])+grid[i][j]
                else:
                    result[i][j] = result[i-1][j]+grid[i][j] if i-1>=0 else result[i][j-1]+grid[i][j]
        return result[-1][-1]
