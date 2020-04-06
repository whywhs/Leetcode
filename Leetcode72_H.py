# 编辑距离。这个题目是一个二维的动态规划，我想的做法是没有加外面一行的，直接从第一行开始计算，这样代码上长一些。
# 之前用的标准的做法就是在外面包上一行，相当于考虑了一种情况就是一个为空时。外面的一行就是0,len_w1+1，这样第一行也会直接进行计算了
# 在这里需要注意的一点就是写[reuslt[0][i] if a else result[0][i-1]+1 for i in range(len_w1)]时，result[0][i-1]永远都
# 是最开始的初始值，他不会因为你在这个循环中改变而改变。


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if word1=="" or word2=="":
            return len(word1)+len(word2)
        len_w1,len_w2 = len(word1),len(word2)
        result = [[0]*len_w1 for i in range(len_w2)]
        result[0][0] = 0 if word1[0]==word2[0] else 1
        for i in range(1,len_w1):
            if word1[i] == word2[0]:
                result[0][i] = i
            else:
                result[0][i] = result[0][i-1]+1
        for j in range(1,len_w2):
            if word2[j] == word1[0]:
                result[j][0] = j
            else:
                result[j][0] = result[j-1][0]+1
        for i in range(1,len_w2):
            for j in range(1,len_w1):
                if word1[j] == word2[i]:
                    result[i][j] = result[i-1][j-1]
                else:
                    result[i][j] = min(result[i-1][j],result[i][j-1],result[i-1][j-1])+1
        return result[len_w2-1][len_w1-1]


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if word1=="" or word2=="":
            return len(word1)+len(word2)
        len_w1,len_w2 = len(word1),len(word2)
        result = [[i]*(len_w1+1) for i in range(len_w2+1)]
        result[0] = [i for i in range(len_w1+1)]
        for i in range(1,len_w2+1):
            for j in range(1,len_w1+1):
                if word1[j-1] == word2[i-1]:
                    result[i][j] = result[i-1][j-1]
                else:
                    result[i][j] = min(result[i-1][j],result[i][j-1],result[i-1][j-1])+1
        return result[len_w2][len_w1]