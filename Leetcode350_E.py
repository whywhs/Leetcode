#查找两个数组中较小的数组，以小的进行检索，如果在大的中发现有小的存在的，那么result就append，同时大的还要将重复的进行删除。
#采用remove是因为，它只会删除第一个查找到的重复项。
#时间比较长，原因可能在于remove仍要遍历大数组。
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)
        nums_a= nums1 if len_nums1<=len_nums2 else nums2
        nums_b= nums2 if len_nums1<=len_nums2 else nums1
        result=[]
        for i in nums_a:
            if i in nums_b:
                nums_b.remove(i)
                result.append(i)
        return result
        
 #通过dict进行数组中项的计数，如果发现重复，则计数减一。
 #该算法时间更快。
 class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic = {}
        result=[]
        for i in nums1:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        for j in nums2:
            if j in dic and dic[j]>0:
                result.append(j)
                dic[j]-=1
        return result
        
