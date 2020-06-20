# 正则表达式匹配。这个题目采用的是递归的做法。
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dict_my = {}
        def func(a,b):
            # dict_my是用来记忆匹配过的字符串，用来减少用时的。
            if (a,b) in dict_my:
                return dict_my[(a,b)]
            # 如果b是空，那么a空的时候，就是True，否则Fasle
            if not b: return not a
            # 判断first是否匹配成功。
            first = True if len(a)>0 and (b[0]==a[0] or b[0]=='.') else False
            # 如果b[1]==*，那么就是两种情况。第一是a和b[2:]进行，相当于是b[0,1]没有使用。另一种就是b[0,1]使用，然后匹配a[1:]
            if len(b)>1 and b[1]=='*':
                res = func(a,b[2:]) or (first and func(a[1:],b))
            # 如果b[1]!=*的话，那么就是看首字符是否匹配了，然后在对a[1:],b[1:]进行匹配。
            else:
                res = first and func(a[1:],b[1:])
            dict_my[(a,b)] = res
            return res
        return func(s,p)
        