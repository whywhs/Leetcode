# 括号生成。这个题目是一个递归算法。思路就是在n-1的基础上，每一位后面加上一个括号即可，然后用dict来记录重复。
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dict_all = {}
        result = self.func(n,dict_all)
        return result

    def func(self,n,dict_all):
        if n==1:
            return ['()']
        sub = []
        result = self.func(n-1,dict_all)
        for i in result:
            for j in range(len(i)):
                now = i[:j]+'()'+i[j:]
                if now not in dict_all:
                    sub.append(i[:j]+'()'+i[j:])
                    dict_all[now] = 1
        return sub