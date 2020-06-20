# 数字的按位与。这个题目的求解思路是找m和n的公共前缀。公共前缀的部分即是最后保留的部分，其它部分经过与之后就都变成0了。
class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        m_b = bin(m)
        n_b = bin(n)
        if len(m_b)!=len(n_b):
            return 0
        else:
            m_b,flag = list(m_b),0
            for i in range(2,len(m_b)):
                if flag==0 and m_b[i]!=n_b[i]:
                    flag = 1
                if flag==1:
                    m_b[i] = '0'
            return int(''.join(m_b),2)