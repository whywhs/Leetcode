# 机器人的运动范围。这个题目就是一个计算最大岛屿面积的题目。我先对不满足要求的点置0，相当于设置为了海洋。剩下的1就相当于是陆地。
# 这里记录下python的dict合并，是通过update，dict1.update(dict2)
class Solution(object):
    def movingCount(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        if k==0:
            return 1
        result = [[1]*n for i in range(m)]
        count_max = 0 
        dict_all = {}
        for i in range(m):
            for j in range(n):
                now = str(i)+str(j)
                sum_sub = sum(map(int,now))
                if sum_sub>k:
                    result[i][j] = 0
        
        for i in range(m):
            for j in range(n):
                if result[i][j] == 1 and (i,j) not in dict_all:
                    now,dict_all = [[i,j]],{}
                    while(now!=[]):
                        sub = now.pop()
                        around = self.find(sub[0],sub[1],m,n,dict_all,result)
                        for k in around:
                            if result[k[0]][k[1]]==1:
                                now.append(k)
                    count = len(dict_all)
                    if count>count_max:
                        count_max = count
        return count_max

    def find(self,x,y,len_x,len_y,dict_all,result_all):
        result = []
        a1 = [min(x+1,len_x-1),y]
        a2 = [x,min(y+1,len_y-1)]
        a3 = [max(x-1,0),y]
        a4 = [x,max(y-1,0)]
        for i in [a1,a2,a3,a4]:
            if i!=[x,y] and result_all[i[0]][i[1]]==1 and tuple(i) not in dict_all:
                result.append(i)
                dict_all[tuple(i)]=1
        return result