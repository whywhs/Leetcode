# 最长连续序列。这个题目要求使用O(N)的解法，标准答案是使用了一个哈希表，这里需要注意的一点就是set之后进行查找时间复杂度也是O(1).
# 在这里我是使用了一个dict_all来保存数组中的值，同时也是为了去重，因为重复的数字在长度的求取上没有任何作用。
# 进行查找的过程就是首先判断n-1在不在数组中，如果在的话，那么最长的序列一定是从n-1开始的，所以n直接跳过即可。
# 如果发现不在，那么就将此时的sub_len变为1，然后进行while查找，查找i+1是否在nums中，直到不在为止。
# 对于时间复杂度来说，构建dict_all为O(N)，查找最坏的情况下，应该是O(2N)，所以总的最坏情况是O(3N)，也就是O(N),满足要求。
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict_all = {}
        for i in nums:
            dict_all[i] = 1
        max_len = 0
        for i in dict_all:
            if i-1 not in dict_all:
                len_sub = 1
                while(i+1 in dict_all):
                    len_sub += 1
                    i += 1
                if len_sub>max_len: max_len = len_sub
        return max_len