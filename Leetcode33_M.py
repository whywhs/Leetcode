# 搜索旋转排序数组。这个题目要求使用logn的解法，所以很自然地就是二分法。关键在于如何二分。
# 这个题目二分的关键是来判断那一部分是有序的。即当mid>l的时候，说明左边一定有序，那么当target在左边的范围内，就可以将r变成mid-1，否则移到右边
# 如果mid<l也是同理。这里需要注意的一个地方就是当mid=l时，考虑到会先判断mid是否等于target，那么l一定不等于target，所以就可以直接将l=mid+1即可。
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        l,r = 0,len(nums)-1
        while(l<=r):
            mid = (l+r)//2
            if target == nums[mid]:
                return mid
            if nums[mid]>nums[l]:
                if nums[l]<=target<nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
            elif nums[mid]<nums[l]:
                if nums[mid]<target<=nums[r]:
                    l = mid+1
                else:
                    r = mid-1
            else:
                l = mid+1
        return -1