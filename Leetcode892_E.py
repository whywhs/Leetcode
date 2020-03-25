# 题目懂了之后，就感觉还是好想出来的，代码如下： 对grid进行遍历，计算每一个遍历到的立方体面积，
# 注意表面积要加上底部的面。然后对该index的右和下方进行查看，如果有立方体，则count加上两个部分最小的高度*1，
# 即两块的重叠面积。直到遍历结束，拿总面积减去重叠的count，count要*2，因为一重叠就少了两个面
class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid==[] or grid==[[]]:
            return 0
        len_x,len_y = len(grid),len(grid[0])
        result,count = 0,0
        for i in range(len_x):
            for j in range(len_y):
                if grid[i][j]==0:
                    continue
                result += 4*grid[i][j]+2
                if i+1<len_x and grid[i+1][j]!=0:
                    count += min(grid[i][j],grid[i+1][j])
                if j+1<len_y and grid[i][j+1]!=0:
                    count += min(grid[i][j],grid[i][j+1])

        return result-count*2