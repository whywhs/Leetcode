# 01矩阵。对于这种二维矩阵的题目应该记录一下，之前的那种写法会有些麻烦，要学会这种较为简单的写法。
# 这个题目的思路即找0，然后以0为中心向四周扩散，一次加一。由于用的是原数组，故不需要开辟新的空间。
class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        len_x,len_y = len(matrix),len(matrix[0])
        res,dict_all = [],{}
        for i in range(len_x):
            for j in range(len_y):
                if matrix[i][j] == 0:
                    res.append((i,j))
                    dict_all[(i,j)] = 1
        
        while(res):
            i,j = res.pop(0)
            for x,y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                if x>=0 and x<len_x and y>=0 and y<len_y and (x,y) not in dict_all:
                    matrix[x][y] = matrix[i][j] + 1
                    dict_all[(x,y)] = 1
                    res.append((x,y))
        return matrix