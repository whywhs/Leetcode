# 地图分析。这个题目主要是理解题意。做法采用了多源BFS，即对所有的1首先记录位置。然后以该位置为基础，对每一个1进行四周扩散。
# 如果发现1的周围有1或周围的坐标已经被别的点经过，那么久continue,则最后一次还有未经过的点即离陆地最小的点且在所有陆地中，该点
# 距离最大。
class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        land,dict_my = [],{}
        len_x,len_y = len(grid),len(grid[0])
        for i in range(len_x):
            for j in range(len_y):
                if grid[i][j] == 1:
                    land.append((i,j))
                    dict_my[(i,j)] = 1
        if len(dict_my)==0 or len(dict_my)==len_x*len_y:
            return -1
        
        count = -1
        while(land!=[]):
            count += 1
            sub = []
            for i in land:
                x,y = i
                left = (x,max(y-1,0))
                right = (x,min(y+1,len_y-1))
                up = (min(x+1,len_x-1),y)
                down = (max(x-1,0),y)
                for j in [left,right,up,down]:
                    if j in dict_my or grid[j[0]][j[1]]==1:
                        continue
                    dict_my[j] = 1
                    sub.append(j)
            land = sub
        return count