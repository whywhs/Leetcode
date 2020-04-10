# 翻转字符串里的单词。在python中，s.split()就直接将字符串按照空格来进行划分了
# s.split() 和 s.split(' ')结果不一样，后者出来的结果如果有连续空格是有""的
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # s = s.strip()[::-1]
        # r,z,i = '','',0
        # while(i<len(s)):
        #     if s[i]!= ' ':
        #         r += s[i]
        #         i += 1
        #     else:
        #         z += r[::-1]
        #         z += ' '
        #         r = ''
        #         while(s[i]==' '):
        #             i += 1
        # z += r[::-1]
        # return z

        result = []
        list_s = s.split()
        return ' '.join(list_s[::-1])

        for i in list_s[::-1]:
            if i!='':
                result.append(i)
        return " ".join(result)