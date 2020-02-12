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
