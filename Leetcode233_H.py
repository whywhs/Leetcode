# 数字 1 的个数. 这个题目统计1的个数用的方法很巧妙，是在每一位上统计该位上出现1的次数。
# 假如统计第2位上出现的1的个数。
# 如果第2位上的数字为0，例如3027，那么对应于第二位上取1的范围就是0100-2199，即000-299，即 height*(10**k)
# 如果第2位上的数字为1，例如3127，那么对应于第二位上取1的范围就是0100-3127，即000-327，即 height*(10**k)+low+1
# 如果第2位上的数字为2-9，如果3527，那么对应于第二位上取1的范围就是0100-3199，即000-399，即 (height+1)*(10**k)
# 对于边界条件来说，当height或low为空时，就令height和low为0即可。

class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = str(n)
        count,k = 0,len(s)-1
        for i in range(len(s)):
            height,low = s[:i],s[i+1:]
            if height=='': height = 0
            if low=='': low = 0
            if int(s[i])==0:
                count += int(height)*(10**k)
            elif int(s[i])==1:
                count += int(height)*(10**k) + int(low) + 1
            else:
                count += (int(height)+1)*(10**k)
            k -= 1
        return count
