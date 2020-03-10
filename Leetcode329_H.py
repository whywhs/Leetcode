# 矩阵中的最长递增路径。这个题目就是采用DFS来做的。通过DFS来计算每一个点所能够得到的最长递增路径。同时，为了节省时间，对（i，j）用dict进行记录
# 这里需要注意的是，[i,j]作为一个list是不能够作为dict的键，因为list是可以修改，不能够hash的。
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if matrix==[]:
            return 0
        len_x = len(matrix)
        len_y = len(matrix[0])
        result,dict_my = [],{}
        for i in range(len_x):
            for j in range(len_y):
                result.append(self.dfs(i,j,matrix,len_x,len_y,dict_my))
        return max(result)+1
    
    def find(self,x,y,len_x,len_y):
        result = []
        result1,result2,result3,result4 = [max(x-1,0),y],[min(x+1,len_x-1),y],[x,min(y+1,len_y-1)],[x,max(y-1,0)]
        for i in ([result1,result2,result3,result4]):
            if i!=[x,y]:
                result += [i]
        return result
                
    def dfs(self,i,j,matrix,len_x,len_y,dict_my):
        if (i,j) in dict_my:
            return dict_my[(i,j)]
        list_my = self.find(i,j,len_x,len_y)
        result = []
        for m in list_my:
            if matrix[i][j]<matrix[m[0]][m[1]]:
                result.append(self.dfs(m[0],m[1],matrix,len_x,len_y,dict_my)+1)
        if result!=[]:
            dict_my[(i,j)] = max(result)
            return max(result)
        return 0
