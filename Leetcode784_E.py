# 字母大小写全排列。 这个题目其实简单的方法就是只需要遍历就好，不用递归。
# 遍历的话，就相当于查到有大小写，就变换为小大写，然后result再append上每一个变换过的S即可。
# 再次记录，求ascii是ord()，求字符串是chr()。
# 然后python中字符串还有"isdigit()","isupper","islower()"来判断数字，大写，小写。
# 通过x.upper()，x.lower()返回该字符的大写或小写。
class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        
        num = ord('a')-ord('A')
        result = [S]
        for i in range(len(S)):
            if S[i]>='a' and S[i]<='z':
                now = chr(ord(S[i])-num)
                #result.append(S[:i]+now+S[i+1:])
            elif S[i]>='A' and S[i]<='Z':
                now = chr(ord(S[i])+num)
            else:
                continue
            len_r = len(result)
            for j in range(len_r):
                result.append(result[j][:i]+now+result[j][i+1:])
        return result