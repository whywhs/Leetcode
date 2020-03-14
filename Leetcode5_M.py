# 最长回文子串。这个题目用的是一个动态规划的算法。在满足s[i]==s[j]的前提下，我们来判断字符串是否是一个回文串。然后就又回到了标准的套路上。
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)<2:
            return s
        if len(set(s))==1:
            return s

        len_s = len(s)
        result = [1]*len_s
        max_sub,index = 1,0
        for i in range(len_s):
            for j in range(i):
                if s[i]==s[j]:
                    if s[j:i+1]==s[j:i+1][::-1]:
                        result[i] = max(result[i],i-j+1)
            if result[i]>max_sub:
                max_sub,index = result[i],i

        return s[index-max_sub+1:index+1]
