#有序矩阵中第K小的元素。查找第K小，先将数组拉到一个list,然后用二分法，求出中间值，并将list划分为两个部分。
#根据K取值，来找到应该对哪一个list进行进一步处理。
#循环最后的情况会有两种，一种是只剩下最后一个元素，即满足要求，另一种是剩下了所有相同的元素，则取第一个即可。
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        list_my = matrix[0]
        for i in matrix[1:]:
            list_my += i

        while(len(list_my)!=1):
            if len(set(list_my))==1:
                break
            result_l = []
            result_r = []
            min_l = min(list_my)
            max_l = max(list_my)
            mid = (min_l+max_l)/2.0
            for i in list_my:
                if i>mid:
                    result_r.append(i)
                else:
                    result_l.append(i)
            if len(result_l)<k:
                k = k-len(result_l)
                list_my = result_r
            else:
                list_my = result_l
        
        return list_my[0]
