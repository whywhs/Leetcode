# DFS+DP, 先用DP判断能否分割，再用DFS来进行分割搜索
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        
        def dfs(s,wordDict):
            if s=='':
                return [""]
            result = []
            for i in range(len(s)):
                if s[:i+1] in wordDict:
                    result_sub = dfs(s[i+1:],wordDict)
                    for j in result_sub:
                        if j=="":
                            result.append(s[:i+1])
                        else:
                            result.append(s[:i+1]+' '+j)
            return result

        def judge(s,wordDict):
            len_s = len(s)
            list_judge = [0]*len_s
            list_flag = []
            for i in range(len_s):
                if s[:i+1] in wordDict:
                    list_judge[i]=1
                    list_flag.append(i)
                else:
                    for j in range(len(list_flag)):
                        if s[list_flag[j]+1:i+1] in wordDict:
                            list_judge[i]=1
                            list_flag.append(i)
                            break
                            
            return list_judge
        
        result = judge(s,wordDict)
        if result[-1]:
            result_fin = dfs(s,wordDict)
            return result_fin
        return []
    
    
    
#采用mem来记下之前进行过分割的字符串，可以节省时间
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        mem = {}
        
        def dfs(s,wordDict,mem):
            if s in mem:
                return mem[s]
            if s == '':
                return ['']
            result = []
            for i in range(len(s)):
                if s[:i+1] in wordDict:
                    result_sub = dfs(s[i+1:],wordDict,mem)
                    for j in result_sub:
                        if j=='':
                            result.append(s[:i+1])
                        else:
                            result.append(s[:i+1]+' '+j)
            mem[s]=result
            return result
    
        result = dfs(s,wordDict,mem)
        return result
