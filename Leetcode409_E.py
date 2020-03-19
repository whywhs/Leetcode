# 最长回文串。这个题目就是需要统计偶数次的个数，但是注意的是对于奇数次的不是不统计而是减一即可。
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        for i in set(s):
            num = s.count(i)
            if num%2==0:
                l += num
            else:
                l += num-1
        if l>=len(s):
            return l
        return l+1