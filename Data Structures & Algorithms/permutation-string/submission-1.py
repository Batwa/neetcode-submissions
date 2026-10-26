class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)==0:
            return True
        if len(s1)==1:
            if s2.count(s1[0])>0:
                return True
            else:
                return False
        need = {}      
        for ch in s1:
            need[ch] = need.get(ch, 0) + 1
        l=0
        r=len(s1)
        while l<=len(s2)-len(s1):
            chek=s2[l:r+l]
            have={}
            for ch in chek:
                have[ch] = have.get(ch, 0) + 1
            if have==need:
                return True
            else:
                l+=1
        return False 
