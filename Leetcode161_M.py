# 相隔为1的编辑距离。这个题目真折磨人。
class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        len_s,len_t = len(s),len(t)

        if len_s<len_t:
            return self.isOneEditDistance(t,s)

        if len_s-len_t>1:
            return False
        
        for i in range(len_t):
            if s[i]!=t[i]:
                if len_s==len_t:
                    return s[i+1:]==t[i+1:]
                else:
                    return s[i+1:]==t[i:]

        return len_t+1==len_s