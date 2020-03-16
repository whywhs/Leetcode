# 字符串压缩。简单题，就是不要忘了在循环结束还需要加上末尾的。
class Solution(object):
    def compressString(self, S):
        """
        :type S: str
        :rtype: str
        """
        if len(S)<3:
            return S
        count,result = 1,""
        for i in range(1,len(S)):
            if S[i]==S[i-1]:
                count += 1
            else:
                a = S[i-1]+str(count)
                result += a
                count = 1

        a = S[-1]+str(count)
        result += a
        if len(result)>len(S):
            return S
        return result
