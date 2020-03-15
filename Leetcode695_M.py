# 岛屿的最大面积。深度优先搜索算法和之前岛屿个数那个题目一样。
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid==[]:
            return 0
        count,c_max = 0,0
        len_x,len_y = len(grid),len(grid[0])
        for i in range(len_x):
            for j in range(len_y):
                if grid[i][j]==1:
                    grid[i][j],other = 2,[[i,j]]
                    count += 1
                    while(other!=[]):
                        m = other.pop()
                        m_other = self.find(m[0],m[1],len_x,len_y,grid)
                        count += len(m_other)
                        other += m_other
                    if count > c_max: c_max = count
                    count = 0
        return c_max

    def find(self,x,y,len_x,len_y,grid):
        result = []
        r1 = [max(x-1,0),y]
        r2 = [min(x+1,len_x-1),y]
        r3 = [x,max(y-1,0)]
        r4 = [x,min(y+1,len_y-1)]
        for i in [r1,r2,r3,r4]:
            if i!=[x,y] and grid[i[0]][i[1]]==1:
                grid[i[0]][i[1]] = 2
                result.append(i)
        return result
