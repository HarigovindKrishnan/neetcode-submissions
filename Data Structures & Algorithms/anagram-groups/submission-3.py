class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s={}
        for i in strs:
            s.setdefault("".join(sorted(i)),[]).append(i)

        result=[]
        for i in s.keys():
            result.append(s[i])    

        return result    