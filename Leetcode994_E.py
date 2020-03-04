# 腐烂的橘子。这个题目就是一个遍历问题，和之前的岛屿比较类似，但是是统计次数的。需要注意的就是一开始的所有腐烂的橘子是同时开始腐烂的，而不是一个一个。
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        que = []
        len_x,len_y = len(grid),len(grid[0])
        for i in range(len_x):
            for j in range(len_y):
                if grid[i][j]==2:
                    que.append([i,j])

        count = 0
        while(1):
            sub = []
            for n in que:
                list_my = self.find(n,len_x,len_y)
                for m in list_my:
                    if grid[m[0]][m[1]]==1:
                        grid[m[0]][m[1]]=2
                        sub.append(m)
            if sub==[]:break
            que=sub
            count+=1
        
        for i in range(len_x):
            for j in range(len_y):
                if grid[i][j]==1:
                    return -1 
        return count

    def find(self,x,len_x,len_y):
        result=[]
        i,j = x[0],x[1]
        result+=[[i,j+1]] if j+1<len_y else[]
        result+=[[i,j-1]] if j-1>=0 else[]
        result+=[[i+1,j]] if i+1<len_x else[]
        result+=[[i-1,j]] if i-1>=0 else[]
        return result
