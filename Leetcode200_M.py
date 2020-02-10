#岛屿问题。做法就是对于1来说，始终将与之相接触的1进行置0.那么，对于一个岛屿来讲，最后就只会剩下一个1.则统计数组中1的次数就好了。
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def find(i,j,len_i,len_j,dict_list):
            result_all =[]
            i_u = i-1
            i_d = i+1
            j_r = j+1
            j_l = j-1
            result = [[max(i_u,0),j],[min(i_d,len_i-1),j],[i,min(j_r,len_j-1)],[i,max(0,j_l)]]
            while([i,j] in result):
                result.remove([i,j])
            for m in result:
                if tuple(m) in dict_list:
                    result.remove(m)
            return result
        
        def judge(list_f,grid,dict_list):
            result=[]
            for i in list_f:
                if tuple(i) in dict_list:
                    continue
                dict_list[tuple(i)]=1
                num = int(grid[i[0]][i[1]])
                if num == 1:
                    grid[i[0]][i[1]]="0"
                    result.append([i[0],i[1]])
            return result
        
        if grid==[]:
            return 0
        dict_list = {}
        len_x = len(grid)
        len_y = len(grid[0])
        num_grid = 0
        for i in range(len_x):
            for j in range(len_y):
                num = int(grid[i][j])
                if (i,j) in dict_list or num==0:
                    continue
                dict_list[(i,j)]=1
                list_f = find(i,j,len_x,len_y,dict_list)
                result = judge(list_f,grid,dict_list)
                while(result!=[]):
                    result_all = []
                    for k in result:
                        list_f = find(k[0],k[1],len_x,len_y,dict_list)
                        result = judge(list_f,grid,dict_list)
                        result_all = result_all + result
                    result = result_all
                num_grid = num_grid+1
        return num_grid
