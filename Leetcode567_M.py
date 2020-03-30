# 字符串的排列。 这个题目就是一个滑动窗口的应用。对于我写的代码来说，是复杂了，因为相当于每一次都要从新的i开始重新遍历，这样会有
# 很多的重复计算。所以简便的方法就是，首先维护初始窗口。其次，固定窗口的大小为需要的大小，然后进行位移。位移的具体操作即后面多一个，
# 前面少一个，这样就可以保证窗口内大小一致。
from collections import Counter
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """       
        len_s1,len_s2 = len(s1),len(s2)
        dict_s1 = Counter(s1)
        dict_s2 = Counter(s2[:len_s1])
        if dict_s1 == dict_s2:
            return True
        i = 0
        j = len_s1
        while(j<len_s2):
            dict_s2[s2[i]] -=1
            if dict_s2[s2[i]] ==0:
                dict_s2.pop(s2[i])
            dict_s2[s2[j]] = dict_s2.setdefault(s2[j],0)+1
            if dict_s2==dict_s1:
                return True
            i += 1
            j += 1
        return False




        # dict_my = Counter(s1)
        # i,len_s1,len_s2 = 0,len(s1),len(s2)
        # dict_my1 = copy.deepcopy(dict_my)
        # while(i<len_s2):
        #     if s2[i] not in dict_my:
        #         i = i+1
        #         continue
        #     dict_my1 = copy.deepcopy(dict_my)
        #     j = i
        #     if j+len_s1>len_s2:
        #         break
        #     while(j<i+len_s1):
        #         if s2[j] not in dict_my1:
        #             break
        #         dict_my1[s2[j]] -= 1
        #         if dict_my1[s2[j]] == 0:
        #             dict_my1.pop(s2[j])
        #         if dict_my1 == {}:
        #             return True
        #         j = j+1
        #     i = i+1
        # return False