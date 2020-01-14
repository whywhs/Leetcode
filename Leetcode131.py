class Solution(object):
    import copy
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        for i in range(len(s)):
            if result == []:
                result.append([s[i]])
            else:
                len_result = len(result)
                for j in range(len_result):
                    result[j].append(s[i])
                    if len(result[j])>=2:
                        if result[j][-1]==result[j][-2]:
                            result.append(result[j][:len(result[j])-2]+[result[j][-1]+result[j][-2]])
                    if len(result[j])>=3:
                        if result[j][-1]==result[j][-3]:
                            result.append(result[j][:len(result[j])-3]+[result[j][-1]+result[j][-2]+result[j][-3]])
        return result
