# 将str1和str2相加，然后进行索引。当 len % index 为0时，就来判断是否满足条件。时间复杂度O(N)，感觉还是比较好理解的。
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        len_s1,len_s2 = len(str1),len(str2)
        len_min = min(len_s1,len_s2)
        str_all = str1+str2
        len_s = len_s1+len_s2
        for i in range(1,len_s+1):
            if len_s%i==0:
                k = len_s/i
                if k<=len_min and len_s1%k==0:
                    rep = str_all[:k]
                    if rep*i==str_all:
                        return rep
        return ""
