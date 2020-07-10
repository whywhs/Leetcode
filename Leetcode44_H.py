# 通配符匹配。这个和前面的正则表达式那一个题目很像。但这里的*是匹配任意字符的，不需要考虑之前的字符。这个题目就相对容易一些。当然也是可以采用之前
# 那个的做法，但是时间复杂度太高过不了。这里采用的就是一个二维的DP，注意边界条件。
# 简单的边界条件就是直接将空字符也算上，那么直接res[0][0]=1即可，只需要判断的就是当j=0使，这个时候就很简单了。
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        res = [[0 for i in range(len(s)+1)] for j in range(len(p)+1)]
        res[0][0] = 1
        for i in range(1,len(p)+1):
            for j in range(len(s)+1):
                if j==0:
                    if p[i-1]=='*':
                        res[i][j] = res[i-1][j]
                    continue
                if p[i-1]=='*':
                    res[i][j] = res[i-1][j] or res[i][j-1]
                elif p[i-1]=='?':
                    res[i][j] = res[i-1][j-1]
                else:
                    res[i][j] = res[i-1][j-1] if p[i-1]==s[j-1] else 0
        return res[-1][-1]==1