# 回文数。 这个题目可以直接用str来判断，但是还有更好的方法。对一半的数字进行旋转，如果数字长度是奇数位，那么一半的数字
# 就除以10之后与原始相比，如果偶数那就直接相比。这样可以避免溢出。但是要注意几个边界条件，一个是带0的除了0其它都是False
# 另一个是负数全部False。
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x%10==0 and x!=0) or x<0: return False
        r = 0
        while(r<x):
            right = x%10
            r = r*10+right
            x = x//10
        return r//10==x if r>x else r==x