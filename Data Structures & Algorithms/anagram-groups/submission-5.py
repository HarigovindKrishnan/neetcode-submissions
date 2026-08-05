class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=[]
        map={}
        for s in strs:
            map.setdefault("".join(sorted(s)),[]).append(s)

        for i in map:
            result.append(map[i])
        
        return result

        


        