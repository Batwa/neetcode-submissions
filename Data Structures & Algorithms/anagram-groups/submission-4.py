class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        for x in strs:
            a="".join(sorted(x))
            if a in dic:
                dic[a].append(x)
            else:
                dic[a]=[x]
        return list(dic.values())
