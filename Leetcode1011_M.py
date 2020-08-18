# 在 D 天内送达包裹的能力。这个题目可以采用二分法来解决，二分法的思路就是最小重量为max(nums)，最大重量为sum(nums)。
# 那么对最小最大重量进行二分，来统计天数，如果天数比预期的大了，那么说明取得mid小了，就i=mid+1。 记住这里一定是+1，因为mid一定不可能了。
# 对于j = mid来说，说明是选的大了，但是不能mid-1，因为允许在更小的天数完成，所以mid也是可以的。
# 同时，这里不需要进行相等的判断，因为有可能a可以，a的中值也是可以的。
class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        i,j = max(weights),sum(weights)
        while(i<j):
            mid = (i+j)//2
            days = self.func(weights,mid)
            if days>D:
                i = mid+1
            elif days<=D:
                j = mid
        return j

    def func(self,weights,mid):
        days,i = 0,0
        while(i<len(weights)):
            now = 0
            while(i<len(weights) and now+weights[i]<=mid):
                now += weights[i]
                i += 1
            days += 1
        return days