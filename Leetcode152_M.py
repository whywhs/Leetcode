#为啥我写了这么长，好在时间上超过了100%的代码，还是比较欣慰的。。。
#首先判断nums中有没有0，如果有0就将0分开。其次，通过判断最长的含有偶数个负数的list，该list的乘积就是最大的连续乘积
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def multi(nums):
            origin = 1
            for i in nums:
                origin = origin*i
            return origin
        
        def judge(nums):
            len_nums = len(nums)
            if len(nums)==1:
                return nums[0]
            result = [1 if nums[i]>0 else -1 for i in range(len_nums)]
            if result.count(-1)%2==0:
                return multi(nums)
            
            for i in range(len_nums):
                if result[i]==-1:
                    flag1 = i
                    break
            flag1_l = 0 if flag1==0 else multi(nums[:flag1])
            flag1_r = 0 if flag1+1==len_nums else multi(nums[flag1+1:])
            
            for j in range(len_nums):
                if result[-j-1]==-1:
                    flag2 = j
                    break
            flag2_l = 0 if len_nums-flag2-1==0 else multi(nums[:len_nums-flag2-1])
            flag2_r = 0 if len_nums-flag2==len_nums else multi(nums[len_nums-flag2:])
            
            return max(flag1_l,flag1_r,flag2_l,flag2_r)
        
        result = []
        result_sub = []
        if len(nums)==1:
            return nums[0]
        for i in range(len(nums)):
            if nums[i]==0:
                result.append(result_sub)
                result_sub = []
                continue
            result_sub.append(nums[i])
        result.append(result_sub)
        
        result_all=[]
        for j in result:
            if j!=[]:
                result_all.append(judge(j))
        max_result = max(result_all)
        return 0 if 0 in nums and max_result<0 else max_result 


# 这种解法是更合适的，使用了动态规划的解法。思路就是维护两个数组，一个数组是让大的更大，另一个是让小的更小。
# 数组大的更大所采用的就是，当前值nums[i],前一时刻的最大值*当前值，后一时刻的最大值*当前值
# 数组小的更小采用的道理一样。
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        f_pre_min,f_pre_max = 1,1
        max_all = float('-inf')
        for i in range(len(nums)):
            f_max = max(nums[i],f_pre_max*nums[i],f_pre_min*nums[i])
            f_min = min(nums[i],f_pre_max*nums[i],f_pre_min*nums[i])      
            f_pre_max = f_max
            f_pre_min = f_min
            if f_max>max_all:
                max_all = f_max
        return max_all