# 盛最多水的容器。 这个题目用双指针的方法，虽然我想到了双指针，但是具体的没有想对。
# 具体的思路就是两个指针，哪一边指的值小，则进行移动。但是每一次的面积都是需要计算的。
# 之所以不移动大的一边，是因为两个指针都是在往中间移动，即两指针之间的index是一定减小的。那么如果移动大的一边，总的面积一定减小。
# 所以只需要移动小的一边即可。
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        len_h = len(height)
        i,j = 0,len_h-1
        size = 0
        while(i<j):
            size_now = min(height[i],height[j])*(j-i)
            if size_now>size: size = size_now
            if height[i]<=height[j]:
                i += 1
            else:
                j -= 1
        return size