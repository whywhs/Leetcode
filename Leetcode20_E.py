#有效地括号，这道题总的来说就是要细心，不然很容易出错
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)==0:
            return True
        if s[0] in [')','}',']']:
            return False
        
        dict_all = {}
        list_all = ['(',')','{','}','[',']']
        k=1
        for i in list_all:
            dict_all[i]=k
            k=k+1
        
        a = [dict_all[s[0]]]
        for i in s[1:]:
            if i==' ':
                continue
            num = dict_all[i]
            if num%2==1:
                a.append(num)
                continue
            if a!=[] and num == a[-1]+1:
                a.pop(-1)
                continue
            return False
        if a==[]:
            return True
        return False
