#根据情况进行判断，回文串只有两种可能情况，一种是新的字符与前一字符相同构成回文，另一种是新的字符与前前一个字符相等三者构成回文
class Solution(object):
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
    
#回溯法，记得if s==''中return回来的必须是[[]]，不然for mm in result_sub这一行是没有办法运行的
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def judge(s):
            if s=='':
                return [[]]
            result = []
            for i in range(len(s)):
                if s[:i+1]==s[:i+1][::-1]:
                    result_sub = judge(s[i+1:])
                    for mm in result_sub:
                        result.append([s[:i+1]]+mm)
            
            return result
        
        result = judge(s)
        return result   
