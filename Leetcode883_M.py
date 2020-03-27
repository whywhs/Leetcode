# 三维形体投影面积。这个题目就是求横轴的max+纵轴的max+所有数的和一起。
class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        len_x,len_y = len(grid),len(grid[0])
        dict_y,result_x,count_all = {},[],0
        for i in range(len_x):
            max_x = 0
            for j in range(len_y):
                now = grid[i][j]
                if now != 0:
                    count_all += 1
                    if j in dict_y:
                        dict_y[j] = max(dict_y[j],now)
                    else:
                        dict_y[j] = now
                    if now > max_x:
                        max_x = now
            result_x.append(max_x)
        result_y = sum([dict_y[i] for i in dict_y])
        return sum(result_x)+count_all+result_y