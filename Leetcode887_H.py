# 鸡蛋掉落。这个题目必须要用二分法才可以通过时间。二分法的原理在于left和right一个是递增函数，一个是递减函数。
# 那么这两个函数的交点即为所需要的max，min。 因为max(left,right)就是找两个连线上方的部分。那么在交点前，递增的一定在递减的
# 下方，递减的一定在递增的上方。则交点就是min(max(left,right))。即result是mid的函数。
class Solution(object):
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        result =  [[1 for i in range(N+1)] for j in range(K+1)]
        result[1] = [i for i in range(N+1)]
        for i in range(2,N+1):
            for j in range(2,K+1):
                a,b = 1,i-1
                while(a<b):
                    mid = (a+b)//2
                    left,right = result[j-1][mid-1],result[j][i-mid]
                    if left<right:
                        a = mid+1
                    elif left>right:
                        b = mid-1
                    else:
                        a = b = mid
                r1 = max(result[j-1][a-1],result[j][i-a])
                r2 = max(result[j-1][b-1],result[j][i-b])
                result[j][i] = min(r1,r2)+1
        return result[-1][-1]