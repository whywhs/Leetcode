# 找到字符串中所有字母异位词。这个题目也是滑动窗口的题目，和之前那个做法很像，维护两个dict，另一个dict在滑动。然后分别和dict进行
# 比较，如果相等就把index加入。 发现一个问题就是Counter算法相比于遍历加入dict要慢。
#from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        result = []
        len_p,len_s = len(p),len(s)
        dict_p,dict_s = {},{}
        for i in p:
            dict_p[i] = dict_p.setdefault(i,0)+1
        for i in s[:len_p]:
            dict_s[i] = dict_s.setdefault(i,0)+1
        # dict_p = Counter(p)
        # dict_s = Counter(s[:len_p])
        if dict_p == dict_s:
            result.append(0)
        i = 0
        j = len_p
        while(j<len_s):
            dict_s[s[i]] -= 1
            if dict_s[s[i]] == 0:
                dict_s.pop(s[i])
            dict_s[s[j]] = dict_s.setdefault(s[j],0)+1
            if dict_s == dict_p:
                result.append(i+1)
            i = i+1
            j = j+1
        return result