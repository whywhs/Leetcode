# 至少有K个重复字符的最长子串。这个题用了递归的做法。简单的说就是对字符串以统计字数小于K的字符来进行拆分。然后获取每一部分的最大值。
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if s=="":
            return 0
        result = []
        for i in set(s):
            if s.count(i)<k:
                result+= [self.longestSubstring(j,k) for j in s.split(i)]
                return max(result)
        return len(s)
