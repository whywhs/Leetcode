# 合并两个有序数组。其中一个数组长度是足够包含另外一个数组的。
class Solution(object):
    def merge(self, A, m, B, n):
        """
        :type A: List[int]
        :type m: int
        :type B: List[int]
        :type n: int
        :rtype: None Do not return anything, modify A in-place instead.
        """
        k = m-1
        j = -1
        while(B!=[]):
            now = B.pop()
            while(k>=0 and A[k]>now):
                A[j] = A[k]
                k,j = k-1,j-1
            A[j] = now
            j = j-1
        
        A[:len(B)] = B
