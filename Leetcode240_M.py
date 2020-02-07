#对于这种数组本身已经排列好的，很方便的一个方法就是从右上角开始。如果target比start小，则向左移动，因为下方一列肯定是都大的。
#如果target比start大，则向下移动，因为左边这一行肯定都是小的。
#所以，当满足边界条件时就可以输出False，如果途中查到就输出True.
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix==[]:
            return False
        len_x = len(matrix)
        len_y = len(matrix[0])
        x = 0
        y = len_y-1
        while(y>=0 and x<len_x):
            start = matrix[x][y]
            if start>target:
                y = y-1
            elif start<target:
                x = x+1
            else:
                return True
        return False
