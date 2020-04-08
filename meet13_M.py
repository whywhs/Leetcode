# 机器人的运动范围。这个题目就是一个计算最大岛屿面积的题目。我先对不满足要求的点置0，相当于设置为了海洋。剩下的1就相当于是陆地。
# 这里记录下python的dict合并，是通过update，dict1.update(dict2)
# 做这种题目一定要考虑清楚，是否还需要两个for循环，是否可以只用一个while来进行。
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
        dict_all = {}
        for i in range(m):
            for j in range(n):
                now = str(i)+str(j)
                sum_sub = sum(map(int,now))
                if sum_sub>k:
                    result[i][j] = 0
        
        now,count,dict_all = [[0,0]],0,{}
        while(now!=[]):
            sub = now.pop()
            if tuple(sub) not in dict_all:
                dict_all[tuple(sub)] = 1
                around = self.find(sub[0],sub[1],m,n,dict_all,result)
                now += around
        count = len(dict_all)
        return count

    def find(self,x,y,len_x,len_y,dict_all,result_all):
        result = []
        a1 = [min(x+1,len_x-1),y]
        a2 = [x,min(y+1,len_y-1)]
        a3 = [max(x-1,0),y]
        a4 = [x,max(y-1,0)]
        for i in [a1,a2,a3,a4]:
            if i!=[x,y] and result_all[i[0]][i[1]]==1 and tuple(i) not in dict_all:
                result.append(i)
        return result