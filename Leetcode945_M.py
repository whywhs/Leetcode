# 这个是O(N)的解法，是计数排序，即桶排序。 桶排序完成之后，重新遍历，当当前值大于1，则将后面的一个数加上当前值-1.
# 这样，所有的数都会累加到最后一位，然后再通过一个等差数列求和来完成。
# 另外还有一种计数做法，通过先对A进行排序。然后，当A[i-1]<A[i]时，那么就将A[i]变成A[i-1]+1，同时count也进行加。最后count即结果。
class Solution(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        count = 0
        num = [0]*40001
        for i in A:
            num[i]+=1
        
        for i in range(len(num)-1):
            if num[i]>=2:
                num[i+1] += num[i]-1
                count += num[i]-1
        count += num[-1]*(num[-1]-1)*0.5
        return int(count)
        
        # 排序统计
        count = 0
        A.sort()
        for i in range(1,len(A)):
            if A[i]<=A[i-1]:
                count += A[i-1]+1-A[i]
                A[i] = A[i-1]+1
        return count