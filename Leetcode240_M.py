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
