class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s=='':
            return -1
        count = {}
        for i in range(len(s)):
            if count.has_key(s[i]):
                continue
            s_count = s.count(s[i])
            if s_count==1:
                return i
            count[s[i]] = s_count
        return -1
