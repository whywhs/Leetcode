# 解码方法。这个题目做法上还是比较简单的，当前i一定是大于等于i-1的，这个是首先的。
# 另外，当当前i与i-1构成一对时，那么就在i结果的基础上再加上一个i-2即可。但特别需要注意的就是10的问题。
# 在这里我是用一个list来将0与前面的划成一个数了，因为0是不能单独存在的。
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0]=="0":
            return 0
        list_s = []
        for i in s:
            if i=="0":
                list_s[-1]+=i
                if int(list_s[-1])>20:
                    return 0
            else:
                list_s.append(i)
        
        if len(list_s)==1:
            return 1
        result = [1]*len(list_s)
        if int(list_s[0]+list_s[1]) < 27:
            result[1]=2

        for i in range(2,len(list_s)):
            result[i] = result[i-1]
            if int(list_s[i-1]+list_s[i]) < 27:
                result[i] += result[i-2]
        return result[-1]
