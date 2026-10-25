class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s =="":
            return 0
        l=0
        longest=1
        seen={}
        seen[s[0]]=0
        for r in range(1,len(s)):
            if s[r] in seen:
                l=max(l, seen[s[r]]+1)
            longest=max(longest,r-l+1)
            seen[s[r]]=r
        return longest
