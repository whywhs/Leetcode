# 旋转图像及面试题中的旋转矩阵。这个题目很简单的一个思路就是，先对矩阵进行转置，再对转置后的矩阵每一行进行倒序。
# list中倒序可以用list.reverse()
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        for i in range(n):
            matrix[i] = matrix[i][::-1]