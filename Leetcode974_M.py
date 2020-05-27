# 和可被K整除的子数组。这个题目可以采用O(N**2)的解法，是比较好写的，但是会超时。
# 这个题目标准的解法是O(N)的前缀和。 前缀和可以在如果数组是要求连续的和的情况下运用。因为前缀和res中，任意两个i-1,j之差就是nums[i,j
# 之和。对于本题来说，可以被K整除的子数组，分两种情况，第一就是当前数组就可以被整除，那么就是余数为0，另外一种就是[i,j]之间的数组可以被
# 整除。那么就是(res[j]-res[i-1])%K==0, 这个可以拆分为res[j]%k == res[i-1]%k，也就是说，两个前缀和对于K的余数是相同的。利用这一点
# 我们就只需要判断前缀和中所有数与K的余数。
# 对于结果来说，不是有几个k就有几个结果，而是一个叠加的过程，根据余数的不同。如果余数是0，那么就是1+2+3+4... 如果余数不是0 那么就是
# 0+1+2+3... 因为对于余数是0的来说，本身就可以组成正确的子数组，而对于非0的来说，至少两个在一起才可以组成。
class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        count,res = 0,0
        dict_mod = {}
        for i in range(len(A)):
            res += A[i]
            mod = res%K
            if mod in dict_mod:
                dict_mod[mod] = [dict_mod[mod][0]+dict_mod[mod][1],dict_mod[mod][1]+1]
            else:
                dict_mod[mod] = [0,1] if mod!=0 else [1,2]
        return sum([i[0] for _,i in dict_mod.items()])