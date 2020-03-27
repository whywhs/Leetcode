# 丑数II。这个题目普通的方法没办法过，采用了一个动态规划的算法。相当于构建了三个数组，每个数组其实就是专门乘上2,5,3中的一个。
# 因为数组的index是递增的，所以，相当于所有的index都会过一遍。这个时间复杂度要比从1，n进行循环小很多，因为越到后面，间隔越大。
class Solution:
    def nthUglyNumber(self, n):
        result = [1]
        i,j,k = 0,0,0
        while(len(result)!=n):
            ugly_min = min(result[i]*2,result[j]*3,result[k]*5)
            result.append(ugly_min)
            if ugly_min == result[i]*2:
                i += 1
            if ugly_min == result[j]*3:
                j += 1
            if ugly_min == result[k]*5:
                k += 1
        return result[-1]