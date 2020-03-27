# 超级丑数。这个题目和丑数II的差别在于将丑数II中的固定2,3,5因数变为了任意的因数。
# 做法相当于在丑数II的基础上再加一层循环。即维护了一个len_test列表来存储每一个因数所使用的index.
# 这个题目对丑数II进行了一个提醒，即会出现相同数的情况。比如2*7与7*2，对于丑数II，它是进行了遍历。
# 所以，在这个题目中也要遍历，如果当前的min是好几个数乘以它的index，那么这几个数的index均加一。
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        result = [1]
        len_test = [0]*len(primes)
        while(len(result)!=n):
            result_now = [result[len_test[i]]*primes[i] for i in range(len(primes))]
            min_now = min(result_now)
            result.append(min_now)
            for j in range(len(len_test)):
                if result[len_test[j]] * primes[j]==min_now:
                    len_test[j] += 1
        return result[-1]