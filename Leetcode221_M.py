# 最大正方形。这个题目有两个解法。简单的解法是采用DP来做的。DP是维护了一个当前角标下，最长的正方形边长。
# DP的公式就是，当前为1的情况下，当前res的值，是周围三个res值最小的加一。当前如果为0，那么res为0。最后统计最大的边长即可知道面积。
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix==[] or matrix==[[]]:
            return 0
        max_l = 0
        res = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i==0 or j==0:
                    res[i][j] = 1 if matrix[i][j]=='1' else 0
                    if res[i][j]>max_l:
                        max_l = res[i][j]
                    continue
                if matrix[i][j] == '1':
                    res[i][j] = min(res[i-1][j],res[i][j-1],res[i-1][j-1])+1
                    if res[i][j]>max_l:
                        max_l = res[i][j]
                else:
                    res[i][j] = 0
        return max_l**2



# 这个是暴力解法，即维护了一个judge函数，来判断当前的1可以组成的最大的一个正方形。相当于是一个边一个边的来进行查找。如果该边全部都是1
# 说明正方形边长加1.

    #     if matrix==[] or matrix==[[]]:
    #         return 0
    #     min_size,l = 0,0
    #     len_x,len_y = len(matrix[0]),len(matrix)
    #     for i in range(len_x):
    #         if i+l>=len_x:
    #             break
    #         for j in range(len_y):
    #             if j+l>=len_y:
    #                 break 
    #             if matrix[j][i]=='1':
    #                 size = self.judge(i,j,matrix,len_x,len_y)
    #                 if size>min_size:
    #                     min_size = size
    #                     l = min_size**0.5
    #     return min_size
    #     # print(self.judge(0,1,matrix,4,5))

    # def judge(self,i,j,matrix,len_x,len_y):
    #     min_size,l = 1,1
    #     s_i,s_j = i,j
    #     while(i+1<len_x and j+1<len_y and matrix[s_j][i+1]=='1' and matrix[j+1][s_i]=='1'):
    #         l = l+1
    #         for m in range(1,l):
    #             if matrix[j+1][s_i+m]!='1' or matrix[s_j+m][i+1]!='1':
    #                 return (l-1)**2
    #         i,j = i+1,j+1
    #         min_size = l*l
    #     return min_size   