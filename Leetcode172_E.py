# 阶乘后的0. 这个题目因为算的是阶乘，所以可以直接用/5来计算其中能够被5整除的数。
# 20！ 1*2*3*4*5*6*7*8*9*10*11*12*13*14*15*16*17*18*19*20
# 20/5 = 4说明20！中有4个是5的倍数，那么肯定有4个5。就这样反复除，直到不能够除尽，就得到了结果。

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while(n>=5):
            count += int(n/5)
            n = int(n/5)
            
        return count
