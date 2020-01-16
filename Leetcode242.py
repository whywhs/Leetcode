#通过count来计算字符的个数，并通过一个字典保存计算过的字符来节省时间
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        count = {}
        for i in s:
            if count.has_key(i):
                continue
            s_count = s.count(i)
            t_count = t.count(i)
            if s_count != t_count:
                return False
            count[i] = s_count
        
        return True
