# 寻找两个有序数组的中位数。 这个方法我用的是while循环，不符合题目要求。明天继续更新
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n1,n2 = len(nums1),len(nums2)
        n = (n1+n2)//2+1
        i,j,result = 0,0,[]
        
        while(n>0):
            if j==n2:
                result += nums1[i:i+n]
                break
            if i==n1:
                result += nums2[j:j+n]
                break          
            while(i<n1 and j<n2 and n>0 and nums1[i]<=nums2[j]):
                result.append(nums1[i])
                i += 1
                n -= 1
                if n==0:
                    break
            while(i<n1 and j<n2 and n>0 and nums2[j]<nums1[i]):
                result.append(nums2[j])
                j += 1
                n -= 1
                if n==0:
                    break
        
        if (n1+n2)%2==0:
            return (result[-1]+result[-2])/2.0
        return float(result[-1])