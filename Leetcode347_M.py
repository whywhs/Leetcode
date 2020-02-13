class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count_my={}
        max_num = max(nums)
        for i in nums:
            if i<0:
                i = -i+max_num
            if i not in count_my:
                count_my[i]=0
            count_my[i]+=1
            
        list_a=[count_my[i] for i in count_my]
        list_result=[0]*(max(list_a)+1)
        for i in list_a:
            list_result[i]+=1
        list_result=list_result[::-1]
        
        result=[]
        for i in range(len(list_result)):
            if list_result[i]>0:
                w = [len(list_result)-i-1]*list_result[i]
                result+=w
            if len(result)>=k:
                break
                
        result_all=[]
        for i in count_my:
            if count_my[i] in result:
                if i>max_num:
                    result_all.append(max_num-i)
                else:
                    result_all.append(i)
        return result_all
