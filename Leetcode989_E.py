# 数组形式的整数加法。这个题目需要注意的就是在while那里，一定要记得是max(len_a,len_k)，因为两个相加之后长度肯定是两者之间的最大值
# range（负数）是没有的返回[]。
class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        k_s = str(K)
        len_a,len_k = len(A),len(k_s)
        i = 1
        while(i<=len_a and i<=len_k):
            A[-i] = A[-i] + int(k_s[-i])
            i = i+1
        A = [int(k_s[i]) for i in range(len_k-len_a)] + A 
        i = 1
        while(i<max(len_a,len_k)):
            if A[-i]>=10:
                A[-i] -= 10
                A[-i-1] += 1
            i = i+1
        if A[0]>=10:
            A[0] -= 10
            A = [1]+A
        return A