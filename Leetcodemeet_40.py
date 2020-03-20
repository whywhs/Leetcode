# 最小的K个数。这个题目一开始最先想到的就是最小堆，对arr构建堆，然后对K进行遍历。
# 这个题目的一个较好的方法是可以采用桶排序，因为题目中给定了数值的范围。相当于是一个O(N)的方法。
class Solution(object):
    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans,index = [],k
        result = [0]*10001
        for i in arr:
            result[i] += 1
        for i in range(10001):
            while(result[i]!=0):
                ans.append(i)
                result[i]=result[i]-1
                k=k-1
            if k<=0: break
        return ans[:index]


        #import heapq
        #result = []
        #heapq.heapify(arr)
        #for i in range(k):
        #    result.append(heapq.heappop(arr))
        #return result