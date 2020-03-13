# 多数元素。常规解法就不说了，这里有一个解法叫摩尔投票法。具体的操作就是，对数组里面的数进行两两抵消，剩下的就是多数元素。
# 具体操作就是，维护两个数major与count，当major与当前遍历数不同的情况下两两抵消，相同的情况下count+1，最后剩下的major就是要找的数。
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #len_s = len(nums)
        #for i in set(nums):
        #    if nums.count(i)>len_s//2:
        #        return i

        major,count = 0,0
        for i in nums:
            if count==0:
                major = i
                count += 1
            else:
                if major == i:
                    count += 1
                else:
                    count -= 1

        return major
