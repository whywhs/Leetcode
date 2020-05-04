# 跳跃游戏II. 这两个方法第一个是用了贪心的思路，即每一次更新到下一步可以跳到的最大的位置。即在0的时候，看下一步的位置i+nums[i]最大的
# 就是我们下一步要走到的地方，整个算法复杂度O(n)。
# 第二个方法就是采用了dict+list的方法，list来记录下一步所有可以到达的位置，dict记录已经计算过的位置，那么时间复杂度应该还是O(n)

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return 0
        if nums[0]+1 >= len(nums):
            return 1
        start,max_sub,count = 0,0,0
        while(max_sub<len(nums)-1):
            for i in range(nums[start]):
                now = start+i+1
                if now+nums[now]>max_sub:
                    max_sub = now+nums[now]
                    k = start+i+1
            start = k
            count += 1
        return count+1


        # if len(nums)==1:
        #     return 0
        # res = [0]
        # count = 0
        # sub,dict_all = [],{}
        # while(res):
        #     now = res.pop()
        #     if now not in dict_all:
        #         dict_all[now] = 1
        #         for i in range(nums[now]):
        #             if now+i+1==len(nums)-1:
        #                 return count+1
        #             sub.append(now+i+1)
        #     if res==[]:
        #         count += 1
        #         res = sub
        #         sub = []