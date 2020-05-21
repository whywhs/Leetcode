# 最长回文子串。这个题目用的是一个动态规划的算法。在满足s[i]==s[j]的前提下，我们来判断字符串是否是一个回文串。然后就又回到了标准的套路上。
# 需要注意的是经典解法，一个是DP，一个是中心扩展。DP方法就是创建res，然后res[i][j] = res[i+1][j-1] and s[i]==s[j]。 但是一定要注意
# 的就是循环，不能for i 然后 for j 这样相当于从i开始直接找最长，这样会漏掉一些，就比如abcdcba，当a==a，但是由于bcdcb还没有循环到，
# 因为此时的i是在a这个地方，还没有到b,所以就会漏检。 这里的做法就是按照序列长度来进行查找。 第一个for 就是序列长度，从0开始，0代表当前
# 是一个单字母。 然后内层是i的起始位置。 通过j= i+l来计算j 的位置即可。
# 另外一种做法是采用了中心拓展。 这个思路就是两种，一个是奇数中心，一个是偶数中心。那么计算两种结果里最大的一个长度，即可知道当前最大的。
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
    #     # 中心拓展
    #     max_len,be = 1,0
    #     for i in range(len(s)):
    #         start,end = i,i+1
    #         l1,r1 = self.func(start,start,s)
    #         l2,r2 = self.func(start,end,s)
    #         now = max(r1-l1+1,r2-l2+1)
    #         if now>max_len:
    #             be = l1 if r1-l1>r2-l2 else l2
    #             max_len = now
    #     return s[be:be+max_len]


    # def func(self,start,end,s):
    #     while start>=0 and end<len(s) and s[start]==s[end]:
    #         start -= 1
    #         end += 1
    #     return start+1,end-1

        # # 动态规划
        # if len(s)<=1:
        #     return s
        
        # begin,max_len = 0,1
        # res = [[0 for i in range(len(s))] for j in range(len(s))]
        # for l in range(len(s)):
        #     for i in range(len(s)):
        #         j = i+l
        #         if j>=len(s):
        #             break
        #         if l==0:
        #             res[i][j] = 1
        #         elif l==1:
        #             res[i][j] = 1 if s[i]==s[j] else 0
        #         else:
        #             res[i][j] = 1 if (s[i]==s[j] and res[i+1][j-1]) else 0
                
        #         if res[i][j]==1 and j-i+1>max_len:
        #             begin = i
        #             max_len = j-i+1
        # return s[begin:begin+max_len]












# class Solution(object):
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         if len(s)<2:
#             return s
#         if len(set(s))==1:
#             return s

#         len_s = len(s)
#         result = [1]*len_s
#         max_sub,index = 1,0
#         for i in range(len_s):
#             for j in range(i):
#                 if s[i]==s[j]:
#                     if s[j:i+1]==s[j:i+1][::-1]:
#                         result[i] = max(result[i],i-j+1)
#             if result[i]>max_sub:
#                 max_sub,index = result[i],i

#         return s[index-max_sub+1:index+1]
