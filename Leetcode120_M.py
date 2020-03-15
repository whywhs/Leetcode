# 三角形最小路径和。用了动态规划的算法，对每一个位置上都求了当前的最小，然后对最后一行再求最小即是所有的最小。这个题目我相当于用了dict来进行求解。
# 对于O(N)的做法，相当于每次只要维护前一层的数值即可。即每一次进行到下一层，就覆盖掉上一层保存的值。
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if triangle==[[]]:
            return 0
        dict_r = {}
        dict_r[0] = [triangle[0][0]]
        for i in range(1,len(triangle)):
            for j in range(len(triangle[i])):
                if j==0:
                    dict_r[i] = [dict_r[i-1][0]+triangle[i][j]]
                elif j+1==len(triangle[i]):
                    dict_r[i].append(dict_r[i-1][-1]+triangle[i][j])
                else:
                    dict_r[i].append(min(dict_r[i-1][j-1],dict_r[i-1][j])+triangle[i][j])
        
        return min(dict_r[len(triangle)-1])
